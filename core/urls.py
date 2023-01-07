from django.urls import path
from core import views

app_name = 'core'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('articles/', views.ArticleList.as_view(), name='article-list'),
    path('articles/<int:pk>/', views.ArticleDetail.as_view(), name='article-detail'),
    path('articles/create/', views.ArticleCreate.as_view(), name='article-create'),
    path('articles/update/<int:pk>/', views.ArticleUpdate.as_view(), name='article-update'),
    path('articles/delete/<int:pk>/', views.ArticleDelete.as_view(), name='article-delete'),
]
