from django.shortcuts import render
from datetime import date
items = []

# Create your views here.
def index(request):
  print("Items - >",items)
  today = date.today()
  d = today.strftime("%A,  %B %d")
  if request.method == 'POST':
    item = request.POST.get('newItem')
    print("Item - >",item)
    items.append(item)
  return render(request, 'todo/index.html', {'kindOfDay':d, 'newListItems': items})