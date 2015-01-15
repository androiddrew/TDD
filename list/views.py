from django.shortcuts import render, redirect
from django.http import HttpResponse
from list.models import Item, List
# Create your views here.

def home_page(request):
	# removed now that home page does not handle POST requests
	# if request.method == 'POST':
	# 	new_item_text = request.POST['item_text'] #
	# 	Item.objects.create(text=new_item_text)
	# 	return redirect('/lists/the-only-list-in-the-world/')
	return render(request, 'home.html')

def view_list(request):
	items = Item.objects.all()
	return render(request,'list.html', {'items': items})

def new_list(request):
	list_ = List.objects.create()
	Item.objects.create(text=request.POST['item_text'], list = list_)
	return redirect('/lists/the-only-list-in-the-world/')
