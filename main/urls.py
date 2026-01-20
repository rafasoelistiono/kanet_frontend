# from django.urls import path
# from main.views import show_main, create_news, show_news, show_xml, show_json, show_json_by_id, show_xml_by_id, register, login_user, logout_user, edit_news, delete_news, add_news_entry_ajax

# app_name = 'main'

# urlpatterns = [
#     path('', show_main, name='show_main'),
#     path('create-news/', create_news, name='create_news'),
#     path('news/<str:id>/', show_news, name='show_news'),
#     path('xml/', show_xml, name='show_xml'),
#     path('json/', show_json, name='show_json'),
#     path('xml/<str:news_id>/', show_xml_by_id, name='show_xml_by_id'),
#     path('json/<str:news_id>/', show_json_by_id, name='show_json_by_id'),
#     path('register/', register, name='register'),
#     path('login/', login_user, name='login'),
#     path('logout/', logout_user, name='logout'),
#     path('news/<uuid:id>/edit', edit_news, name='edit_news'),
#     path('news/<uuid:id>/delete', delete_news, name='delete_news'),
#     path('create-news-ajax', add_news_entry_ajax, name='add_news_entry_ajax'),
# ]


# main/urls.py
from django.urls import path
from main.views import show_main, register_view, login_view, logout_view, halte_sekitar_view, navigasi_halte_view, jadwal_halte_list_view, jadwal_halte_detail_view, lokasi_sekarang_view, feedback_view

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('halte-sekitar/', halte_sekitar_view, name='halte_sekitar'),
    path('navigasi/<int:halte_id>/', navigasi_halte_view, name='navigasi_halte'),
    path('jadwal-halte/', jadwal_halte_list_view, name='jadwal_halte_list'),
    path('jadwal-halte/<int:halte_id>/', jadwal_halte_detail_view, name='jadwal_halte_detail'),
    path('lokasi-sekarang/', lokasi_sekarang_view, name='lokasi_sekarang'),
    path('feedback/', feedback_view, name='feedback'),
]