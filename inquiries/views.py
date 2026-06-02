from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Inquiry
from products.models import ProductCategory


def submit_inquiry(request):
    if request.method == 'POST':
        inquiry = Inquiry.objects.create(
            full_name=request.POST.get('full_name', ''),
            email=request.POST.get('email', ''),
            phone=request.POST.get('phone', ''),
            company=request.POST.get('company', ''),
            country=request.POST.get('country', ''),
            product_interest=request.POST.get('product_interest', ''),
            message=request.POST.get('message', ''),
        )
        # Send notification email
        try:
            send_mail(
                subject=f"New Inquiry from {inquiry.full_name} - AgroHub",
                message=f"""
New inquiry received:

Name: {inquiry.full_name}
Email: {inquiry.email}
Phone: {inquiry.phone}
Company: {inquiry.company}
Country: {inquiry.country}
Product Interest: {inquiry.product_interest}

Message:
{inquiry.message}
                """,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=True,
            )
        except Exception:
            pass

        messages.success(request, "Thank you! Your inquiry has been submitted. We will get back to you shortly.")
        return redirect('core:contact')

    return redirect('core:contact')
