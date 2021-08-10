from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, ReviewViewSet, UserViewSet

router_v1 = DefaultRouter(trailing_slash='optional')
router_v1.register('users/?', UserViewSet)

router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/?',
    CommentViewSet, basename="comments")
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments/?',
    ReviewViewSet, basename="reviews")
router_v1.register('users/?', UserViewSet)

urlpatterns = [

    path('v1/', include(router_v1.urls)),    
]
