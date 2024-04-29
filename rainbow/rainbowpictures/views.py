from django.shortcuts import render
from django.http import HttpResponse

from django.core.mail import BadHeaderError, send_mail
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect

def send_email(request):
    name=request.POST.get('name','')
    f_email=request.POST.get('email','')
    from_email=settings.EMAIL_HOST_USER
    phone=request.POST.get('phone','')
    subject=request.POST.get('subject','')
    description=request.POST.get('description','')
    full_message = f"""
    Received message below from {f_email}, {subject}
    ________________________
    
    Phone : {phone}
    Name : {name}

    {description}
    """

    if subject and name and f_email:
        try:
            send_mail(subject, full_message, from_email, ['testaman2023@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        messages.success(request,"Message send successfully")
        return HttpResponseRedirect('/')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')

# Create your views here.

def Home(request):
    return render(request,"index.html")

def Portfolio(request):
    return render(request,'Portfolio.html')

def Contact(request):
    return render(request,'Contact.html')

def Formsubmit(request):

    name=request.POST.get('name')
    email=request.POST.get('email')
    phone=request.POST.get('phone')
    subject=request.POST.get('subject')
    description=request.POST.get('description')
    data={
        "name":name,
        "email":email,
        "phone":phone,
        "subject":subject,
        "description":description
    }
    return render(request,"Contact.html",{"data":data}) 

def Clients(request):
    return render(request,'clients.html')

def Blog(request):
    return render(request,'blog.html')

def About(request):
    return render(request,'about.html')

def Service(request):
    return render(request,'services.html')

def Candid(request):
    return render(request,'Candid.html')

def Marketing(request):
    return render(request,'marketing.html')

# from django.conf import settings
# from django.core.mail import send_mail
# from django.shortcuts import reverse
# from django.views.generic import TemplateView, FormView

# # from .forms import ContactForm


# class SuccessView(TemplateView):
#     template_name = "success.html"


# class ContactView(FormView):
#     form_class = ContactForm
#     template_name = "contact.html"

#     def get_success_url(self):
#         return reverse("contact")

#     def form_valid(self, form):
#         email = form.cleaned_data.get("email")
#         subject = form.cleaned_data.get("subject")
#         message = form.cleaned_data.get("message")

#         full_message = f"""
#             Received message below from {email}, {subject}
#             ________________________


#             {message}
#             """
#         send_mail(
#             subject="Received contact form submission",
#             message=full_message,
#             from_email=settings.DEFAULT_FROM_EMAIL,
#             recipient_list=[settings.NOTIFY_EMAIL],
#         )
#         return super(ContactView, self).form_valid(form)