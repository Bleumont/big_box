from django.urls import path
from .views import *

urlpatterns = [
    path('box/', all_boxes, name='all_boxes'),
    path('box/<int:box_id>/', BoxView.as_view(), name='single_box'),
    path('box/<str:slug>/', SlugSearch.as_view(), name='search_slug'),
    path('box/<int:box_id>/activity/', box_activities, name='box_activities'),
    path('box/<int:box_id>/activity/<int:activity_id>/', single_box_activity, name='single_box_activity'),
]
