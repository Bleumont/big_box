from django.db.models import query
from django.db.models.fields import SlugField
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Box, Activity
from django.views import View


def all_boxes(request):
    boxes = Box.objects.all()
    context = {'boxes': boxes}
    
    return render(request, 'bigbox/boxes.html', context)


class BoxView(View):
    template_name = 'bigbox/box.html'
    def get(self, request, box_id=None, *args, **kwargs):
        if box_id is not None:
            single_box = Box.objects.get(id=box_id)
            context = {'single_box': single_box, 'active': single_box.activities}

        return render(request, self.template_name, context)


class SlugSearch(View):
    def get(self, request, slug=None):
        if slug is not None:
            slug_boxes = Box.objects.filter(slug__icontains=slug)
            if slug_boxes is None:
                return render('No hay coincidencias.')
            else:
                context = {'slug_boxes': slug_boxes}
            
        return render(request, 'bigbox/box.html', context)

    
def box_activities(request, box_id):
    box_activity = Box.objects.get(id=box_id)
    activity_list = box_activity.activities.all()
    paginator = Paginator(activity_list, 20)
    page = request.GET.get('page')
    activities = paginator.get_page(page)
    context = {'box_activities': activities, 'box': box_activity}

    return render(request, 'bigbox/activities.html', context)


def single_box_activity(request, box_id, activity_id):
    single_activity = Activity.objects.filter(id=activity_id, box=box_id)
    context = {'activity': single_activity}

    return render(request, 'bigbox/activity.html', context)
