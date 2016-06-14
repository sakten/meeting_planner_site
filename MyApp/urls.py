"""MyApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from Main_Static import views
import registration.views
from registration.forms import RegistrationFormUniqueEmail
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^members/(\d+)/$', views.user_detail),
    url(r'^members/$',views.list_all_users),
    url(r'^meetings/',views.MeetingsCalendar_render),

    url(r'^event_list/$', views.event_list.as_view(), name ="event_list"),
	url(r'^add_event/$', views.add_event.as_view(), name ="add_event"),
	url(r'^event/(?P<hidden_index>\d+)/$', views.event_view.as_view(), name ="event"),
	url(r'^delete_event/(?P<hidden_index>\d+)/$', views.delete_event.as_view(), name ="delete_event"),  #should fix it all
    url(r'^edit_event/(?P<hidden_index>\d+)/$', views.edit_event.as_view(), name ="edit_event"),
    url(r'^add_member/(?P<hidden_index>\d+)/$', views.add_member.as_view(), name ="add_member"),
    url(r'^home/',views.Home_render),
    url(r'^add_user/$',views.add_user.as_view(),name = "add_user"),
    url(r'^register/$', registration.views.RegistrationView.as_view, {'form': RegistrationFormUniqueEmail}, name='registration_register'),
    url(r'^accounts/', include('registration.urls')),

]
