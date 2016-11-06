from django.shortcuts import render
from Charge_new.forms import ChargesForm
from django.http import HttpResponse
from Charge_new.generate import random_transactions


# данные от пользователя
def user(request):
    if request.method == 'POST':
        value = ChargesForm(request.POST)
        if value.is_valid:
            return render(request, 'main.html', {'form': value})
    else:
        value = ChargesForm()
        return render(request, 'main.html', {'form': value})


# данные от генератора

def generator(request):
    e = random_transactions()
    profit = []
    spendings = []
    for x in e:
        if x[1] > 0:
            profit.append(x)
        else:
            spendings.append(x)
    return render(request, 'generator.html', {'i': profit, 'j': spendings})
