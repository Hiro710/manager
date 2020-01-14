from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # managerアプリを呼び出す(managerフォルダのurls.pyを繋ぐ)
    path('', include('manager.urls')),
]
