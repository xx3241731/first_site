
from django.contrib import admin
from django.urls import path
from mysite.views import homepage,lotto,showpost,mychart,mychart2,chart

urlpatterns = [
    path('', homepage),
    path('lotto/',lotto),#連結設置好後 在第4行引入lotto 並到views去define
    path('admin/', admin.site.urls),
    path('post/<str:slug>/', showpost),
    path('mychart/', mychart),
    path('mychart/<int:bid>/',mychart),
    path('mychart2/',mychart2),
    path('chartbydate/<int:year>/<int:month>', chart),
    path('chartbydate/<int:year>/', chart),
]
