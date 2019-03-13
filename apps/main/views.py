from django.urls import reverse
from django.views.generic import TemplateView, RedirectView
from .utils import place_order, process_client_order_list


class IndexView(TemplateView):
    template_name = "index.html"


class PaymentRedirectView(RedirectView):
    
    def __init__(self):
        self.payment_url = None
        super(PaymentRedirectView, self).__init__()

    def dispatch(self, request, *args, **kwargs):
        pay_amount = request.POST.get("order_amount")
        order_url = request.build_absolute_uri(reverse('order_list'))
    
        placed_order = place_order(pay_amount, order_url)
        self.payment_url = placed_order.payment_url \
            if placed_order else reverse('index')

        return \
            super(PaymentRedirectView, self).dispatch(request, *args, **kwargs)
    
    def get_redirect_url(self, *args, **kwargs):
        return self.payment_url


class OrderListView(TemplateView):
    template_name = "order_list.html"
    
    def get_context_data(self, **kwargs):
        processed_order_list = process_client_order_list()
        context = dict(orders=processed_order_list)
        return context
