from ntpath import join
from django.shortcuts import render
from .forms import ExcelUploadModelForm
from .models import ExcelUpload
import csv
from django.contrib.auth.models import User
from Cool.models import BStudyMember


# Create your views here.

def upload_excel_view(request):
    form=ExcelUploadModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form=ExcelUploadModelForm()
        obj=ExcelUpload.objects.get(activated=False)
        with open(obj.file_name.path,'r') as f:
            reader=csv.reader(f)
            print(reader)
            for i, row in enumerate(reader):
                print(row[1],"1 ",row[2])
                if i==0:
                    pass
                else:
                    row=" ".join(row)
                    row=row.replace(";"," ")
                    row=row.split()
                    #print(row)
                    #print(user.password)
                    BStudyMember.objects.create(
                         first_name=row[0],
                         middle_name=row[1],
                         sir_name=row[2],
                         level=row[3],
                         gender=row[4],
                         leader_status =row[5],
                         phone_number=row[6]
                    )
            obj.activated=True
            obj.save()
    return render(request,'csvs/upload.html',{"form":form})

def learn_javascript(request):
    return render(request,"csvs/learn_javascript.html",{})