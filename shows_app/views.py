from django.shortcuts import render,  redirect
from .models import *
from django.urls import reverse
from django.contrib import messages

from .models import Shows

def root(request):
	return redirect('/shows')

def index(request):
	context= {
		"all_shows": Shows.objects.all()
	}

	return render(request, 'index.html', context)
		

def create_new(request):
	errors = Shows.objects.basic_validator(request.POST)
	if len(errors) > 0:
		for key, value in errors.items():
			messages.error(request, value)
		return redirect('/shows/new')
	else:
		create_new = Shows.objects.create(title= request.POST['title'], network = request.POST['network'], release_date= request.POST['release_date'], description = request.POST['description'])
		print(create_new.id)

		return redirect(f'/shows/{create_new.id}')
	return redirect('/shows/new')	

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

def update_show(request, show_id):
	errors = Shows.objects.basic_validator(request.POST)
	if len(errors) > 0:
		for key, value in errors.items():
			messages.error(request, value)
		return redirect(f'/shows/{show_id}/edit')
		
	show = Shows.objects.get(id=show_id)
	show.title = request.POST['title']
	show.network = request.POST['network']
	show.release_date = request.POST['release_date']
	show.description = request.POST['description']
	show.save()
	return redirect(f'/shows/{show_id}')

def delete_show(request, show_id):
	delete_show = Shows.objects.get(id=show_id).delete()
	
	return redirect('/shows')