from django.urls import path
from  .views import upload_files_view,learn_javascript

app_name="csvs"
urlpatterns = [
    path("",upload_files_view,name='uploads'),
    path("java/",learn_javascript,name='java')

    
]
