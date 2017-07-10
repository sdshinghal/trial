from templating.models import File, Campaign
from templating.forms import FileUploadForm, DashboardFilterForm
from templating.serializers import FileSerializer, CampaignSerializer
from rest_framework.views import APIView
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import HTMLFormRenderer, TemplateHTMLRenderer
from django.shortcuts import render, redirect
import django_filters
import logging

logging.basicConfig(level=20)


class Dashboard(generics.ListAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    filter_fields = ('campaign_name', 'platform_source', 'campaign_date')
    renderer_classes = (TemplateHTMLRenderer, )


# Attempt 3


# def dashboard(request):
#     platforms = [campaign.platform_source for campaign in Campaign.objects.all()]
#     dates = [campaign.campaign_date for campaign in Campaign.objects.all()]
#     form = DashboardFilterForm
#     if request.GET.get('campaign'):
#         # import pdb
#         # pdb.set_trace()
#         campaign_filter = request.GET.get('campaign_name')
#         platform_filter = request.GET.get('platform_source')
#         dates_filter = request.GET.get('campaign_date')
#         if campaign_filter == 'All':
#             campaigns = Campaign.objects.all()
#         else:
#             campaigns = Campaign.objects.filter(campaign_name=campaign_filter)
#         if platform_filter == 'All':
#             pass
#         else:
#             campaigns = campaigns.filter(platform_source=platform_filter)
#         if dates_filter == 'All':
#             pass
#         else:
#             campaigns = campaigns.filter(campaign_date=dates_filter)
#
#         return render(request, 'templating/dashboard.html', {"campaigns": campaigns})
#     # elif request.GET.get('platform'):
#     #     platform_filter = request.GET.get('platform_source')
#     #     campaigns = Campaign.objects.filter(platform_source=platform_filter)
#     # elif request.GET.get('dates'):
#     #     dates_filter = request.GET.get('campaign_date')
#     #     campaigns = Campaign.objects.filter(campaign_date=dates_filter)
#     else:
#         campaigns = Campaign.objects.all()
#
#     context_dict = {"campaigns": campaigns, "platforms": platforms, "dates": dates, "form": form}
#     return render(request, 'templating/dashboard.html', context_dict)


def dashboard(request):
    form = DashboardFilterForm
    campaigns = Campaign.objects.all()
    dates = [campaign.campaign_date for campaign in Campaign.objects.all()]
    platforms = [campaign.platform_source for campaign in Campaign.objects.all()]

    # query = request.GET.get("q")
    # if query:
    #     campaigns = campaigns.filter(campaign_name=query)[:]
    #     return render(request, 'templating/dashboard.html', {"campaigns": campaigns})
    #
    # else:
    #     return render(request, 'templating/dashboard.html', {"campaigns": campaigns})

    if request.GET.get('campaign'):

        campaign_filter = request.GET.get('campaign')

        if campaign_filter == 'all':
            campaigns = Campaign.objects.all()
        else:
            campaigns = campaigns.filter(campaign_name=campaign_filter)[:]

    if request.GET.get('platform'):
        platform_filter = request.GET.get('platform')

        if platform_filter == 'all':
            campaigns = campaigns
        else:
            campaigns = campaigns.filter(platform_source=platform_filter)

    if request.GET.get('dates'):
        dates_filter = request.GET.get('dates')

        if dates_filter == 'all':
            campaigns = campaigns
        else:
            campaigns = Campaign.objects.filter(campaign_date=dates_filter)

    context_dict = {"campaigns": campaigns, "platforms": platforms, "dates": dates, "form": form}
    return render(request, 'templating/dashboard.html', context_dict)

#
# class DashboardFilter(django_filters.FilterSet):
#
#     class Meta:
