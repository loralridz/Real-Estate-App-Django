from django.shortcuts import render,get_object_or_404
from django.core.mail import send_mail
from django.views.generic import ListView
from .models import Contact,Property
from .choices import bedroom_choices,bathroom_choices,price_choices,location_choices

# Create your views here.
def home(request):
	return render(request,'app/home.html',{})

def searchproperty(request):
 

	context = {
		'propertys' : Property.objects.all(),
		'bedroom_choices' : bedroom_choices,
		'bathroom_choices' : bathroom_choices,
		'price_choices' : price_choices,
		'location_choices' : location_choices,

	}

	return render(request,'app/searchproperty.html',context)

# class based lists
class PropertyListView(ListView):
	model = Property
	template_name = 'app/property.html'
	queryset = Property.objects.all()
   
	# Default name of all objects would be objectlist so change the list 
	# Named as posts as home has context of posts mentioned
	#context_object_name = 'propertys'
	# in order to views new posts above and old below
	# putting minus sign before to do 
	#ordering = ['-dateposted']
	# how many objects per page
	#paginate_by = 3
	# app/model_viewtype.html


def about(request):
	return render(request,'app/about.html',{})

def blog(request):
	return render(request,'app/blog.html',{})

def propertysingle(request,propertyid):
	propertys = get_object_or_404(Property,pk=propertyid)
	context = {
		'propertys' : propertys
	}
	return render(request,'app/property-single.html',context)

def contact(request):
	# Someone adding or posting data is a POST request
	if request.method == "POST":

		fname = request.POST['fname']
		sname = request.POST['sname']
		email = request.POST['email']
		message = request.POST['message']
		contact = Contact(fname=fname, sname=sname
			,email=email
			,message=message
			)
		contact.save()
		send_mail(
				'Message recieved from ' + fname,		# Subject
				message + ' With Email '+email,	# Message
				email,		# From email
				['djangofreaks@gmail.com'], # To Email
				fail_silently = False

			)
		return render(request,'app/contact.html',{'fname':fname})

	else:
		return render(request,'app/contact.html',{})

