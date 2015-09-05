from django.shortcuts import render
from django.template import RequestContext, loader
from django.shortcuts import render_to_response,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.
def index(request):
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('index.html')
    # context = RequestContext(request, {
    #     'latest_question_list': latest_question_list,
    # })
    return HttpResponse(template.render())

def login_user(request):
    from django.contrib.auth import authenticate, login, logout
    logout(request)
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
