from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from CBV_app.models import Company,Employee
from django.urls import reverse_lazy

# Create your views here.


class CBView(TemplateView):
    template_name = 'index.html'
    # dict = {'key':'value'}
    # return render(request,'CBV_app/index.html',context=dict)

class Comp_list(ListView):
    # model = Comapany.objects.all()....order_by()
    model = Company
    #Company_list
    context_object_name = 'CompL'

class Comp_detail(DetailView):
    model = Company
    context_object_name = 'CompD'
    template_name = 'CBV_app/Company_details.html'

class CreateV(CreateView):
    fields = '__all__'
    model = Company

class DeleteV(DeleteView):
    model = Company
    success_url = reverse_lazy("CBV_app:list")
    template_name = 'CBV_app/Company_delete.html'

class UpdateV(UpdateView):
    fields = '__all__'
    model = Company
    template_name = "CBV_app/Company_update.html"

class CreateVE(CreateView):
    model = Employee
    fields = '__all__'
    context_object_name = "emp"
    template_name = "CBV_app/Company_create_E.html"

class DeleteE(DeleteView):
    model = Employee
    success_url = reverse_lazy("CBV_app:list")
    template_name = 'CBV_app/Company_delete_E.html'






