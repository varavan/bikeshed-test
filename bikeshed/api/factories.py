
def bike_view_factory(bike):

    return {
        'id': bike.id,
        'model': bike.model,
        'brand': bike.brand.name,
        'type': bike.type,
        'created_by': bike.created_by.email,
        'created_at': bike.created_at,
        'headline': bike.headline,
        'image': {
            'normal': bike.image.url,
            'thumbnail': bike.image_thumbnail.url
        },
        'description': bike.description,
        'price': bike.price
    }