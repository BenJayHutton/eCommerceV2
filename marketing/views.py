from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.conf import settings
from django.views.generic import UpdateView, View
from django.shortcuts import render, redirect

from .forms import MarketingPreferenceForm
from .mixins import CsrfExemptMixin
from .models import MarketingPreference
from .utils import Mailchimp

MAILCHIMP_EMAIL_LIST_ID = getattr(settings, "MAILCHIMP_EMAIL_LIST_ID", None)

class MarketingPreferenceUpdateView(SuccessMessageMixin, UpdateView):
    form_class = MarketingPreferenceForm
    template_name = 'base/forms.html'
    success_url = '/marketing/settings/email/'
    success_message = 'Your email prefefence have bee updated'

    def dispatch(self, *args, **kwargs):
        user = self.request.user
        if not user.is_authenticated:
            return redirect("/account/login/?next=/marketing/settings/email/")
        return super(MarketingPreferenceUpdateView, self).dispatch(*args, **kwargs)


    def get_context_data(self, *args, **kwargs):
        context = super(MarketingPreferenceUpdateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Update Email Preference'
        return context


    def get_object(self):
        user = self.request.user        
        obj, created = MarketingPreference.objects.get_or_create(user=user)
        return obj




'''
POST METHOD

data[merges][FNAME]: Ben

data[list_id]: d70ff2ba46

data[merges][ADDRESS]:

data[ip_opt]: 196.52.84.23

data[reason]: manual

data[email_type]: html

data[merges][EMAIL]: benjayhutton@outlook.com

data[merges][LNAME]: Hutton

data[id]: d12ef5ee6f

data[merges][PHONE]:

fired_at: 2020-10-06 16:01:47

data[merges][BIRTHDAY]:

type: unsubscribe

data[web_id]: 339463537

data[email]: benjayhutton@outlook.com

'''


class MailchimpWebhookView(CsrfExemptMixin, View):
    def post(self, request, *args, **kwargs):
        data = request.POST
        list_id = data,get('data[list_id]')
        if str(list_id) == str(MAILCHIMP_EMAIL_LIST_ID):
            hook_type = data.get("type")
            email = data.get('data[email]')
            response_status, response_status = Mailchimp().check_subscription_status(email)
            sub_status = response['status']
            is_subbed = None
            mailchimp_subbed = None
            if sub_status =="subscribed":
                is_subbed, mailchimp_subbed(True,True)
            elif sub_status =="unsubscribed":
                is_subbed, mailchimp_subbed(False,False)
            if is_subbed is not None and mailchimp_subbed is not None:
                qs = MarketingPreference.objects.filter(user__email__iexact=email)
                if qs.exits():
                    qs.Update(subscribed=is_subbed, mailchimp_subscribed = mailchimp_subbed, mailchimp_msg=str(data))
        return HttpResponse("Thank you", status=200)


# def mailchimp_webhook_view(request):
#     data = request.POST
#     list_id = data,get('data[list_id]')
#     if str(list_id) == str(MAILCHIMP_EMAIL_LIST_ID):
#         hook_type = data.get("type")
#         email = data.get('data[email]')
#         response_status, response_status = Mailchimp().check_subscription_status(email)
#         sub_status = response['status']
#         is_subbed = None
#         mailchimp_subbed = None
#         if sub_status =="subscribed":
#             is_subbed, mailchimp_subbed(True,True)
#         elif sub_status =="unsubscribed":
#             is_subbed, mailchimp_subbed(False,False)
#         if is_subbed is not None and mailchimp_subbed is not None:
#             qs = MarketingPreference.objects.filter(user__email__iexact=email)
#             if qs.exits():
#                 qs.Update(subscribed=is_subbed, mailchimp_subscribed = mailchimp_subbed, mailchimp_msg=str(data))
#     return HttpResponse("Thank you", status=200)