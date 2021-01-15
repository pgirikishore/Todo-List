from django.shortcuts import render, redirect
from datetime import date

# Create your views here.
def index(request):
  today = date.today()
  d = today.strftime("%A,  %B %d") # DayofWeek, Month Day
  if request.method == 'POST':
    item = request.POST.get('newItem') # Get the item entered by user
    request.session.modified = True # To allow session variables to be modified
    if not 'items' in request.session or not request.session['items']: # Check if cookie is already present
      request.session['items'] = list()
      items = request.session['items']
      items.append(item)
      request.session['items'] = items
    else:
      items = request.session['items']
      items.append(item)
      request.session['items'] = items
  return render(request, 'todo/index.html', {'kindOfDay':d, 'newListItems': request.session.get('items',[])}) 

def delete_item(request, item_id):
  today = date.today()
  d = today.strftime("%A,  %B %d") # DayofWeek, Month Day
  if request.method == "GET":
    print("Inside delete_item")
    items = request.session['items']
    items.remove(item_id)
    request.session['items'] = items
  # return render(request, 'todo/index.html', {'kindOfDay': d, 'newListItems': request.session.get('items',[])})
  return redirect("https://todo.pgirikishore.repl.co/")