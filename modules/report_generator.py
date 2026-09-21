from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from xml.sax.saxutils import escape
import os


def generate_report(requirements, metrics):

    os.makedirs("reports", exist_ok=True)

    filename = "reports/ReqGuard_Report.pdf"

    doc = SimpleDocTemplate(
        filename,
        pagesize=A4
    )

    styles = getSampleStyleSheet()

    story = []

    # --------------------------------
    # REPORT TITLE
    # --------------------------------

    story.append(
        Paragraph(
            "<b>ReqGuard AI Report</b>",
            styles["Title"]
        )
    )

    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            "<b>Software Requirements Analysis Report</b>",
            styles["Heading2"]
        )
    )

    story.append(Spacer(1, 15))

    # --------------------------------
    # OVERALL METRICS
    # --------------------------------

    story.append(
        Paragraph(
            f"<b>Total Requirements:</b> "
            f"{metrics['total']}",
            styles["BodyText"]
        )
    )

    story.append(Spacer(1, 8))

    story.append(
        Paragraph(
            f"<b>Ambiguous Requirements:</b> "
            f"{metrics['ambiguous']}",
            styles["BodyText"]
        )
    )

    story.append(Spacer(1, 8))

    story.append(
        Paragraph(
            f"<b>Good Requirements:</b> "
            f"{metrics['good']}",
            styles["BodyText"]
        )
    )

    story.append(Spacer(1, 8))

    story.append(
        Paragraph(
            f"<b>Average Quality Score:</b> "
            f"{metrics['average']}",
            styles["BodyText"]
        )
    )

    story.append(Spacer(1, 25))

    # --------------------------------
    # REQUIREMENT ANALYSIS
    # --------------------------------

    story.append(
        Paragraph(
            "<b>Requirement Analysis</b>",
            styles["Heading2"]
        )
    )

    story.append(Spacer(1, 15))

    for req in requirements:

        # Requirement ID
        story.append(
            Paragraph(
                f"<b>{escape(str(req['id']))}</b>",
                styles["Heading3"]
            )
        )

        story.append(Spacer(1, 5))

        # Original requirement
        story.append(
            Paragraph(
                f"<b>Requirement:</b> "
                f"{escape(str(req['text']))}",
                styles["BodyText"]
            )
        )

        story.append(Spacer(1, 8))

        # Ambiguity
        ambiguity = req.get("ambiguity", [])

        if ambiguity:

            story.append(
                Paragraph(
                    "<b>Ambiguous Words:</b> "
                    + escape(", ".join(ambiguity)),
                    styles["BodyText"]
                )
            )

        else:

            story.append(
                Paragraph(
                    "<b>Ambiguity:</b> No ambiguity detected.",
                    styles["BodyText"]
                )
            )

        story.append(Spacer(1, 8))

        # Readability
        if "readability" in req:

            story.append(
                Paragraph(
                    f"<b>Readability Score:</b> "
                    f"{req['readability']}/100",
                    styles["BodyText"]
                )
            )

            story.append(Spacer(1, 8))

        # Requirement Type
        if "type" in req:

            story.append(
                Paragraph(
                    f"<b>Requirement Type:</b> "
                    f"{escape(str(req['type']))}",
                    styles["BodyText"]
                )
            )

            story.append(Spacer(1, 8))

        story.append(
            Paragraph(
                "----------------------------------------",
                styles["Normal"]
            )
        )

        story.append(Spacer(1, 15))

    # --------------------------------
    # BUILD PDF
    # --------------------------------

    doc.build(story)

    return filename