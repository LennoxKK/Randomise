from cgitb import lookup
from functools import wraps
import math
import sys
from itertools import permutations
import random
from operator import ge
from pickletools import int4
from secrets import choice
from tokenize import group
from types import new_class
from unittest import result
from urllib import request, response
from django.db import IntegrityError
from django.shortcuts import get_object_or_404, render,get_list_or_404
from django.http import HttpResponse,Http404
from typing import Counter

from django.urls import is_valid_path,reverse

from Cool.data import Events
from .models import Article, BStudyMember, Groups_BackUp,The_member
from .forms import BibleStudyMemberRegisterForm, InputForm,MemberForm,Bible_SleaderForm
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
    View
    )
TemplateView.as_view(extra_context={
    "name":"Good Luck"
})



def capture_error(f):
    def  wrapper(*args, **kwargs):
        try:
            return f(*args,**kwargs)
        except:
            return HttpResponse(print("Oops!", sys.exc_info()[0], "occurred."))
    return wrapper

@capture_error
def events_View(request):
         if request.method == "POST":
             Events.__setitem__ (Events["latest"]+1,{
            "date":request.POST['date'],
            "time":request.POST["time"]
              })
             Events['latest']+=1
             context={
                'events':Events
              }
             print(Events)
             return render(request,"Cool/events.html",context)
         return render(request,"Cool/events.html")
 














#generate numbers
def name_generator():
    # The six names to combine
    names=["Markos","Wycliff","Lennox","Geoffrey","Gregory","Mark","James","Ochieng","Kizito","Ziro","Amrose","Beja","Anderson","Michael","Ryan","Budi","Jakes","Amos","Nyale","Raphael","Benson","Janji","Gongolo","Kahati","Kanyoe"]
    rand=random.randint(0,2000)
    full_name=list(permutations(names,3))[rand]
    full_name=(" ".join(full_name))
    return full_name

#generate phone_number
def phone_gen():
    phone=[0,1,2,3,4,5,6,7,8,9]
    rand=random.randint(0,2000)
    phone=list(permutations(phone,8))[rand]
    phone=[str(i) for i in phone]
    phone="".join(phone)
    return phone
def data():
    queryset=BStudyMember.objects.all()
    #if already migrated then dont
    bs_query=BStudyMember.objects.all()
    unlock = 0
    s=0
    Total_members={}
    print(queryset)
    for i in queryset:
        print(i.phone_number)
        full_name=name_generator().split(" ")
        Total_members.__setitem__(str(s),{'year':i.level,'gender':i.gender,'bs_leader':i.leader_status,'id':s,"name":i.first_name +"  "+i.middle_name+"  "+i.sir_name,"sir_name":i.sir_name,'phone':i.phone_number})
        # if len(bs_query)==0 and unlock==1  :

        #      BStudyMember.objects.create(
        #          first_name=full_name[2],
        #          middle_name=full_name[0],
        #          sir_name=full_name[1],
        #          level=i.year_of_study,
        #          gender=i.gender,
        #          leader_status =i.leader_status,
        #          phone_number="07"+str(phone_gen())
        #        )
        s+=1
    return Total_members


Total_members=data()
members_per_group=int(10)
total_groups=math.ceil(len(data())/members_per_group)


#create the groups.
groups={}
for i in range(total_groups):
    groups.__setitem__('group'+str(i),{})



#get the least presented class
def least_class(group,remains):
    group=Counter(group)
    classes=[]
    available=Counter({})
    for item in group:
        classes.append(group[item]['year'])
    for j in [1,2,3,4,5]:
        if j in classes:
            continue
        classes.append(j)
    ratios=Counter(classes).most_common()
    for instance in remains:
            available.__setitem__(remains[instance]['year'],instance)
    i=len(ratios)-1
    #check if there is a class missing
   # print("ratios",ratios)
    smallest_class=[]
    while(i>0):
        if ratios[i][0] in available:
            smallest_class.append(ratios[i][0])
            smallest_class.append(available[ratios[i][0]])
            break
        i-=1

    return smallest_class

    #The logic for the grouping
