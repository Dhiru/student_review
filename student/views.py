from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.base import View

from student.models import *
import json

class GetStudentList(View):
    def get(self, request):
        user_list = []
        users = UserAccount.objects.all()
        user_ids = [user.id for user in users]
        points = Points.objects.filter(user__id__in=user_ids)
        user_points = {each_point.user.id: each.points for each_point in points}
        user_point_ids = user_points.keys()
        for user in users:
            user_dic = dict()
            user_dic['id'] = user.id
            user_dic['name'] = user.name
            user_dic['age'] = user.age
            user_dic['class'] = user.student_class
            user_dic['points'] = user_points[user.id] if user.id in user_point_ids else ''
            user_list.append(user_dic)
        return render(request, 'student_list.html', {'user_list': json.dumps(user_list)})


class MainView(View):
    def get(self, request):
        return render(request, 'main.html', {})


