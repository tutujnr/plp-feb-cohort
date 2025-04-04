from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import JsonResponse
from operator import attrgetter
from .models import *
from .forms import ContactForm


class HomePageView(TemplateView):
    template_name = 'portfolio/portfolio_main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'personal': Personal.objects.all(),
            'about': About.objects.all(),
            'technologies': Technology.objects.all(),
            'portfolio': Portfolio.objects.all(),
            'contact_form': ContactForm(),
            'message_sent': False,
        })
        return context

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            email_body = (
                f"Name: {form.cleaned_data['your_name']}\n"
                f"Email: {form.cleaned_data['your_email']}\n"
                f"Subject: {form.cleaned_data['subject']}\n\n"
                f"{form.cleaned_data['message']}"
            )

            return JsonResponse({'status': 'success', 'message_sent': True})

class DigitalCVPageView(TemplateView):
    template_name = 'portfolio/digital_cv.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        experiences = Experience.objects.all()
        for experience in experiences:
            experience.descriptions.set(
                Description.objects.filter(experience=experience).order_by('order_number')
            )

        certifications = Portfolio.objects.filter(filter='filter-certification')
        grouped_portfolio = {}
        for item in sorted(certifications, key=attrgetter('year'), reverse=True):
            issuer_name = item.issuer.name if item.issuer else "Unknown Issuer"
            grouped_portfolio.setdefault(issuer_name, []).append(item)

        context.update({
            'experiences': experiences,
            'personal': Personal.objects.all(),
            'education': Education.objects.all(),
            'technologies': Technology.objects.all(),
            'portfolio': certifications,
            'grouped_portfolio': grouped_portfolio,
        })

        return context

