from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.http import JsonResponse
from orders.models import Order
from .models import Payment
import json


class Paypal(View):
    def post(self, request, *args, **kwargs):        
        body = json.loads(request.body.decode("utf-8"))
        user = None
        if request.user.is_authenticated:
            user = request.user

        paymentMethod = body["paymentMethod"]
        orderPk = body["orderPk"]
        orderId = body["orderId"]
        total = body["total"]
        vat = body["vat"]
        shipping = body["shipping"]
        subTotal = body["subTotal"]
        paypalOrderID = body["paypalOrderID"]
        paypalPayerID = body["paypalPayerID"]
        is_paid = body["is_paid"]
        
        order_obj = Order.objects.get(pk=orderPk)
        is_prepared = order_obj.check_done()
        if is_prepared:
            if is_paid:
                order_obj.mark_paid()
                request.session['cart_item_count'] = 0
                del request.session['cart_id']
                new_payment_obj = Payment.objects.get_or_create(
                    user=user,
                    order=order_obj,
                    paymentMethod=paymentMethod,
                    paypalOrderID=paypalOrderID,
                    paypalPayerID=paypalPayerID,
                    is_paid=True,
                    summery=body,
                    total=subTotal
                )
                return JsonResponse({"cartSuccess": True})
            else:
                return JsonResponse({"cartSuccess": False})
        return JsonResponse({"cartSuccess": False})


class PaymentHome(TemplateView):
    template_name = 'payment/home.html'

    def dispatch(self, *args, **kwargs):
        user = self.request.user
        if not user.is_staff:
            return render(self.request, "400.html", {})
        return super(PaymentHome, self).dispatch(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(PaymentHome, self).get_context_data(*args, **kwargs)
        return context
