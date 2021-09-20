from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rest.views import Index, PostViewSet
    # PostList, PostDetails

# post_list, post_details

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')

urlpatterns=[
    path('', Index),
    # path('post/', post_list),
    # path('post/<int:pk>', post_details),
    # path('post/', PostList.as_view()),
    # path('post/<int:id>/', PostDetails.as_view()),
    path('api/', include(router.urls)),
]