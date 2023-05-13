from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
import requests
from bs4 import BeautifulSoup
def home(request):
    return render(request, './index.html')


def get_urls(request):
    query = request.GET.get('query')
    page = int(request.GET.get('page'))
    url = f"https://www.google.com/search?q=filetype:pdf {query}&start={10*page}"
    # print(page)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.find_all('a', href=True)
    # print([str(x['href']) for x in links if str(x['href']).endswith('pdf')])
    data= {str(x.find_next('h3').text):str(x['href']) for x in links if str(x['href']).endswith('pdf')}
    # print(data)
    return JsonResponse({'data': data})
