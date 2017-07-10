from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.utils import timezone

SOURCE_CHOICES = {
    ('adwords', 'AdWords'),
    ('taboola', 'Taboola'),
    ('outbrain', 'Outbrain'),
    ('timesinternet', 'Times Internet')
}


class File(models.Model):
    """
    File to be uploaded
    """
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    date = models.DateField(blank=False, null=False, default=timezone.now())
    created_at = models.DateField(blank=False, null=False, default=timezone.now())
    updated_at = models.DateField(blank=False, null=False, default=timezone.now())
    file = models.FileField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    source = models.CharField(choices=SOURCE_CHOICES, default='adwords', max_length=100)

    def __str__(self):
        """
        Name of file
        :return: String representation of file
        """
        return str(self.name)


class Campaign(models.Model):
    """
    Stores details for each campaign
    """
    utm_source = models.CharField(db_index=True, max_length=255, null=True, blank=True)
    utm_medium = models.CharField(db_index=True, max_length=255, null=True, blank=True)
    utm_campaign = models.CharField(db_index=True, max_length=255, null=True, blank=True)
    utm_content = models.CharField(db_index=True, max_length=255, null=True, blank=True)
    utm_keyword = models.CharField(db_index=True, max_length=255, null=True, blank=True)
    campaign_name = models.CharField(max_length=255, null=True, blank=True)
    campaign_date = models.DateField(db_index=True, null=False, blank=False)
    unique_visits = models.IntegerField(null=True, blank=True)
    visits = models.IntegerField(null=True, blank=True)
    bounce_count = models.IntegerField(null=True, blank=True)
    actions_count = models.IntegerField(null=True, blank=True)
    total_spent = models.DecimalField(max_digits=30, decimal_places=2, null=True, blank=True)
    platform_source = models.CharField(max_length=255, null=False, blank=False, default=1)
    platform_ad_id = models.BigIntegerField(null=True, blank=True)
    platform_campaign_id = models.BigIntegerField(null=True, blank=True)
    platform_adset_id = models.BigIntegerField(null=True, blank=True)
    platform_url = models.TextField(max_length=200, null=True, blank=True)
    platform_campaign_status = models.TextField(max_length=200, null=True, blank=True)
    platform_ad_status = models.TextField(max_length=200, null=True, blank=True)
    ad_introduction_text = models.TextField(max_length=400, null=True, blank=True)
    ad_headline_text = models.TextField(max_length=400, null=True, blank=True)
    ad_line_text = models.TextField(max_length=400, null=True, blank=True)
    image_url = models.URLField(max_length=255, null=True, blank=True)
    cost_per_mile = models.DecimalField(max_digits=30, decimal_places=2, null=True, blank=True)
    cost_per_click = models.DecimalField(max_digits=30, decimal_places=2, null=True, blank=True)
    cost_per_action = models.DecimalField(max_digits=30, decimal_places=2, null=True, blank=True)
    cost_per_pixel = models.DecimalField(max_digits=30, decimal_places=2, null=True, blank=True)
    click_through_rate = models.DecimalField(max_digits=30, decimal_places=2, null=True, blank=True)
    impressions = models.IntegerField(null=True, blank=True)
    clicks = models.IntegerField(null=True, blank=True)
    likes = models.IntegerField(null=True, blank=True)
    shares = models.IntegerField(null=True, blank=True)
    follows = models.IntegerField(null=True, blank=True)
    comments = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    file = models.ForeignKey(File, null=True, blank=True)

    class Meta:
        db_table = 'campaigns'

    def __str__(self):
        return "{0}_{1}".format(self.campaign_name, str(self.campaign_date))


class CampaignConversion(models.Model):
    """
    Stores the conversion metrics retrieved from Redash.
    """
    campaign_date = models.DateField(db_index=True, null=False, blank=False)
    utm_source = models.CharField(db_index=True, max_length=255, null=True, blank=True)
    utm_medium = models.CharField(db_index=True, max_length=255, null=True, blank=True)
    utm_campaign = models.CharField(db_index=True, max_length=255, null=True, blank=True)
    utm_content = models.CharField(db_index=True, max_length=255, null=True, blank=True)
    initiated = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    registered = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    documents_received = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    activated = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    invested = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'campaign_conversions'

    def __str__(self):
        return "{0}_{1}_{2}".format(self.campaign_date, self.utm_source, self.utm_medium)
