from django.urls import path
from .views import ViewRateActivity,ViewRateActivityCRUD

urlpatterns = [
    path('activities/',ViewRateActivity.as_view()),
    path('activities/<int:pk>/',ViewRateActivityCRUD.as_view())
]

