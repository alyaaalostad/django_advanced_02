from django.shortcuts import render, redirect
from .models import Store
from .forms import StoreModelForm, CreateModelForm

# Create your views here.
def store_list(request):
    context = {
        "stores": Store.objects.all()
    }
    return render(request, 'store_list.html', context)


def create_view(request):
	form = CreateModelForm()
	if request.method == "POST":
			form = CreateModelForm(request.POST, request.FILES or None)
			if form.is_valid():
				classroom.save()
				return redirect('store-list')
			print (form.errors)
	context = {
	"form": form,
	}
	return render(request, 'create.html', context)


def store_detail(request, store_slug):
	store = Store.objects.get(slug=store_slug)
	context = {
		"store": store,
	}
	return render(request, 'detail.html', context)
