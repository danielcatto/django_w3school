from django.http import HttpResponse
from django.template import loader
from .models import Member
from utils.calculos.cal_idade import calcular_idade as c_idade, convert_date_format as conv_data


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
    
    #calcular idade da pessoa 
    data_ani =  str(mymember.birth_date)  
    data_formatada = conv_data(data_ani)
    anos, meses = c_idade(data_formatada)
    idade = f'{anos} anos e {meses} meses'

    # Creates a context dictionary with the member's details
    context = {
        'mymember': mymember, 'tempo_de_vida': idade,
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

def myfirst(request):
   template = loader.get_template('myfirst.html')
   
   return HttpResponse(template.render( ))