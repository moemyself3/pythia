from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from .models import ObsQueue, SurveyField

def index(request):
    return render(request, "index.html")

def observed(request, pk):
    queue_item = ObsQueue.objects.get(pk=pk)
    print(queue_item.survey_field_id)
    survey_field = SurveyField.objects.get(pk=queue_item.survey_field_id)

    # Remove queue item from list
    queue_item.delete()

    # Add 1 to observation in survey fields table
    survey_field.observations = survey_field.observations + 1
    survey_field.save()

    return render(request, "dashboard/fragments/obsqueuetable.html")

def ObsQueueView(request):
    object_list = ObsQueue.objects.all()
    context = {'object_list': object_list}

    if "HX-Request" in request.headers:
        return render(request, "dashboard/fragments/obsqueuetable.html", context)

    return render(request, "dashboard/obsqueue.html", context)

def SurveyFieldsView(request):
    object_list = SurveyField.objects.all().order_by("survey_field_id")
    paginator = Paginator(object_list, 15)
    page_number = request.GET.get("page")
    if not page_number:
        page_number = 1
    page_obj = paginator.page(page_number)
    page_nav_list = paginator.get_elided_page_range(page_number, on_each_side=1, on_ends=1)
    context = {'page_obj': page_obj, 'page_nav_list': page_nav_list}
    return render(request, "dashboard/surveyfields.html", context)
