from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
import requests
from bs4 import BeautifulSoup
my_list = []
def home(request):
    my_list.clear()
    return render(request, 'home/index.html')


def update_list(request):
    query = request.GET.get('query')
    page = int(request.GET.get('page'))
    filetypes = ['pdf','docx','ipub','xlsx','csv','ppt']
    url = f'https://google.com/search?q={query}&start={10*page}&num=10'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.find_all('a', href=True)
    my_list= [str(x['href']) for x in links if str(x['href']).endswith('pdf')]
    print(my_list)
    return JsonResponse({'my_list': my_list})
