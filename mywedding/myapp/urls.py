
from django.urls import path,include
from . import views
app_name='myapp'
urlpatterns = [

  path('',views.index,name='index'),
  path('go/',views.go,name='go'),
  path('ex/',views.ex,name='ex'),
  path('<slug:c_slug>/',views.allyear,name='allyear'),
  #path('<slug:c_slug>/<slug:p_slug>/', views.proDetail, name='prodCatdetail'),

]