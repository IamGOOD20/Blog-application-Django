from django.urls import path
# from . import views
from .views import *

app_name = 'blog'

urlpatterns = [
    # path('', views.post_list, name='post_list'),
    path('', PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         post_detail,
         name='post_detail'
         ),
    path('<int:post_id>/share/', post_share, name='post_share'),
]
