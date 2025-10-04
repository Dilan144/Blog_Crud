from django.urls import path
from .views import ( 
                    PostListView, 
                    PostDetailView, 
                    PostCreateView, 
                    PostUpdateView,
                    PostDeleteView
            )
                    
urlpatterns = [
    path("", PostListView.as_view(), name="post-list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/new/", PostCreateView.as_view(), name="post_new"),
    path("post/<int:pk>/editar/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/eliminar/", PostDeleteView.as_view(), name="post-delete"),
]
