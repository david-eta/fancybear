"""
Note:
- These views assume the existence of corresponding HTML templates and forms.
- The 'send_mail' function is used to send emails. Ensure that email settings are properly configured in the Django settings file.
- The 'deposit_withdraw' function is a placeholder and requires implementation for actual deposit and withdrawal functionality.
"""

# from django.http import HttpResponse
# from django.template.loader import render_to_string
# from portfolios.models import Portfolio
from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import FeedbackForm, BugReportForm
#'home_view': Renders the base HTML template. No context data is passed.
def home_view(request, *args, **kwargs):
    """
    Take in a request (Django sends request)
    Return HTML as a response (We pick to return the response)
    """
    # Render the template with the context
    return render(request, "base.html", context={})
#'aboutUs_view': Renders the 'about_us.html' template.
def aboutUs_view(request):
    return render(request, 'about_us.html')
#'contactUs_view': Renders the 'contact_us.html' template. If a POST request is received, processes the submitted feedback form, sends an email to the admin, and sends a confirmation email to the user.
def contactUs_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save()
            # Send an email to the admin
            send_mail(
                'New Feedback from Fancy Bear Stocks Web App',
                f'Name: {feedback.name}\nEmail: {feedback.email}\n\nFeedback: {feedback.feedback}',
                'fancybear1@yahoo.com', # from email
                ['fancybear1@yahoo.com'], # to email
                fail_silently=False,
            )
            
            html_content = generate_feedback_report_email(feedback.feedback)
            # Send an email to the user with a recap of their feedback
            send_mail(
                'Thank you for your feedback',
                f'We have received your feedback:\n\n{feedback.feedback}\n\nWe will take it into consideration.',
                'fancybear1@yahoo.com', # from email
                [feedback.email], # to email
                html_message=html_content, # Use the generated HTML content

                fail_silently=False,
            )
            return redirect('contact') # Redirect back to the contact_us page after saving
    else:
        form = FeedbackForm()
    return render(request, 'contact_us.html', {'form': form})
#'reportBug_view': Renders the 'report_bug.html' template. If a POST request is received, processes the submitted bug report form, sends an email to the admin, and sends a confirmation email to the user.
def reportBug_view(request):
    if request.method == 'POST':
        form = BugReportForm(request.POST)
        if form.is_valid():
            bug_report = form.save()
            # Send an email to the admin
            send_mail(
                'New Bug Report from Fancy Bear Stocks Web App',
                f'Name: {bug_report.name}\nEmail: {bug_report.email}\n\nBug Description: {bug_report.bug_description}',
                'fancybear1@yahoo.com', # from email
                ['fancybear1@yahoo.com'], # to email
                fail_silently=False,
            )
            
            html_content = generate_bug_report_email(bug_report.bug_description)

            # Send an email to the user with a recap of their bug report
            send_mail(
                'Thank you for reporting the bug',
                f'We have received your bug report:\n\n{bug_report.bug_description}\n\nWe will take your feedback into consideration.',
                'fancybear1@yahoo.com', # from email
                [bug_report.email], # to email
                html_message=html_content, # Use the generated HTML content
                fail_silently=False,
            )
            return redirect('report') # Redirect back to the report_bug page after saving
    else:
        form = BugReportForm()
    return render(request, 'report_bug.html', {'form': form})

# email_generator.py
#'generate_bug_report_email': Generates an HTML email content for bug report confirmation.
def generate_bug_report_email(bug_description):
    html_content = f"""
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                color: #333;
            }}
            .header {{
                background-color: #f8f9fa;
                padding: 20px;
                text-align: center;
            }}
            .main-content {{
                padding: 20px;
            }}
            .footer {{
                background-color: #f8f9fa;
                padding: 20px;
                text-align: center;
                font-size: 0.8em;
                color: #6c757d;
            }}
            .bug-description {{
                font-style: italic;
                color: #6c757d;
            }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>Thank you for reporting the bug</h1>
        </div>
        <div class="main-content">
            <p>We have received your bug report:</p>
            <p class="bug-description"><i>{bug_description}</i></p>
            <p>We will work on fixing it.</p>
        </div>
        <div class="footer">
            <p>Best regards,</p>
            <p>Fancy Bear Team</p>
        </div>
    </body>
    </html>
    """
    return html_content
#'generate_feedback_report_email': Generates an HTML email content for feedback confirmation.
def generate_feedback_report_email(feedback_description):
    html_content = f"""
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                color: #333;
            }}
            .header {{
                background-color: #f8f9fa;
                padding: 20px;
                text-align: center;
            }}
            .main-content {{
                padding: 20px;
            }}
            .footer {{
                background-color: #f8f9fa;
                padding: 20px;
                text-align: center;
                font-size: 0.8em;
                color: #6c757d;
            }}
            .bug-description {{
                font-style: italic;
                color: #6c757d;
            }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>Thank you for giving us feedback</h1>
        </div>
        <div class="main-content">
            <p>We have received your feedback:</p>
            <p class="bug-description"><i>{feedback_description}</i></p>
            <p>We will take it into consideration.</p>
        </div>
        <div class="footer">
            <p>Best regards,</p>
            <p>Fancy Bear Team</p>
        </div>
    </body>
    </html>
    """
    return html_content
#'deposit_withdraw': Placeholder function for handling deposit and withdrawal logic. Renders the 'deposit_withdraw.html' template.
def deposit_withdraw(request):
    # Here you can handle the logic for depositing and withdrawing money
    # For now, we'll just render the template
    return render(request, 'deposit_withdraw.html')
