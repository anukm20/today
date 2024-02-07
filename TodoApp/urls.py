from django.urls import path
from . import views
app_name='phone'
urlpatterns = [
    path('',views.Home,name='home'),
    path('<slug:c_slug>/',views.Home,name='product_by_category'),
    path('details/<int:id>',views.Details,name='details'),

]
