from django.urls import path
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView
from . import views

urlpatterns = [
    path('vpost/', PostListView.as_view(),name='vpost-page'),
    path('vpost/<int:pk>', PostDetailView.as_view(),name='post-vdetail'),    
    path('vpost/new/', PostCreateView.as_view(),name='post-vform'),
    path('vpost/<int:pk>/update', PostUpdateView.as_view(),name='post-vupdate'),
    path('vpost/<int:pk>/delete', PostDeleteView.as_view(),name='post-vdelete'),
    
]