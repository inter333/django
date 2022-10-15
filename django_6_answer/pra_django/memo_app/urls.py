from django.urls import path
from . import views
from memo_app import views
#from memo_app.views import IndexView

#app_name="memo_app"

urlpatterns = [
    #path('',IndexView.as_view()),
    path('', views.index, name='index'),
    path('post', views.post, name='post'),
    path('post_comment/<str:memo>', views.post_comment, name='comment'),
    path('add_comment/<str:memo>', views.comment, name='add_comment'),
    path('<int:now_page>', views.index, name='index'),
    path('set_record_number', views.set_record_number, name='set_record_number'),
    path('set_order_number', views.set_order_number, name='set_order_number'),
    path('update/<int:num>',views.update,name='update'),
    path('delete/<int:num>',views.delete,name='delete'),
]
