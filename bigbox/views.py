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
    def get(self, request, box_id=None, slug=None, *args, **kwargs):
        if box_id is not None:
            single_box = Box.objects.get(id=box_id)
            context = {'single_box': single_box, 'active': single_box.activities}
        if slug is not None:
            slug_boxes = Box.objects.filter(slug__icontains=slug)
            context = {'slug_boxes': slug_boxes}

        return render(request, self.template_name, context)

def box_activities(request, box_id):
    box_activity = Box.objects.get(id=box_id)
    activity_list = box_activity.activities.all()
    paginator = Paginator(activity_list, 20)
    page = request.GET.get('page')
    activities = paginator.get_page(page)
    context = {'box_activities': activities}

    return render(request, 'bigbox/activities.html', context)

def single_box_activity(request, box_id, activity_id):
    box = Box.objects.get(id=box_id)
    single_activity = Activity.objects.get(id=activity_id)
    context = {'activity': single_activity}

    return render(request, 'bigbox/activity.html', context)

# def search_by_slug(request):
#     if request.method == 'POST':
#         query= request.POST.get('q')
#         submitbutton = request.POST.get('submit')
#         if query is not None:
#             lookups= Q(slug__icontains=query)
#             results= Box.objects.filter(lookups).distinct()
#             context={'results': results, 'submitbutton': submitbutton}

#             return render(request, 'bigbox/box.html', context)
#         else:
#             return render(request, 'bigbox/box.html')
#     else:
#         return render(request, 'bigbox/box.html')



#     query = request.GET.get('q')
#     slug_boxes = Box.objects.filter(slug__icontains=query)
#     print(slug_boxes)
#     context = {'slugs': slug_boxes}
    
#     return render(request, 'bigbox/box.html', context)

# Crear una url y vista para buscar una box por el campo slug
# i) base_url/box/{slug}/ puede llamar al mismo template / archivo html del
# punto 4.