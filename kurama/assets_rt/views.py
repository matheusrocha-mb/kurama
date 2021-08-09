import json
import logging

from rest_framework.views import APIView
from rest_framework.response import Response
from requests.models import HTTPError

from kurama.assets_rt.services import AssetTickerService, AssetDaySummaryService


logger = logging.getLogger("kurama.assets_rt.views")


class RealTimeValueView(APIView):

    def get(self, request, *args, **kwargs):
        asset_name = self.kwargs.get('op')
        try:
            response = AssetTickerService(request, asset_name).get_lower_sell_offer()
            return Response(response, content_type=json)
            
        except:
            return HTTPError


class DaySummaryView(APIView):

    def get(self, request, *args, **kwargs):
        asset_name = self.kwargs.get('op')
        try:
            response = AssetDaySummaryService(request, asset_name).get_day_summary()
            return Response(response, content_type=json)
        except:
            return HTTPError


class LastValueView(APIView):

    def get(self, request, *args, **kwargs):
        asset_name = self.kwargs.get('op')
        try:
            response = AssetTickerService(request, asset_name).get_last_price()
            return Response(response, content_type=json)
        except:
            return HTTPError


class HigherBuyOfferView(APIView):

    def get(self, request, *args, **kwargs):
        asset_name = self.kwargs.get('op')
        try:
            response = AssetTickerService(request, asset_name).get_higher_buy_offer()
            return Response(response, content_type=json)
        except:
            return HTTPError


class HigherPriceView(APIView):

    def get(self, request, *args, **kwargs):
        asset_name = self.kwargs.get('op')
        try:
            response = AssetTickerService(request, asset_name).get_higher_price()
            return Response(response, content_type=json)
        except:
            return HTTPError


class LowerPriceView(APIView):

    def get(self, request, *args, **kwargs):
        asset_name = self.kwargs.get('op')
        try:
            response = AssetTickerService(request, asset_name).get_lower_price()
            return Response(response, content_type=json)
        except:
            return HTTPError


class GetAllTickersView(APIView):

    def get(self, request, *args, **kwargs):
        asset_name = self.kwargs.get('op')
        try:
            response = AssetTickerService(request, asset_name).get_lower_sell_offer()
            return Response(response, content_type=json)
            
        except:
            return HTTPError
