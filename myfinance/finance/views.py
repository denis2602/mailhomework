from django.shortcuts import render

from django.http import HttpResponse

def hello_world(request):
    return HttpResponse('<h1>Hello, World!</h1>'
                        '<a href="charges/">Account</a>')

def return_back(request):
    return HttpResponse('<a href="/">Come back</a>'
                        '<p></p>'
                        '<p>Таблица доходов и расходов</p>'
                        '<table>'
                        '   <tr>'
                        '       <th>Доход/расход</th>'
                        '       <th>Сумма</th>'
                        '       <th>Дата сделки</th>'
                        '   </tr>'
                        '   <tr>'
                        '       <th>Доход</th>'
                        '       <th>15 000</th>'
                        '       <th>28.09.2016</th>'
                        '   </tr>'
                        '   <tr>'
                        '       <th>Расход</th>'
                        '       <th>9 000</th>'
                        '       <th>30.09.2016</th>'
                        '   </tr>'
                        '   <tr>'
                        '       <th>Расход</th>'
                        '       <th>2 000</th>'
                        '       <th>08.10.2016</th>'
                        '   </tr>'
                        '   <tr>'
                        '       <th>Доход</th>'
                        '       <th>18 000</th>'
                        '       <th>15.10.2016</th>'
                        '   </tr>')
# Create your views here.
