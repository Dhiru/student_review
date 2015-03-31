from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.base import View
from django.http import HttpResponseRedirect
from student.models import *
import json


class MainView(View):
    def get(self, request):
        return render(request, 'main.html', {})


class GetStudentList(View):
    def get(self, request):
        user_list = []
        users = UserAccount.objects.all()
        user_ids = [user.id for user in users]
        points = Points.objects.filter(user__id__in=user_ids)
        user_points = {each_point.user.id: each_point.points for each_point in points}
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


class SetStudentPoint(View):
    def get(self, request):
        user_list = []
        behaviour_list = []
        users = UserAccount.objects.all()
        for user in users:
            user_dic = dict()
            user_dic['id'] = user.id
            user_dic['name'] = user.name
            user_dic['age'] = user.age
            user_dic['class'] = user.student_class
            user_list.append(user_dic)
        behaviours = Behaviour.objects.all()
        for behaviour in behaviours:
            behaviour_dic = dict()
            behaviour_dic['id'] = behaviour.id
            behaviour_dic['behaviour_name'] = behaviour.behaviour_name
            behaviour_dic['points'] = behaviour.points
            behaviour_list.append(behaviour_dic)
        return render(
            request,
            'add_behaviour.html', 
            {
                'user_list': user_list, 
                'behaviour_list': behaviour_list
            }
        )
        
    def post(self, request):
        student = request.POST.get('student', '')
        behaviour_point = int(request.POST.get('behaviour', ''))
        user = UserAccount.objects.get(id=student)
        try:
            point = Points.objects.get(user__id=user.id)
            point.points = behaviour_point
            point.save()
        except Points.DoesNotExist:
            point = Points()
            point.user = user
            point.points = behaviour_point
            point.save()
        return HttpResponseRedirect('/students/')


class AddStudent(View):
    def get(self, request):
        return render(request, 'add_student.html', {})
    
    def post(self, request):
        name = request.POST.get('name', '')
        age = int(request.POST.get('age', ''))
        student_class =request.POST.get('class', '')
        user = UserAccount()
        user.name = name
        user.age = age
        user.student_class = student_class
        user.save()
        return HttpResponseRedirect('/students/')


class AddBehaviour(View):
    def get(self, request):
        behaviour_list = []
        behaviours = Behaviour.objects.all()
        for behaviour in behaviours:
            behaviour_dic = dict()
            behaviour_dic['id'] = behaviour.id
            behaviour_dic['behaviour_name'] = behaviour.behaviour_name
            behaviour_dic['points'] = behaviour.points
            behaviour_list.append(behaviour_dic)
        return render(request, 'add_new_behaviour.html', {'behaviour_list': behaviour_list})
    
    def post(self, request):
        name = request.POST.get('behaviour_name', '')
        points = int(request.POST.get('points', ''))
        behaviours = Behaviour()
        behaviours.behaviour_name = name
        behaviours.points = points
        behaviours.save()
        return HttpResponseRedirect('/addbehaviour/')
        

    

