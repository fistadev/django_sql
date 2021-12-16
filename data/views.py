from django.shortcuts import render
from django.views.generic import ListView, TemplateView 

from django.http import HttpResponseRedirect
from django.urls import reverse
import logging
import csv

from django.shortcuts import render
from .models import BuildingData, MeterData, HalfHourlyData
# from .forms import UploadFileForm

import pandas as pd
import plotly.express as px
from plotly.offline import plot
import plotly.graph_objects as go
import csv, io
from django.contrib import messages



# class HomeView(ListView):
#     # model = Books
#     template_name = 'data/index.html'
#     context_object_name = 'home_list'


# one parameter named request
def data_upload(request):
    # declaring template
    template = "data/index.html"
    data = BuildingData.objects.all()
# prompt is a context variable that can have different values      depending on their context
    prompt = {
        # 'order': 'Order of the CSV should be id, name',
        'profiles': data    
              }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = BuildingData.objects.update_or_create(
            id=column[0],
            name=column[1],
        )
    # for column in csv.reader(io_string, delimiter=',', quotechar="|"):
    #     _, created = MeterData.objects.update_or_create(
    #         building_id=column[0],
    #         id=column[1],
    #         fuel=column[2],
    #         unit=column[3],
    #     )
    # for column in csv.reader(io_string, delimiter=',', quotechar="|"):
    #     _, created = HalfHourlyData.objects.update_or_create(
    #         consumption=column[0],
    #         meter_id=column[1],
    #         reading_date_time=column[2],
    #     )
    context = {}
    return render(request, template, context)





# def home(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('upload-home'))
#     else:
#         form = UploadFileForm()
#     return render(request, 'upload/index.html', {'form': form})


def results(request):
    item = BuildingData.objects.all().values()
    # upload = Upload.objects.all().values()
    df = pd.DataFrame(item)
    mydict = {
        "df": df.to_html()
    }
    # df = pd.read_csv(upload)

    fig = px.line(df, x = 'original_publish_year', y = 'title', title='Books by Year')
    fig.show()

    return render(request, 'upload/results.html', context=mydict)



