from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload_clipping/', views.upload_clipping, name='upload_clipping'),
    path('upload_img/', views.upload_img, name='upload_img'),
    path('overview/', views.overview, name='overview'),
    path('overview/<int:id>', views.overview_by_book, name='overview_book'),
    path('export/<int:clipping_id>', views.export_clipping, name='export'),
    path('del_clipping/', views.del_clipping, name='del_clipping'),
    path('add_clipping/', views.add_clipping, name='add_clipping'),
    path('book/', views.book, name='book'),
    path('book/<int:book_id>', views.view_by_book, name='book_clipping'),
    path('author/', views.author, name='author'),
    path('register/', views.register, name='register'),
    path('statistics/', views.statistics, name='statistics'),
    path('statistics/clippingNum/<int:year>', views.get_clipping_num_per_month),
]