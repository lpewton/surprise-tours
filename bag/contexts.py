from django.shortcuts import get_object_or_404

from tours.models import Tour


def bag_contents(request):
    """
    Create the contents of the bag
    """

    bag_items = []
    bag = request.session.get('bag', {})
    total = 0
    product_count = 0

    for tour_id, quantity in bag.items():
        tour = get_object_or_404(Tour, pk=tour_id)
        tour_total = quantity * tour.price
        total += tour_total
        product_count += quantity
        bag_items.append({
            'tour_id': tour_id,
            'quantity': quantity,
            'tour': tour,
            'tour_total': tour_total,
        })

    context = {
        'bag_items': bag_items,
        'total': total,
    }

    return context
