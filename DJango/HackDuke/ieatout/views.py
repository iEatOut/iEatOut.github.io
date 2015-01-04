from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from GraphLoader import priceGraph
from GraphLoader2 import priceNut
from ieatout.models import UserProfile
import time
from geopy.geocoders import GoogleV3



def index(request):
     # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    #context_dict = {'boldmessage': "I am bold font from the context",'hoe': "3"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    User = UserProfile.objects.all()
    Usersize = len(User)
    UserA = User[(Usersize-1):(Usersize)] #Get the top user profile
    UserFields = UserProfile._meta.get_all_field_names()
    
    geolocator = GoogleV3()
    
    UserL = UserProfile.objects.all().values_list('location')
    UserLOfficial = UserL[Usersize-1]
    Loc = "".join(UserLOfficial)
    
    address, (latitude, longitude) = geolocator.geocode(Loc)
    AddressString = "".join(address)
    #AddressString = AddressString[1:]
    AddressList = [x.strip() for x in AddressString.split(',')]
    length = len(AddressList)
    State = AddressList[length-3]
    Zip = AddressList[length-2][3:]


    
    UserA = UserProfile.objects.all().values_list('allergy')
    UserAOfficial = UserA[Usersize-1]
    Allergy = "".join(UserAOfficial)
    
    UserH = UserProfile.objects.all().values_list('health')
    UserHOfficial = UserH[Usersize-1]
    Health = "".join(UserHOfficial)
    
    UserP = UserProfile.objects.all().values_list('state')
    UserPOfficial = UserP[Usersize-1]
    perference = "".join(UserPOfficial)
    
    a = "****"
    print a
    print type(Loc)
    print a
    
    #UserFields = UserProfile.get_model_fields(UserA)

    #priceGraph("1900 Broadway", "New York", "10023", ["Gluten-Free"], ["Low Sodium"])
    #priceNut("1900 Broadway", "New York", "10023", ["Gluten-Free"], ["Low Sodium"])
    
    #CHANGE STATE TO SOMETHING HEALTH RELATED
    
    priceGraph(Loc, State, Zip, [Allergy], [Health])
    priceNut(Loc, State, Zip, [Allergy], [Health])
    
    time.sleep(10)
    return render_to_response('list.html', context)
    

def result(request):

    context = RequestContext(request)
    return render_to_response('list.html', context)
    
from ieatout.forms import UserProfileForm

def add_category(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = UserProfileForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = UserProfileForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    
    return render(request, 'add_category.html', {'form': form})
