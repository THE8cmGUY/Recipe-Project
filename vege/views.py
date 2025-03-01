from django.shortcuts import render
from .models import *
from django.shortcuts import redirect

# Create your views here.

def recipies(request):
    if request.method == 'POST':
        data = request.POST
        recipe_name = data.get('receipe_name')
        recipe_description = data.get('receipe_des')
        recipe_image = request.FILES.get('receipe_image')
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
    context = {'receipes':queryset}
        
        
        
    
    return render(request , 'recipe.html' , context)
def delete_recipies(request , id):
    queryset = Receipe.objects.get(id=id)
    queryset.delete()
    return redirect('/recipies/')
    
