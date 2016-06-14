from django.shortcuts import render, get_object_or_404
from Main_Static.models import event
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy
from Main_Static.models import myuser
from Main_Static import event_creation_logic
from django.shortcuts import redirect
from django.contrib.messages import constants as messages
from django.core import urlresolvers
MESSAGE_TAGS = {
    messages.INFO: '',
    50: 'critical',
}
from django.contrib import messages

def Home_render(request):
    name = ("a", "b", "c", "l");
    return render(request, "Home.html", {})

class add_user(CreateView):
    model=myuser
    template_name = "add_user.html"
    success_url = reverse_lazy("event_list")
    fields = ["user","start_work","finish_work","birth"]

def list_all_users(request):
    my_users = myuser.objects.all()
    return render(request, "MembersList.html", {"users": my_users})


def user_detail(request, uid):
    print(uid)
    user = get_object_or_404(myuser, pk=uid)
    return render(request, "User.html", {"user": user})


def MeetingsCalendar_render(request):
    return render(request, "events.html", {})


# © https://bitbucket.org/EkaterinaChichvarina/kat0d-mentor-repo/src/ff50b68ee5d4/ControllersIO/?at=master
class event_list(ListView):
    template_name = "event_list.html"
    model = event
    queryset = event.objects.order_by(("pk")).reverse()
    paginate_by = 20  # how many objects on each page we want
    paginate_orphans = 2  # how many objects we can leave on the last page
    context_object_name = "event_list"  # context variable with objects list to read it in template
    page_kwarg = "page"  # name of argument that will be used for pages travers


class event_view(DetailView):
    template_name = "events.html"
    model = event
    pk_url_kwarg = "hidden_index"


class add_event(CreateView):
    model = event
    template_name = "add_event.html"
    success_url = reverse_lazy("event_list")  # or you can use address, for example: success_url = "/user_list/"
    fields = ["name", "members","length","date"]  # order of fields on adding page. Can use ExtUser or User field
    def post(self,request, *args, **kwargs):
        temp=event()
        temp.name=request.POST["name"]
        temp.members=request.POST["members"]
        temp.length=request.POST["length"]
        temp.date=request.POST["date"]
        temp.start_time,temp.finish_time = event_creation_logic.find_time(temp.members,temp.length)
        #temp.finish_time=temp.start_time;
        if (temp.start_time=="00:00:00"):
            temp.is_impossible="Sorry, but your meeting is impossible to plan"
            return render(request, "add_event.html")#страничка редиректа если не удалось сохдать встречу
        else:
           temp.is_impossible=""
           temp.save()
        return render(request, "event_list.html")

class delete_event(DeleteView):
    template_name = "delete_event.html"
    model = event
    pk_url_kwarg = "hidden_index"
    success_url = reverse_lazy("event_list")  # or "/user_list/"


class edit_event(UpdateView):
    model = event
    pk_url_kwarg = "hidden_index"
    fields = ["start_time", "finish_time", "name","date"]
    template_name = "edit_event.html"
    success_url = reverse_lazy("event_list")  # or "/user_list/"


class add_member(UpdateView):
    model = event
    pk_url_kwarg = "hidden_index"
    fields = ["members"]
    template_name = "add_member.html"
    success_url = reverse_lazy("event_list")  # or "/user_list/"
    #event_creation_logic.find_time("1#2#3")

# class test_logic(event)#Page 201+
