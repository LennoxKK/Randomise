from re import template
from django.urls import path
from . import views
from Cool.views import ( BibleStudyMemberCreateView, GroupsView,
MemberDetailView,
MemberListView, 
BibleStudyMemberUpdateView,
MemberDeleteView,
CourseView,
CourseListView,
MyList,
events_View,
detail_view_for_each_group, groupings_side_view, revert_bs_leader)
app_name="Cool"
urlpatterns=[

    path("events/",events_View, name="events"),
    path('groups/', GroupsView.as_view(),name="all-groups",),
    path('groups/print', GroupsView.as_view(template_name="Cool/print_view.html"),name="print-view",),
    path("groups/<str:group_name>/",detail_view_for_each_group,name="group-detail-view"),

    #The course class view used for the about view, uses the template defined 
    #within the class
    path('about/', CourseView.as_view(),),
    #path('', MyList.as_view(),),
    #path('', CourseListView.as_view(),),

    #The same course class used for the detail view with anothr template 
   # path("<int:id>/", CourseView.as_view(template_name="the_member_detail.html"),),

    #path('create/', CourseCreateView.as_view(),name="member-create"),
    #path('<int:id>/update/', CourseCreateView.as_view(),name="member-create"),
    path('create/', BibleStudyMemberCreateView.as_view(),name="member-create"),
   # path("<int:my_id>/",dynamic_lookup_view),
   # path("",member_list_view,name="list_view"),
    
    path('', MemberListView.as_view(),name="member-list"),  
    #path("",revert_bs_leader,name="revert-view"),
    path('<int:id>/', MemberDetailView.as_view(),name="member-detail"),
    path('<int:id>/update/', BibleStudyMemberUpdateView.as_view(),name="member-update"),
    path('<int:id>/delete/', MemberDeleteView.as_view(),name="member-delete"),

    #Groupings
    path("groupings",groupings_side_view,name="groupings"),
    path('groupings/groups', GroupsView.as_view(),name="groups-groupings",),
]