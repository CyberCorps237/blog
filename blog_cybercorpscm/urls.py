from django.urls import path
from django.conf.urls.static import static
from blog_cybercorpscm import views
from cybercorpscm_blog import settings


urlpatterns = [
    path("",views.index, name = 'index'),   
    path('post/<int:post_id>',views.post, name = 'post'),   
    path("contact/",views.contact, name = 'contact'),   
    path("about/",views.apropos, name = 'about'),   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)