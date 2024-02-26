"""
To render html web pages
"""
# from django.http import HttpResponse
# from django.template.loader import render_to_string
# from portfolios.models import Portfolio
from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import FeedbackForm, BugReportForm

def home_view(request, *args, **kwargs):
    """
    Take in a request (Django sends request)
    Return HTML as a response (We pick to return the response)
    """
    # Render the template with the context
    return render(request, "base.html", context={})

def aboutUs_view(request):
    return render(request, 'about_us.html')

def contactUs_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save()
            # Send an email
            send_mail(
                'New Feedback from Fancy Bear Stocks Web App',
                f'Name: {feedback.name}\nEmail: {feedback.email}\nFeedback: {feedback.feedback}',
                'markshperkin1@gmail.com',  # from email
                ['fancybear530@gmail.com'],  # to email
                fail_silently=False,
            )
            return redirect('contact')  # Redirect back to the contact_us page after saving
    else:
        form = FeedbackForm()
    return render(request, 'contact_us.html', {'form': form})

def reportBug_view(request):
    if request.method == 'POST':
        form = BugReportForm(request.POST)
        if form.is_valid():
            bug_report = form.save()
            # Send an email
            send_mail(
                'New Bug Report from Fancy Bear Stocks Web App',
                f'Name: {bug_report.name}\nEmail: {bug_report.email}\nBug Description: {bug_report.bug_description}',
                'markshperkin1@gmail.com',  # from email
                ['fancybear530@gmail.com'],  # to email
                fail_silently=False,
            )
            return redirect('report')  # Redirect back to the report_bug page after saving
    else:
        form = BugReportForm()
    return render(request, 'report_bug.html', {'form': form})