from django.shortcuts import render


def index(request):
    if request.method == 'POST':
        form = ContactForm()
        first_name = form.
    return render(request, "index.html")


