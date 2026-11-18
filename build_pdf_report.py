import os
import json
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#718096"))
        if self._pageNumber > 1:
            self.drawString(54, 750, "Rajasthan Royals | IPL 2027 Auction War Room Intelligence • Official 18-Nov-2026 Baseline")
            self.setStrokeColor(colors.HexColor("#E2E8F0"))
            self.setLineWidth(0.5)
            self.line(54, 744, 558, 744)

        footer_text = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(558, 36, footer_text)
        self.drawString(54, 36, "CONFIDENTIAL • PREPARED FOR RAJASTHAN ROYALS WAR ROOM • ITC GRAND GOA (16-DEC-2026)")
        self.setStrokeColor(colors.HexColor("#E2E8F0"))
        self.setLineWidth(0.5)
        self.line(54, 46, 558, 46)
        self.restoreState()

def build_pdf_report(filename="RR_SupeRR_Selector_Methodology_Report.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()

    c_pink = colors.HexColor("#D81B60")
    c_navy = colors.HexColor("#0B1B3D")
    c_dark = colors.HexColor("#1A202C")
    c_muted = colors.HexColor("#4A5568")
    c_green = colors.HexColor("#0D9488")
    c_amber = colors.HexColor("#D97706")
    c_rose = colors.HexColor("#E11D48")

    title_style = ParagraphStyle(
        'DocTitle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=18, leading=22,
        textColor=c_navy, spaceAfter=3
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle', parent=styles['Normal'],
        fontName='Helvetica', fontSize=10, leading=13,
        textColor=c_pink, spaceAfter=8
    )

    h1_style = ParagraphStyle(
        'Heading1_Custom', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=11, leading=15,
        textColor=c_navy, spaceBefore=8, spaceAfter=3,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'Heading2_Custom', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=9.5, leading=12,
        textColor=c_pink, spaceBefore=6, spaceAfter=2,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'Body_Custom', parent=styles['Normal'],
        fontName='Helvetica', fontSize=8, leading=11,
        textColor=c_dark, spaceAfter=3
    )

    bullet_style = ParagraphStyle(
        'Bullet_Custom', parent=styles['Normal'],
        fontName='Helvetica', fontSize=7.5, leading=10,
        textColor=c_dark, leftIndent=10, firstLineIndent=-7,
        spaceAfter=2
    )

    formula_style = ParagraphStyle(
        'Formula_Custom', parent=styles['Normal'],
        fontName='Courier-Bold', fontSize=7, leading=9,
        textColor=colors.HexColor("#0D47A1"),
        backColor=colors.HexColor("#F0F4F8"),
        borderColor=colors.HexColor("#BBDEFB"),
        borderWidth=0.5, borderPadding=3,
        spaceBefore=2, spaceAfter=3
    )

    with open('ipl2027_official_teams_database.json', 'r', encoding='utf-8') as f:
        db = json.load(f)

    meta = db['metadata']
    top_batters = db['top_10_batters']
    top_bowlers = db['top_10_bowlers']
    franchises = db['franchises']
    rr_squad = db['rr_retained_squad']
    budget_a = db['budget_scenarios']['scenario_a_balanced']
    playing_xi = db['playing_xi']

    story = []

    # Title Block
    story.append(Paragraph("RAJASTHAN ROYALS — IPL 2027 AUCTION INTELLIGENCE WAR ROOM", ParagraphStyle('TopTag', fontName='Helvetica-Bold', fontSize=8, textColor=c_pink, spaceAfter=2)))
    story.append(Paragraph("Targeting the Most Reliable Players Under Pressure", title_style))
    story.append(Paragraph("Official BCCI Retention, Trade & Release Baseline (18 November 2026) • 200,999 Deliveries Screened", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_pink, spaceBefore=1, spaceAfter=6))

    # Executive Mandate & Snapshot
    story.append(Paragraph("1. Executive Mandate & Official BCCI Snapshot (18 November 2026)", h1_style))
    story.append(Paragraph(
        "Following the official BCCI retention deadline on 17/18 November 2026 ahead of the IPL 2027 Mini-Auction in <b>ITC Grand Goa on 16 December 2026</b>, all 10 franchises finalized their retained rosters. Across the tournament, <b>184 players were retained (55 overseas)</b>, leaving <b>₹297.95 Cr</b> in total purse to contest <b>66 vacant slots</b>.",
        body_style
    ))

    # Metric Callout Table
    stat_data = [
        [
            Paragraph("<b>200,999</b><br/><font size=5.5 color='#718096'>DELIVERIES SCREENED</font>", ParagraphStyle('C1', alignment=1)),
            Paragraph("<b>184 RETAINED</b><br/><font size=5.5 color='#718096'>STRICTLY UNAVAILABLE</font>", ParagraphStyle('C2', alignment=1)),
            Paragraph("<b>₹27.05 Cr</b><br/><font size=5.5 color='#718096'>RR REMAINING PURSE</font>", ParagraphStyle('C3', alignment=1)),
            Paragraph("<b>6 SLOTS (3 OS)</b><br/><font size=5.5 color='#718096'>RR OPEN POSITIONS</font>", ParagraphStyle('C4', alignment=1))
        ]
    ]
    t_stat = Table(stat_data, colWidths=[126, 126, 126, 126])
    t_stat.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F8FAFC")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#E2E8F0")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#E2E8F0")),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_stat)
    story.append(Spacer(1, 4))

    # Section: RR Retained Squad & Gap Analysis
    story.append(Paragraph("2. Rajasthan Royals Retained Squad (19 Players) & Gap Analysis", h1_style))
    story.append(Paragraph(
        "Rajasthan Royals retained 19 players committing ₹92.95 Cr, including monumental incoming trades for <b>Ravindra Jadeja</b> (from CSK) and <b>Mohammed Shami</b> (from SRH/LSG). With <b>Sanju Samson traded to CSK</b> and <b>Shimron Hetmyer released</b>, RR’s core squad gaps are strictly defined:",
        body_style
    ))
    story.append(Paragraph("<b>• Gap 1 (No. 3 Anchor):</b> Vacancy left by Sanju Samson requiring an Indian top-order stabilizer who anchors against early collapse while Jaiswal and Parag strike.", bullet_style))
    story.append(Paragraph("<b>• Gap 2 (Middle-Order Spin Destructor & Finishing):</b> Left-handed power to destroy wrist-spin in overs 7–15 and execute clutch death boundary hitting.", bullet_style))
    story.append(Paragraph("<b>• Gap 3 (Death Bowling Seam Spearhead):</b> Express death-overs specialist to pair with Sandeep Sharma, Jofra Archer, and Mohammed Shami.", bullet_style))
    story.append(Paragraph("<b>• Gap 4 (Indian Depth & Wicketkeeper Backup):</b> RR has only 3 overseas slots remaining (5 retained); at least 3 of 6 acquisitions must be domestic Indian players, including a backup keeper for Dhruv Jurel.", bullet_style))

    story.append(Spacer(1, 4))
    story.append(Paragraph("3. Pressure Performance Index (PPI) Mathematical Formulation", h1_style))
    story.append(Paragraph("<b>Batter PPI:</b> PPI = [0.35 × SR_press + 0.35 × Avg_press + 0.30 × (SR_press - SR_base) + 0.40 × (40 - Dot%_press)] × Sample_Factor", formula_style))
    story.append(Paragraph("<b>Bowler PPI:</b> PPI = [7.0 × (12.0 - Econ_press) + 2.0 × Wkts_press + 0.6 × Dot%_press + 3.0 × (Econ_base - Econ_press)] × Sample_Factor", formula_style))

    story.append(PageBreak())

    # Section 3: Top 10 Verified Auction-Eligible Batters
    story.append(Paragraph("4. Top 10 Verified Auction-Eligible Batters for Rajasthan Royals", h1_style))
    story.append(Paragraph(
        "Screened from 200,999 deliveries and officially verified as released or independent entrants. All 184 retained players strictly excluded:",
        body_style
    ))

    bat_table_data = [
        ["#", "Player Name", "Prev Team", "Type", "PPI", "Press SR", "Press Avg", "Fit", "Max Bid", "Tactical Role"]
    ]
    for b in top_batters:
        bat_table_data.append([
            f"#{b['rank']}",
            b['name'],
            b['previous_franchise'],
            b['classification'][:2].upper(),
            f"{b['ppi_score']:.1f}",
            f"{b['p_sr']:.1f}",
            f"{b['p_avg']:.1f}",
            f"{b['rr_fit_score']:.0f}%",
            b['max_bid'],
            b['why_target'][:38] + "..."
        ])

    t_bat = Table(bat_table_data, colWidths=[18, 90, 48, 22, 35, 42, 42, 30, 45, 132])
    t_bat.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_navy),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 6.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('FONTSIZE', (0,1), (-1,-1), 6.5),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#F8FAFC")]),
    ]))
    story.append(t_bat)
    story.append(Spacer(1, 6))

    # Section 4: Top 10 Verified Auction-Eligible Bowlers
    story.append(Paragraph("5. Top 10 Verified Auction-Eligible Bowlers for Rajasthan Royals", h1_style))
    story.append(Paragraph(
        "Premier wicket-takers and lockdown death bowling specialists meeting RR's tactical bowling requirements:",
        body_style
    ))

    bowl_table_data = [
        ["#", "Player Name", "Prev Team", "Type", "PPI", "Press Econ", "Wkt Rate", "Fit", "Max Bid", "Tactical Role"]
    ]
    for w in top_bowlers:
        bowl_table_data.append([
            f"#{w['rank']}",
            w['name'],
            w['previous_franchise'],
            w['classification'][:2].upper(),
            f"{w['ppi_score']:.1f}",
            f"{w['p_econ']:.2f}",
            f"{w['p_w_rate']:.2f}",
            f"{w['rr_fit_score']:.0f}%",
            w['max_bid'],
            w['why_target'][:38] + "..."
        ])

    t_bowl = Table(bowl_table_data, colWidths=[18, 90, 48, 22, 35, 42, 42, 30, 45, 132])
    t_bowl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1E3A8A")),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 6.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('FONTSIZE', (0,1), (-1,-1), 6.5),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#F8FAFC")]),
    ]))
    story.append(t_bowl)
    story.append(Spacer(1, 6))

    # Section 5: Auction Budget Strategy (₹27.05 Cr Purse)
    story.append(Paragraph("6. Rajasthan Royals Auction Budget Allocation Strategy (₹27.05 Cr Purse)", h1_style))
    story.append(Paragraph(
        "With ₹27.05 Cr and 6 vacant slots (max 3 overseas), RR cannot engage in reckless bidding wars. Our recommended <b>Balanced Scenario A</b> achieves maximum tactical value:",
        body_style
    ))

    bud_data = [
        ["Priority", "Target Name", "Role", "Category", "Allocated Bid", "Walk-Away Price", "Remaining Purse"]
    ]
    running_purse = 27.05
    for i, p in enumerate(budget_a['purchases'], 1):
        running_purse -= p['bid']
        bud_data.append([
            f"P{i}",
            p['name'],
            p['role'],
            p['type'],
            f"₹{p['bid']:.1f} Cr",
            f"₹{p['walk_away']:.1f} Cr",
            f"₹{running_purse:.2f} Cr"
        ])

    t_bud = Table(bud_data, colWidths=[38, 105, 85, 55, 65, 75, 81])
    t_bud.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#065F46")),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 7),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('FONTSIZE', (0,1), (-1,-1), 7),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#F8FAFC")]),
    ]))
    story.append(t_bud)
    story.append(Spacer(1, 6))

    # Section 6: Optimized RR Playing XI
    story.append(Paragraph("7. Optimized Rajasthan Royals Playing XI & Impact Player Model", h1_style))
    story.append(Paragraph(
        "<b>Batting First Playing XI:</b><br/>"
        "1. <b>Yashasvi Jaiswal</b> (IND, Opener LHB) • 2. <b>Vaibhav Sooryavanshi / Lhuan-dre Pretorius</b> (Opener)<br/>"
        "3. <b>Ajinkya Rahane</b> (IND - Target, No. 3 Anchor) • 4. <b>Riyan Parag</b> (IND, No. 4 Striker/OB)<br/>"
        "5. <b>Dhruv Jurel</b> (Wk) (IND, Keeper-Batter) • 6. <b>Nehal Wadhera</b> (IND - Target, LHB Finisher)<br/>"
        "7. <b>Ravindra Jadeja</b> (IND, SLA All-Rounder) • 8. <b>Jofra Archer</b> ✈️ (OS, Express Fast Bowler)<br/>"
        "9. <b>Mohammed Shami</b> (IND, Seam Bowler) • 10. <b>Ravi Bishnoi</b> (IND, Leg-Spinner)<br/>"
        "11. <b>Sandeep Sharma</b> (IND, Death Specialist Seamer)<br/>"
        "<b>Tactical Impact Player Substitution:</b> <b>Matheesha Pathirana</b> ✈️ (Target) replaces Ajinkya Rahane during the bowling innings, giving RR an unmatched pace-and-spin siege (Archer + Shami + Sandeep + Pathirana + Jadeja + Bishnoi).",
        body_style
    ))

    doc.build(story, canvasmaker=NumberedCanvas)
    print("Methodology PDF report built successfully as RR_SupeRR_Selector_Methodology_Report.pdf!")

if __name__ == '__main__':
    build_pdf_report()
