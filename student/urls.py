from django.conf.urls import patterns, url
from student.views import *

urlpatterns = patterns('', 
                       url(r'^$', MainView.as_view(), name='main'),
                       url(r'^students/$', GetStudentList.as_view(), name='get_students'),
                       url(r'^givepoints/$', SetStudentPoint.as_view(), name='set_points'),
                       url(r'^adduser/$', AddStudent.as_view(), name='add_user'), 
                       url(r'^addbehaviour/$', AddBehaviour.as_view(), name='add_behavior'),
)
