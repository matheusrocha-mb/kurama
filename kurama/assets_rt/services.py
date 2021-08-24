import requests
from logging import error
import time

from kurama.settings import Assets, Method


class AssetTickerService():
    def __init__(self, request, asset_name):
        self.request_method = Method.TICKER
        self.asset = Assets(asset_name)
        self.json = self._get_asset_response()


    def _get_asset_response(self):
        try:
            response = requests.get(f'https://www.mercadobitcoin.net/api/{self.asset.name}/{self.request_method}')
            return response.json()
        except error as e:
            return self._build_fail_response(e)

    def get_higher_price(self):
        return {
            'higher_price': self.json['ticker']['high'],
            'Data': self._build_data()
        }

    def get_lower_price(self):
        return {
            'lower_price': self.json['ticker']['low'],
            'Data': self._build_data()
        }

    def get_last_price(self):
        return {
            'last_price': self.json['ticker']['last'],
            'Data': self._build_data()
        }

    def get_higher_buy_offer(self):
        return {
            'higher_buy_offer': self.json['ticker']['buy'],
            'Data': self._build_data()
        }

    def get_lower_sell_offer(self):
        return {
            'lower_sell_offer': self.json['ticker']['sell'],
            'Data': self._build_data()
        }
        
    def get_all_response(self):
        return self.json

    def _build_data(self):
        date = self.json['ticker']['date']
        return time.strftime("%d-%m-%Y %H:%M:%S", time.localtime(date))
  
    def _build_fail_response(self, e):
        return {
            'error': e
        }


class AssetDaySummaryService():
    def __init__(self, request, asset_name):
        self.request_method = Method.DAY_SUMMARY
        self.asset = Assets(asset_name)
        self.year = request.data.get('year')
        self.month = request.data.get('month')
        self.day = request.data.get('day')

    def get_day_summary(self):
        try:
            response = requests.get(f'https://www.mercadobitcoin.net/api/{self.asset.name}/{self.request_method}/{self.year}/{self.month}/{self.day}')
            return response.json()

        except error as e:
            return self._build_fail_response(e)

    def _build_fail_response(self, e):
        return {
            'error': e,
        }


class Teste2():
    pass