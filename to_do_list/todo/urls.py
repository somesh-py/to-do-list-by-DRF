from django.urls import path
from . import views


urlpatterns = [
    path('',views.Homeview),
    path('get/<str:pk>',views.DetailView),
    path('create/',views.CreateView),
    path('update/<str:pk>',views.UpdateView),
    path('delete/<str:pk>',views.DeleteView),
]
