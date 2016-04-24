from django.db import models
from django.contrib.auth.models import User
#from Main_Static.event_creation_logic import find_time
class myuser(models.Model):
    user = models.ForeignKey(User)
    start_work = models.TimeField()
    finish_work = models.TimeField()
    birth = models.DateField()
 #   test = models.DateField()
  #  free_segments=[]
   # particip_events=models.CharField(max_length=1000)  #Dangerous const

class arr_el(models.Model):
    time=models.TimeField()
    start_or_finish = models.BooleanField() #start false
    def make_arr_el(time ,start_or_finish):
        elem=arr_el()
        elem.time=time
        elem.start_or_finish=start_or_finish
        elem.save()
        return elem



class event(models.Model):
    start_time = models.TimeField()
    finish_time = models.TimeField()
    length = models.TimeField()
    hidden_index = models.AutoField(primary_key = True)
    name=models.CharField(max_length=127)
    is_impossible=models.CharField(max_length=127)
    members=models.CharField(max_length=1000) #Dangerous const
    class Meta:
      verbose_name = "Event_description"



# name = models.CharField(255)

