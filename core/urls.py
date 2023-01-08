from django.urls import path
from core import views

app_name = 'core'

urlpatterns = [
    path('', views.base.IndexView.as_view(), name='index'),
    path('login/', views.base.Login.as_view(), name='login'),
    path('logout/', views.base.Logout.as_view(), name='logout'),
    path('articles/', views.article.ArticleList.as_view(), name='article-list'),
    path('articles/<int:pk>/', views.article.ArticleDetail.as_view(), name='article-detail'),
    path('articles/create/', views.article.ArticleCreate.as_view(), name='article-create'),
    path('articles/update/<int:pk>/', views.article.ArticleUpdate.as_view(), name='article-update'),
    path('articles/delete/<int:pk>/', views.article.ArticleDelete.as_view(), name='article-delete'),
]
