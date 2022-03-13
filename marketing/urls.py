from django.urls import re_path
from.views import MarketingPreferenceUpdateView, MailchimpWebhookView

urlpatterns = [
    re_path(r'^settings/email/$', MarketingPreferenceUpdateView.as_view(), name='marketing-pref'),
    re_path(r'^webhook/mailchimp/$', MailchimpWebhookView.as_view(), name='webhook-mailchimp'),
]
