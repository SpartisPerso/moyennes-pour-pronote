(() => {
  "use strict";

  const ROOT_ID = "pronote-moyennes-extension";
  const INLINE_AVERAGE_CLASS = "pm-inline-average";
  const NOTE_LABEL_PATTERN = /Note\s+(?:de\s+l['’])?élève\s*:\s*([0-9]+(?:[,.][0-9]+)?)(?:\s*\/\s*([0-9]+(?:[,.][0-9]+)?))?/i;
  const numberFormatter = new Intl.NumberFormat("fr-FR", {
    minimumFractionDigits: 2,
    maximumFractionDigits: 2,
  });

  let lastSignature = "";
  let refreshTimer = 0;

  function isVisible(element) {
    const style = getComputedStyle(element);
    return style.display !== "none" && style.visibility !== "hidden" && element.getClientRects().length > 0;
  }

  function findNotesTree() {
    return Array.from(document.querySelectorAll('[role="tree"]')).find(
      (tree) => isVisible(tree) && tree.querySelector('[aria-label*="Note élève"]'),
    );
  }

  function normalizeSubject(value) {
    return value.replace(/\s+/g, " ").trim();
  }

  function parseVisibleNotes(tree) {
    const notesBySubject = new Map();
    let currentSubject = "";

    for (const row of tree.querySelectorAll('[role="treeitem"]')) {
      const level = row.getAttribute("aria-level");

      if (level === "1") {
        currentSubject = normalizeSubject(
          row.querySelector(".ie-titre-gros")?.textContent ||
            row.querySelector(".titre-principal")?.textContent ||
            row.textContent ||
            "",
        );
        continue;
      }

      if (level !== "2") {
        continue;
      }

      const subject = normalizeSubject(
        row.querySelector(".ie-titre-gros")?.textContent ||
          row.querySelector(".titre-principal")?.textContent ||
          currentSubject,
      );
      const noteLabel = row
        .querySelector('[aria-label*="Note élève"]')
        ?.getAttribute("aria-label");
      const match = noteLabel?.match(NOTE_LABEL_PATTERN);

      if (!subject || !match) {
        continue;
      }

      const value = Number(match[1].replace(",", "."));
      const scale = match[2] ? Number(match[2].replace(",", ".")) : 20;

      if (!Number.isFinite(value) || !Number.isFinite(scale) || scale <= 0) {
        continue;
      }

      const notes = notesBySubject.get(subject) || [];
      notes.push((value / scale) * 20);
      notesBySubject.set(subject, notes);
    }

    return Array.from(notesBySubject, ([subject, notes]) => ({
      subject,
      noteCount: notes.length,
      average: notes.reduce((sum, note) => sum + note, 0) / notes.length,
    }));
  }

  function formatAverage(value) {
    return `${numberFormatter.format(value)} / 20`;
  }

  function createElement(tagName, className, text) {
    const element = document.createElement(tagName);
    if (className) {
      element.className = className;
    }
    if (text !== undefined) {
      element.textContent = text;
    }
    return element;
  }

  function buildPanel(subjects, generalAverage, showSubjectList) {
    const panel = createElement("section", "pm-panel");
    panel.id = ROOT_ID;
    panel.setAttribute("aria-label", "Moyennes estimées");
    panel.setAttribute("aria-live", "polite");

    const header = createElement("header", "pm-header");
    const headingGroup = createElement("div", "pm-heading-group");
    headingGroup.append(
      createElement("h2", "pm-title", "Moyennes estimées"),
      createElement(
        "p",
        "pm-subtitle",
        "Notes ramenées sur 20, matières de même poids",
      ),
    );

    const general = createElement("div", "pm-general");
    general.append(
      createElement("span", "pm-general-label", "Moyenne générale"),
      createElement("strong", "pm-general-value", formatAverage(generalAverage)),
    );
    header.append(headingGroup, general);

    panel.append(header);

    if (showSubjectList) {
      const list = createElement("div", "pm-list");
      for (const item of subjects) {
        const row = createElement("div", "pm-row");
        const subjectGroup = createElement("div", "pm-subject-group");
        subjectGroup.append(
          createElement("span", "pm-subject", item.subject),
          createElement(
            "span",
            "pm-note-count",
            `${item.noteCount} ${item.noteCount > 1 ? "notes" : "note"}`,
          ),
        );
        row.append(
          subjectGroup,
          createElement("strong", "pm-average", formatAverage(item.average)),
        );
        list.append(row);
      }
      panel.append(list);
    }

    return panel;
  }

  function removeInlineAverages() {
    for (const average of document.querySelectorAll(`.${INLINE_AVERAGE_CLASS}`)) {
      average.remove();
    }
  }

  function displayInlineAverages(tree, subjects) {
    removeInlineAverages();
    const subjectByName = new Map(subjects.map((item) => [item.subject, item]));

    for (const row of tree.querySelectorAll('[role="treeitem"][aria-level="1"]')) {
      const content = row.querySelector(".zone-contenu-format");
      const subject = normalizeSubject(
        row.querySelector(".ie-titre-gros")?.textContent || "",
      );
      const item = subjectByName.get(subject);

      if (!content || !item) {
        continue;
      }

      const average = createElement(
        "div",
        `zone-complementaire ${INLINE_AVERAGE_CLASS}`,
      );
      average.setAttribute(
        "aria-label",
        `Moyenne de ${subject} : ${formatAverage(item.average)}`,
      );
      average.append(
        createElement("span", "pm-inline-average-label", "Moyenne :"),
        createElement(
          "span",
          "note-devoir pm-inline-average-value",
          formatAverage(item.average),
        ),
      );
      content.append(average);
    }
  }

  function removePanel() {
    document.getElementById(ROOT_ID)?.remove();
    removeInlineAverages();
    lastSignature = "";
  }

  function refresh() {
    const tree = findNotesTree();
    if (!tree) {
      removePanel();
      return;
    }

    const subjects = parseVisibleNotes(tree);
    if (subjects.length === 0) {
      removePanel();
      return;
    }

    const generalAverage =
      subjects.reduce((sum, item) => sum + item.average, 0) / subjects.length;
    const isSubjectView = Boolean(
      tree.querySelector('[role="treeitem"][aria-level="1"]'),
    );
    const signature = JSON.stringify({ subjects, generalAverage, isSubjectView });
    const existingPanel = document.getElementById(ROOT_ID);
    const inlineAverageCount = tree.querySelectorAll(
      `.${INLINE_AVERAGE_CLASS}`,
    ).length;
    const inlineDisplayIsCurrent = isSubjectView
      ? inlineAverageCount === subjects.length
      : inlineAverageCount === 0;

    if (signature === lastSignature && existingPanel && inlineDisplayIsCurrent) {
      return;
    }

    existingPanel?.remove();
    if (isSubjectView) {
      displayInlineAverages(tree, subjects);
    } else {
      removeInlineAverages();
    }
    const panel = buildPanel(subjects, generalAverage, !isSubjectView);
    const insertionPoint = tree.parentElement || document.querySelector("main");
    insertionPoint?.prepend(panel);
    lastSignature = signature;
  }

  function scheduleRefresh() {
    clearTimeout(refreshTimer);
    refreshTimer = window.setTimeout(refresh, 100);
  }

  const observer = new MutationObserver(scheduleRefresh);
  observer.observe(document.documentElement, {
    childList: true,
    subtree: true,
    characterData: true,
    attributes: true,
    attributeFilter: ["aria-label", "aria-checked", "class"],
  });

  scheduleRefresh();
})();
