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
from plotly.offline import plot
import plotly.graph_objects as go
import csv, io
from django.contrib import messages



# class HomeView(ListView):
#     model = Books
#     template_name = 'upload/index.html'
#     context_object_name = 'home_list'


# one parameter named request
def book_upload(request):
    # declaring template
    template = "upload/graphs.html"
    data = BooksComplete.objects.all()
# prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'Order of the CSV should be title, author, num_rating, num_reviews, avg_rating, num_pages, original_publish_year, award',
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
        _, created = BooksComplete.objects.update_or_create(
            title=column[0],
            author=column[1],
            num_rating=column[2],
            num_reviews=column[3],
            avg_rating=column[4],
            num_pages=column[5],
            original_publish_year=column[6],
            award=column[7],
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
    item = BooksComplete.objects.all().values()
    # upload = Upload.objects.all().values()
    df = pd.DataFrame(item)
    mydict = {
        "df": df.to_html()
    }
    # df = pd.read_csv(upload)

    fig = px.line(df, x = 'original_publish_year', y = 'title', title='Books by Year')
    fig.show()

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


def plot_view(request):
    """ 
    View demonstrating how to display a graph object
    on a web page with Plotly. 
    """
    
    # Generating some data for plots.
    x = [i for i in range(-10, 11)]
    y1 = [3*i for i in x]
    y2 = [i**2 for i in x]
    y3 = [10*abs(i) for i in x]

    # List of graph objects for figure.
    # Each object will contain on series of data.
    graphs = []

    # Adding linear plot of y1 vs. x.
    graphs.append(
        go.Scatter(x=x, y=y1, mode='lines', name='Line y1')
    )

    # Adding scatter plot of y2 vs. x. 
    # Size of markers defined by y2 value.
    graphs.append(
        go.Scatter(x=x, y=y2, mode='markers', opacity=0.8, 
                   marker_size=y2, name='Scatter y2')
    )

    # Adding bar plot of y3 vs x.
    graphs.append(
        go.Bar(x=x, y=y3, name='Bar y3')
    )

    # Setting layout of the figure.
    layout = {
        'title': 'Title of the figure',
        'xaxis_title': 'X',
        'yaxis_title': 'Y',
        'height': 420,
        'width': 560,
    }

    # Getting HTML needed to render the plot.
    plot_div = plot({'data': graphs, 'layout': layout}, 
                    output_type='div')

    return render(request, 'upload/graphs.html', 
                  context={'plot_div': plot_div})