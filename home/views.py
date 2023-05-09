from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
my_list = []
def home(request):
    my_list.clear()
    return render(request, 'home/index.html')


def update_list(request):
    my_list.append(f'{len(my_list)+1}')
    return JsonResponse({'my_list': my_list})
