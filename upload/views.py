from django.shortcuts import render
from django.views.generic import ListView, TemplateView 

from django.http import HttpResponseRedirect
from django.urls import reverse
import logging
import csv

from django.shortcuts import render
from .models import *
# from .forms import UploadFileForm

import pandas as pd
import plotly.express as px
import csv, io
from django.contrib import messages



# class HomeView(ListView):
#     model = Books
#     template_name = 'upload/index.html'
#     context_object_name = 'home_list'


# one parameter named request
def book_upload(request):
    # declaring template
    template = "upload/upload.html"
    data = Books.objects.all()
# prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'Order of the CSV should be title, author, genres',
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
        _, created = Books.objects.update_or_create(
            title=column[0],
            author=column[1],
            genres=column[2],
        )
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
    item = Books.objects.all().values()
    # upload = Upload.objects.all().values()
    df = pd.DataFrame(item)
    mydict = {
        "df": df.to_html()
    }
    # df = pd.read_csv(upload)

    # fig = px.line(df, x = 'AAPL_x', y = 'AAPL_y', title='Apple Share Prices over time (2014)')
    # fig.show()
    return render(request, 'upload/results.html', context=mydict)






# class HomeView(ListView):
#     model = Books
#     template_name = 'upload/index.html'


# def upload_csv(request):
#     data = {}
#     if "GET" == request.method:
#         return render(request, "upload/index.html", data)
# # if not GET, then proceed with processing
#     try:
#         csv_file = request.FILES["csv_file"]
#         if not csv_file.name.endswith('.csv'):
#             messages.error(request,'File is not CSV type')
#             return HttpResponseRedirect(reverse("upload:upload_csv"))
#         #if file is too large, return message
#         if csv_file.multiple_chunks():
#             messages.error(request,"Uploaded file is too big (%.2f MB)." % (csv_file.size/(1000*1000),))
#             return HttpResponseRedirect(reverse("upload:upload_csv"))
#         file_data = csv_file.read().decode("utf-8")          

#         lines = file_data.split("\n")
#         #loop over the lines and save them in db. If error shows up , store as string and then display
#         for line in lines:                                          
#             fields = line.split(",")
#             data_dict = {}
#             data_dict["name"] = fields[0]
#             data_dict["start_date_time"] = fields[1]
#             data_dict["end_date_time"] = fields[2]
#             data_dict["notes"] = fields[3]
#             try:
#                 form = UploadFileForm(data_dict)
#                 if form.is_valid():
#                     form.save()                                  
#                 else:
#                     logging.getLogger("error_logger").error(form.errors.as_json())                                                                                    
#             except Exception as e:
#                 logging.getLogger("error_logger").error(repr(e))                             
#         pass

#     except Exception as e:
#         logging.getLogger("error_logger").error("Unable to upload file. "+repr(e))
#         messages.error(request,"Unable to upload CVS file. "+repr(e))

#     return HttpResponseRedirect(reverse("upload:upload_csv"))

# def chart_data(request):
#     data = []
#     with open("data.csv") as csvfile:
#         csv_reader = csv.reader(csvfile, delimiter=',')
#         for row in csv_reader:
#             data.append(row)

#     return render(request, 'template.html',
#                   {'data': data})