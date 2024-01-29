from django.shortcuts import render
from django.conf import settings
from django.views.generic.base import TemplateView
import stripe  

stripe.api_key = settings.STRIPE_SECRET_KEY
 
class HomePageView(TemplateView):
    template_name='packages.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context 
# Create your views here.
def charge(request):
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount = 500,
            currency = 'inr',
            description = 'Payment Gateway',
            source=request.POST['stripeToken']

        )
        return render(request, 'charge.html',charge)