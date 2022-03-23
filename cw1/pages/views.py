from django.db.models import Avg, Sum
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password, check_password
from .models import Professor, Module, Rating
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login, logout
import json
from django.contrib.auth.models import User
flag = 0

# Create your views here.
@csrf_exempt
def listAll(request):
    if request.method == 'GET':
        result = []
        list = Module.objects.all()
        for r in list:
            result_data = {}
            result_data['m_code'] = r.m_code
            result_data['m_name'] = r.m_name
            result_data['m_year'] = r.m_year
            result_data['m_semester'] = r.m_semester
            result_data['prof'] = []
            for prof in r.prof_module.all():
                temp = {}
                temp['p_code'] = prof.p_code
                temp['p_name'] = prof.p_Name
                result_data['prof'].append(temp)
            result.append(result_data)
        result = json.dumps(result)
        return HttpResponse(result,content_type='application/json')
    else:
        res = HttpResponse()
        res.content = 'Unsupported method'
        res.status_code = 400
        return res

@csrf_exempt
def ratingAll(request):
    if request.method == 'GET':
        result = []
        Proflist = Professor.objects.all()
        for r in Proflist:
            result_data = {}
            rating = Rating.objects.filter(professor_id=r.id).aggregate(avg=Avg("rating"))
            result_data['p_Name'] = r.p_Name
            result_data['p_code'] = r.p_code
            result_data['rating'] = round(rating['avg'])
            result.append(result_data)
        result = json.dumps(result)
        return HttpResponse(result, content_type='application/json')
    else:
        res = HttpResponse()
        res.content = 'Unsupported method'
        res.status_code = 400
        return res

@csrf_exempt
def averageRating(request,p,m):
    if request.method == 'GET':
        result = []
        try:
            prof = Professor.objects.get(p_code=p)
            module = Module.objects.filter(m_code=m)
            count = 0
            total = 0
            mname = ''
            mcode = ''
            for m in module:
                rating = Rating.objects.filter(professor_id=prof.id,module_id=m.id).aggregate(sum=Sum("rating"))
                if Rating.objects.filter(professor_id=prof.id,module_id=m.id).exists():
                    total += rating['sum']
                    mname = m.m_name
                    mcode = m.m_code
                    count += Rating.objects.filter(professor_id=prof.id,module_id=m.id).count()
            result_data = {}
            result_data['p_Name'] = prof.p_Name
            result_data['p_code'] = prof.p_code
            result_data['m_name'] = mname
            result_data['m_code'] = mcode
            if count == 0:
                return HttpResponse("Invalid object, try another one", content_type='application/json')
            result_data['rating'] = round(total/count)
            result.append(result_data)
            result = json.dumps(result)
        except ObjectDoesNotExist:
            result = "Invalid object, try another one"
        return HttpResponse(result, content_type='application/json')
    else:
        res = HttpResponse()
        res.content = 'Unsupported method'
        res.status_code = 400
        return res

@csrf_exempt
def rate(request, p,m,y,s,r):
    if flag == 0:
        return HttpResponse("Please login", content_type='application/json')
    if request.method == 'POST':
        result = ''
        if float(r) < 1 or float(r) > 5:
            result = 'Rating should between 1-5'
            return HttpResponse(result, content_type='application/json')
        try:
            prof = Professor.objects.get(p_code = p)
            module = Module.objects.get(m_code=m,m_year=y,m_semester=s,prof_module=prof.id)
            try:
                Rating.objects.create(module=module, professor=prof, rating=float(r))
            except Exception:
                result = "Unable to rate"
            result = 'Success!'
        except ObjectDoesNotExist:
            result = "Invalid object, try another one"
        return HttpResponse(result, content_type='application/json')
    else:
        res = HttpResponse()
        res.content = 'Unsupported method'
        res.status_code = 400
        return res

@csrf_exempt
def register(request):
    if request.method == "POST":
        result = ''
        data = json.loads(request.body)
        username =data['username']
        c = User.objects.filter(username=username).count()
        if c > 0:
            return HttpResponse("Username already exists!", content_type='application/json')
        email = data['email']
        if email.find("@") == -1:
            return HttpResponse("Enter valid email address!", content_type='application/json')
        pwd = make_password(data['pwd'])
        try:
            User.objects.create_user(username, email, pwd)
        except Exception:
            result = "Unable to rate"
        result = 'Success!'
        return HttpResponse(result, content_type='application/json')
    else:
        res = HttpResponse()
        res.content = 'Unsupported method'
        res.status_code = 400
        return res

@csrf_exempt
def Login(request):
    global flag
    if request.method == "POST":
        data = json.loads(request.body)
        username = data['username']
        pwd = data['pwd']
        user = authenticate(request,username=username, password=pwd)
        if user is not None:
            login(request,user)
            flag = 1
            return HttpResponse("Success", content_type='application/json')
        else:
            return HttpResponse("Invalid username or password", content_type='application/json')
    else:
        res = HttpResponse()
        res.content = 'Unsupported method'
        res.status_code = 400
        return res

@csrf_exempt
def Logout(request):
    logout(request)
    global flag
    flag = 0
    return HttpResponse("Logged out!", content_type='application/json')
