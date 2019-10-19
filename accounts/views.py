from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect, render_to_response
from django.views.generic import DetailView, TemplateView
from accounts.models import MCQ, UserProfile
import random
import datetime
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout
from django.http import JsonResponse
from django.template import RequestContext
from django.db import IntegrityError


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email_1 = request.POST['email_1']
        email_2 = request.POST['email_2']
        email_3 = request.POST['email_3']
        name_1 = request.POST['name_1']
        name_2 = request.POST['name_2']
        name_3 = request.POST['name_3']
        number_1 = request.POST['number_1']
        number_2 = request.POST['number_2']
        number_3 = request.POST['number_3']

        # for validation of the user

        def validate():
            if username and password and email_1 and name_1 and number_1:
                pass
            else:
                return 1

            if User.objects.filter(username=username).exists():
                return 2

        if validate() == 1:
            return render_to_response('Login.html', {"error": "Some fields are empty !!!"})
        try:
            user = User.objects.create(username=username, password=password)
            user.set_password(password)
            user.save()
        except IntegrityError as e:
            return render(request, 'Login.html', {'error': 'Username already exists!'})
        prof = UserProfile()
        prof.user = user
        prof.name_1 = name_1
        prof.name_2 = name_2
        prof.name_3 = name_3
        prof.email_1 = email_1
        prof.email_2 = email_2
        prof.email_3 = email_3
        prof.number_1 = number_1
        prof.number_2 = number_2
        prof.number_3 = number_3
        try:
            prof.save()
        except IntegrityError as e:
            return render(request, 'Login.html', {'error': 'Username already exists'})
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            u = request.user
            data = UserProfile.objects.get(user=u)
            time = datetime.datetime.now() + datetime.timedelta(seconds=1800)
            time_sec = (time.hour*60*60) + \
                (time.minute*60)+(time.second)
            data.timer = time_sec
            ls = range(1, 101)
            sel_q = random.sample(ls, 30)
            sel_q_str = ','.join([str(a) for a in sel_q])
            print(sel_q_str)
            data.sel_ques = sel_q_str
            data.save()
        return display(request)
    else:
        return render(request, 'Login.html')


def rules(request):
    return render(request, 'rules.html')


def display(request):
    if request.method == 'POST':
        currentuser = request.user
        data = UserProfile.objects.get(user=currentuser)
        ls = data.sel_ques.split(',')
        print(ls)
        if ls[0] == '':
            return loggedout(request)
        m = random.choice(ls)
        ls.remove(m)
        new_str = ','.join(ls)
        data.sel_ques = new_str
        data.ansq = data.ansq+','+str(m)
        print(data.ansq)
        data.save()
        show = MCQ.objects.get(id=int(m))
        now = datetime.datetime.now()
        now_sec = (now.hour*60*60)+(now.minute*60)+(now.second)
        t = data.timer-now_sec
        value = {'v': show, 'u': data, 't': int(t)}
        return render(request, 'MCQ.html', value)

    else:
        return render(request, 'MCQ.html', {})


def anscheck(request):
    if request.method == 'POST':
        currentuser = request.user
        data = UserProfile.objects.get(user=currentuser)
        ls = data.ansq.split(',')
        m = int(ls[-1])
        show = MCQ.objects.get(id=m)
        n = 0
        if request.POST.get('select'):
            n = request.POST.get('select')
        if show.answer == int(n):
            data.score += 1
            n = 0
            data.save()
            return display(request)
        else:
            n = 0
            return display(request)


def loggedout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('register')


def about_us(request):
    return render(request, 'abtus.html')
