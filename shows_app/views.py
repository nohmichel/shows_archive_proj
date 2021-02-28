from django.shortcuts import render,  redirect
from .models import *
from django.urls import reverse

def root(request):
	return redirect('/shows')

def index(request):
	context= {
		"all_shows": Shows.objects.all(),
	}
	return render(request, 'index.html', context)

def create_new(request):
	create_new = Shows.objects.create(title= request.POST['title'], network = request.POST['network'], release_date= request.POST['release_date'], description = request.POST['description'])
	print(create_new.id)
	return redirect(f'/shows/{create_new.id}')

def show_bio(request, show_id):
	context= {
		"one_show": Shows.objects.get(id=show_id)
	}
	return render(request, 'show_bio.html', context)

def shows(request):
	context= {
		"all_shows": Shows.objects.all(),
	}
	return render(request, 'shows.html', context)	


def edit_show(request, show_id):
	context= {
		"one_show": Shows.objects.get(id=show_id),
		"all_shows": Shows.objects.all(),
	}
	return render(request, 'edit_show.html', context)

def update_show(request):
	show = Shows.objects.get(id=show_id)
	show.title = request.POST.get('title')
	show.network = request.POST.get()

	return redirect('/shows/<int:show_id>')

def delete_show(request, show_id):
	delete_show = Shows.objects.get(id=show_id).delete()
	# delete_show.delete()

	return redirect('/shows')