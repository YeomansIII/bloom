from django.shortcuts import render
from django.template import RequestContext, loader
from django.shortcuts import render_to_response,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import PlantType, UserPlant, Player, Background
import datetime


# Create your views here.
def index(request):
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('index.html')
    # context = RequestContext(request, {
    #     'latest_question_list': latest_question_list,
    # })
    return HttpResponse(template.render())

@login_required(login_url='/login/')
def play(request, plant_name):
    if request.POST:
        cur_date = datetime.datetime.today().date()
        plant = UserPlant.objects.get(owner__user=request.user, name=plant_name)
        plant.last_press = cur_date
        plant.save()
        td = plant.created_date - plant.last_press
        return HttpResponse('/media/plant_zips/'+plant.type.imagezip.image_base+"/"+str(td.days)+".png")
    plant = UserPlant.objects.get(owner__user=request.user, name=plant_name)
    day_num = (plant.created_date - plant.last_press).days
    my_plants = UserPlant.objects.filter(owner__user=request.user)
    template = loader.get_template('play.html')
    context = RequestContext(request, {
        'day_num' : day_num,
        'plant' : plant,
        'my_plants' : my_plants,
    })
    return HttpResponse(template.render(context))

@login_required(login_url='/login/')
def welcome(request):
    template = loader.get_template('welcome.html')
    return HttpResponse(template.render())

@login_required(login_url='/login/')
def pick_plant(request):
    #player = Player.objects.get(user=request.user)
    print(request.user.username)
    my_plants = UserPlant.objects.filter(owner__user=request.user)
    print(my_plants)
    template = loader.get_template('choose.html')
    context = RequestContext(request, {
        'my_plants': my_plants,
    })
    return HttpResponse(template.render(context))

@login_required(login_url='/login/')
def create_plant(request):
    if request.POST:
        plantType = request.POST['plantType']
        plantType = PlantType.objects.get(name=plantType)
        plantName = request.POST['plantName']
        background = request.POST['background']
        background = Background.objects.get(background_name=background)
        player = Player.objects.get(user=request.user)
        new_plant = UserPlant.objects.create(name=plantName, type=plantType, owner=player, background=background)
        new_plant.save()
        return HttpResponse("/play/myplant/"+new_plant.name)
    plant_types = PlantType.objects.all()
    backgrounds = Background.objects.all()
    template = loader.get_template('create.html')
    context = RequestContext(request, {
        'plant_types': plant_types,
        'backgrounds' : backgrounds,
    })
    return HttpResponse(template.render(context))

@login_required(login_url='/login/')
def customize_plant(request, plant_name):
    if request.POST:
        plant = UserPlant.objects.get(name=plant_name, owner__user=request.user)
        if 'background' in request.POST:
            background = Background.objects.get(background_name=request.POST['background'])
            plant.background = background
        if 'plantName' in request.POST:
            plant.name = request.POST['plantName']
        plant.save()
        return HttpResponse("/play/myplant/"+plant.name)
    backgrounds = Background.objects.all()
    plant = UserPlant.objects.get(name=plant_name, owner__user=request.user)
    template = loader.get_template('customize.html')
    context = RequestContext(request, {
        'backgrounds' : backgrounds,
        'plant' : plant
    })
    return HttpResponse(template.render(context))

def logout_user(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect('/')

def login_user(request):
    if request.user.is_authenticated():
        return redirect('/play/')
    from django.contrib.auth import authenticate, login
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/play/')
    return render_to_response('login.html', context_instance=RequestContext(request))

def create_user(request):
    if request.user.is_authenticated():
        return redirect('/play/')
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        #password2 = request.POST['password2']

        user = User.objects.filter(username=username)
        if user.count() != 0:
            return HttpResponse("That username is already taken")
        else:
            user = User.objects.create(username=username)
            user.set_password(password)
            user.save()
            if user:
                return redirect('/login/')
    return render_to_response('signup.html', context_instance=RequestContext(request))


@login_required(login_url='/login/')
def friends(request):
    template = loader.get_template('friends.html')
    return HttpResponse(template.render())