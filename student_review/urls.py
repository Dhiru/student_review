from django.conf.urls import patterns, include, url
from tastypie.api import Api
from student.api import UserResource, AttendenceResource, PointsResource, BehaviourResource


v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(AttendenceResource())
v1_api.register(PointsResource())
v1_api.register(BehaviourResource())


urlpatterns = patterns('',
    url(r'^', include('student.urls')),
    url(r'^api/', include(v1_api.urls)),
)
