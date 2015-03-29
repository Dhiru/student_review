from django.conf.urls import patterns, url
from student.views import *

urlpatterns = patterns('', 
                       url(r'^$', MainView.as_view(), name='main'),
                       url(r'^students/$', GetStudentList.as_view(), name='get_students'),
)
