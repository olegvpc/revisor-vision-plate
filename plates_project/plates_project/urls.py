from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.contrib import admin

from django.conf.urls import url
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from plates.views import PlateGetViewSet, PlateAddViewSet, IndexView

from rest_framework.authtoken import views

router = DefaultRouter()
router.register(r'plate/get', PlateGetViewSet)
router.register(r'plate/add', PlateAddViewSet)

urlpatterns = [

    path('', IndexView.as_view(), name='index'),
    # path('plate/get/', getting_plate),
    path('', include(router.urls)),

    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    # JWT-эндпоинты, для управления JWT-токенами:
    path('auth/', include('djoser.urls.jwt')),
]
