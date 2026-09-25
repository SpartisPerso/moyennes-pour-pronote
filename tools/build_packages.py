"""Construit les paquets a soumettre aux boutiques et le paquet d'installation manuelle."""

import json
import shutil
import zipfile
from pathlib import Path

PROJECT = Path(__file__).resolve().parent.parent
EXTENSION = PROJECT / "extension"
DIST = PROJECT / "dist"
FIREFOX_ID = "{9e9cc269-cc06-47a7-94ca-5164ea68e1f9}"
MANUAL_FILES = ("GUIDE_INSTALLATION.html", "GUIDE_INSTALLATION.md", "README.md")


def extension_files() -> list[Path]:
    return sorted(path for path in EXTENSION.rglob("*") if path.is_file())


def write_zip(target: Path, entries: dict[str, Path | str]) -> Path:
    target.parent.mkdir(parents=True, exist_ok=True)
    target.unlink(missing_ok=True)
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as archive:
        for name, source in sorted(entries.items()):
            if isinstance(source, Path):
                archive.write(source, name)
            else:
                archive.writestr(name, source)
    return target


def firefox_manifest() -> str:
    manifest = json.loads((EXTENSION / "manifest.json").read_text(encoding="utf-8"))
    # Firefox impose un identifiant explicite et une declaration de collecte pour Manifest V3.
    manifest["browser_specific_settings"] = {
        "gecko": {
            "id": FIREFOX_ID,
            "data_collection_permissions": {"required": ["none"]},
        }
    }
    return json.dumps(manifest, ensure_ascii=False, indent=2) + "\n"


def build() -> None:
    files = extension_files()
    store_entries = {
        path.relative_to(EXTENSION).as_posix(): path for path in files
    }

    chromium = write_zip(DIST / "moyennes-pour-pronote-chrome-edge.zip", store_entries)

    firefox_entries = dict(store_entries)
    firefox_entries["manifest.json"] = firefox_manifest()
    firefox = write_zip(DIST / "moyennes-pour-pronote-firefox.zip", firefox_entries)

    # Dossier decompresse utilisable par web-ext lint et web-ext run.
    source_dir = DIST / "firefox-source"
    shutil.rmtree(source_dir, ignore_errors=True)
    for name, source in firefox_entries.items():
        target = source_dir / name
        target.parent.mkdir(parents=True, exist_ok=True)
        if isinstance(source, Path):
            shutil.copy2(source, target)
        else:
            target.write_text(source, encoding="utf-8")

    manual_entries = {
        f"extension/{path.relative_to(EXTENSION).as_posix()}": path for path in files
    }
    for name in MANUAL_FILES:
        manual_entries[name] = PROJECT / name
    manual = write_zip(DIST / "Moyennes-pour-PRONOTE.zip", manual_entries)

    version = json.loads((EXTENSION / "manifest.json").read_text(encoding="utf-8"))["version"]
    print(f"Version {version}")
    for archive in (chromium, firefox, manual):
        print(f"{archive.relative_to(PROJECT).as_posix()} ({archive.stat().st_size} octets)")
    print(f"{source_dir.relative_to(PROJECT).as_posix()}/ (source Firefox pour web-ext)")


if __name__ == "__main__":
    if not shutil.which("python"):
        raise SystemExit("Python est requis.")
    build()
