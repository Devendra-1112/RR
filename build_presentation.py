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
    change_report = db.get('eligibility_audit_change_report', [])
    retired_list = db.get('retired_players_registry', [])

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

    # SLIDE 1: COVER
    s1 = prs.slides.add_slide(blank_layout)
    add_bg(s1)
    
    accent = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(0.4), prs.slide_height)
    accent.fill.solid()
    accent.fill.fore_color.rgb = RR_PINK
    accent.line.fill.background()

    tb = s1.shapes.add_textbox(Inches(1.2), Inches(1.8), Inches(11), Inches(4.5))
    tf = tb.text_frame
    tf.word_wrap = True

    p = tf.paragraphs[0]
    p.text = "RAJASTHAN ROYALS"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = RR_PINK
    p.space_after = Pt(8)

    p2 = tf.add_paragraph()
    p2.text = "IPL 2027 AUCTION INTELLIGENCE WAR ROOM"
    p2.font.size = Pt(36)
    p2.font.bold = True
    p2.font.color.rgb = RR_WHITE
    p2.space_after = Pt(14)

    p3 = tf.add_paragraph()
    p3.text = "Complete Regulatory Eligibility Audit & 100% Verified Auction Targets"
    p3.font.size = Pt(18)
    p3.font.color.rgb = RR_MUTED
    p3.space_after = Pt(24)

    p4 = tf.add_paragraph()
    p4.text = (
        "Official BCCI Baseline: 18-Nov-2026 | Mini-Auction: 16-Dec-2026 (ITC Grand Goa)\n"
        "200,999 Deliveries Screened • Strict Exclusion of Retired & Pakistani Players • ₹27.05 Cr Purse Management"
    )
    p4.font.size = Pt(12)
    p4.font.color.rgb = RR_ACCENT_AMBER

    # SLIDE 2: EXECUTIVE SUMMARY & DATA AUDIT
    s2 = prs.slides.add_slide(blank_layout)
    add_bg(s2)
    add_header(s2, "Executive Mandate & Data Quality Audit", "PHASE 1 & 2 • AUDIT BASELINE")

    kpis = [
        ("200,999", "Deliveries Screened", "IPL 87,687 + T20I 113,312 (883 matches)", RR_ACCENT_BLUE),
        ("184", "Players Retained", "Strictly classified VERIFIED UNAVAILABLE", RR_ACCENT_ROSE),
        ("67", "Pakistani Players", "Excluded under BCCI IPL policy directives", RR_ACCENT_AMBER),
        ("9", "Retired IPL Players", "Audited and confirmed unavailable", RR_ACCENT_GREEN),
        ("₹27.05 Cr", "RR Auction Purse", "6 vacant slots (maximum 3 overseas)", RR_PINK)
    ]
    card_w = Inches(2.2)
    card_h = Inches(2.2)
    for idx, (val, title, sub, color) in enumerate(kpis):
        left = Inches(0.8 + idx * 2.4)
        top = Inches(1.6)
        card = add_card(s2, left, top, card_w, card_h)
        tb = s2.shapes.add_textbox(left + Inches(0.15), top + Inches(0.2), card_w - Inches(0.3), card_h - Inches(0.4))
        tf = tb.text_frame
        tf.word_wrap = True
        p1 = tf.paragraphs[0]
        p1.text = val
        p1.font.size = Pt(26)
        p1.font.bold = True
        p1.font.color.rgb = color
        p1.alignment = PP_ALIGN.CENTER
        
        p2 = tf.add_paragraph()
        p2.text = title.upper()
        p2.font.size = Pt(9.5)
        p2.font.bold = True
        p2.font.color.rgb = RR_WHITE
        p2.alignment = PP_ALIGN.CENTER
        p2.space_before = Pt(4)

        p3 = tf.add_paragraph()
        p3.text = sub
        p3.font.size = Pt(8)
        p3.font.color.rgb = RR_MUTED
        p3.alignment = PP_ALIGN.CENTER
        p3.space_before = Pt(4)

    # Narrative Card
    c_nar = add_card(s2, Inches(0.8), Inches(4.2), Inches(11.7), Inches(2.6))
    tb_n = s2.shapes.add_textbox(Inches(1.0), Inches(4.3), Inches(11.3), Inches(2.4))
    tf_n = tb_n.text_frame
    tf_n.word_wrap = True
    p = tf_n.paragraphs[0]
    p.text = "CRITICAL SQUAD VOIDS & RECRUITMENT CONSTRAINTS (RAJASTHAN ROYALS)"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = RR_PINK
    p.space_after = Pt(4)
    p = tf_n.add_paragraph()
    p.text = (
        "• Incoming Monumental Trades: Ravindra Jadeja (from CSK) and Mohammed Shami (from SRH/LSG) transform RR's bowling & all-round spine.\n"
        "• Outgoing Impact: Sanju Samson traded to CSK (creating an urgent No. 3 Indian top-order anchor requirement); Shimron Hetmyer released.\n"
        "• Strict Overseas Quota: RR has retained 5 overseas players (Archer, Burger, Shanaka, Ferreira, Pretorius); max 3 overseas slots can be bought.\n"
        "• Regulatory Integrity: Zero tolerance for retired players or Pakistani players; 100% of auction targets must be verified eligible."
    )
    p.font.size = Pt(10)
    p.font.color.rgb = RR_WHITE

    # SLIDE 3: ELIGIBILITY AUDIT & CHANGE REPORT
    s3 = prs.slides.add_slide(blank_layout)
    add_bg(s3)
    add_header(s3, "Auction Eligibility Audit & Candidate Disqualification Report", "REGULATORY AUDIT")

    card_chg = add_card(s3, Inches(0.8), Inches(1.5), Inches(11.7), Inches(5.4))
    table_shape = s3.shapes.add_table(len(change_report) + 1, 5, Inches(1.0), Inches(1.8), Inches(11.3), Inches(4.8))
    tbl = table_shape.table
    tbl.columns[0].width = Inches(1.8)
    tbl.columns[1].width = Inches(1.3)
    tbl.columns[2].width = Inches(2.7)
    tbl.columns[3].width = Inches(2.0)
    tbl.columns[4].width = Inches(3.5)

    headers = ["Removed Player", "List", "Disqualification Reason", "Verified Replacement", "Strategic Tactical Upgrade"]
    for c_idx, h in enumerate(headers):
        cell = tbl.cell(0, c_idx)
        cell.fill.solid()
        cell.fill.fore_color.rgb = RR_NAVY
        p = cell.text_frame.paragraphs[0]
        p.text = h
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = RR_WHITE

    for r_idx, chg in enumerate(change_report, 1):
        row_vals = [
            chg['removed_player'],
            chg['list'],
            chg['reason_for_removal'],
            f"{chg['replacement_player']} (VERIFIED)",
            chg['why_replacement_better']
        ]
        for c_idx, val in enumerate(row_vals):
            cell = tbl.cell(r_idx, c_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = RR_CARD_BG if r_idx % 2 == 1 else RR_NAVY
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.size = Pt(7.5)
            p.font.color.rgb = RR_WHITE if c_idx != 3 else RR_ACCENT_GREEN

    # SLIDE 4: CORRECTED TOP 10 BATSMEN
    s4 = prs.slides.add_slide(blank_layout)
    add_bg(s4)
    add_header(s4, "Top 10 Verified Auction-Eligible Batsmen for Rajasthan Royals", "BATSMEN SHORTLIST")

    table_shape_bat = s4.shapes.add_table(11, 7, Inches(0.8), Inches(1.5), Inches(11.7), Inches(5.4))
    tbl_bat = table_shape_bat.table
    tbl_bat.columns[0].width = Inches(0.6)
    tbl_bat.columns[1].width = Inches(2.2)
    tbl_bat.columns[2].width = Inches(1.1)
    tbl_bat.columns[3].width = Inches(1.1)
    tbl_bat.columns[4].width = Inches(1.2)
    tbl_bat.columns[5].width = Inches(1.2)
    tbl_bat.columns[6].width = Inches(4.3)

    b_headers = ["#", "Player Name", "Origin", "PPI", "Press SR", "Max Bid", "Tactical Solution for RR"]
    for c_idx, h in enumerate(b_headers):
        cell = tbl_bat.cell(0, c_idx)
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
            cell = tbl_bat.cell(r_idx, c_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = RR_CARD_BG if r_idx % 2 == 1 else RR_NAVY
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.size = Pt(8.5)
            p.font.color.rgb = RR_WHITE

    # SLIDE 5: CORRECTED TOP 10 BOWLERS
    s5 = prs.slides.add_slide(blank_layout)
    add_bg(s5)
    add_header(s5, "Top 10 Verified Auction-Eligible Bowlers for Rajasthan Royals", "BOWLERS SHORTLIST")

    table_shape_b = s5.shapes.add_table(11, 7, Inches(0.8), Inches(1.5), Inches(11.7), Inches(5.4))
    tbl_b = table_shape_b.table
    tbl_b.columns[0].width = Inches(0.6)
    tbl_b.columns[1].width = Inches(2.2)
    tbl_b.columns[2].width = Inches(1.1)
    tbl_b.columns[3].width = Inches(1.1)
    tbl_b.columns[4].width = Inches(1.2)
    tbl_b.columns[5].width = Inches(1.2)
    tbl_b.columns[6].width = Inches(4.3)

    w_headers = ["#", "Player Name", "Origin", "PPI", "Press Econ", "Max Bid", "Tactical Solution for RR"]
    for c_idx, h in enumerate(w_headers):
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

    # SLIDE 6: BUDGET STRATEGY & PLAYING XI
    s6 = prs.slides.add_slide(blank_layout)
    add_bg(s6)
    add_header(s6, "Auction Budget Strategy (₹27.05 Cr) & Optimized Playing XI", "TACTICAL BLUEPRINT")

    card_bud = add_card(s6, Inches(0.8), Inches(1.6), Inches(5.7), Inches(5.2))
    tb_b = s6.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(5.3), Inches(4.8))
    tf_b = tb_b.text_frame
    tf_b.word_wrap = True
    p = tf_b.paragraphs[0]
    p.text = "BALANCED ACQUISITION STRATEGY (₹25.0 CR SPENT • ₹2.05 CR BUFFER)"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = RR_ACCENT_GREEN
    p.space_after = Pt(6)
    p = tf_b.add_paragraph()
    p.text = (
        "• P1: Matheesha Pathirana (OS Death Bowler) — Bid: ₹9.5 Cr | Walk-away: ₹11.0 Cr\n"
        "• P2: Nehal Wadhera (IND Left-Hand Finisher) — Bid: ₹5.5 Cr | Walk-away: ₹6.5 Cr\n"
        "• P3: Rahul Tripathi (IND No. 3 Anchor/Striker) — Bid: ₹3.5 Cr | Walk-away: ₹4.5 Cr\n"
        "• P4: Mahipal Lomror (IND Spin Destroyer) — Bid: ₹2.5 Cr | Walk-away: ₹3.5 Cr\n"
        "• P5: Abishek Porel (IND Backup Keeper) — Bid: ₹2.5 Cr | Walk-away: ₹3.2 Cr\n"
        "• P6: M Shahrukh Khan (IND Power Finisher) — Bid: ₹1.5 Cr | Walk-away: ₹2.5 Cr\n\n"
        "Composition Outcome: 5 Indians + 1 Overseas | Total Squad: 25 | Overseas: 6/8"
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
        "3. Rahul Tripathi (Indian No. 3 Anchor/Striker - Auction Target)\n"
        "4. Riyan Parag (Indian Middle-Order Batter/Off-Spinner)\n"
        "5. Dhruv Jurel (Wk) (Indian Crisis Batter)\n"
        "6. Nehal Wadhera (Indian LHB Finisher - Auction Target)\n"
        "7. Ravindra Jadeja (Indian Elite All-Rounder)\n"
        "8. Jofra Archer ✈️ (Overseas Express Fast Bowler)\n"
        "9. Mohammed Shami (Indian Fast Bowler)\n"
        "10. Ravi Bishnoi (Indian Leg-Spinner)\n"
        "11. Sandeep Sharma (Indian Death Seamer)\n\n"
        "Impact Sub: Matheesha Pathirana ✈️ (Auction Target) replaces Rahul Tripathi during the bowling innings."
    )
    p.font.size = Pt(10)
    p.font.color.rgb = RR_WHITE

    prs.save("RR_SupeRR_Selector_Auction_Strategy.pptx")
    print("Presentation saved successfully as RR_SupeRR_Selector_Auction_Strategy.pptx!")

if __name__ == '__main__':
    create_deck()
