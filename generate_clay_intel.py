"""
Company Intel - Clay.com SCOUT Research
2-Slide Executive Deck - High contrast, readable, professional
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
import os

# High-contrast color system
NAVY = RGBColor(0x1B, 0x2A, 0x4A)
BLUE = RGBColor(0x00, 0x78, 0xD4)
TEAL = RGBColor(0x00, 0xB2, 0x94)
RED = RGBColor(0xD1, 0x34, 0x38)
GOLD = RGBColor(0xC8, 0x96, 0x00)
PURPLE = RGBColor(0x5C, 0x2D, 0x91)
GREEN = RGBColor(0x10, 0x7C, 0x10)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
BLACK = RGBColor(0x1A, 0x1A, 0x1A)
DARK_GRAY = RGBColor(0x33, 0x33, 0x33)
MID_GRAY = RGBColor(0x55, 0x55, 0x55)
LIGHT_GRAY = RGBColor(0xF5, 0xF5, 0xF5)
CARD_WHITE = RGBColor(0xFF, 0xFF, 0xFF)
BORDER = RGBColor(0xDD, 0xDD, 0xDD)

SW = Inches(13.333)
SH = Inches(7.5)


def rect(s, l, t, w, h, c):
    sh = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, l, t, w, h)
    sh.fill.solid()
    sh.fill.fore_color.rgb = c
    sh.line.fill.background()
    return sh


def rnd(s, l, t, w, h, fill, border=None):
    sh = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, l, t, w, h)
    sh.fill.solid()
    sh.fill.fore_color.rgb = fill
    if border:
        sh.line.color.rgb = border
        sh.line.width = Pt(1)
    else:
        sh.line.fill.background()
    return sh


def tx(s, l, t, w, h, text, sz=12, c=BLACK, bold=False, al=PP_ALIGN.LEFT, fn="Segoe UI"):
    b = s.shapes.add_textbox(l, t, w, h)
    tf = b.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = text
    p.font.size = Pt(sz)
    p.font.color.rgb = c
    p.font.bold = bold
    p.font.name = fn
    p.alignment = al
    return b


def pill(s, l, t, text, color, w=Inches(1.1)):
    rnd(s, l, t, w, Inches(0.28), color)
    tx(s, l, t + Inches(0.01), w, Inches(0.26),
       text, sz=8.5, c=WHITE, bold=True, al=PP_ALIGN.CENTER)


def metric_box(s, x, y, num, label, accent):
    rnd(s, x, y, Inches(1.9), Inches(0.95), CARD_WHITE, BORDER)
    rect(s, x, y, Inches(1.9), Pt(5), accent)
    tx(s, x, y + Inches(0.12), Inches(1.9), Inches(0.4),
       num, sz=22, c=accent, bold=True, al=PP_ALIGN.CENTER, fn="Segoe UI Semibold")
    tx(s, x, y + Inches(0.55), Inches(1.9), Inches(0.3),
       label, sz=9.5, c=MID_GRAY, al=PP_ALIGN.CENTER)


def slide_1(prs):
    """Slide 1: Company Overview, Metrics, Positioning"""
    sl = prs.slides.add_slide(prs.slide_layouts[6])
    sl.background.fill.solid()
    sl.background.fill.fore_color.rgb = LIGHT_GRAY

    # Header
    rect(sl, Inches(0), Inches(0), SW, Inches(1.15), NAVY)
    rect(sl, Inches(0), Inches(0), SW, Pt(5), BLUE)
    tx(sl, Inches(0.7), Inches(0.15), Inches(5), Inches(0.5),
       "Clay", sz=32, c=WHITE, bold=True, fn="Segoe UI Semibold")
    tx(sl, Inches(0.7), Inches(0.62), Inches(6), Inches(0.3),
       "COMPANY OVERVIEW  AND  POSITIONING", sz=11, c=TEAL, bold=True)
    tx(sl, Inches(8.5), Inches(0.22), Inches(4.5), Inches(0.35),
       "clay.com  |  April 2026", sz=11, c=WHITE, al=PP_ALIGN.RIGHT)
    tx(sl, Inches(8.5), Inches(0.58), Inches(4.5), Inches(0.3),
       "SCOUT Framework  |  Company Intelligence Brief", sz=9, c=RGBColor(0x99, 0xAA, 0xBB), al=PP_ALIGN.RIGHT)

    # Metrics row
    ms = [
        ("300K+", "GTM Teams", BLUE),
        ("150+", "Data Providers", TEAL),
        ("140M", "Monthly AI Runs", PURPLE),
        ("26", "Customers Found", RED),
        ("16", "Published Case Studies", GREEN),
        ("SOC 2 + ISO", "Compliance Certified", NAVY),
    ]
    for i, (n, l, c) in enumerate(ms):
        metric_box(sl, Inches(0.45 + i * 2.1), Inches(1.35), n, l, c)

    # Left card: What they do + capabilities
    rnd(sl, Inches(0.4), Inches(2.55), Inches(6.0), Inches(3.05), CARD_WHITE, BORDER)
    rect(sl, Inches(0.4), Inches(2.55), Inches(6.0), Pt(5), BLUE)
    tx(sl, Inches(0.65), Inches(2.65), Inches(4), Inches(0.3),
       "WHAT THEY DO", sz=12, c=BLUE, bold=True)
    tx(sl, Inches(0.65), Inches(3.0), Inches(5.5), Inches(0.8),
       "AI-powered GTM data platform combining 150+ enrichment providers, "
       "intent signals, and CRM data. Enables sales and marketing teams to "
       "find, enrich, and reach best-fit customers at scale. One person can "
       "run campaigns that previously required the entire GTM team.",
       sz=11, c=DARK_GRAY)

    tx(sl, Inches(0.65), Inches(3.85), Inches(4), Inches(0.3),
       "KEY CAPABILITIES", sz=11, c=BLUE, bold=True)
    caps = [
        "Data enrichment from 150+ providers in one platform",
        "AI research agent builder (Claygent) with MCP support",
        "Real-time intent signal monitoring across channels",
        "CRM sync and workflow orchestration at scale",
        "Native email sequencer for outbound campaigns",
    ]
    for i, cap in enumerate(caps):
        tx(sl, Inches(0.75), Inches(4.15 + i * 0.27), Inches(5.4), Inches(0.25),
           f"    {cap}", sz=10.5, c=DARK_GRAY)

    # Right card: Positioning + audience
    rnd(sl, Inches(6.6), Inches(2.55), Inches(6.3), Inches(3.05), CARD_WHITE, BORDER)
    rect(sl, Inches(6.6), Inches(2.55), Inches(6.3), Pt(5), TEAL)
    tx(sl, Inches(6.85), Inches(2.65), Inches(5), Inches(0.3),
       "POSITIONING", sz=12, c=TEAL, bold=True)
    tx(sl, Inches(6.85), Inches(3.0), Inches(5.8), Inches(0.7),
       '"Every GTM data point imaginable, in one place."\n\n'
       'Understand your total market, your customers, and the gap '
       'between them. Then act on it.',
       sz=11, c=DARK_GRAY)

    tx(sl, Inches(6.85), Inches(3.85), Inches(5), Inches(0.3),
       "TARGET BUYERS", sz=11, c=TEAL, bold=True)
    buyers = [
        ("Revenue Ops / Sales Ops", "Primary buyer, data enrichment owner"),
        ("Growth / Demand Gen", "Outbound campaigns, lead scoring"),
        ("Marketing Operations", "CRM hygiene, audience segmentation"),
        ("C-Suite (CEO, CRO)", "Executive champions in testimonials"),
    ]
    for i, (role, ctx) in enumerate(buyers):
        y = Inches(4.15) + Inches(i * 0.32)
        tx(sl, Inches(6.95), y, Inches(2.6), Inches(0.28),
           role, sz=10.5, c=DARK_GRAY, bold=True)
        tx(sl, Inches(9.7), y, Inches(3.0), Inches(0.28),
           ctx, sz=10, c=MID_GRAY)

    # Bottom: Quote + Segments
    rect(sl, Inches(0.4), Inches(5.8), Inches(12.4), Inches(0.75), NAVY)
    tx(sl, Inches(0.7), Inches(5.85), Inches(9), Inches(0.35),
       '"Clay is a game changer for marketing, data, and operations. '
       'We have 3x our enrichment rate with Clay\'s combination of data providers."',
       sz=11, c=WHITE)
    tx(sl, Inches(0.7), Inches(6.2), Inches(6), Inches(0.25),
       "Adam Wall, Head of Sales Operations, Anthropic", sz=10, c=TEAL, bold=True)

    # Segment pills
    segs = [("AI / ML", PURPLE), ("SaaS", BLUE), ("Security", RED), ("Fintech", TEAL), ("Enterprise", GREEN)]
    for i, (seg, color) in enumerate(segs):
        pill(sl, Inches(9.6 + i * 0.85), Inches(6.0), seg, color, Inches(0.78))
    tx(sl, Inches(9.6), Inches(6.28), Inches(4.2), Inches(0.2),
       "Customer Segments", sz=8, c=RGBColor(0x99, 0xAA, 0xBB), al=PP_ALIGN.CENTER)

    # Footer
    tx(sl, Inches(0.7), Inches(6.75), Inches(12), Inches(0.2),
       "Source: clay.com  |  SCOUT Framework  |  ISV Intel", sz=8, c=MID_GRAY)


def slide_2(prs):
    """Slide 2: Full Customer Evidence Map"""
    sl = prs.slides.add_slide(prs.slide_layouts[6])
    sl.background.fill.solid()
    sl.background.fill.fore_color.rgb = LIGHT_GRAY

    # Header
    rect(sl, Inches(0), Inches(0), SW, Inches(1.15), NAVY)
    rect(sl, Inches(0), Inches(0), SW, Pt(5), TEAL)
    tx(sl, Inches(0.7), Inches(0.15), Inches(8), Inches(0.5),
       "Clay  |  Customer Evidence Map", sz=28, c=WHITE, bold=True, fn="Segoe UI Semibold")
    tx(sl, Inches(0.7), Inches(0.62), Inches(8), Inches(0.3),
       "26 CUSTOMERS  |  16 CASE STUDIES  |  10 LOGO FEATURES", sz=11, c=TEAL, bold=True)
    tx(sl, Inches(9.5), Inches(0.4), Inches(3.5), Inches(0.3),
       "clay.com  |  April 2026", sz=10, c=WHITE, al=PP_ALIGN.RIGHT)

    # Case study grid - 2 columns, 8 per column
    rnd(sl, Inches(0.4), Inches(1.3), Inches(12.5), Inches(4.45), CARD_WHITE, BORDER)
    rect(sl, Inches(0.4), Inches(1.3), Inches(12.5), Pt(5), TEAL)
    tx(sl, Inches(0.65), Inches(1.4), Inches(5), Inches(0.3),
       "CASE STUDIES WITH QUOTES (16)", sz=12, c=TEAL, bold=True)

    # Column headers
    for x_off in [Inches(0.55), Inches(6.55)]:
        tx(sl, x_off + Inches(0.4), Inches(1.75), Inches(1.8), Inches(0.22),
           "Customer", sz=9, c=MID_GRAY, bold=True)
        tx(sl, x_off + Inches(2.3), Inches(1.75), Inches(1.5), Inches(0.22),
           "Key Result", sz=9, c=MID_GRAY, bold=True)
        tx(sl, x_off + Inches(3.8), Inches(1.75), Inches(2.2), Inches(0.22),
           "Contact", sz=9, c=MID_GRAY, bold=True)

    cases_l = [
        ("OpenAI", "2x enrichment coverage", "Scotty Huhn, Revenue Strategy"),
        ("Anthropic", "3x enrichment rate", "Adam Wall, Head of Sales Ops"),
        ("Rippling", "2x email performance", "Ryan Narod, VP Corp. Mktg"),
        ("Figma", "GTM orchestration layer", "Kyle Ketchum, Marketing Ops"),
        ("Intercom", "Consolidated data sources", "A. DeMoulin, Dir. GTM Ops"),
        ("Verkada", "Automated enrichment", "Davide Grieco, Dir. Growth"),
        ("Mistral AI", "25K accounts / 2 weeks", "Joel Davidson, VP RevOps"),
        ("Vanta", "Essential GTM pillar", "Stevie Case, CRO"),
    ]
    cases_r = [
        ("ElevenLabs", "Auto lead pre-qualification", "Raman Khanna, Growth"),
        ("Sendoso", "10x outbound productivity", "Kris Rudegraap, CEO"),
        ("Hex", "+50% win-rate", "Bryanna Clancy, GTM Eng."),
        ("Sana", "60% CRM accuracy lift", "F. Hillstrom, GTM Ops"),
        ("Rootly", "100% outbound automation", "JJ Tang, CEO & Co-founder"),
        ("Legora", "+70% campaign velocity", "F. Pavan, Dir. Demand Gen"),
        ("Exit Five", "27K contacts enriched", "Dan Murphy, COO"),
        ("depthfirst", "95%+ CRM fill rates", "Mark Hardy, Head of RevOps"),
    ]

    for i, (name, result, person) in enumerate(cases_l):
        y = Inches(2.0) + Inches(i * 0.42)
        bg_color = LIGHT_GRAY if i % 2 == 0 else CARD_WHITE
        rect(sl, Inches(0.55), y, Inches(5.9), Inches(0.38), bg_color)
        # Colored dot
        dot = sl.shapes.add_shape(MSO_SHAPE.OVAL, Inches(0.65), y + Inches(0.1), Inches(0.15), Inches(0.15))
        dot.fill.solid()
        dot.fill.fore_color.rgb = TEAL
        dot.line.fill.background()
        tx(sl, Inches(0.95), y + Inches(0.05), Inches(1.6), Inches(0.28),
           name, sz=10.5, c=BLACK, bold=True)
        tx(sl, Inches(2.85), y + Inches(0.05), Inches(1.6), Inches(0.28),
           result, sz=10, c=BLUE, bold=True)
        tx(sl, Inches(4.35), y + Inches(0.05), Inches(2.1), Inches(0.28),
           person, sz=9, c=MID_GRAY)

    for i, (name, result, person) in enumerate(cases_r):
        y = Inches(2.0) + Inches(i * 0.42)
        bg_color = LIGHT_GRAY if i % 2 == 0 else CARD_WHITE
        rect(sl, Inches(6.55), y, Inches(6.25), Inches(0.38), bg_color)
        dot = sl.shapes.add_shape(MSO_SHAPE.OVAL, Inches(6.65), y + Inches(0.1), Inches(0.15), Inches(0.15))
        dot.fill.solid()
        dot.fill.fore_color.rgb = PURPLE
        dot.line.fill.background()
        tx(sl, Inches(6.95), y + Inches(0.05), Inches(1.5), Inches(0.28),
           name, sz=10.5, c=BLACK, bold=True)
        tx(sl, Inches(8.85), y + Inches(0.05), Inches(1.8), Inches(0.28),
           result, sz=10, c=BLUE, bold=True)
        tx(sl, Inches(10.35), y + Inches(0.05), Inches(2.3), Inches(0.28),
           person, sz=9, c=MID_GRAY)

    # Logo features bar
    rect(sl, Inches(0.4), Inches(5.95), Inches(12.5), Inches(1.3), NAVY)
    tx(sl, Inches(0.7), Inches(6.02), Inches(5), Inches(0.3),
       "ALSO FEATURED (LOGOS AND PARTNERS)", sz=11, c=TEAL, bold=True)

    logos = ["HubSpot", "Notion", "Ramp", "Grafana", "Cursor", "Okta", "Klaviyo", "Uber", "Canva", "Google"]
    for i, name in enumerate(logos):
        x = Inches(0.6) + Inches(i * 1.26)
        rnd(sl, x, Inches(6.4), Inches(1.12), Inches(0.35), BLUE)
        tx(sl, x, Inches(6.41), Inches(1.12), Inches(0.33),
           name, sz=9.5, c=WHITE, bold=True, al=PP_ALIGN.CENTER)

    tx(sl, Inches(0.7), Inches(6.85), Inches(12), Inches(0.2),
       "Source: clay.com homepage, /customers, /about  |  Researched via SCOUT Framework  |  ISV Intel  |  April 2026",
       sz=8.5, c=RGBColor(0x99, 0xAA, 0xBB))


def main():
    prs = Presentation()
    prs.slide_width = SW
    prs.slide_height = SH
    slide_1(prs)
    slide_2(prs)
    out = os.path.join(os.path.expanduser("~"), "Desktop", "clay-company-intel.pptx")
    prs.save(out)
    print(f"Saved: {out}")
    return out


if __name__ == "__main__":
    main()
