from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView
from django.views import View
from django.urls import reverse_lazy
from rest_framework import viewsets
from .serializers import ItemSerializer
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

# def index(request):
#     item_list = Item.objects.all()
    
#     context = {
#         'item_list': item_list,

#     }
#     return render(request, 'food/index.html',context) 


class IndexClassView(ListView):
    model = Item;
    template_name = 'food/index.html'
    context_object_name = 'item_list'


# def item(request):
#     return HttpResponse('This is an item view')
class ItemView(View):
    def get(self, request):
        return HttpResponse('This is an item view')

# def detail(request,item_id):
#     item = Item.objects.get(pk=item_id)
#     context = {
#         'item': item,
#     }
#     return render(request, 'food/detail.html',context)
class ItemDetailView(DetailView):
    model = Item
    template_name = 'food/detail.html'
    context_object_name = 'item'




# def create_item(request):
#     form = ItemForm(request.POST or None)

#     if form.is_valid():
#         form.save()
#         return redirect('food:index')
#     return render(request, 'food/item-form.html', {'form': form})


# this is class based view for create item

class CreateItem(LoginRequiredMixin,CreateView):
    model = Item;
    fields = ['item_name','item_desc','item_price','item_image']
    template_name = 'food/item-form.html'

    def form_valid(self,form):
        form.instance.user_name = self.request.user

        return super().form_valid(form)

# def update_item(request,id):
#     item = Item.objects.get(id=id)
#     form = ItemForm(request.POST or None, instance=item)

#     if form.is_valid():
#         form.save()
#         return redirect('food:index')
#     return render(request, 'food/item-form.html', {'form': form, 'item': item})


# class ItemUpdateView(UpdateView):
#     model = Item
#     form_class = ItemForm
#     template_name = 'food/item-form.html'
#     success_url = reverse_lazy('food:index')

class UpdateItemView(LoginRequiredMixin,View):
    template_name = 'food/item-form.html'

    def get(self, request, id):
        item = Item.objects.get(id=id)
        form = ItemForm(instance=item)
        context = {'form': form, 'item': item}
        return render(request, self.template_name, context)

    def post(self, request, id):
        item = Item.objects.get(id=id)
        form = ItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()
            return redirect('food:index')

        context = {'form': form, 'item': item}
        return render(request, self.template_name, context)

# def delete_item(request,id):
#     item = Item.objects.get(id=id)

#     if request.method == 'POST':
#         item.delete()
#         return redirect('food:index')
#     return render(request, 'food/item-delete.html',{'item':item})

class DeleteItemView(LoginRequiredMixin,View):
    template_name = 'food/item-delete.html'

    def get(self, request, id):
        item = Item.objects.get(id=id)
        context = {'item': item}
        return render(request, self.template_name, context)

    def post(self, request, id):
        item = Item.objects.get(id=id)

        if request.method == 'POST':
            item.delete()
            return redirect('food:index')

        context = {'item': item}
        return render(request, self.template_name, context)

