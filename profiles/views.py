from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect

from .forms import UserProfileForm, ReviewForm
from .models import UserProfile, Review
from checkout.models import Order


def MyProfile(request):
    """
    Render the user profile page
    """
    if request.user.is_authenticated:
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

    else:
        messages.error(request, 'You are not logged in')

        return render(request, "home/index.html")


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

    if order.user_profile:
        if order.user_profile.user == request.user:
            context = {
                'order': order,
            }

            return render(request, "profiles/order-detail.html", context)

        else:
            messages.error(
                request, 'You are not logged in with the correct user!')

            return render(request, "home/index.html")

    else:
        messages.error(
            request, 'Sorry, you are not logged in with the correct user')
        return redirect(reverse('home'))


def review(request):
    """
    Where the user can submit a review for a tour
    """
    form = ReviewForm()
    context = {
            'form': form,
        }

    if request.method == "GET":
        if request.user.is_authenticated is False:
            messages.error(
                request, "Please log in to access this page")

            return render(request, "home/index.html")

    if request.method == "POST":
        form = ReviewForm(request.POST)

        if form.is_valid():
            form_review = form.save(commit=False)
            form_review.user = request.user
            form.save()
            messages.success(request, 'Review sent successfully!')

            return render(request, "profiles/review.html", context)

        else:
            messages.error(
                request, "Couldn't send review,"
                         "please make sure rating is between 0 and 10")

    return render(request, "profiles/review.html", context)


def pendingReviews(request):
    """
    Where the admin sees the submitted reviews and can approve them
    """
    if request.user.is_superuser:
        reviews = Review.objects.filter(approved=False)

        context = {
            'reviews': reviews,
        }

        return render(request, "profiles/pending-reviews.html", context)

    else:
        messages.error(request, 'Sorry, only store owners can do that.')

        return redirect(reverse('home'))


def approveReview(request, review_id):
    """
    Allow admin to approve review
    """
    if request.user.is_superuser:
        review = get_object_or_404(Review, pk=review_id)
        review.approved = True
        review.save()
        messages.success(
            request, "Review posted correctly")

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    else:
        messages.error(request, 'Sorry, only store owners can do that.')

        return redirect(reverse('home'))


def rejectReview(request, review_id):
    """
    Allow admin to reject and delete review
    """
    if request.user.is_superuser:
        review = get_object_or_404(Review, pk=review_id)
        review.delete()
        messages.success(
            request, "Review not approved and deleted")

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    else:
        messages.error(request, 'Sorry, only store owners can do that.')

        return redirect(reverse('home'))
