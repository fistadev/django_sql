from django.shortcuts import render
from django.views.generic import ListView, TemplateView 

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
import logging
import csv

from .models import Upload
from .forms import UploadFileForm


class HomeView(ListView):
    model = Upload
    template_name = 'upload/index.html'


def upload_csv(request):
    data = {}
    if "GET" == request.method:
        return render(request, "upload/index.html", data)
# if not GET, then proceed with processing
    try:
        csv_file = request.FILES["csv_file"]
        if not csv_file.name.endswith('.csv'):
            messages.error(request,'File is not CSV type')
            return HttpResponseRedirect(reverse("upload:upload_csv"))
        #if file is too large, return message
        if csv_file.multiple_chunks():
            messages.error(request,"Uploaded file is too big (%.2f MB)." % (csv_file.size/(1000*1000),))
            return HttpResponseRedirect(reverse("upload:upload_csv"))
        file_data = csv_file.read().decode("utf-8")          

        lines = file_data.split("\n")
        #loop over the lines and save them in db. If error shows up , store as string and then display
        for line in lines:                                          
            fields = line.split(",")
            data_dict = {}
            data_dict["name"] = fields[0]
            data_dict["start_date_time"] = fields[1]
            data_dict["end_date_time"] = fields[2]
            data_dict["notes"] = fields[3]
            try:
                form = UploadFileForm(data_dict)
                if form.is_valid():
                    form.save()                                  
                else:
                    logging.getLogger("error_logger").error(form.errors.as_json())                                                                                    
            except Exception as e:
                logging.getLogger("error_logger").error(repr(e))                             
        pass

    except Exception as e:
        logging.getLogger("error_logger").error("Unable to upload file. "+repr(e))
        messages.error(request,"Unable to upload CVS file. "+repr(e))

    return HttpResponseRedirect(reverse("upload:upload_csv"))

# def chart_data(request):
#     data = []
#     with open("data.csv") as csvfile:
#         csv_reader = csv.reader(csvfile, delimiter=',')
#         for row in csv_reader:
#             data.append(row)

#     return render(request, 'template.html',
#                   {'data': data})