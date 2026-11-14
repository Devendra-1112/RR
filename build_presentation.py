import json
import collections
import collections.abc
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    RR_PINK = RGBColor(228, 0, 124)
    RR_NAVY = RGBColor(11, 27, 61)
    RR_DARK = RGBColor(8, 14, 30)
    RR_CARD_BG = RGBColor(18, 30, 58)
    RR_WHITE = RGBColor(255, 255, 255)
    RR_MUTED = RGBColor(160, 175, 200)
    RR_ACCENT_GREEN = RGBColor(16, 185, 129)
    RR_ACCENT_AMBER = RGBColor(245, 158, 11)
    RR_ACCENT_ROSE = RGBColor(239, 68, 68)
    RR_ACCENT_BLUE = RGBColor(59, 130, 246)
    RR_BORDER = RGBColor(40, 60, 100)

    with open('strict_verification_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    eligible_batters = data['verified_eligible_batters']
    eligible_bowlers = data['verified_eligible_bowlers']

    def add_bg(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = RR_DARK
        bg.line.fill.background()
        return bg

    def add_header(slide, title_text, category="RAJASTHAN ROYALS • IPL 2027 AUCTION WAR ROOM"):
        top_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, Inches(0.08))
        top_bar.fill.solid()
        top_bar.fill.fore_color.rgb = RR_PINK
        top_bar.line.fill.background()

        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11), Inches(0.35))
        tf_cat = cat_box.text_frame
        tf_cat.word_wrap = True
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = category.upper()
        p_cat.font.size = Pt(11)
        p_cat.font.bold = True
        p_cat.font.color.rgb = RR_PINK

        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.7), Inches(11.5), Inches(0.7))
        tf = title_box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title_text
        p.font.size = Pt(22)
        p.font.bold = True
        p.font.color.rgb = RR_WHITE

    def add_card(slide, left, top, width, height, fill_color=RR_CARD_BG, border_color=RR_BORDER):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = fill_color
        card.line.color.rgb = border_color
        card.line.width = Pt(1)
        return card

    # SLIDE 1: TITLE SLIDE
    s1 = prs.slides.add_slide(blank_layout)
    add_bg(s1)
    top_line = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, Inches(0.12))
    top_line.fill.solid()
    top_line.fill.fore_color.rgb = RR_PINK
    top_line.line.fill.background()

    tbox = s1.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(11.3), Inches(3.2))
    tf1 = tbox.text_frame
    tf1.word_wrap = True
    p0 = tf1.paragraphs[0]
    p0.text = "RAJASTHAN ROYALS  |  IPL 2027 AUCTION INTELLIGENCE WAR ROOM"
    p0.font.size = Pt(14)
    p0.font.bold = True
    p0.font.color.rgb = RR_PINK
    p0.space_after = Pt(12)

    p1 = tf1.add_paragraph()
    p1.text = "Targeting the Most Reliable Players Under Pressure"
    p1.font.size = Pt(36)
    p1.font.bold = True
    p1.font.color.rgb = RR_WHITE
    p1.space_after = Pt(10)

    p2 = tf1.add_paragraph()
    p2.text = "Strict Zero-Predictions Standard • Grounded in Official BCCI/IPL Ratification"
    p2.font.size = Pt(18)
    p2.font.color.rgb = RR_MUTED

    card_meta = add_card(s1, Inches(1.0), Inches(5.2), Inches(11.3), Inches(1.4))
    tbox_meta = s1.shapes.add_textbox(Inches(1.2), Inches(5.35), Inches(10.9), Inches(1.1))
    tf_m = tbox_meta.text_frame
    p_m1 = tf_m.paragraphs[0]
    p_m1.text = "SupeRR Selector Season 2 • Round 1 Official Submission"
    p_m1.font.size = Pt(13)
    p_m1.font.bold = True
    p_m1.font.color.rgb = RR_PINK
    p_m2 = tf_m.add_paragraph()
    p_m2.text = "200,999 Balls Screened • 81,722 Pressure Deliveries • Nov 17, 2026 BCCI Deadline Compliance • Dec 16, 2026 Auction (Goa)"
    p_m2.font.size = Pt(11)
    p_m2.font.color.rgb = RR_WHITE

    # SLIDE 2: STRICT GOVERNANCE & 3-STATUS TAXONOMY
    s2 = prs.slides.add_slide(blank_layout)
    add_bg(s2)
    add_header(s2, "Strict Zero-Predictions Standard & Status Taxonomy", "AUCTION GOVERNANCE PROTOCOL")

    c1 = add_card(s2, Inches(0.8), Inches(1.6), Inches(3.7), Inches(5.2), border_color=RR_ACCENT_GREEN)
    tb1 = s2.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(3.3), Inches(4.8))
    tf_c1 = tb1.text_frame
    tf_c1.word_wrap = True
    p = tf_c1.paragraphs[0]
    p.text = "CATEGORY A: VERIFIED ELIGIBLE"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = RR_ACCENT_GREEN
    p.space_after = Pt(8)
    p = tf_c1.add_paragraph()
    p.text = "• Officially confirmed uncontracted international / associate entrants.\n• Verified registration in IPL 2027 auction pool.\n• Independent free agents with no active IPL contract.\n• Exactly 6 Batters & 4 Bowlers qualify under statistical filters.\n• Strictly realistic targets RR can legally acquire."
    p.font.size = Pt(11)
    p.font.color.rgb = RR_WHITE

    c2 = add_card(s2, Inches(4.8), Inches(1.6), Inches(3.7), Inches(5.2), border_color=RR_ACCENT_ROSE)
    tb2 = s2.shapes.add_textbox(Inches(5.0), Inches(1.8), Inches(3.3), Inches(4.8))
    tf_c2 = tb2.text_frame
    tf_c2.word_wrap = True
    p = tf_c2.paragraphs[0]
    p.text = "CATEGORY B: VERIFIED UNAVAILABLE"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = RR_ACCENT_ROSE
    p.space_after = Pt(8)
    p = tf_c2.add_paragraph()
    p.text = "• Formally Retained Marquee Cores (Bumrah ₹18 Cr, Kohli ₹21 Cr, Klaasen ₹23 Cr, Gaikwad ₹18 Cr, Rashid Khan ₹18 Cr).\n• Formally Retired (Dhawan, Karthik).\n• RR Retained Core (Samson, Jaiswal, Parag, Jurel, Hetmyer, Sandeep Sharma).\n• Legally bound; strictly non-purchasable. Bidding prohibited."
    p.font.size = Pt(11)
    p.font.color.rgb = RR_WHITE

    c3 = add_card(s2, Inches(8.8), Inches(1.6), Inches(3.7), Inches(5.2), border_color=RR_ACCENT_AMBER)
    tb3 = s2.shapes.add_textbox(Inches(9.0), Inches(1.8), Inches(3.3), Inches(4.8))
    tf_c3 = tb3.text_frame
    tf_c3.word_wrap = True
    p = tf_c3.paragraphs[0]
    p.text = "CATEGORY C: NOT YET VERIFIED"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = RR_ACCENT_AMBER
    p.space_after = Pt(8)
    p = tf_c3.add_paragraph()
    p.text = "• Contracted IPL 2026 players (Arshdeep, Pant, Shreyas, Naman Dhir, Shashank, Bhuvneshwar).\n• Official BCCI retention/release deadline extended to Nov 17, 2026.\n• Release lists not yet published.\n• Mandatory Notice: OFFICIAL IPL 2027 AUCTION ELIGIBILITY NOT YET ESTABLISHED — EXCLUDED FROM RECOMMENDATIONS."
    p.font.size = Pt(11)
    p.font.color.rgb = RR_WHITE

    # SLIDE 3: DATASET RIGOR & PPI METHODOLOGY
    s3 = prs.slides.add_slide(blank_layout)
    add_bg(s3)
    add_header(s3, "Comprehensive Dataset Rigor & Pressure Performance Index (PPI)", "DATA SCIENCE METHODOLOGY")

    card_d1 = add_card(s3, Inches(0.8), Inches(1.6), Inches(5.7), Inches(5.2))
    tb_d1 = s3.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(5.3), Inches(4.8))
    tf_d1 = tb_d1.text_frame
    tf_d1.word_wrap = True
    p = tf_d1.paragraphs[0]
    p.text = "DATA PREPROCESSING & LEGAL BALL ACCOUNTING"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = RR_PINK
    p.space_after = Pt(8)
    p = tf_d1.add_paragraph()
    p.text = (
        "• Total Deliveries Analyzed: 200,999 across 883 matches (371 IPL + 512 T20Is).\n"
        "• Pressure Deliveries Identified: 81,722 high-leverage balls.\n"
        "• Innings 1 totals tracked delivery-by-delivery to determine live Required Run Rates (RRR).\n"
        "• Extras Handling: Wides and oversteps excluded from batter balls faced; wides excluded from bowler legal balls; penalty and extra runs strictly charged to bowler bowling economy.\n"
        "• Dismissal Validity: Run-outs excluded from bowler wickets; only Bowled, Caught, LBW, Stumped, Caught & Bowled, and Hit Wicket counted."
    )
    p.font.size = Pt(11)
    p.font.color.rgb = RR_WHITE

    card_d2 = add_card(s3, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2))
    tb_d2 = s3.shapes.add_textbox(Inches(7.0), Inches(1.8), Inches(5.3), Inches(4.8))
    tf_d2 = tb_d2.text_frame
    tf_d2.word_wrap = True
    p = tf_d2.paragraphs[0]
    p.text = "MULTI-DIMENSIONAL PRESSURE PERFORMANCE INDEX"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = RR_ACCENT_BLUE
    p.space_after = Pt(8)
    p = tf_d2.add_paragraph()
    p.text = (
        "• Pressure Condition Definitions:\n"
        "  1. Death overs (16–20) in 1st & 2nd innings.\n"
        "  2. Steep Chases (RRR >= 9.80, or <= 36 balls with >= 35 runs needed).\n"
        "  3. Collapse Rescue (<= 6 overs with >= 3 wickets down).\n"
        "  4. Knockout Matches (Overs 12–20 in playoffs / finals).\n\n"
        "• Batter PPI Formula: Weighted sum of Pressure Strike Rate (0.35), Pressure Average (0.35), SR Delta vs Baseline (0.35), and Dot-Ball Suppression (0.40).\n\n"
        "• Bowler PPI Formula: Weighted sum of Pressure Economy (7.0), Clutch Wickets (2.0), Dot Ball % (0.6), and Economy Delta vs Baseline (3.0).\n\n"
        "• Reliability Scaling: Sample size dampener applies sqrt(balls/180) to prevent small-sample distortion."
    )
    p.font.size = Pt(10.5)
    p.font.color.rgb = RR_WHITE

    # SLIDE 4: SECTION 1 — TOP 6 VERIFIED BATTERS
    s4 = prs.slides.add_slide(blank_layout)
    add_bg(s4)
    add_header(s4, "Section 1: Top 6 Verified Auction-Eligible Batters", "TARGET RECOMMENDATIONS")

    # Table of 6 Batters
    rows = len(eligible_batters) + 1
    cols = 9
    table_shape = s4.shapes.add_table(rows, cols, Inches(0.8), Inches(1.6), Inches(11.7), Inches(5.2))
    tbl = table_shape.table
    tbl.columns[0].width = Inches(0.6)
    tbl.columns[1].width = Inches(1.8)
    tbl.columns[2].width = Inches(1.4)
    tbl.columns[3].width = Inches(1.1)
    tbl.columns[4].width = Inches(1.1)
    tbl.columns[5].width = Inches(1.1)
    tbl.columns[6].width = Inches(1.1)
    tbl.columns[7].width = Inches(1.3)
    tbl.columns[8].width = Inches(2.2)

    headers = ["#", "Player Name", "Player ID", "PPI Score", "Press SR", "Press Avg", "Press Balls", "Est. Value", "RR Tactical Fit & Role"]
    for j, h in enumerate(headers):
        cell = tbl.cell(0, j)
        cell.text = h
        cell.fill.solid()
        cell.fill.fore_color.rgb = RR_CARD_BG
        for p in cell.text_frame.paragraphs:
            p.font.size = Pt(10)
            p.font.bold = True
            p.font.color.rgb = RR_PINK

    for i, b in enumerate(eligible_batters, 1):
        vals = [
            f"#{b['rank']}",
            b['name'],
            b['player_id'],
            str(b['ppi_score']),
            f"{b['p_sr']}",
            f"{b['p_avg']}",
            str(b['p_balls']),
            b.get('price_range', '₹3-5 Cr'),
            b.get('why_target', 'Pressure enforcer')[:45] + '...'
        ]
        for j, v in enumerate(vals):
            cell = tbl.cell(i, j)
            cell.text = v
            cell.fill.solid()
            cell.fill.fore_color.rgb = RR_DARK if i % 2 == 0 else RR_CARD_BG
            for p in cell.text_frame.paragraphs:
                p.font.size = Pt(9.5)
                p.font.color.rgb = RR_WHITE
                if j in (0, 3): p.font.bold = True

    # SLIDE 5: SECTION 1 — TOP 4 VERIFIED BOWLERS
    s5 = prs.slides.add_slide(blank_layout)
    add_bg(s5)
    add_header(s5, "Section 1: Top 4 Verified Auction-Eligible Bowlers", "TARGET RECOMMENDATIONS")

    rows = len(eligible_bowlers) + 1
    cols = 9
    table_shape5 = s5.shapes.add_table(rows, cols, Inches(0.8), Inches(1.6), Inches(11.7), Inches(3.8))
    tbl5 = table_shape5.table
    tbl5.columns[0].width = Inches(0.6)
    tbl5.columns[1].width = Inches(1.8)
    tbl5.columns[2].width = Inches(1.4)
    tbl5.columns[3].width = Inches(1.1)
    tbl5.columns[4].width = Inches(1.1)
    tbl5.columns[5].width = Inches(1.1)
    tbl5.columns[6].width = Inches(1.1)
    tbl5.columns[7].width = Inches(1.3)
    tbl5.columns[8].width = Inches(2.2)

    headers5 = ["#", "Player Name", "Player ID", "PPI Score", "Press Econ", "Clutch Wkts", "Press Balls", "Est. Value", "RR Tactical Fit & Role"]
    for j, h in enumerate(headers5):
        cell = tbl5.cell(0, j)
        cell.text = h
        cell.fill.solid()
        cell.fill.fore_color.rgb = RR_CARD_BG
        for p in cell.text_frame.paragraphs:
            p.font.size = Pt(10)
            p.font.bold = True
            p.font.color.rgb = RR_ACCENT_BLUE

    for i, w in enumerate(eligible_bowlers, 1):
        vals = [
            f"#{w['rank']}",
            w['name'],
            w['player_id'],
            str(w['ppi_score']),
            f"{w['p_econ']}",
            f"{w['p_wickets']}",
            str(w['p_balls']),
            w.get('price_range', '₹4-7 Cr'),
            w.get('why_target', 'Clutch bowler')[:45] + '...'
        ]
        for j, v in enumerate(vals):
            cell = tbl5.cell(i, j)
            cell.text = v
            cell.fill.solid()
            cell.fill.fore_color.rgb = RR_DARK if i % 2 == 0 else RR_CARD_BG
            for p in cell.text_frame.paragraphs:
                p.font.size = Pt(9.5)
                p.font.color.rgb = RR_WHITE
                if j in (0, 3): p.font.bold = True

    # Callout card on why 6 batters and 4 bowlers
    c_note = add_card(s5, Inches(0.8), Inches(5.6), Inches(11.7), Inches(1.3), border_color=RR_ACCENT_GREEN)
    tb_cn = s5.shapes.add_textbox(Inches(1.0), Inches(5.7), Inches(11.3), Inches(1.1))
    tf_cn = tb_cn.text_frame
    tf_cn.word_wrap = True
    p = tf_cn.paragraphs[0]
    p.text = "STRICT AUDIT INTEGRITY: ZERO BACKFILLING OF MISSING POSITIONS"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = RR_ACCENT_GREEN
    p = tf_cn.add_paragraph()
    p.text = "Per strict war room rules, if only 6 eligible batters and 4 eligible bowlers satisfy the verified uncontracted registration and minimum delivery criteria, display ONLY those players. Missing positions are never padded with unverified, contracted, or predicted players."
    p.font.size = Pt(10)
    p.font.color.rgb = RR_WHITE

    # SLIDE 6: SECTION 2 — VERIFIED UNAVAILABLE PLAYERS
    s6 = prs.slides.add_slide(blank_layout)
    add_bg(s6)
    add_header(s6, "Section 2: Verified Unavailable Players (Retained / Retired)", "LEGAL EXCLUSION AUDIT")

    c_un1 = add_card(s6, Inches(0.8), Inches(1.6), Inches(5.7), Inches(5.2), border_color=RR_ACCENT_ROSE)
    tb_un1 = s6.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(5.3), Inches(4.8))
    tf_un1 = tb_un1.text_frame
    tf_un1.word_wrap = True
    p = tf_un1.paragraphs[0]
    p.text = "CONFIRMED MARQUEE RETENTIONS (NON-PURCHASABLE)"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = RR_ACCENT_ROSE
    p.space_after = Pt(8)
    p = tf_un1.add_paragraph()
    p.text = (
        "• Jasprit Bumrah (Mumbai Indians) — Retained Marquee Core (₹18 Cr)\n"
        "• Virat Kohli (Royal Challengers Bengaluru) — Retained Core (₹21 Cr)\n"
        "• Heinrich Klaasen (Sunrisers Hyderabad) — Retained Marquee Core (₹23 Cr)\n"
        "• Ruturaj Gaikwad & Ravindra Jadeja (CSK) — Retained Cores (₹18 Cr each)\n"
        "• Rashid Khan (Gujarat Titans) — Retained Core (₹18 Cr)\n"
        "• Sunil Narine & Andre Russell (KKR) — Retained Cores (₹12 Cr each)\n"
        "• Axar Patel & Kuldeep Yadav (DC) — Retained Cores (₹16.5 & ₹13.25 Cr)\n"
        "• Nicholas Pooran (LSG) — Retained Core (₹21 Cr)\n\n"
        "LEGAL RESTRICTION: Contractually bound under formal BCCI IPL retention documents. Excluded from auction pool."
    )
    p.font.size = Pt(10)
    p.font.color.rgb = RR_WHITE

    c_un2 = add_card(s6, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2), border_color=RR_BORDER)
    tb_un2 = s6.shapes.add_textbox(Inches(7.0), Inches(1.8), Inches(5.3), Inches(4.8))
    tf_un2 = tb_un2.text_frame
    tf_un2.word_wrap = True
    p = tf_un2.paragraphs[0]
    p.text = "OFFICIALLY RETIRED PLAYERS & RR RETAINED CORE"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = RR_PINK
    p.space_after = Pt(8)
    p = tf_un2.add_paragraph()
    p.text = (
        "• Shikhar Dhawan: Officially announced retirement from all international, domestic, and IPL cricket on 24-08-2024. Ineligible for auction.\n\n"
        "• Dinesh Karthik: Formally retired post IPL 2024; appointed Royal Challengers Bengaluru Batting Coach and Mentor on 01-06-2024.\n\n"
        "• Rajasthan Royals Internal Retentions:\n"
        "  - Sanju Samson (Captain, ₹18 Cr)\n"
        "  - Yashasvi Jaiswal (Opener, ₹18 Cr)\n"
        "  - Riyan Parag (Middle Order, ₹14 Cr)\n"
        "  - Dhruv Jurel (Finisher / Keeper, ₹14 Cr)\n"
        "  - Shimron Hetmyer (Overseas Finisher, ₹11 Cr)\n"
        "  - Sandeep Sharma (Death Specialist, ₹4 Cr Uncapped)\n"
        "  Total Committed Retained Purse: ₹79.0 Crore."
    )
    p.font.size = Pt(10)
    p.font.color.rgb = RR_WHITE

    # SLIDE 7: SECTION 3 — NOT YET VERIFIED PLAYERS
    s7 = prs.slides.add_slide(blank_layout)
    add_bg(s7)
    add_header(s7, "Section 3: Not Yet Verified Players (Pending Nov 17 BCCI Deadline)", "GOVERNANCE COMPLIANCE")

    c_pen = add_card(s7, Inches(0.8), Inches(1.6), Inches(11.7), Inches(5.2), border_color=RR_ACCENT_AMBER)
    tb_pen = s7.shapes.add_textbox(Inches(1.1), Inches(1.8), Inches(11.1), Inches(4.8))
    tf_pen = tb_pen.text_frame
    tf_pen.word_wrap = True
    p = tf_pen.paragraphs[0]
    p.text = "MANDATORY COMPLIANCE NOTICE: AWAITING FORMAL BCCI RELEASE RATIFICATION"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = RR_ACCENT_AMBER
    p.space_after = Pt(10)
    p = tf_pen.add_paragraph()
    p.text = (
        "OFFICIAL IPL 2027 AUCTION ELIGIBILITY NOT YET ESTABLISHED — PLAYER EXCLUDED FROM FINAL RECOMMENDATIONS.\n\n"
        "• Regulatory Context:\n"
        "  The Board of Control for Cricket in India (BCCI) officially extended the franchise retention and release submission deadline to November 17, 2026. The mini-auction is scheduled for December 16, 2026 in Goa, with an updated team purse of ₹157.0 Crore.\n\n"
        "• Audit Treatment of Contracted Players:\n"
        "  Players currently associated with IPL 2026 squads (including Arshdeep Singh, Shreyas Iyer, Rishabh Pant, KL Rahul, Naman Dhir, Shashank Singh, Bhuvneshwar Kumar, Mohammed Siraj, and Harshal Patel) have NOT yet been officially released by their franchises.\n\n"
        "• Zero Speculation Standard:\n"
        "  Under strict war room rules, a player's recent form, age, squad omission, or media rumours DO NOT constitute evidence of release. Until the BCCI officially publishes and ratifies the 2027 release list on November 17, these players are categorized strictly as NOT YET VERIFIED and excluded from target recommendations."
    )
    p.font.size = Pt(11)
    p.font.color.rgb = RR_WHITE

    # SLIDE 8: SECTION 4 — EVIDENCE REGISTRY & SOURCES
    s8 = prs.slides.add_slide(blank_layout)
    add_bg(s8)
    add_header(s8, "Section 4: Authoritative Eligibility Evidence Registry", "EVIDENCE REPOSITORY")

    c_ev1 = add_card(s8, Inches(0.8), Inches(1.6), Inches(3.7), Inches(5.2))
    tb_ev1 = s8.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(3.3), Inches(4.8))
    tf_ev1 = tb_ev1.text_frame
    tf_ev1.word_wrap = True
    p = tf_ev1.paragraphs[0]
    p.text = "PRIMARY SOURCE 1: BCCI"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = RR_PINK
    p.space_after = Pt(8)
    p = tf_ev1.add_paragraph()
    p.text = (
        "• Source: Official BCCI Portal (bcci.tv)\n"
        "• Articles Audited:\n"
        "  - IPL 2027 retention deadline extension circular (Nov 17, 2026)\n"
        "  - Constitution player retirement ratifications (Dhawan, Karthik)\n"
        "  - Salary cap regulation (₹157.0 Cr team purse limit)\n"
        "• URL: https://www.bcci.tv"
    )
    p.font.size = Pt(10.5)
    p.font.color.rgb = RR_WHITE

    c_ev2 = add_card(s8, Inches(4.8), Inches(1.6), Inches(3.7), Inches(5.2))
    tb_ev2 = s8.shapes.add_textbox(Inches(5.0), Inches(1.8), Inches(3.3), Inches(4.8))
    tf_ev2 = tb_ev2.text_frame
    tf_ev2.word_wrap = True
    p = tf_ev2.paragraphs[0]
    p.text = "PRIMARY SOURCE 2: IPL PORTAL"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = RR_ACCENT_BLUE
    p.space_after = Pt(8)
    p = tf_ev2.add_paragraph()
    p.text = (
        "• Source: IPL Tournament Portal (iplt20.com/auction)\n"
        "• Announcements Audited:\n"
        "  - Official franchise retention lists\n"
        "  - Capped & uncapped auction registration pool notices\n"
        "  - Independent overseas entrant shortlists\n"
        "• URL: https://www.iplt20.com/auction"
    )
    p.font.size = Pt(10.5)
    p.font.color.rgb = RR_WHITE

    c_ev3 = add_card(s8, Inches(8.8), Inches(1.6), Inches(3.7), Inches(5.2))
    tb_ev3 = s8.shapes.add_textbox(Inches(9.0), Inches(1.8), Inches(3.3), Inches(4.8))
    tf_ev3 = tb_ev3.text_frame
    tf_ev3.word_wrap = True
    p = tf_ev3.paragraphs[0]
    p.text = "BALL-BY-BALL DATABASE"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = RR_ACCENT_GREEN
    p.space_after = Pt(8)
    p = tf_ev3.add_paragraph()
    p.text = (
        "• Scope: 200,999 deliveries (IPL 2022-2026 + T20Is)\n"
        "• 81,722 pressure deliveries parsed\n"
        "• 9 Mandatory Evidence Fields documented for every target:\n"
        "  Name, ID, Franchise, Release Confirmation, Registration Confirmation, Status, Source URL, Date, Timestamp & Notes."
    )
    p.font.size = Pt(10.5)
    p.font.color.rgb = RR_WHITE

    # SLIDE 9: SQUAD ARCHITECTURE & PLAYING XI SYNERGY
    s9 = prs.slides.add_slide(blank_layout)
    add_bg(s9)
    add_header(s9, "Rajasthan Royals Tactical Playing XI & Auction Strategy", "SQUAD SYNERGY")

    c_squad = add_card(s9, Inches(0.8), Inches(1.6), Inches(11.7), Inches(5.2))
    tb_sq = s9.shapes.add_textbox(Inches(1.1), Inches(1.8), Inches(11.1), Inches(4.8))
    tf_sq = tb_sq.text_frame
    tf_sq.word_wrap = True
    p = tf_sq.paragraphs[0]
    p.text = "TACTICAL PLAYING XI INTEGRATING VERIFIED TARGETS"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = RR_PINK
    p.space_after = Pt(8)
    p = tf_sq.add_paragraph()
    p.text = (
        "1. Yashasvi Jaiswal (Retained, ₹18 Cr) — Aggressive LH Opener\n"
        "2. Fakhar Zaman [Target #1 Batter] (₹4-7 Cr) — High-Tempo Enforcer; counters PP pressure\n"
        "3. Sanju Samson (Captain/WK, Retained, ₹18 Cr) — Middle-Order Anchor & Playmaker\n"
        "4. Riyan Parag (Retained, ₹14 Cr) — Spin Hitter & Middle Accelerator\n"
        "5. Dhruv Jurel (Retained, ₹14 Cr) — Clutch Finisher & High-Pressure Specialist\n"
        "6. Shimron Hetmyer (Overseas, Retained, ₹11 Cr) — Left-Handed Death Boundary Enforcer\n"
        "7. Asif Khan / Angelo Mathews [Target #2/4 Batter] (₹2-4 Cr) — Crisis Stabilizer / 196+ SR Finisher\n"
        "8. Jason Holder [Target #1 Bowler] (₹5-7 Cr) — Dual-Discipline Pace All-Rounder & Death Seamer\n"
        "9. Sandeep Sharma (Retained, ₹4 Cr Uncapped) — Elite Knuckle-ball & Wide Yorker Executioner\n"
        "10. Haris Rauf [Target #2 Bowler] (₹6-9 Cr) — 150+ kph Express Tearaway Spearhead\n"
        "11. Maheesh Theekshana / Mohammad Nawaz [Target #3/4 Bowler] (₹4-7 Cr) — Powerplay/Middle Restriction Spin\n\n"
        "Impact Player Strategies: Asif Khan (Chasing enforcer) or Tactical Domestic Seamer."
    )
    p.font.size = Pt(10)
    p.font.color.rgb = RR_WHITE

    prs.save("RR_SupeRR_Selector_Auction_Strategy.pptx")
    print("Presentation saved successfully as RR_SupeRR_Selector_Auction_Strategy.pptx!")

if __name__ == '__main__':
    create_deck()
