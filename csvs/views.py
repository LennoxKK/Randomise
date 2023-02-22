from ntpath import join
from django.shortcuts import render
from .forms import CsvModelForm
from .models import Csv
import csv
from django.contrib.auth.models import User
from Sales.models import Sales

# Create your views here.

def upload_files_view(request):
    form=CsvModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form=CsvModelForm()
        obj=Csv.objects.get(activated=False)
        with open(obj.file_name.path,'r') as f:
            reader=csv.reader(f)
            for i, row in enumerate(reader):
                if i==0:
                    pass
                else:
                    row=" ".join(row)
                    row=row.replace(";"," ")
                    row=row.split()
                    product=row[0].upper()
                    user=User.objects.get(username=row[2])
                    print(row)
                    print(user.password)
                    Sales.objects.create(
                        product=product,
                        quantity=int(row[1]),
                        salesman=user
                    )
            obj.activated=True
            obj.save()
    return render(request,'csvs/upload.html',{"form":form})

def learn_javascript(request):
    return render(request,"csvs/learn_javascript.html",{})