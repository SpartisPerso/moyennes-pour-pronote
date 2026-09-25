"""Rasterise le logo (icon.svg) aux tailles exigees par les boutiques d'extensions."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

SUPERSAMPLE = 8
TOP_COLOR = (31, 156, 124)
BOTTOM_COLOR = (11, 77, 60)
CORNER_RADIUS = 28
OVERLINE = (39, 30, 50, 9)  # x, y, largeur, hauteur dans un carre de 128
X_BOX = (45, 55, 83, 97)  # x gauche, y haut, x droit, y bas
X_STROKE = 15
ICON_SIZES = (16, 32, 48, 96, 128)
STORE_LOGO_SIZE = 300
PROMO_TILES = ((440, 280), (1400, 560))

PROJECT = Path(__file__).resolve().parent.parent
ICONS_DIR = PROJECT / "extension" / "icons"
STORE_DIR = PROJECT / "store"
WHITE = (255, 255, 255, 255)


def vertical_gradient(size: int) -> Image.Image:
    gradient = Image.new("RGB", (1, size))
    for y in range(size):
        ratio = y / max(size - 1, 1)
        gradient.putpixel(
            (0, y),
            tuple(
                round(start + (end - start) * ratio)
                for start, end in zip(TOP_COLOR, BOTTOM_COLOR)
            ),
        )
    return gradient.resize((size, size), Image.NEAREST)


def draw_round_stroke(draw, start, end, width) -> None:
    draw.line([start, end], fill=WHITE, width=round(width))
    for x, y in (start, end):
        draw.ellipse(
            (x - width / 2, y - width / 2, x + width / 2, y + width / 2), fill=WHITE
        )


def render_badge(size: int) -> Image.Image:
    canvas = size * SUPERSAMPLE
    scale = canvas / 128

    badge = vertical_gradient(canvas).convert("RGBA")
    mask = Image.new("L", (canvas, canvas), 0)
    ImageDraw.Draw(mask).rounded_rectangle(
        (0, 0, canvas - 1, canvas - 1), radius=round(CORNER_RADIUS * scale), fill=255
    )
    badge.putalpha(mask)

    glyph = Image.new("RGBA", (canvas, canvas), (0, 0, 0, 0))
    draw = ImageDraw.Draw(glyph)

    bar_x, bar_y, bar_width, bar_height = OVERLINE
    draw.rounded_rectangle(
        (
            bar_x * scale,
            bar_y * scale,
            (bar_x + bar_width) * scale,
            (bar_y + bar_height) * scale,
        ),
        radius=bar_height / 2 * scale,
        fill=WHITE,
    )

    left, top, right, bottom = (value * scale for value in X_BOX)
    draw_round_stroke(draw, (left, top), (right, bottom), X_STROKE * scale)
    draw_round_stroke(draw, (right, top), (left, bottom), X_STROKE * scale)

    return Image.alpha_composite(badge, glyph).resize((size, size), Image.LANCZOS)


def load_font(size: int) -> ImageFont.FreeTypeFont | None:
    for name in ("seguisb.ttf", "segoeuib.ttf", "arialbd.ttf"):
        candidate = Path("C:/Windows/Fonts") / name
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size)
    return None


def fit_font(draw, text: str, max_width: int, start_size: int):
    for size in range(start_size, 7, -1):
        font = load_font(size)
        if font is None or draw.textlength(text, font=font) <= max_width:
            return font
    return load_font(8)


def wrap_text(draw, text: str, font, max_width: int) -> list[str]:
    lines: list[str] = []
    current = ""
    for word in text.split():
        candidate = f"{current} {word}".strip()
        if not current or draw.textlength(candidate, font=font) <= max_width:
            current = candidate
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def render_promo_tile(width: int, height: int) -> Image.Image:
    tile = Image.new("RGBA", (width, height), (233, 243, 240, 255))
    badge_size = round(height * 0.52)
    badge_x = round(height * 0.13)
    tile.alpha_composite(render_badge(badge_size), (badge_x, (height - badge_size) // 2))

    draw = ImageDraw.Draw(tile)
    text_x = badge_x + badge_size + round(height * 0.09)
    text_width = width - text_x - round(height * 0.1)

    title_font = fit_font(draw, "Moyennes pour PRONOTE", text_width, round(height * 0.14))
    subtitle_font = load_font(round(height * 0.06))
    if title_font is None or subtitle_font is None:
        return tile

    subtitle = "Moyennes par matière et moyenne générale"
    lines = wrap_text(draw, subtitle, subtitle_font, text_width)
    line_height = round(subtitle_font.size * 1.35)
    block_height = title_font.size * 1.5 + len(lines) * line_height
    y = (height - block_height) / 2

    draw.text((text_x, y), "Moyennes pour PRONOTE", font=title_font, fill=(14, 60, 49, 255))
    y += title_font.size * 1.5
    for line in lines:
        draw.text((text_x, y), line, font=subtitle_font, fill=(82, 99, 93, 255))
        y += line_height
    return tile


def main() -> None:
    ICONS_DIR.mkdir(parents=True, exist_ok=True)
    STORE_DIR.mkdir(parents=True, exist_ok=True)

    for size in ICON_SIZES:
        render_badge(size).save(ICONS_DIR / f"icon-{size}.png")
        print(f"extension/icons/icon-{size}.png")

    render_badge(STORE_LOGO_SIZE).save(STORE_DIR / f"logo-{STORE_LOGO_SIZE}.png")
    print(f"store/logo-{STORE_LOGO_SIZE}.png")

    for width, height in PROMO_TILES:
        render_promo_tile(width, height).save(STORE_DIR / f"promo-{width}x{height}.png")
        print(f"store/promo-{width}x{height}.png")


if __name__ == "__main__":
    main()
