from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, JsonResponse
from django.shortcuts import redirect
from django.urls import reverse
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
        return ProductPurchase.objects.products_by_request(self.request)  #by_request(self.request).digital()


class VerifyOwnership(View):

    def get(self, request, *args, **kwargs):
        if request.request.accepts('application/json'):
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
        order_qs = Order.objects.filter(order_id=order_id)
        for order in order_qs:
            email = order.billing_profile.email
        if order_id is not None:
            Order.objects.email_order(order_id)
            messages.success(request, "An email has been sent to: "+email)
            url_redirect = (reverse("orders:detail", kwargs={"order_id": order_id}))
            return redirect(url_redirect)
        else:
            raise Http404
