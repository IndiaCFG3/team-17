from django.urls import path
from . import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView,PostGraphView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('', views.home , name = 'blog-home'),
    path('', PostListView.as_view() , name = 'blog-home'),
    path('user/<str:title>', UserPostListView.as_view() , name = 'user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view() , name = 'post-detail'),
    path('post/new/', PostCreateView.as_view() , name = 'post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view() , name = 'post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view() , name = 'post-delete'),
    path('about/', views.about , name = 'blog-about'),
    path('post/graph/', PostGraphView.as_view() , name = 'post-graph'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)