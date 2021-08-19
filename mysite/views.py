from django.shortcuts import render

# Create your views here.
from django.utils.datetime_safe import datetime


# def index(request):
#    msg = 'Hello'
#    return render(request, 'index.html', locals())


def index(request, tvno=0):
    tv_list = [{'name': '公視', 'tvcode': 'JAzRXylm3M0'},
               {'name': '民視', 'tvcode': 'XxJKnDLYZz4'},
               {'name': 'NCC', 'tvcode': 'XWq5kBlakcQ'},
               {'name': '華視', 'tvcode': 'wM0g8EoUZ_E'},
               {'name': 'Java code', 'tvcode': 'videoseries?list=PLTb8yNz82VDW-Ka3DMZUvhf16zZCPFiGe'},
               ]
    now = datetime.now()
    hour = now.timetuple().tm_hour
    tvno = tvno
    tv = tv_list[tvno]
    return render(request, 'tv.html', locals())


def engtv(request, tvno='0'):
    tv_list = [{'name': 'SkyNews', 'tvcode': 'Vnf3QhF4G7s'},
               {'name': 'Euro News', 'tvcode': 'VOw7bts_rGQ'},
               {'name': 'France News', 'tvcode': 'Cbwe0tBSJfM'},
               {'name': 'Al News', 'tvcode': '-upyPouRrB8'},
               ]
    now = datetime.now()
    tvno = tvno
    tv = tv_list[tvno]
    return render(request, 'engtv.html', locals())


def carlist(request, maker=0):
    car_maker = ['SAAB', 'Ford', 'Honda', 'Mazda', 'Nissan', 'Toyota']
    car_list = [[], ['Fiesta', 'Focus', 'Modeo', 'EcoSport', 'Kuga', 'Mustang'],
                ['Fit', 'Odyssey', 'CR-V', 'City', 'NSX'],
                ['Mazda3', 'Mazda5', 'Mazda6', 'CX-3', 'CX-5', 'MX-5'],
                ['Tida', 'March', 'Livina', 'Sentra', 'Teana', 'X-Trail', 'Juke', 'Murano'],
                ['Camry', 'Altis', 'Yaris', '86', 'Prius', 'Vios', 'RAV4', 'Wish']
                ]
    maker = maker
    maker_name = car_maker[maker]
    cars = car_list[maker]
    return render(request, 'carlist.html', locals())


def carprice(request, maker=0):
    car_maker = ['Ford', 'Honda', 'Mazda']
    car_list = [[{'model': 'Fiesta', 'price': 203500, 'qty': 2}, {'model': 'Focus', 'price': 605000, 'qty': 5},
                 {'model': 'Mustang', 'price': 900000, 'qty': 6}],
                [{'model': 'Fit', 'price': 450000, 'qty': 1}, {'model': 'City', 'price': 150000, 'qty': 10},
                 {'model': 'NSX', 'price': 1200000, 'qty': 7}],
                [{'model': 'Mazda3', 'price': 329999, 'qty': 3}, {'model': 'Mazda5', 'price': 603000, 'qty': 11},
                 {'model': 'Mazda6', 'price': 850000, 'qty': 1}],
                ]
    maker = maker
    maker_name = car_maker[maker]
    cars = car_list[maker]
    return render(request, 'carprice.html', locals())
