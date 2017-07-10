from django.contrib import admin
from .models import Campaign, File


class CampaignAdmin(admin.ModelAdmin):
    """
    Admin for the Campaigns model
    """
    list_display = ('campaign_name', 'utm_source', 'utm_medium', 'utm_content', 'utm_campaign', 'utm_keyword',
                    'unique_visits', 'visits', 'bounce_count', 'actions_count', 'campaign_date', 'platform_ad_id',
                    'platform_campaign_id', 'platform_url', 'image_url', 'platform_campaign_status',
                    'platform_ad_status', 'ad_introduction_text', 'ad_headline_text', 'ad_line_text', 'total_spent',
                    'cost_per_mile', 'cost_per_click', 'cost_per_pixel', 'cost_per_action', 'click_through_rate',
                    'impressions', 'clicks', 'likes', 'shares', 'follows', 'comments', 'created_at', 'updated_at')
    search_fields = ['utm_campaign', 'campaign_date', 'utm_source', 'utm_medium']


class FileAdmin(admin.ModelAdmin):
    """
    Admin for the File model
    """
    list_display = ('owner', 'name', 'file', 'source', 'date')
    search_fields = ['name', 'source', 'owner']

admin.site.register(Campaign, CampaignAdmin)
admin.site.register(File, FileAdmin)
