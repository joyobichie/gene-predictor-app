from django.urls import path
from . import views

urlpatterns = [
   path('predict_traits/',views.predict_traits_view,name='predict_traits',)
]