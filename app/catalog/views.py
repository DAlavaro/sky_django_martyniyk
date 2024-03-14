# main/view.py
from django.shortcuts import render


def index(request):
    template = 'catalog/index.html'
    context = {
        'title': 'Skystore',
        'description': 'Skystore - это отличный вариант хранения ваших плагинов и примеров кода, который вы бы хотели продать',
    }
    return render(request, template, context)


def contacts(request, ):
    template = 'catalog/contacts.html'
    if request.method == 'POST':
        data = request.POST.dict()
        print(data)
        msg = data.get('message', '')
        name = data.get('name', '')
        phone = data.get('phone', '')
        flag = 'принято'
    else:
        msg = ''
        name = ''
        phone = ''
        flag = 'не принято'
    context = {'title': 'Контакты',
               'msg': msg,
               'name': name,
               'phone': phone,
               'flag': flag
               }
    return render(request, template, context)