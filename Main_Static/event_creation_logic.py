from Main_Static.models import myuser
from Main_Static.models import arr_el
from django.db import models
import datetime



def get_key(arr_el):
    return arr_el.time

def parse(timestr):
    ry=[]
    timestr.replace('"',':')
    ry=timestr.split(':')
    return int(ry[0])*3600+int(ry[1])*60+int(ry[2])

def find_time(members_string, leng): #В порядке теста сначала вернём имена пользователей
    index_arr=members_string.split("#")
    fin_arr=[]
    for i in index_arr:
        try:
            pk_i = int(i)
        except:
            continue
        current_user = myuser.objects.get(pk=pk_i)#Если передать строку с несуществующими id пользоватлей, на это строке вылетит
        print(current_user.start_work)
        fin_arr.append(arr_el.make_arr_el(current_user.start_work,False))
        #print(temp.start_or_finish)
        fin_arr.append(arr_el.make_arr_el(current_user.finish_work,True))
    count=0
    for i in fin_arr:
        print(i.time,' ', i.start_or_finish)
    fin_arr.sort(key=get_key)
    print (arr_el.objects.all())
    store_start=models.TimeField
    finish=models.TimeField
    result_start=models.TimeField
    result_start="00:00:00"
    members_number= len(fin_arr) / 2 #Криво, косо, переделать
    print (members_number)
    print("oilseed")
    for i in fin_arr:
        if (i.start_or_finish  == False) :
            count+=1
            if (count==members_number) :
                store_start=i.time
        if (i.start_or_finish == True):
            if (count == members_number):
                if (parse(str(i.time)) - parse(str(store_start)))>=parse(str(leng)) :
                    result_start=store_start
                    print(result_start)
            count-=1;
            print( result_start)
    return result_start



    #короче предположим что я разобрался
     #cтраница 110 книжки модификаторы filter
#fin_arr массив, который мы осортируем по времени, в котором элементы содержат следующее : начало это или конец временного отрезка, кому принадлежит отрезок, pyfxtybt dhtv
# for i in fin_arr :
#
#
#На самом деле на этом этапе на плевать кому принадлежит время, так как всё равно нужно чтобы участвовали все
#
#
#
#
#
#
#


