import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def generate_pdf_report(report_data, filename="session_report.pdf"):
    """Generates a professional PDF telemetry report for the user's session."""
    doc = SimpleDocTemplate(filename, pagesize=letter)
    story = []
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'TitleStyle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#4A90E2'),
        spaceAfter=15,
        alignment=1 # Center
    )
    
    subtitle_style = ParagraphStyle(
        'SubtitleStyle',
        parent=styles['Normal'],
        fontSize=12,
        textColor=colors.HexColor('#555555'),
        spaceAfter=25,
        alignment=1
    )
    
    heading_style = ParagraphStyle(
        'HeadingStyle',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=colors.HexColor('#2C3E50'),
        spaceAfter=10
    )
    
    # Title & Subtitle
    story.append(Paragraph("✨ AuraSync AI - Professional Wellness Report", title_style))
    story.append(Paragraph("Real-Time Computer Vision Ergonomic & Cognitive Telemetry", subtitle_style))
    story.append(Spacer(1, 15))
    
    # Metrics Table Data
    data = [
        ["Telemetry Metric", "Session Data Details"],
        ["Session Timestamp", report_data.get('session_date', 'N/A')],
        ["Total Duration", f"{report_data.get('duration_seconds', 0)} seconds"],
        ["Frames Monitored", str(report_data.get('total_frames_monitored', 0))],
        ["Fatigue / Drowsiness Alerts", str(report_data.get('fatigue_alerts_count', 0))],
        ["Bad Posture Events", str(report_data.get('bad_posture_count', 0))],
        ["Overall Focus Efficiency Score", report_data.get('overall_focus_score', '100%')]
    ]
    
    table = Table(data, colWidths=[200, 250])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (1, 0), colors.HexColor('#4A90E2')),
        ('TEXTCOLOR', (0, 0), (1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#F4F4F9')),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#DDDDDD')),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('TOPPADDING', (0, 1), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
    ]))
    
    story.append(table)
    story.append(Spacer(1, 30))
    story.append(Paragraph("<b>AI Coach Note:</b> Maintain a 20-20-20 visual break interval and keep your shoulders aligned with your spine to prevent chronic fatigue.", heading_style))
    
    doc.build(story)
    print(f"[PDF REPORT] Professional PDF telemetry report successfully generated: {filename}")