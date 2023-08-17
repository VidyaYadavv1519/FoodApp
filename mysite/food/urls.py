from .import views
from django.urls import path
from .views import UpdateItemView
# Namespacing
app_name = 'food'
urlpatterns = [
    #/food/
    path('',views.IndexClassView.as_view(),name='index'),
    #/food/1
    path('<int:pk>/',views.ItemDetailView.as_view(),name='detail'),
    path('item/',views.ItemView.as_view(),name='item'),
    # add items
    path('add',views.CreateItem.as_view(),name='create_item'),
    # edit item
    path('update/<int:id>/',views.UpdateItemView.as_view(),name='update_item'),
    # delete item
    path('delete/<int:id>/',views. DeleteItemView.as_view(),name='delete_item'),
]