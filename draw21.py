#!/usr/bin/env python3
"""Front page for make.fun's news-image-20261121 contest: the world news
of Saturday 21 November 2026, drawn as one newspaper page.

Every story was verified against at least two published sources dated
21 November 2026 (Al Jazeera, TRT World, The Jerusalem Post, The Times
of Israel, AP via NPR, Reuters, CNN, The Wall Street Journal, BBC,
France 24, UPI, Dawn, The Straits Times/AP, Nature, ESA):
  1. Iran strikes US bases in Bahrain: the IRGC says missiles and
     drones hit two US Patriot radars at al-Riffa and Awali; Bahrain
     says a civilian industrial site was hit and set ablaze, with
     no injuries reported.
  2. Mexico captures "El Chapo Isidro": FBI Top 10 fugitive Fausto
     Isidro Meza Flores seized in Guasave, Sinaloa, with US
     intelligence help; 11 people killed in the backlash (4 soldiers,
     7 gunmen).
  3. A Russian ballistic missile hits Kryvyi Rih, President
     Zelenskyy's hometown: 2 killed, a 7-year-old boy among them,
     and about 60 wounded.
  4. COP31 runs into overtime in Antalya: the summit passes its
     Friday deadline with no deal; the draft drops fossil fuels.
  5. Wall Street slides into correction: the S&P 500 falls 3.7% on
     Friday's trading, the Dow and S&P enter correction territory,
     and the Nasdaq wipes out its 2026 gains; the Nikkei falls 5.06%.
  6. BepiColombo reaches Mercury: the ESA-JAXA probe enters orbit
     after eight years and 10 billion km, only the second mission
     ever to orbit the planet.
Ticker: Trump calls the FBI crime-database hack "not good"; drones
set the Russian cargo ship Sparta II ablaze in the Gulf of Finland;
Wolbachia mosquitoes cut dengue 69% in a Brazil trial.

Left out on purpose, because they were first reported on an earlier
day: the ICJ's Myanmar genocide ruling (19 Nov), the Anthropic IPO
(19 Nov), the Riemann-hypothesis claim (20 Nov), the UK-EU reset
deal signing (20 Nov), and the FBI database breach first reported
by CNN on 20 Nov (its Saturday confirmation is in the ticker only
through Trump's Saturday comment).

Flat-shape illustrations only -- no photos and no borrowed artwork.
Running this file writes entry.png (1024 x 1024) next to it.
"""

import math

from PIL import Image, ImageDraw, ImageFont

PAGE = 1024
PAPER = (247, 242, 232)
INK = (22, 22, 22)
RED = (178, 48, 40)
GREY = (96, 96, 96)
TEAL = (40, 96, 120)


def load(path, size):
    return ImageFont.truetype(path, size)


BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
PLAIN = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def split_lines(draw, text, font, width):
    lines, current = [], ""
    for word in text.split():
        test = (current + " " + word).strip()
        if draw.textlength(test, font=font) <= width:
            current = test
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def block(draw, x, y, text, font, fill, width, centre=False, gap=1.14):
    for line in split_lines(draw, text, font, width):
        lx = x + (width - draw.textlength(line, font=font)) / 2 if centre else x
        draw.text((lx, y), line, font=font, fill=fill)
        y += int(font.size * gap)
    return y


def panel_text(draw, x, y, w, tag, head, body, head_size=25, body_size=18):
    draw.text((x, y), tag, font=load(BOLD, 19), fill=RED)
    y = block(draw, x, y + 26, head, load(BOLD, head_size), INK, w)
    block(draw, x, y + 4, body, load(PLAIN, body_size), GREY, w)


