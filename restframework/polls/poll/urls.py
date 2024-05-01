from django.urls import path
from .views import *

app_name = "poll"

urlpatterns = [
    path("", PollList.as_view(), name="polls_list"),
    path("<int:pk>/", PollDetail.as_view(), name="detail"),
]   
