
def bag_contents(request): 
    
    bag_items = []
    bag = request.session.get('bag', {})

    context = {
        'bag_items': bag_items,
    }

    return context