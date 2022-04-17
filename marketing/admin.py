from django.contrib import admin

from .models import MarketingPreference

@admin.register(MarketingPreference)
class MarketingPreferenceAdmin(admin.ModelAdmin):
    list_display = [
        '__str__', 'subscribed', 'updated'
    ]
    readonly_fields = [
        'mailchimp_subscribed',
        'mailchimp_msg',
        'timestamp',
        'updated',
    ]

    class meta:
        model = MarketingPreference
        fields = [
            'user',
            'subscribed',
            'mailchimp_msg',
            'mailchimp_subscribed',
            'timestamp',
            'updated',
        ]
