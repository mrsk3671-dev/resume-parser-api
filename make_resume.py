from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_resume_pdf(filename="resume.pdf"):
    c = canvas.Canvas(filename, pagesize=letter)
    text = c.beginText(50, 750)
    text.setFont("Helvetica", 12)

    lines = [
        "John Doe",
        "Email: john.doe@example.com",
        "Phone: +1 555 123 4567",
        "",
        "Experience",
        "- Software Engineer at ABC Corp (2019–2023)",
        "  Worked on Python, FastAPI, and Docker-based projects.",
        "- Intern at XYZ Ltd (2018–2019)",
        "  Assisted in developing web applications with Django.",
        "",
        "Education",
        "- B.Sc. in Computer Science, Stanford University (2015–2019)",
        "",
        "Skills",
        "- Python, FastAPI, Docker, SQL, Git, Linux"
    ]

    for line in lines:
        text.textLine(line)

    c.drawText(text)
    c.save()

if __name__ == "__main__":
    create_resume_pdf()
