from django.shortcuts import render
from django.core.mail import EmailMessage
from django.conf import settings
from .forms import ContactForm
from django.http import HttpResponse
from reportlab.pdfgen import canvas

def download_resume(request):
    # Create a PDF response
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Sangeetha_Resume.pdf"'

    # Create PDF
    p = canvas.Canvas(response)
    p.setFont("Helvetica-Bold", 18)
    p.drawString(100, 800, "Sangeetha Priya - Resume")

    p.setFont("Helvetica", 12)
    p.drawString(100, 770, "Email: sangeethachellamuthu18@gmail.com")
    p.drawString(100, 750, "Skills: Python, Django, HTML, CSS, JavaScript, MySQL")
    p.drawString(100, 730, "Experience: Fresher / Projects in Web Development")
    p.drawString(100, 710, "GitHub: https://github.com/... (your link)")
    p.drawString(100, 690, "LinkedIn: https://linkedin.com/in/... (your link)")

    # Finish PDF
    p.showPage()
    p.save()

    return response


def resume(request):
    form = ContactForm()
    success = False
    error = None

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            sender_email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            subject = f"Portfolio message from {name}"
            body = f"From: {name} <{sender_email}>\n\n{message}"

            try:
                email = EmailMessage(
                    subject=subject,
                    body=body,
                    from_email=settings.EMAIL_HOST_USER,
                    to=[settings.DEFAULT_TO_EMAIL],
                    reply_to=[sender_email],
                )
                email.send(fail_silently=False)
                success = True
                form = ContactForm()  # reset form after success
            except Exception as e:
                error = str(e)

    return render(request, "resume/resume.html", {
        "form": form,
        "success": success,
        "error": error,
    })


def index(request):
    return render(request, 'resume/index.html')

