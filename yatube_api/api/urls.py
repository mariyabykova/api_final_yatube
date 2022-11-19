from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

from .views import PostViewSet, GroupViewSet, CommentViewSet


router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet)
router.register(
    r'^posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comment'
)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]