from django.urls import path
from . import views


app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('detail/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('services/', views.ServicesView.as_view(), name='Services'),
    path('staff/', views.StaffView.as_view(), name='staff'),
    path('staff/<int:pk>/', views.StaffDetailView.as_view(), name='staffdetail'),
    path('book/', views.BookView.as_view(), name='book'),
    path('book2/', views.Book2View.as_view(), name='book2'),

]