# ------------------------------------------------------------------ scenes
def scene_bahrain(d, x, y, w, h):
    """Night over the Gulf: two radar domes on a base, missile streaks
    overhead, and a fire glowing at an industrial site by the water."""
    d.rectangle([x, y, x + w, y + h], fill=(16, 26, 46))
    for sx, sy in ((x + 26, y + 14), (x + 96, y + 30), (x + 180, y + 12),
                   (x + 260, y + 26), (x + 340, y + 16), (x + 420, y + 28)):
        d.ellipse([sx - 1, sy - 1, sx + 1, sy + 1], fill=(255, 255, 255))
    # pale moon
    d.ellipse([x + w - 64, y + 12, x + w - 28, y + 48], fill=(235, 230, 200))
    # missile streaks, top right to bottom left
    for sx, sy, ln in ((x + 300, y + 18, 64), (x + 350, y + 44, 52),
                       (x + 250, y + 8, 44)):
        d.line([sx, sy, sx - ln, sy + ln // 2], fill=(255, 190, 90), width=4)
        d.ellipse([sx - 4, sy - 4, sx + 4, sy + 4], fill=(255, 230, 160))
    # the base: wall, two radar domes, watchtower
    base = y + h - 46
    d.rectangle([x, base, x + w, y + h], fill=(52, 74, 96))
    d.rectangle([x, base - 8, x + w, base], fill=(30, 44, 62))
    for dx in (x + 52, x + 150):
        d.ellipse([dx, base - 62, dx + 56, base - 6], fill=(225, 225, 225))
        d.rectangle([dx + 6, base - 12, dx + 50, base - 6], fill=(180, 180, 180))
    d.rectangle([x + w - 96, base - 88, x + w - 76, base - 8], fill=(30, 44, 62))
    d.rectangle([x + w - 104, base - 100, x + w - 68, base - 88], fill=(30, 44, 62))
    # fire glow at the industrial site, right side
    fx = x + w - 150
    d.ellipse([fx - 30, base - 42, fx + 30, base + 6], fill=(235, 110, 40))
    d.ellipse([fx - 16, base - 32, fx + 16, base - 2], fill=(255, 205, 90))
    for ox, oy, r in ((-14, -46, 9), (4, -62, 12), (16, -48, 8)):
        d.ellipse([fx + ox - r, base + oy - r, fx + ox + r, base + oy + r],
                  fill=(80, 80, 90))
    # sea strip at the bottom
    d.rectangle([x, y + h - 18, x + w, y + h], fill=(24, 54, 78))
    d.line([x + 10, y + h - 9, x + 90, y + h - 9], fill=(120, 160, 190), width=2)
    d.line([x + 130, y + h - 9, x + 210, y + h - 9], fill=(120, 160, 190), width=2)


def scene_sinaloa(d, x, y, w, h):
    """Dusk in the Sinaloa desert: a low sun, mountain ridges, a
    cactus, and a helicopter sweeping its searchlight. All heights
    scale with the scene height h so nothing leaves the frame."""
    d.rectangle([x, y, x + w, y + h], fill=(238, 178, 110))
    d.rectangle([x, y, x + w, y + h * 0.42], fill=(244, 200, 140))
    cx, cy, r = x + w * 0.68, y + h * 0.30, max(12, int(h * 0.28))
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(255, 226, 150))
    ground = y + h - 30
    for mx, my, mw, mh in ((0.00, 0.52, 0.36, 0.52), (0.30, 0.46, 0.40, 0.62),
                           (0.64, 0.54, 0.36, 0.44)):
        px, py = x + w * mx, y + h * my
        mh_px = h * mh
        d.polygon([(px, ground), (px + w * mw / 2, py),
                   (px + w * mw, ground)], fill=(150, 96, 62))
    d.rectangle([x, ground, x + w, y + h], fill=(120, 78, 50))
    # cactus
    cx0 = x + 34
    ch = int(h * 0.42)
    d.rectangle([cx0, y + h - 30 - ch, cx0 + 12, y + h - 30], fill=(58, 110, 66))
    d.rectangle([cx0 - 16, y + h - 30 - ch + 12, cx0 - 4, y + h - 30 - ch + 26],
                fill=(58, 110, 66))
    d.rectangle([cx0 + 16, y + h - 30 - ch + 18, cx0 + 28, y + h - 30 - ch + 32],
                fill=(58, 110, 66))
    # helicopter with searchlight
    hx, hy = x + w * 0.58, y + h * 0.20
    d.ellipse([hx - 26, hy - 10, hx + 26, hy + 10], fill=(40, 40, 44))
    d.line([hx - 44, hy - 8, hx + 44, hy - 8], fill=(40, 40, 44), width=3)
    d.line([hx + 24, hy, hx + 44, hy - 12], fill=(40, 40, 44), width=3)
    d.polygon([(hx - 8, hy + 10), (hx - 30, hy + 48), (hx + 2, hy + 48)],
              fill=(255, 240, 180))


def scene_kryvyi(d, x, y, w, h):
    """A grey daylight city: apartment blocks, one hit, with a blast
    flash and a smoke column rising over the rooftops. Every vertical
    measure is a fraction of the scene height h, so the drawing stays
    inside its frame at any size."""
    d.rectangle([x, y, x + w, y + h], fill=(205, 210, 216))
    for sx, sy in ((0.07, 0.16), (0.36, 0.10), (0.62, 0.20), (0.86, 0.12)):
        px, py = x + w * sx, y + h * sy
        d.ellipse([px, py, px + w * 0.11, py + h * 0.12],
                  fill=(235, 235, 238))
    base = y + h - h * 0.18
    blocks = ((0.00, 0.13, 0.55), (0.15, 0.10, 0.72), (0.27, 0.14, 0.50),
              (0.43, 0.11, 0.64), (0.56, 0.13, 0.56), (0.71, 0.10, 0.76),
              (0.83, 0.12, 0.44), (0.94, 0.06, 0.58))
    for bx, bw, bh in blocks:
        bh_px = h * bh
        d.rectangle([x + w * bx, base - bh_px, x + w * (bx + bw), base],
                    fill=(96, 100, 110))
        for wy in range(3):
            wy0 = base - bh_px + 8 + wy * h * 0.20
            if wy0 + 8 < base:
                d.rectangle([x + w * bx + 8, wy0, x + w * bx + 16, wy0 + 8],
                            fill=(210, 200, 140))
    # blast flash and smoke over the damaged block, kept in-frame
    fx = x + w * 0.20
    fr = h * 0.14
    d.ellipse([fx - fr, base - h * 0.62, fx + fr, base - h * 0.34],
              fill=(240, 130, 50))
    d.ellipse([fx - fr / 2, base - h * 0.55, fx + fr / 2, base - h * 0.41],
              fill=(255, 215, 110))
    for ox, oy, rr in ((-0.03, -0.64, 0.07), (0.02, -0.72, 0.075),
                       (-0.01, -0.74, 0.055)):
        px, py = fx + w * ox, base + h * oy
        d.ellipse([px - h * rr, py - h * rr, px + h * rr, py + h * rr],
                  fill=(70, 70, 78))
    d.rectangle([x, base, x + w, y + h], fill=(130, 128, 120))
    for rx in (0.05, 0.48, 0.80):
        px = x + w * rx
        d.rectangle([px, base + h * 0.05, px + w * 0.06, base + h * 0.11],
                    fill=(90, 88, 84))


def scene_cop31(d, x, y, w, h):
    """A summit running late: a round clock past midnight on the left,
    a speaker's podium on the right, and a strip of small national
    flags along the bottom. Sized from the scene height h."""
    d.rectangle([x, y, x + w, y + h], fill=(228, 236, 226))
    # clock, left
    cx, cy, r = x + w * 0.26, y + h * 0.44, min(34, int(h * 0.34))
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(255, 255, 255),
              outline=INK, width=3)
    for k in range(12):
        ang = k * math.pi / 6
        px, py = cx + (r - 6) * math.sin(ang), cy - (r - 6) * math.cos(ang)
        d.ellipse([px - 2, py - 2, px + 2, py + 2], fill=INK)
    d.line([cx, cy, cx, cy - r + 10], fill=INK, width=3)
    d.line([cx, cy, cx + (r - 13), cy + 7], fill=INK, width=3)
    d.ellipse([cx - 4, cy - 4, cx + 4, cy + 4], fill=RED)
    # podium with microphone, right
    px0 = x + w * 0.62
    d.rectangle([px0, y + h * 0.52, px0 + w * 0.30, y + h - 16],
                fill=(110, 76, 50))
    d.rectangle([px0 - 6, y + h * 0.46, px0 + w * 0.30 + 6, y + h * 0.52],
                fill=(90, 60, 40))
    d.line([px0 + w * 0.15, y + h * 0.46, px0 + w * 0.15, y + h * 0.30],
           fill=INK, width=2)
    d.ellipse([px0 + w * 0.15 - 4, y + h * 0.30 - 4,
               px0 + w * 0.15 + 4, y + h * 0.30 + 4], fill=INK)
    # strip of small flags along the bottom
    cols = [(0, 51, 153), (200, 16, 46), (0, 122, 61), (255, 210, 0),
            (46, 109, 164), (120, 60, 140)]
    fw, fh = 30, 10
    fy = y + h - 13
    total = len(cols) * (fw + 6) - 6
    fx = x + (w - total) / 2
    for i, col in enumerate(cols):
        d.rectangle([fx + i * (fw + 6), fy, fx + i * (fw + 6) + fw, fy + fh],
                    fill=col, outline=INK, width=1)