#groups['default']={1:{"gender":"F",'year':3},2:{"gender":"M",'year':1},3:{"gender":"F",'year':2},4:{"gender":"F",'year':5}}
next_gender=None
Total_members_list=[x for x in Total_members]
pending_items=None
#print(Total_members)
class_ratio=[]
gender_ratio=[]
def check_gender_balance(g,h):
    g=Counter(g)
    h=Counter(h)
    m=f=False
    if h['gender']=='M':
        m=True
    else:
        f=True
    m_c=f_c=0
    for i in g:
        if g[i]['gender']=='M':
            m_c+=1
        else:
            f_c+=1
    if m==True and (m_c-f_c)<=0:
        return True
    elif f==True and (f_c-m_c)<=0:
        return True
    return False
for i in groups:
    each_group=groups[i]
    if len(each_group)==0:
        for item in Total_members:
            if item in Total_members_list:
                 each_group.__setitem__(int(item),Total_members[(item)])
                 Total_members_list.remove(item)
                 break
       
    for member_id in Total_members:
        #Strike gender balance
        next_gender=Counter(([each_group[item]['gender'] for item in each_group])).most_common()
        gender_ratio=next_gender
        #check the most dominant gender
        if len(next_gender)==2:
             if next_gender[0][1] - next_gender[1][1] <= 1:
                 next_gender=next_gender[1][0]
             else:
                 next_gender=next_gender[0][1]
        else:
            if next_gender=="M":
                next_gender="F"
            else:
                next_gender='M'
       #Strike class or year balance i.e  each year to be well distributed
       #get the maximum number of members in a group per class
        max_per_class=-(-members_per_group//5)
     #   print(max_per_class)
        next_class=Counter(([each_group[item]['year'] for item in each_group])).most_common()
        class_ratio=next_class
        class_size=sum([size_of_each_tuple[1] for size_of_each_tuple in next_class])
       # print(class_size)
       # print(next_class)
       # print("member_id",member_id)
       #print(Total_members[member_id]['gender'] )
       #print(next_class[0][1])
        if  member_id  in Total_members_list and class_size<members_per_group and check_gender_balance(each_group,Total_members[member_id]) and next_class[-1][1]<max_per_class:
           each_group.__setitem__(member_id,Total_members[member_id])
           Total_members_list.remove(member_id)
           #print("Hello")



#print(Total_members_list)
#get the remains
remains={}
for key in Total_members_list:
    remains.__setitem__(key,Total_members[key])

#add back all the remainders to the groups
Total_members_list=[x for x in remains]
item=None
try:
   
    for group in groups:
         each_group=groups[group]
         gender=Counter([remains[x]['gender'] for x in remains]).most_common() # M =2, F=7
         while(len(each_group)<members_per_group and len(least_class(each_group,remains))==2): # M =2, F=7
             item=least_class(each_group,remains)[1]
             each_group.__setitem__(item,remains[item])
             remains.__delitem__(item)
except IndexError:
    def er404():
        return Http404("Error occured !")
    er404()
track=len(remains)
for each_group in groups: #group 23 len =5
    each_group=groups[each_group]
    for member in remains:# remains 1
        if (len(each_group)<members_per_group and track>0): # track 11
            if remains[member]:#member
                each_group.__setitem__(member,remains[member])
                remains[member]={}
                track-=1
            



   # continue
    



#for i in groups :
#    each_group=groups[i]
#    next_class=Counter(([each_group[item]['year'] for item in each_group])).most_common()
#    next_gender=Counter(([each_group[item]['gender'] for item in each_group])).most_common()
#    print(i,len(groups[i]),[next_class,next_gender])   
#    for j in groups[i]:
#        print("                ",groups[i][j])

all_data=[]
for i in groups:
    track=0
    class_ratio=[]
    ratio_gender=[]
    intersted_bs_leaders=0
    for j in groups[i]:
        mydict=groups[i][j]
        mydict['group_name']=i
        ratio_gender.append(mydict['gender'])
        class_ratio.append(mydict['year'])
        if mydict['bs_leader'] == True:
            intersted_bs_leaders+=1
        if track==len(groups[i])-1:
            mydict['gender_ratio']=Counter(ratio_gender).most_common()
            mydict['class_ratio']=Counter(class_ratio).most_common()
            mydict['int_leaders']=intersted_bs_leaders
            #get data from back ups
            back_up = Groups_BackUp.objects.all()
            if groups[i] in back_up:
                 mydict['backed_up']=99
        all_data.append(mydict)
        
        track+=1


"""
#get the least gender
def gender_ratio(group):
    group=Counter(group)
    classes=[]
    for item in group:
        classes.append(group[item]['gender'])
    ratio=Counter(classes).most_common()
    return ratio

def check_gender_balance(g,h):
    g=Counter(g)
    h=Counter(h)
    m=f=False
    if h['gender']=='M':
        m=True
    else:
        f=True
    m_c=f_c=0
    for i in g:
        if g[i]['gender']=='M':
            m_c+=1
        else:
            f_c+=1
    if m==True and (m_c-f_c)<=0:
        return True
    elif f==True and (f_c-m_c)<=0:
        return True
    return False

b=[]

def exists(b,k):
    for i in b:
        if k==(i):
            return 1
    return 0

def my_Groups(Total_members,groups,y,b):
   for i in d:
       g=d[i]
       for j in data():
            m=data()[j]
            if len(g)<y-1 and check_gender_balance(g,m):
                max_pop = -(-y//4)
               # print(max_pop)
                group_pop=0
                for x in g:
                    if g[x]['year']==m['year']:
                        group_pop+=1
                if group_pop==0 and j :
                    g.__setitem__(j,m)
                    b.append(j)
                if group_pop<=max_pop and j not in b:
                    g.__setitem__(j,m)
                    b.append(j)
my_Groups(data(),d,y,b)

#- [('F', 11), ('M', 6)] :: class_ratio -- [(2, 7), (3, 6), (1, 3), (4, 1)] :
#Add bs leaders


#Fill those groups with less members
#Merge small groups

re={}
for i in range(len(d)):
    if len(d["group"+str(i)])<=(-(-y//2)):
        re.update(d["group"+str(i)])
        d.__delitem__("group"+str(i))
d.__setitem__("merged",re)

#Get the remaining groups which haven't been grouped yet.
remains={}
for i in data():
    if exists(b,i)==1:
        continue
    remains.__setitem__(i,data()[i])

#return the remains back to the groups


for group in d:
    #print(groups,len(d[groups]))
    group_size=len(d[group])  #merged 
    #print(group)
    while(group_size<y): #group size =4

        #get the smallest available class size
        year=least_class(d[group],remains)[0]
        #get the smallest available gender size
        gender=gender_ratio(remains)
        if len(gender)==2 and gender[0][1] >= gender[1][1]:
            gender=gender[1][0]
        else:
            gender=gender[0][0]
        item=least_class(d[group],remains)[1]
        d[group][group_size]=remains[item]
        remains.__delitem__(item)
        group_size+=1



#Take the data into a list
#get the gender and class ratios

all_data=[]
for i in d:
    track=0
    class_ratio=[]
    ratio_gender=[]
    for j in d[i]:
        mydict=d[i][j]
        mydict['group_name']=i
        ratio_gender.append(mydict['gender'])
        class_ratio.append(mydict['year'])

        if track==len(d[i])-1:
            mydict['gender_ratio']=Counter(ratio_gender).most_common()
            mydict['class_ratio']=Counter(class_ratio).most_common()
        all_data.append(mydict)
        track+=1


d.update(remains)
class_ratio=[]
ratio_gender=[]
all_data.append({"remains":remains})
"""
##for i in remains:
##    mydict=remains[i]
##    mydict['group_name']="remains"
##    ratio_gender.append(mydict['gender'])
##    class_ratio.append(mydict['year'])
##    if track==len(remains)-1:
##        mydict['gender_ratio']=Counter(ratio_gender).most_common()      
##        mydict['class_ratio']=Counter(class_ratio).most_common()
##    all_data.append(mydict)

#Add the remains back to the groups
#Disclaimer this code works best with a maximum of about ten members per group

#View for all the groups 

class ObjectMixin(object):
    model=The_member
    lookup='id'
    def get_object(self):
        id=self.kwargs.get(self.lookup)
        obj=None
        if id  is not None:
            obj=get_object_or_404(self.model,id=id)
        return obj
class GroupsView(ListView):
    model=Article
    data()
    template_name='Cool/bible_study_list.html'
    def post(self,request,*args,id=None, **kwargs):
        if 'group-name' in request.POST:
             group_name=request.POST['group-name'] # group7
             back_up = Groups_BackUp.objects.all() # bs members' ids
             proceed = 0
             for i in back_up:
              #  print(str(i.name),group_name)
                if str(i.name) == group_name:
                    proceed = 1
                    break
             
            # if Groups_BackUp.objects.get(name=group_name):
             
             if proceed == 1:
                backup_data=get_object_or_404(Groups_BackUp,name=group_name)# Get the object
                prev_data=(backup_data.info.split(',')[1:-1]) # remove the '[]'
                for i in prev_data:# id2,id2,id3
                     i=int(i)
                     print(i)
                     member=get_object_or_404(BStudyMember,id=i+250)#id1
                     member.leader_status=True
                   #  print(member.sir_name,member.first_name, member.mi)
                     member.save()
        if 'bs-leader' in request.POST:
             choice = request.POST['bs-leader']
             if choice:
                  group_name=choice.split('-')[0]
                  id=int(choice.split('-')[1])
             group_members=groups[group_name]
             backup_data=[]
             for member in group_members:
                 member=group_members[member]
                 if member['id'] == id:
                     #print("Hello",id)
                     continue
                 bs_member=BStudyMember.objects.get(id=int(member['id'])+250)
                 if(bs_member.leader_status==True):
                     backup_data.append(bs_member.id)
                     bs_member.leader_status = False
                     bs_member.save()
                     print(bs_member.leader_status)
        #create backup

             Groups_BackUp.objects.create(name=group_name,info=backup_data)
                # form.leader_status=False
        context={
            "groups":all_data,
            "input":InputForm(),
         }
        return render(request ,self.template_name,context)

    def get_context_data(self,**kwargs):
     group_size=None
     #Call the base implementation first to get a context
     context=super().get_context_data(**kwargs)
     #Add another queryset
     context={
        "groups":all_data,
        "input":InputForm(),
        'group_size':group_size,
     }
     return context
#Revert the bible study leader choice
def revert_bs_leader():
    if request.method == "POST":
        group_name=request.POST['group-name']
        backup_data=get_list_or_404(Groups_BackUp,name=group_name)
        prev_data=backup_data.info
        for data in prev_data:
            member=get_object_or_404(BStudyMember,id=data)
            member.leader_status=True
        return reverse('Cool:all-groups')
          #  member.save()
    
    
#Detail view for particular groups
def detail_view_for_each_group(request,group_name):
   
    form=None
    full=False
    leader=None
    fields=Bible_SleaderForm(request.POST or None)
  #  print(fields,request.POST)

    try:
        request.POST.__init__(mutable=True)
        if request.method=="POST":
             choice_leader=request.POST['leader']
             #print(choice_leader)
             leader=The_member.objects.get(id=int(choice_leader)+159)
             group_members=groups[group_name]
             for each in group_members:
                each_group=group_members[each]
                if each_group['bs_leader']==True and int(choice_leader) != int(choice_leader):
                    form=The_member.objects.get(id=int(each)+159)
                    form.leader_status=False
                    form.save()
                   # print(each_group['bs_leader'])
                   # print(form.leader_status)
             full=True
        group_members=groups[group_name]
    except(KeyError,TypeError):
        raise Http404("No group_name matches your search")
    return render(request,
    "Cool/group_detail.html",
    {"group_members":group_members,
    "group_name":group_name,
    "form":form,
    "full":full,
    "leader":leader,
    "fields":fields})

class BibleStudyMemberCreateView(CreateView):
    model=BStudyMember
    template_name="Cool/bs_member_create.html"
    form_class=BibleStudyMemberRegisterForm
    success_url='/Cool'
    def form_valid(self,form):
        try :   
             return super().form_valid(form)
        except IntegrityError as e:
             return HttpResponse('Oops!',e,"error!")

 
class MemberListView(ListView):
    template_name="Cool/the_member_list.html"
    context_object_name="list"
    queryset=BStudyMember.objects.all()


class MemberDetailView(DetailView):
    template_name="Cool/the_member_detail.html"
   # queryset=The_member.objects.all()

    def get_object(self):
        id=self.kwargs.get("id")
        return get_object_or_404(BStudyMember,id=id)


class BibleStudyMemberUpdateView(UpdateView):
    template_name="Cool/bs_member_create.html"
    form_class=BibleStudyMemberRegisterForm
    #queryset=BStudyMember.objects.all()
   # success_url='/'
    def get_object(self):
        id=self.kwargs.get("id")
        return get_object_or_404(BStudyMember,id=id)

    def form_valid(self,form):
        return super().form_valid(form)
    
class MemberDeleteView(DeleteView):
    template_name="Cool/the_member_delete.html"
   # queryset=The_member.objects.all()

    def get_object(self):
        id=self.kwargs.get("id")
        return get_object_or_404(The_member,id=id)

    def get_success_url(self):
        return reverse("The_member:member-list")
    


# Inherited functions into classes
#Using the same class for different functions
# That is for the about view and detail view


class CourseView(View):
    template_name="Cool/about.html"
    def get(self,request,*args,id=None, **kwargs):
        context={
            "default":"Hello"
        }
        if id is not None:
            obj=get_object_or_404(The_member,id=id)
            context['object']=obj  
            print(obj)
        return render(request,self.template_name,context)


class CourseObjectMixin(object):
    model=The_member
    lookup='id'
    def get_object(self):
        id=self.kwargs.get(self.lookup)
        obj=None
        if id  is not None:
            obj=get_object_or_404(self.model,id=id)
        return obj
#class CourseCreateView(CourseObjectMixin,View):
#    template_name="Cool/bs_member_create.html"
#    print("get")
#    def get(self,request,*args,id=None, **kwargs):
#        #GET METHOD
#        obj=self.get_object()
#        form=BibleStudyMemberRegisterForm(instance=obj)
#        context={"form":form}
#        return render(request,self.template_name,context)
#    def post(self,request,*args,id=None, **kwargs):
#        #POST METHOD
#        print("post")
#        obj=self.get_object()
#        form=BibleStudyMemberRegisterForm(request.POST,instance=obj)
#        context={"form":form}
#        if form.is_valid():
#            form.save()
#            BibleStudyMemberRegisterForm()
  #      return render(request ,self.template_name,context)
 #   def get_success_url(self):
 #       return reverse("Cool:member-detail")
    

class CourseListView(View):
    template_name="Cool/the_member_list.html"
    queryset=BStudyMember.objects.all()
    def get_queryset(self):
        return self.queryset
    
    def get(self,request,*args,**kwargs):
        context={"object_list":self.get_queryset()}
        return render(request,self.template_name,context)
    
# Class inheritance
class MyList(CourseListView):
    queryset= The_member.objects.filter(id=300)


#Grouping Side View
def groupings_side_view(request):
    request.POST.__init__(mutable=True)
    if request.method == "POST":
         #  print(request.POST)
         pass
    return render(request,"Cool/grouping-side.html")

#group leader

 


