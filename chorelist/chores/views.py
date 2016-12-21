from django.shortcuts import get_object_or_404, render

# Create your views here.

from django.http import HttpResponse, Http404
from .models import ChoreList, Chore
	#not needed if use render
#from django.template import RequestContext, loader

def index(request):
	#makes list of all chorelists
	lists = ChoreList.objects.all()
######### Long Way ###################### requires loader & requestcontext
	#gets specified template 'loader' to use at chures.index
	#template = loader.get_template('chores/index.html')
	#Loads the specified content to populate the template
	#context = RequestContext(request, {
		#'chorelists': lists
		#})
	#renders template with specified context
	#return HttpResponse(template.render(context))

############ Short Way ######################
	context = {'chorelists': lists }
	return render(request, 'chores/index.html', context)


def detail(request, chorelist_id):
	#try:    #try catch block incase of invalid chorelist_id
		#list = ChoreList.objects.get(pk=chorelist_id)  #searches by primary key
	# get_object_or_404 skips need for try-except
		list = get_object_or_404(ChoreList, pk=chorelist_id)
	#except ChoreList.DoesNotExist:
		#raise Http404('Chorelist does not exist')
	#same as above but adds context as an expression instead of a variable
		return render(request, 'chores/detail.html', {'chorelist': list })

# def chores(request, chorelist_id):
# 	list = get_object_or_404(ChoreList, pk=chorelist_id)
# 	chores = list.chore_set.all()
# 	return render(request, 'chores/chores.html', {'chorelist': list, 'chores': chores})

def choredetail(request, chorelist_id, chore_id):
	list = get_object_or_404(ChoreList, pk=chorelist_id)
	chore = get_object_or_404(Chore, pk=chore_id)
	return render(request, 'chores/choredetail.html', {'chorelist': list, 'chore': chore})