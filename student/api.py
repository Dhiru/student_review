from tastypie.resources import ModelResource
from tastypie import fields
from student.models import UserAccount, Attendence, Points, Behaviour

class UserResource(ModelResource):
    class Meta:
        queryset = UserAccount.objects.all()
        resource_name = 'user'


class AttendenceResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        queryset = Attendence.objects.all()
        resource_name = 'attendence'


class PointsResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        queryset = Points.objects.all()
        resource_name = 'points'


class BehaviourResource(ModelResource):
    class Meta:
        queryset = Behaviour.objects.all()
        resource_name = 'behaviour'
