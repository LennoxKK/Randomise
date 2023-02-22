from django.urls import path
from  .views import upload_excel_view,learn_javascript

app_name="excel-uploads"
urlpatterns = [
    path("groupingse/upload",upload_excel_view,name='exceluploads'),
    path("java/",learn_javascript,name='java')

    
]
