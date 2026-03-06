from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf(summary):

    file_name = "weekly_feedback_report.pdf"

    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("Weekly Customer Feedback Report", styles["Title"]))
    story.append(Spacer(1, 20))

    for line in summary:
        story.append(Paragraph(line, styles["Normal"]))
        story.append(Spacer(1, 10))

    doc = SimpleDocTemplate(file_name)
    doc.build(story)

    return file_name