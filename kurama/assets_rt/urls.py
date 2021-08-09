from django.urls import path 

from kurama.assets_rt.views import RealTimeValueView
from kurama.assets_rt.views import DaySummaryView
from kurama.assets_rt.views import LastValueView
from kurama.assets_rt.views import HigherBuyOfferView
from kurama.assets_rt.views import LowerPriceView
from kurama.assets_rt.views import HigherPriceView
from kurama.assets_rt.views import GetAllTickersView


urlpatterns = [
    path('<int:op>/', RealTimeValueView.as_view(), name='asset_real_time'),
    path('<int:op>/higher-offer/', HigherBuyOfferView.as_view(), name='asset_higher_offer'),
    path('<int:op>/price/lower/', LowerPriceView.as_view(), name='asset_lower_price'),
    path('<int:op>/price/higher/', HigherPriceView.as_view(), name='asset_higher_price'),
    path('<int:op>/price/last/', LastValueView.as_view(), name='asset_last_price_trade'),
    path('<int:op>/ticker/all', GetAllTickersView.as_view(), name='asset_all_ticker'),
    path('<int:op>/day-summary/', DaySummaryView.as_view(), name='asset_day_summary'),
]