def scene_markets(d, x, y, w, h):
    """A market chart falling: red bars stepping down, a bold down
    arrow, and the day's percentage in red."""
    d.rectangle([x, y, x + w, y + h], fill=(244, 244, 242))
    d.line([x + 14, y + h - 26, x + w - 14, y + h - 26], fill=INK, width=2)
    d.line([x + 14, y + 14, x + 14, y + h - 26], fill=INK, width=2)
    step = (w - 52) / 6
    bw = max(8, int(step - 8))
    for i, bh in enumerate((0.24, 0.32, 0.30, 0.44, 0.50, 0.62)):
        bh_px = h * bh
        bx = x + 26 + i * step
        d.rectangle([bx, y + h - 26 - bh_px, bx + bw, y + h - 26],
                    fill=(200, 50, 44))
    # down arrow across the bars
    d.line([x + 30, y + 30, x + w - 40, y + h - 60], fill=RED, width=6)
    d.polygon([(x + w - 40, y + h - 60), (x + w - 66, y + h - 62),
               (x + w - 44, y + h - 36)], fill=RED)
    d.text((x + w - 10, y + 8), "-3.7%", font=load(BOLD, 20), fill=RED,
           anchor="ra")


def scene_mercury(d, x, y, w, h):
    """Deep space: a cratered Mercury filling the frame and a small
    two-panel spacecraft arriving from the right."""
    d.rectangle([x, y, x + w, y + h], fill=(10, 12, 24))
    for sx, sy in ((x + 22, y + 14), (x + 70, y + 40), (x + 130, y + 10),
                   (x + 190, y + 30), (x + 240, y + 12), (x + 290, y + 36),
                   (x + 340, y + 16), (x + 400, y + 28)):
        d.ellipse([sx - 1, sy - 1, sx + 1, sy + 1], fill=(255, 255, 255))
    cx, cy, r = x + w * 0.36, y + h * 0.56, 62
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(178, 164, 148))
    for ox, oy, cr in ((-24, -18, 12), (14, -28, 9), (26, 8, 14),
                       (-8, 22, 10), (30, -2, 6), (-30, 8, 7)):
        d.ellipse([cx + ox - cr, cy + oy - cr, cx + ox + cr, cy + oy + cr],
                  fill=(140, 128, 112))
        d.ellipse([cx + ox - cr + 3, cy + oy - cr + 3,
                   cx + ox + cr - 3, cy + oy + cr - 3], fill=(168, 154, 138))
    # spacecraft: body plus two solar wings
    sx, sy = x + w * 0.72, y + h * 0.30
    d.rectangle([sx - 34, sy - 8, sx - 6, sy + 8], fill=(60, 110, 190))
    d.rectangle([sx + 6, sy - 8, sx + 34, sy + 8], fill=(60, 110, 190))
    d.rectangle([sx - 8, sy - 12, sx + 8, sy + 12], fill=(220, 220, 220))
    d.ellipse([sx - 4, sy - 4, sx + 4, sy + 4], fill=RED)
    d.line([sx, sy + 12, cx + 30, cy - 30], fill=(255, 220, 120), width=2)


