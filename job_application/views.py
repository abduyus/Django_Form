from django.shortcuts import render
from django.contrib import messages
from django.core.mail import EmailMessage
from .forms import ApplicationForm
from .models import Form

def index(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            date = form.cleaned_data['date']
            occupation = form.cleaned_data['occupation']

            Form.objects.create(first_name=first_name, last_name=last_name,
                                 email=email, date=date, occupation=occupation)
            
            message_body = f"A new job application form was submitted. Thank you, {first_name}. Here is your submission data:" \
                            "\n{first_name}\n{last_name}\n{email}\n{date}\n{occupation}"
            email_message = EmailMessage("Form submission confirmation", message_body, to=[email])
            email_message.send()
            messages.success(request, "Your application has been submitted successfully!")
    else:
        form = ApplicationForm()
    return render(request, "index.html", {'form': form})


