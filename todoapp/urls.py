from . import views
from django.urls import include, path
app_name='todoapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('add/',views.add,name='add'),
    path('done/<int:task_id>',views.done,name='done'),
    path('update/<int:task_id>',views.update,name='update')
]
