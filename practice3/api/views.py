from django.shortcuts import render, HttpResponse
from .forms import example_form
# Create your views here.
def index(request):
    if request.method == 'POST':
        form = example_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            return HttpResponse('SUCCESS')
    else:
        form = example_form()
    return render(request, 'index.html', {'form':form})
    