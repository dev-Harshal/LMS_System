from django.shortcuts import render
from . forms import *
from django.http import HttpResponse
import pandas as pd

# Create your views here.


def index(request):
    if request.method == 'POST':
        form = DatasheetForm(request.POST,request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['file']
            ddf = pd.read_excel(csv_file, engine='openpyxl')
            # data = df.items()
            list_of_dicts = ddf.to_dict(orient='records')
            print(list_of_dicts[0])
            return HttpResponse("done")
        else:
            return HttpResponse("{}".format(form.errors))
            
    else:
        form = DatasheetForm()
        return render(request,'myapp/index.html',context = {'form':form})
