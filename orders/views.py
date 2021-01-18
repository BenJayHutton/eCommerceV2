from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, JsonResponse
from django.views.generic import ListView, DetailView, View

from .models import Order, ProductPurchase


class OrderListView(LoginRequiredMixin, ListView):

    def get_context_data(self, *args, **kwargs):
        request = self.request
        context = super(OrderListView, self).get_context_data(*args, **kwargs)
        context['title'] = "Orders"
        return context

    def get_queryset(self):
        return Order.objects.by_request(self.request).not_created()


class OrderDetailView(LoginRequiredMixin, DetailView):

    def get_context_data(self, *args, **kwargs):
        request = self.request
        context = super(OrderDetailView, self).get_context_data(*args, **kwargs)
        context['title'] = "Order Details"
        return context

    def get_object(self):
        qs = Order.objects.by_request(self.request).filter(order_id=self.kwargs.get('order_id'))
        if qs.count()==1:
            return qs.first()
        raise Http404


class LibraryView(LoginRequiredMixin, ListView):
    template_name = 'orders/library.html'

    def get_context_data(self, *args, **kwargs):
        request = self.request
        context = super(LibraryView, self).get_context_data(*args, **kwargs)
        context['title'] = "Library View"
        return context

    def get_queryset(self):
        return ProductPurchase.objects.products_by_request(self.request) #by_request(self.request).digital()


class VerifyOwnership(View):

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            data = request.GET
            product_id = data.get('product_id')
            if product_id is not None:
                product_id = int(product_id)
                ownership_ids = ProductPurchase.objects.products_by_id(request)
                if product_id in ownership_ids:
                    return JsonResponse({'owner': True})
                return JsonResponse({'owner': False})
        raise Http404


class OrderConfirmation(View):
    def post(self, request):
        order_id = request.POST.get('order_id', None)
        if order_id is not None:
            Order.objects.email_order(order_id)
            #print success to messages
        else:
            #print order not found to messages
            raise Http404
        raise Http404
