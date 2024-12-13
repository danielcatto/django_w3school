from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
    # Fetches all members from the database
    mymembers = Member.objects.all().values()
    # Loads the 'all_members.html' template
    template = loader.get_template('all_members.html')
    # Creates a context dictionary with the member data
    context = {
        'mymembers': mymembers,
    }

    # Renders the template with the context and returns the HTML response
    return HttpResponse(template.render(context, request))

def details(request, id):
    # Fetches a specific member by ID
    mymember = Member.objects.get(id=id)
    # Loads the 'details.html' template
    template = loader.get_template('details.html')
    # Creates a context dictionary with the member's details
    context = {
        'mymember': mymember,
    }
    # Renders the template with the context and returns the HTML response
    return HttpResponse(template.render(context, request))



def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())
    

def testing(request):
  mydata = Member.objects.filter(firstname='daniel').values()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))