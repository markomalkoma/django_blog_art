from django.urls import path
from . import views
from .views import PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns=[path('', views.home, name='blog-home'),
			 path('about/', views.about, name='blog-about'),
                         path('reverse/<name>/<int:order>', views.reverse, name='blog-reverse'),
                         path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
                         path('post/new/', PostCreateView.as_view(), name='post-create'),
                         path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
                         path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
                         path('comment/new/<int:post_id>/', views.comment_create, name='comment-create'),
                         path('comment/detail/', views.comment_detail, name='comment-detail'),
                         path('comment/<int:comment_id>/update/', views.comment_update, name='comment-update'),
                         path('comment/<int:comment_id>/delete/', views.comment_delete, name='comment-delete'),
                         path('subcomment/new/<int:comment_id>/', views.subcomment_create, name='subcomment-create'),
                         path('subcomment/detail/', views.subcomment_detail, name='subcomment-detail'),
                         path('subcomment/<int:subcomment_id>/update/', views.subcomment_update, name='subcomment-update'),
                         path('subcomment/<int:subcomment_id>/delete/', views.subcomment_delete, name='subcomment-delete'),
                         ]