# ------------------------------------------------------------------- page
def main():
    img = Image.new("RGB", (PAGE, PAGE), PAPER)
    d = ImageDraw.Draw(img)
    M = 36

    d.text((PAGE / 2, 18), "T H E   W O R L D   I N   O N E   I M A G E",
           font=load(BOLD, 26), fill=INK, anchor="ma")
    date_font = load(BOLD, 62)
    while d.textlength("SATURDAY 21 NOVEMBER 2026", font=date_font) > PAGE - 2 * M:
        date_font = load(BOLD, date_font.size - 2)
    d.text((PAGE / 2, 52), "SATURDAY 21 NOVEMBER 2026", font=date_font,
           fill=INK, anchor="ma")
    d.line([M, 138, PAGE - M, 138], fill=INK, width=5)
    d.line([M, 146, PAGE - M, 146], fill=INK, width=2)

    # lead: Iran strikes US bases in Bahrain
    d.rectangle([M, 162, PAGE - M, 442], outline=INK, width=3)
    scene_bahrain(d, M + 10, 172, 452, 260)
    lx = M + 486
    d.text((lx, 180), "GULF \u00b7 IRAN\u2013US", font=load(BOLD, 22), fill=RED)
    y = block(d, lx, 212, "IRAN STRIKES US BASES IN BAHRAIN",
              load(BOLD, 40), INK, PAGE - M - lx - 8)
    block(d, lx, y + 8,
          "Tehran says missiles and drones hit two US Patriot radars; "
          "Bahrain says a civilian industrial site was hit and set "
          "ablaze \u2014 no injuries.",
          load(PLAIN, 22), GREY, PAGE - M - lx - 8)

    # row of three
    y0, y1 = 456, 716
    cw = (PAGE - 2 * M - 24) // 3
    cells = [
        (scene_sinaloa, "MEXICO \u00b7 JUSTICE",
         "MEXICO CAPTURES \u2018EL CHAPO ISIDRO\u2019",
         "FBI Top 10 fugitive seized in Sinaloa; 11 killed in the backlash."),
        (scene_kryvyi, "UKRAINE \u00b7 WAR",
         "MISSILE HITS ZELENSKYY\u2019S HOMETOWN",
         "Two killed, a boy of 7 among them; about 60 wounded."),
        (scene_cop31, "CLIMATE \u00b7 COP31",
         "COP31 RUNS INTO OVERTIME",
         "Antalya talks pass the deadline with no deal; draft drops fossil fuels."),
    ]
    for i, (scene, tag, head, body) in enumerate(cells):
        x0 = M + i * (cw + 12)
        d.rectangle([x0, y0, x0 + cw, y1], outline=INK, width=3)
        scene(d, x0 + 8, y0 + 8, cw - 16, 84)
        panel_text(d, x0 + 12, y0 + 102, cw - 24, tag, head, body)

    # row of two
    y0, y1 = 730, 950
    cw2 = (PAGE - 2 * M - 12) // 2
    cells2 = [
        (scene_markets, "ECONOMY \u00b7 MARKETS",
         "WALL STREET SLIDES INTO CORRECTION",
         "S&P 500 falls 3.7% as AI shares slide; the Nasdaq wipes out "
         "its 2026 gains."),
        (scene_mercury, "SPACE \u00b7 ESA\u2013JAXA",
         "BEPICOLOMBO REACHES MERCURY",
         "Probe enters orbit after 8 years and 10 billion km; only the "
         "second mission ever to orbit the planet."),
    ]
    for i, (scene, tag, head, body) in enumerate(cells2):
        x0 = M + i * (cw2 + 12)
        d.rectangle([x0, y0, x0 + cw2, y1], outline=INK, width=3)
        scene(d, x0 + 8, y0 + 8, 168, y1 - y0 - 16)
        panel_text(d, x0 + 188, y0 + 12, cw2 - 200, tag, head, body,
                   head_size=26)

    d.line([M, 958, PAGE - M, 958], fill=INK, width=3)
    block(d, M, 966,
          "ALSO TODAY \u00b7 Trump: FBI database hack \u2018not good\u2019 \u00b7 "
          "Drones set a Russian ship ablaze in the Gulf of Finland \u00b7 "
          "Wolbachia mosquitoes cut dengue 69% in Brazil",
          load(BOLD, 18), INK, PAGE - 2 * M, centre=True)

    img.save("entry.png", optimize=True)
    print("wrote entry.png")


if __name__ == "__main__":
    main()
