from django.urls import path

from kurama.assets_rt.views import GetAssetRealTimeValueView
from kurama.assets_rt.views import GetAssetDaySummaryView
from kurama.assets_rt.views import GetAssetLastValueView
from kurama.assets_rt.views import GetAssetOfferView
from kurama.assets_rt.views import GetAssetPriceView


urlpatterns = [
    path('<int:op>/', GetAssetRealTimeValueView.as_view(), name='asset_real_time'),
    path('<int:op>/offer/<int:id>', GetAssetOfferView.as_view(), name='asset_offer'),
    path('<int:op>/price/<int:id>', GetAssetPriceView.as_view(), name='asset_price'),
    path('<int:op>/last/trade', GetAssetLastValueView.as_view(), name='asset_last_trade'),
    path('<int:op>/day/summary', GetAssetDaySummaryView.as_view(), name='asset_day_summary'),
]