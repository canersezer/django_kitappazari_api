from django.urls import path
from .views import KitapListCreateAPIView,KitapDetailAPIView,YorumCreateApiView,YorumDeteilApiView



urlpatterns = [
    path('kitaplar/',KitapListCreateAPIView.as_view(),name='kitaplistesi'),
    path('kitaplar/<int:pk>',KitapDetailAPIView.as_view(),name='kitapbilgisi'),
    path('kitaplar/<int:kitap_pk>/yorum_yap',YorumCreateApiView.as_view(),name='yorumyap'),
    path('yorumlar/<int:pk>',YorumDeteilApiView.as_view(),name='yorumlar'),

]
