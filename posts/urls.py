from django.urls import path

from . views import HomeView, ArticalDetailView, AddPostView, DeletePostView, AddCategoryView, CategoryView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticalDetailView.as_view(), name="article"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('add_category/', AddCategoryView.as_view(), name="add_category"),
    path('delete/<int:pk>', DeletePostView.as_view(), name="delete"),
    path('category/<str:cate>', CategoryView, name='category')
]