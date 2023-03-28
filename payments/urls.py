from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from .views import paymentView

app_name = 'payments'
 
urlpatterns = [
    path('', views.home, name="index"),
    path('payment/<str:id>', paymentView.as_view(), name="payment"),
    # path('qrPay/<str:id>', qrView.as_view(), name="view_qr"),
    path('access/token', views.getAccessToken, name='get_mpesa_access_token'),
    path('online/lipa', views.lipa_na_mpesa_online, name='lipa_na_mpesa'),
    path('transaction/complete/<str:id>/<str:contact>/', views.lipa_na_mpesa_online),
    path('logout', views.logout_view, name="logout"),
]
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)