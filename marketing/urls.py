from django.conf.urls import url
from.views import MarketingPreferenceUpdateView, MailchimpWebhookView

urlpatterns = [
    url(r'^settings/email/$', MarketingPreferenceUpdateView.as_view(), name='marketing-pref'),
    url(r'^webhook/mailchimp/$', MailchimpWebhookView.as_view(), name='webhook-mailchimp'),
]
