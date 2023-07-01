from django.shortcuts import render, redirect, get_object_or_404

from .forms import UserProfileForm
from .models import UserProfile

def MyProfile(request):
    """ Render the user profile page """
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == "GET":
        form = UserProfileForm(instance=profile)
        context = {
            'form': form
        }
        return render (request, "profiles/my-profile.html", context)

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user_id = request.user.id
            profile.save()
            context = {
                'form': form
            }
            return render(request, "profiles/my-profile.html", context)
        else: 
            messages.error(request, 'Form failed, please try again')
    
def pastOrders(request):
    """ Displays the user's past orders """
    return render(request, "profiles/past-orders.html")