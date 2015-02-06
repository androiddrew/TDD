from django.shortcuts import render, redirect
from django.http import HttpResponse
from list.forms import ItemForm
from list.models import Item, List
from django.core.exceptions import ValidationError

# Create your views here.

def home_page(request):
	# removed now that home page does not handle POST requests
	# if request.method == 'POST':
	# 	new_item_text = request.POST['item_text'] #
	# 	Item.objects.create(text=new_item_text)
	# 	return redirect('/lists/the-only-list-in-the-world/')
	return render(request, 'home.html', {'form': ItemForm()})

def view_list(request, list_id):
	list_ = List.objects.get(id=list_id)
	error = None

	if request.method == 'POST':
		#Item.objects.create(text=request.POST['item_text'], list=list_)
		try:
			item = Item(text=request.POST['item_text'], list=list_)
			item.full_clean()
			item.save()
			return redirect(list_)
		except ValidationError:
			error = "You can't have an empty list item"
	
	return render(request, 'list.html', {'list': list_, 'error': error})
	

def new_list(request):
	list_ = List.objects.create()
	item = Item(text=request.POST['item_text'], list = list_)
	try:
		item.full_clean()
		item.save()
	except ValidationError:
		list_.delete()
		error = "You can't have an empty list item"
		return render(request, 'home.html', {"error": error})
	#We have defined  a get_absolute_url function in our models which
	#When we redirect and pass a object it will return the value for 
	#get_absolute_url()
	return redirect(list_)

