from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.shared_list, name='shared_list'),
    path('', views.get_css, name='get_css'),
    path('<category>/<next_button>', views.title, name='button'),
]
