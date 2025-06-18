from django.shortcuts import render, redirect
from .forms import Employeeform
from .models import Test

def test_list(request):
    context = {'test_list': Test.objects.all()}
    return render(request, 'App/test_list.html', context)


def test_form(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = Employeeform()
        else:
            test = Test.objects.get(pk=id)
            form = Employeeform(instance=test)
        return render(request, 'App/test_form.html', {'form': form})
    else:
        form = Employeeform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/api/list')
        return render(request, 'App/test_form.html', {'form': form})


def test_delete(request, id):
    employee= Test.objects.get(pk=id)
    employee.delete()

    return redirect('/api/list')

# Create your views here.
