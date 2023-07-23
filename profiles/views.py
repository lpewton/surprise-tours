from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .forms import UserProfileForm, ReviewForm
from .models import UserProfile
from checkout.models import Order


def MyProfile(request):
    """
    Render the user profile page
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == "GET":
        form = UserProfileForm(instance=profile)
        context = {
            'form': form
        }

        return render(request, "profiles/my-profile.html", context)

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
    """
    Displays the user's past orders
    """
    if request.user.is_authenticated:
        profile = get_object_or_404(UserProfile, user=request.user)
        orders = profile.orders.all()

        context = {
            'orders': orders
        }

        return render(request, "profiles/past-orders.html", context)

    else:
        messages.error(
            request, 'You are not logged in,'
                     'please log in to see this information')

        return render(request, "home/index.html")


def orderDetail(request, order_id):
    """
    Displays the user's past order details
    """

    order = get_object_or_404(Order, pk=order_id)

    if order.user_profile.user == request.user:
        context = {
            'order': order,
        }

        return render(request, "profiles/order-detail.html", context)

    else:
        messages.error(request, 'You are not logged in with the correct user!')

        return render(request, "home/index.html")


def review(request,):

    form = reviewForm()
    context = {
            'form': form,
        }

    if request.method == "POST":
        form = reviewForm(request.POST)

        if form.is_valid():
            form_review = form.save(commit=False)
            form_review.user = request.user
            form.save()
            messages.success(request, 'Review sent successfully!')

            return render(request, "profiles/review.html", context)

        else:
            messages.error(
                request, "Couldn't sent review failed, please try again")

    return render(request, "profiles/review.html", context)
