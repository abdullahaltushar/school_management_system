from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('login/',views.login, name="login"),
    path('logout/',views.logout, name="logout"),
   
    # path('activate/', views.activate, name="activate"),
    # path('profile/', views.profile, name="profile"),
    # path('profile_edit/', views.profile_edit, name="profile_edit"),
    # path('edit_product/<int:id>/', views.edit_product, name="edit_product"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)