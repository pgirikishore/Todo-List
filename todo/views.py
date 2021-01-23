from django.shortcuts import render, redirect
from datetime import date

# Create your views here.
def index(request):
  today = date.today()
  d = today.strftime("%A,  %B %d") # DayofWeek, Month Day
  if request.method == 'POST':
    tile = request.POST.get('newTile') # Get the item entered by user
    request.session.modified = True # To allow session variables to be modified
    if not 'tiles' in request.session or not request.session['tiles']: # Check if cookie is already present
      request.session['tiles'] = list()
      tiles = request.session['tiles']
      tiles.append(tile)
      request.session['tiles'] = tiles

      request.session['items'] = dict()
      request.session['items'][tile] = list()
    else:
      tiles = request.session['tiles']
      tiles.append(tile)
      request.session['tiles'] =tiles

      request.session['items'][tile] = list()

  print(request.session.get('tiles',[]))
  print(request.session.get('items',{}))
  
  return render(request, 'todo/index.html', {'kindOfDay':d, 'newTileItems': request.session.get('tiles',[]), 'newItems': request.session.get('items',{})}) 

def delete_tile(request, tile_id):
  print("hi")
  if request.method == "GET":
    tiles = request.session['tiles']
    tiles.remove(tile_id)
    request.session['tiles'] = tiles

    items = request.session['items']
    del items[tile_id]
    request.session['items'] = items

    print(request.session.get('tiles',[]))
    print(request.session.get('items',{}))
  # return render(request, 'todo/index.html', {'kindOfDay': d, 'newTileItems': request.session.get('tiles',[])})
  return redirect("https://todo.pgirikishore.repl.co/")

def delete_item(request, key, item):
  if request.method == "GET":
    items = request.session['items']
    items[key].remove(item)
    request.session['items'] = items

  # return render(request, 'todo/index.html', {'kindOfDay': d, 'newTileItems': request.session.get('tiles',[])})
  return redirect("https://todo.pgirikishore.repl.co/")

def items(request, tile_item):
  print("bye")
  if request.method == 'POST':
    item = request.POST.get('newItem') # Get the item entered by user
    request.session.modified = True # To allow session variables to be modified
    items = request.session['items']
    items[tile_item].append(item)
    request.session['items'] = items
    print(request.session['items'])

  if request.method == "GET":
    tiles = request.session['tiles']
    tiles.remove(tile_item)
    request.session['tiles'] = tiles

    items = request.session['items']
    del items[tile_item]
    request.session['items'] = items

    print(request.session.get('tiles',[]))
    print(request.session.get('items',{}))
  return redirect("https://todo.pgirikishore.repl.co/")