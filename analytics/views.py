from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, Sum, Avg
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render

from orders.models import Order

class SalesView(LoginRequiredMixin, TemplateView):
    template_name = 'analytics/sales.html'

    def dispatch(self,*args, **kwargs):
        user = self.request.user
        if not user.is_staff:
            return render(self.request, "400.html", {})
        return super(SalesView, self).dispatch(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(SalesView, self).get_context_data(*args, **kwargs)
        qs = Order.objects.all()        
        context['orders'] = qs
        context['recent_orders'] = qs.recent()[:6]
        context['shipped_orders'] = qs.recent().by_status(status="shipped")[:5]
        context['paid_orders'] = qs.recent().by_status(status="paid")[:5]
        context['refunded_orders'] = qs.recent().by_status(status="refunded")[:5]
        context['recent_order_total'] = context['recent_orders'].aggregate(
                                            Sum("total"),
                                            Avg("total")
                                            )
        context['recent_cart_data'] = context['recent_orders'].aggregate(
                                            Avg("cart__cart_items__total"),
                                            Count("cart__cart_items__quantity")
                                            )
        #qs = Order.objects.all().aggregate(Sum("total"), Avg("total"), Avg("cart__cart_items__total"), Count("cart__cart_items__quantity"))
        # ann = qs.annotate(products_avg=Avg('cart__products__price'), product_total = Sum('cart__products__price'), product_count = Count('cart__products'))
        return context