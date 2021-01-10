from django.shortcuts import render
from datetime import date

# Create your views here.
def index(request):
  today = date.today()
  d = today.strftime("%A,  %B %d") # DayofWeek, Month Day
  if request.method == 'POST':
    item = request.POST.get('newItem') # Get the item entered by user
    request.session.modified = True # To allow session variables to be modified
    items = request.session.get('items',' ') #Get the session variable. Set it to '' is not available
    request.session['items'] = items+"__!$__"+item #TODO: Must make use of Lists instead of String
    return render(request, 'todo/index.html', {'kindOfDay':d, 'newListItems': request.session.get('items', '').split("__!$__")[1:]}) #TODO: Remove after implementing with Lists.
  else: #TODO: Remove after implementing with Lists.
    return render(request, 'todo/index.html', {'kindOfDay':d, 'newListItems': request.session.get('items', '')}) #TODO: Remove after implementing with Lists.