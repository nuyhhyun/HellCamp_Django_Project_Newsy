from django.shortcuts import render
import requests
import feedparser


def title(request, category, next_button):
    res = requests.get("http://rss.nocutnews.co.kr/Nocut"+category+".xml")
    print(res)
    res.encoding = 'utf-8'
    n_title = feedparser.parse(res.text)
    infos = []
    for i in n_title.entries:
        infos.append({"title": i.title, "link": i.link, "des": i.description})
    return render(request, 'Newsy_app/'+next_button+'.html', {"infos": infos})


def shared_list(request):
    return render(request, 'Newsy_app/shared_list.html', {})


def get_css(request):
    return render(request, 'Newsy_app/design.css', {})
