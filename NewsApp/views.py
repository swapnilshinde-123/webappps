from django.shortcuts import render
import requests

API_KEY='f0525ffa9d284f0a9189a948008dfc24'

# Create your views here.
"""
This a view to fecth the latest news from NewsAPI based on keyword(q) and 
sorted by 'Published Date' by default.

"""
def home(request):
    q = request.GET.get('q')    
    url=f'https://newsapi.org/v2/everything?q={q}&sortBy=publishedAt&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    articles = data['articles']
  
    context = {
        'articles' : articles
    }

    return render(request, 'NewsApp/home.html', context)