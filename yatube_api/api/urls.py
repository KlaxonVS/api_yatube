from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, CommentViewSet, GroupViewSet


router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('posts/(?P<post_id>\\d+)/comments',
                CommentViewSet,
                basename='comments')
router.register('groups', GroupViewSet, basename='groups')


urlpatterns = [
    path('', include(router.urls), name='posts-api'),
]
