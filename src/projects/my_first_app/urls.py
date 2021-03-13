from django.contrib import admin
from django.urls import path

from projects.my_first_app.views import hello_word

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello_word, name='hello_world')
]
