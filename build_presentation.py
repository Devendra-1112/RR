import json
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

    with open('ipl2027_official_teams_database.json', 'r', encoding='utf-8') as f:
        db = json.load(f)

    meta = db['metadata']
    top_batters = db['top_10_batters']
    top_bowlers = db['top_10_bowlers']
    franchises = db['franchises']
    rr_squad = db['rr_retained_squad']
    budget_a = db['budget_scenarios']['scenario_a_balanced']
    playing_xi = db['playing_xi']

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
    p2.text = "Official 18 November 2026 BCCI Retention & Trade Baseline • ITC Grand Goa (16-Dec-2026)"
    p2.font.size = Pt(18)
    p2.font.color.rgb = RR_MUTED

    card_meta = add_card(s1, Inches(1.0), Inches(5.2), Inches(11.3), Inches(1.4))
    tbox_meta = s1.shapes.add_textbox(Inches(1.2), Inches(5.35), Inches(10.9), Inches(1.1))
    tf_m = tbox_meta.text_frame
    p_m1 = tf_m.paragraphs[0]
    p_m1.text = "SupeRR Selector Season 2 • Round 1 Official Strategy Presentation"
    p_m1.font.size = Pt(13)
    p_m1.font.bold = True
    p_m1.font.color.rgb = RR_PINK
    p_m2 = tf_m.add_paragraph()
    p_m2.text = "200,999 Balls Screened • 81,722 Pressure Deliveries • 184 Retained Players Excluded • RR Purse: ₹27.05 Cr (6 Slots Left)"
    p_m2.font.size = Pt(11)
    p_m2.font.color.rgb = RR_WHITE

    # SLIDE 2: 18-NOV-2026 RETENTION & RELEASE AUDIT
    s2 = prs.slides.add_slide(blank_layout)
    add_bg(s2)
    add_header(s2, "Official IPL 2027 Retention & Release Ecosystem (18-Nov-2026)", "TOURNAMENT LANDSCAPE")

    # 4 metric boxes
    m_box_w = Inches(2.75)
    metrics = [
        ("184 PLAYERS", "RETAINED ACROSS 10 TEAMS", RR_PINK),
        ("89 PLAYERS", "OFFICIALLY RELEASED", RR_ACCENT_GREEN),
        ("₹297.95 CR", "TOTAL COMBINED PURSE", RR_ACCENT_BLUE),
        ("ITC GRAND GOA", "MINI-AUCTION (16-DEC-2026)", RR_ACCENT_AMBER)
    ]
    for idx, (val, lbl, clr) in enumerate(metrics):
        left_m = Inches(0.8 + idx * 2.95)
        add_card(s2, left_m, Inches(1.6), m_box_w, Inches(1.2), border_color=clr)
        tb_m = s2.shapes.add_textbox(left_m + Inches(0.1), Inches(1.7), m_box_w - Inches(0.2), Inches(1.0))
        tf = tb_m.text_frame
        p = tf.paragraphs[0]
        p.text = val
        p.font.size = Pt(20)
        p.font.bold = True
        p.font.color.rgb = clr
        p = tf.add_paragraph()
        p.text = lbl
        p.font.size = Pt(9)
        p.font.color.rgb = RR_WHITE

    # Big Summary Card
    add_card(s2, Inches(0.8), Inches(3.0), Inches(11.7), Inches(3.8))
    tb_summary = s2.shapes.add_textbox(Inches(1.0), Inches(3.2), Inches(11.3), Inches(3.4))
    tf_sum = tb_summary.text_frame
    tf_sum.word_wrap = True
    p = tf_sum.paragraphs[0]
    p.text = "MAJOR RETENTION & TRADE SHAKE-UPS ACROSS 10 FRANCHISES"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = RR_PINK
    p.space_after = Pt(8)
    p = tf_sum.add_paragraph()
    p.text = (
        "• Landmark Trades: Hardik Pandya (to PBKS for ₹18 Cr) swapped for Arshdeep Singh (to MI for ₹18 Cr). Sanju Samson traded to CSK; Rishabh Pant traded to DC; Kuldeep Yadav traded to LSG (₹13.5 Cr).\n"
        "• Rajasthan Royals Blockbuster Inflow: Acquired Ravindra Jadeja (from CSK) and Mohammed Shami (from SRH/LSG) alongside Sandeep Sharma, Jofra Archer, and Ravi Bishnoi.\n"
        "• Star Releases Entering Auction Pool: Matheesha Pathirana (released by KKR, ₹18 Cr freed), Trent Boult (released by MI), Mitchell Starc (released by DC), Shimron Hetmyer (released by RR), Avesh Khan (released by LSG, ₹9.75 Cr freed), Nitish Rana (DC), Nehal Wadhera (PBKS), Ajinkya Rahane (KKR), and Deepak Chahar (MI).\n"
        "• Strict Governance Standard: All 184 retained players are 100% EXCLUDED from auction target lists. Bidding on retained or retired players is contractually impossible."
    )
    p.font.size = Pt(11)
    p.font.color.rgb = RR_WHITE

    # SLIDE 3: RR SQUAD (19 RETAINED) & GAPS
    s3 = prs.slides.add_slide(blank_layout)
    add_bg(s3)
    add_header(s3, "Rajasthan Royals 19 Retained Players & Squad Gap Analysis", "RR ROSTER AUDIT")

    card_squad = add_card(s3, Inches(0.8), Inches(1.6), Inches(5.7), Inches(5.2))
    tb_sq = s3.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(5.3), Inches(4.8))
    tf_sq = tb_sq.text_frame
    tf_sq.word_wrap = True
    p = tf_sq.paragraphs[0]
    p.text = "RETAINED SQUAD (19 PLAYERS • ₹27.05 CR PURSE)"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = RR_ACCENT_GREEN
    p.space_after = Pt(6)
    p = tf_sq.add_paragraph()
    p.text = (
        "• Batters (5): Yashasvi Jaiswal, Riyan Parag, Shubham Dubey, Vaibhav Sooryavanshi, Aman Rao Perala\n"
        "• Wicketkeepers (3): Dhruv Jurel, Donovan Ferreira (OS), Lhuan-dre Pretorius (OS)\n"
        "• All-Rounders (2): Ravindra Jadeja (Trade), Dasun Shanaka (OS)\n"
        "• Pace Attack (5): Mohammed Shami (Trade), Jofra Archer (OS), Sandeep Sharma, Nandre Burger (OS), Sushant Mishra\n"
        "• Spin Attack (2): Ravi Bishnoi, Manimaran Siddharth (Trade)\n"
        "• Emerging/Development (2): Brijesh Sharma, Yash Raj Punja\n"
        "• Vacant Auction Slots: 6 Available (Max 3 Overseas Allowed)"
    )
    p.font.size = Pt(10)
    p.font.color.rgb = RR_WHITE

    card_gaps = add_card(s3, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2))
    tb_gp = s3.shapes.add_textbox(Inches(7.0), Inches(1.8), Inches(5.3), Inches(4.8))
    tf_gp = tb_gp.text_frame
    tf_gp.word_wrap = True
    p = tf_gp.paragraphs[0]
    p.text = "CRITICAL SQUAD VULNERABILITIES TO SOLVE"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = RR_ACCENT_ROSE
    p.space_after = Pt(6)
    p = tf_gp.add_paragraph()
    p.text = (
        "1. No. 3 Top-Order Anchor (Critical Gap):\n"
        "   With Sanju Samson traded to CSK, RR lacks an experienced stabilizer at No. 3 to prevent early collapses while Jaiswal and Parag attack.\n\n"
        "2. Middle-Order Spin Destructor & Death Finisher:\n"
        "   Hetmyer's release leaves a void in overs 16–20; RR requires left-handed power hitting to destroy wrist-spin and pace.\n\n"
        "3. Death Seam Spearhead:\n"
        "   While Sandeep Sharma is elite, RR requires a lockdown partner for overs 18 & 20.\n\n"
        "4. Indian Roster Depth & Keeper Backup:\n"
        "   RR already holds 5 overseas players; RR MUST spend purse on premium domestic Indian talent (at least 3-4 Indian buys)."
    )
    p.font.size = Pt(10)
    p.font.color.rgb = RR_WHITE

    # SLIDE 4: TOP 10 BATTERS
    s4 = prs.slides.add_slide(blank_layout)
    add_bg(s4)
    add_header(s4, "Top 10 Verified Auction-Eligible Batters for Rajasthan Royals", "BATTER SCOUTING BOARD")

    # Table of Batters
    rows = 11
    cols = 7
    left = Inches(0.8)
    top = Inches(1.6)
    width = Inches(11.7)
    height = Inches(5.2)

    table_shape = s4.shapes.add_table(rows, cols, left, top, width, height)
    tbl = table_shape.table
    tbl.columns[0].width = Inches(0.6)
    tbl.columns[1].width = Inches(2.2)
    tbl.columns[2].width = Inches(1.1)
    tbl.columns[3].width = Inches(1.1)
    tbl.columns[4].width = Inches(1.2)
    tbl.columns[5].width = Inches(1.2)
    tbl.columns[6].width = Inches(4.3)

    headers = ["#", "Player Name", "Origin", "PPI", "Press SR", "Max Bid", "Tactical Solution for RR"]
    for c_idx, h in enumerate(headers):
        cell = tbl.cell(0, c_idx)
        cell.fill.solid()
        cell.fill.fore_color.rgb = RR_PINK
        p = cell.text_frame.paragraphs[0]
        p.text = h
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = RR_WHITE

    for r_idx, b in enumerate(top_batters, 1):
        row_vals = [
            f"#{b['rank']}",
            b['name'],
            f"{b['classification']} ({b['previous_franchise']})",
            f"{b['ppi_score']:.1f}",
            f"{b['p_sr']:.1f}",
            b['max_bid'],
            b['why_target'][:65] + "..."
        ]
        for c_idx, val in enumerate(row_vals):
            cell = tbl.cell(r_idx, c_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = RR_CARD_BG if r_idx % 2 == 1 else RR_NAVY
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.size = Pt(8.5)
            p.font.color.rgb = RR_WHITE

    # SLIDE 5: TOP 10 BOWLERS
    s5 = prs.slides.add_slide(blank_layout)
    add_bg(s5)
    add_header(s5, "Top 10 Verified Auction-Eligible Bowlers for Rajasthan Royals", "BOWLER SCOUTING BOARD")

    table_shape_b = s5.shapes.add_table(rows, cols, left, top, width, height)
    tbl_b = table_shape_b.table
    tbl_b.columns[0].width = Inches(0.6)
    tbl_b.columns[1].width = Inches(2.2)
    tbl_b.columns[2].width = Inches(1.1)
    tbl_b.columns[3].width = Inches(1.1)
    tbl_b.columns[4].width = Inches(1.2)
    tbl_b.columns[5].width = Inches(1.2)
    tbl_b.columns[6].width = Inches(4.3)

    b_headers = ["#", "Player Name", "Origin", "PPI", "Press Econ", "Max Bid", "Tactical Solution for RR"]
    for c_idx, h in enumerate(b_headers):
        cell = tbl_b.cell(0, c_idx)
        cell.fill.solid()
        cell.fill.fore_color.rgb = RR_ACCENT_BLUE
        p = cell.text_frame.paragraphs[0]
        p.text = h
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = RR_WHITE

    for r_idx, w in enumerate(top_bowlers, 1):
        row_vals = [
            f"#{w['rank']}",
            w['name'],
            f"{w['classification']} ({w['previous_franchise']})",
            f"{w['ppi_score']:.1f}",
            f"{w['p_econ']:.2f}",
            w['max_bid'],
            w['why_target'][:65] + "..."
        ]
        for c_idx, val in enumerate(row_vals):
            cell = tbl_b.cell(r_idx, c_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = RR_CARD_BG if r_idx % 2 == 1 else RR_NAVY
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.size = Pt(8.5)
            p.font.color.rgb = RR_WHITE

    # SLIDE 6: BUDGET SIMULATION & PLAYING XI
    s6 = prs.slides.add_slide(blank_layout)
    add_bg(s6)
    add_header(s6, "Auction Budget Strategy (₹27.05 Cr) & Optimized Playing XI", "TACTICAL BLUEPRINT")

    card_bud = add_card(s6, Inches(0.8), Inches(1.6), Inches(5.7), Inches(5.2))
    tb_b = s6.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(5.3), Inches(4.8))
    tf_b = tb_b.text_frame
    tf_b.word_wrap = True
    p = tf_b.paragraphs[0]
    p.text = "BALANCED ACQUISITION STRATEGY (₹24.0 CR SPENT • ₹3.05 CR BUFFER)"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = RR_ACCENT_GREEN
    p.space_after = Pt(6)
    p = tf_b.add_paragraph()
    p.text = (
        "• P1: Matheesha Pathirana (OS Death Bowler) — Bid: ₹9.5 Cr | Walk-away: ₹11.0 Cr\n"
        "• P2: Nehal Wadhera (IND Left-Hand Finisher) — Bid: ₹5.5 Cr | Walk-away: ₹6.5 Cr\n"
        "• P3: Ajinkya Rahane (IND No. 3 Anchor) — Bid: ₹2.5 Cr | Walk-away: ₹3.5 Cr\n"
        "• P4: Mahipal Lomror (IND Spin Destroyer) — Bid: ₹2.5 Cr | Walk-away: ₹3.5 Cr\n"
        "• P5: Abishek Porel (IND Backup Keeper) — Bid: ₹2.5 Cr | Walk-away: ₹3.2 Cr\n"
        "• P6: Asif Khan (OS Power Finisher Backup) — Bid: ₹1.5 Cr | Walk-away: ₹2.0 Cr\n\n"
        "Composition Outcome: 4 Indians + 2 Overseas | Total Squad: 25 | Overseas: 7/8"
    )
    p.font.size = Pt(10)
    p.font.color.rgb = RR_WHITE

    card_xi = add_card(s6, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2))
    tb_xi = s6.shapes.add_textbox(Inches(7.0), Inches(1.8), Inches(5.3), Inches(4.8))
    tf_xi = tb_xi.text_frame
    tf_xi.word_wrap = True
    p = tf_xi.paragraphs[0]
    p.text = "OPTIMIZED RAJASTHAN ROYALS PLAYING XI"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = RR_ACCENT_AMBER
    p.space_after = Pt(6)
    p = tf_xi.add_paragraph()
    p.text = (
        "1. Yashasvi Jaiswal (Indian LHB Opener)\n"
        "2. Vaibhav Sooryavanshi / Lhuan-dre Pretorius ✈️\n"
        "3. Ajinkya Rahane (Indian No. 3 Anchor - Auction Target)\n"
        "4. Riyan Parag (Indian Middle-Order Batter/Off-Spinner)\n"
        "5. Dhruv Jurel (Wk) (Indian Crisis Batter)\n"
        "6. Nehal Wadhera (Indian LHB Finisher - Auction Target)\n"
        "7. Ravindra Jadeja (Indian Elite All-Rounder)\n"
        "8. Jofra Archer ✈️ (Overseas Express Fast Bowler)\n"
        "9. Mohammed Shami (Indian Fast Bowler)\n"
        "10. Ravi Bishnoi (Indian Leg-Spinner)\n"
        "11. Sandeep Sharma (Indian Death Seamer)\n\n"
        "Impact Sub: Matheesha Pathirana ✈️ (Auction Target) replaces Ajinkya Rahane during the bowling innings."
    )
    p.font.size = Pt(10)
    p.font.color.rgb = RR_WHITE

    prs.save("RR_SupeRR_Selector_Auction_Strategy.pptx")
    print("Presentation saved successfully as RR_SupeRR_Selector_Auction_Strategy.pptx!")

if __name__ == '__main__':
    create_deck()
