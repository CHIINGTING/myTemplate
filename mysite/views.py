from django.shortcuts import render

# Create your views here.
from django.utils.datetime_safe import datetime


def index(request):
    msg = 'Hello'
    return render(request, 'index.html', locals())


def yt(request, tvno=0):
    tv_list = [{'name': '公視', 'tvcode': 'JAzRXylm3M0'},
               {'name': '民視', 'tvcode': 'XxJKnDLYZz4'},
               {'name': 'NCC', 'tvcode': 'XWq5kBlakcQ'},
               {'name': '華視', 'tvcode': 'wM0g8EoUZ_E'},
               {'name': 'Java code', 'tvcode': 'videoseries?list=PLTb8yNz82VDW-Ka3DMZUvhf16zZCPFiGe'},
               ]
    tv1 = tv_list[0]
    tv2 = tv_list[1]
    tv3 = tv_list[2]
    tv4 = tv_list[3]
    tv5 = tv_list[4]
    now = datetime.now()
    tvno = tvno
    tv = tv_list[tvno]
    return render(request, 'tv.html', locals())
