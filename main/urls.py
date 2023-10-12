from django.urls import path
from main.views import show_main
from main.views import show_main, add_product, show_xml, show_xml_by_id, show_json_by_id, show_json, register,  login_user, logout_user
from main.views import increment_quantity, decrement_quantity, delete_item, add_product_ajax, get_product_json


app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'), path('add-product', add_product, name='add_product'),
    path('xml/', show_xml, name='show_xml'), path('xml/<int:id>/', show_xml_by_id, name="show_xml_by_id")
    ,path('json/<int:id>/', show_json_by_id, name="show_json_by_id")
    ,path('json/', show_json, name='show_json'), path('register/', register, name='register')
    ,path('logout/', logout_user, name='logout'),path('login/', login_user, name='login'), 
    path('increment_quantity/<int:product_id>/', increment_quantity, name='increment_quantity'),
    path('decrement_quantity/<int:product_id>/', decrement_quantity, name='decrement_quantity'),
    path('delete_item/<int:product_id>/', delete_item, name='delete_item'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax'),
]
