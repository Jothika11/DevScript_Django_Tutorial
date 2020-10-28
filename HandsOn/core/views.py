import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserForm
from .serializers import UserDataSerializer
# Create your views here.
def hey(request,person):
    return HttpResponse(f"<h1>Hello {person}</h1>")

def index(request):
    return  render(request,"home_page.html")


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        # check whether it's valid:
        form = UserForm(request.POST)
        if form.is_valid():
            user_data = form.cleaned_data
            data={'name': user_data["your_name"],'email': user_data["your_email"],'address': user_data["address"]}
            # print(data)
            dump_data={'data': json.dumps(data)}
            serializer = UserDataSerializer(data=dump_data)
            if serializer.is_valid():
                serializer.save()
            return render(request,'thanks.html',{'name':data["name"],'email':data["email"]})
    else:
        form =UserForm()

    return render(request, 'form.html', {'form': form})