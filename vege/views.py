from django.shortcuts import render
from .models import *
from django.shortcuts import redirect
from django.contrib.auth.models import User

# Create your views here.

def recipies(request):
    if request.method == 'POST':
        data = request.POST
        recipe_name = data.get('receipe_name')
        recipe_description = data.get('receipe_des')
        recipe_image = request.FILES.get('receipe_image')

        if not recipe_name or not recipe_description or not recipe_image:
            return render(request, 'recipe.html', {'error': 'All fields are required.'})

        Receipe.objects.create(
            receipe_name = recipe_name,
            receipe_des = recipe_description,
            receipe_image = recipe_image
            
        )
        print(recipe_name )
        print( recipe_description )
        print(recipe_image)
        return redirect('/recipies/')
    queryset = Receipe.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(receipe_name__icontains = request.GET.get('search') )
    context = {'receipes':queryset}
        
        
        
    
    return render(request , 'recipe.html' , context)


def update_recipes(request , id):
    queryset = Receipe.objects.get(id=id)
    if request.method == 'POST':
        data = request.POST
        
        recipe_name = data.get('receipe_name')
        recipe_desc = data.get('receipe_des')
        recipe_image = request.FILES.get('receipe_image')

        if not recipe_name or not recipe_desc:
            return render(request, 'update_recipes.html', {'error': 'Recipe name and description are required.', 'recipe': queryset})

        queryset.receipe_name = recipe_name
        queryset.receipe_des = recipe_desc
        if recipe_image:
            queryset.receipe_image = recipe_image
        queryset.save()
        return redirect('/recipies/')
        
    context = {'recipe':queryset}
    return render(request , 'update_recipes.html' , context)

def delete_recipies(request , id):
    queryset = Receipe.objects.get(id=id)
    queryset.delete()
    return redirect('/recipies/')


def register(request):
    if request.method == 'POST':
        data = request.POST
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        password = data.get('password')
        username = data.get('username')  # Add this line
        user = User.objects.create(
            username=username,  # Include username in user creation
            first_name = first_name,
            last_name = last_name,
            email = email,
            )
        user.set_password(password)
        user.save()
        print(user.first_name)
        return redirect('/register/')
    return render(request , 'register.html')
def login_user(request):
    if request.method == 'POST':
        data = request.POST
        username  = data.get('username')
        password = data.get('password')
        
    return render(request , 'login.html')
