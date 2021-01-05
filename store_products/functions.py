from .models import *
from store_account.functions import get_user_by_id

#Category start
def get_category_by_id(category_id):
    try:
        category = Category.objects.get(pk=category_id)
    except:
        obj = False
    else:
        obj = {
            "id": category.id,
            "name": category.name,
            "icon": category.icon,
            "status": category.status
        }
    return obj
#Category end

#Brand start
def get_brand_by_id(brand_id):
    try:
        brand = Brand.objects.get(pk=brand_id)
    except:
        obj = False
    else:
        obj = {
            "id": brand.id,
            "user": get_user_by_id(brand.user.id),
            "name": brand.name,
            "logo": brand.logo.name,
            "status": brand.status
        }
    return obj
def get_brands_by_user(user):
    brandList = []
    try:
        brands = Brand.objects.filter(user=User)
    except:
        brandList = False
    else:
        for brand in brands:
            brandList.append(get_brand_by_id(brand.id))
    return brandList
#Brand end

#Size start
def get_size_by_id(size_id):
    size = Size.objects.get(pk=size_id)
    obj = {
        "id": size.id,
        "size": size.size
    }
    return obj
def get_sizes_by_product(product):
    sizeList = []
    try:
        sizes = Size.objects.filter(product=product)
    except:
        sizeList = []
    else:
        for size in sizes:
            sizeList.append(get_size_by_id(size.id))
    return sizeList
#Size end

#Color
def get_color_by_id(color_id):
    color = Color.objects.get(pk=color_id)
    obj = {
        "id": color.id,
        "color": color.color
    }
    return obj
def get_colors_by_product(product):
    colorList = []
    try:
        colors = Color.objects.filter(product=product)
    except:
        colorList = False
    else:
        for color in colors:
            colorList.append(get_color_by_id(color.id))
    return colorList
#Color end

#Spec start
def get_spec_by_id(spec_id):
    spec = Spec.objects.get(pk=spec_id)
    obj = {
        "id": spec.id,
        "value": spec.value
    }
    return obj
def get_specs_by_product(product):
    specList = []
    try:
        specs = Spec.objects.filter(product=product)
    except:
        specList = False
    else:
        for spec in specs:
            specList.append(get_spec_by_id(spec.id))
    return specList
#Spec end

#Review start
def get_review_by_id(review_id):
    review = Review.objects.get(pk=review_id)
    obj = {
        "id": review.id,
        "name": review.name,
        "email": review.email,
        "rating": review.rating,
        "comment": review.comment,
        "date": review.date
    }
    return obj
def get_reviews_by_product(product):
    reviewList = []
    try:
        reviews = Review.objects.filter(product=product)
    except:
        reviewList = False
    else:
        for review in reviews:
            reviewList.append(get_review_by_id(review.id))
    return reviewList
#Review end


#Image start
def get_image_by_id(image_id):
    image = Image.objects.get(pk=image_id)
    obj = {
        "id": image.id,
        "image": image.image
    }
    return obj
def get_images_by_product(product):
    imageList = []
    try:
        images = Image.objects.filter(product=product)
    except:
        imageList = False
    else:
        for image in images:
            imageList.append(get_image_by_id(image.id))
    return imageList
#Image end

#Produc start
def get_product_by_id(product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except:
        obj = False
    else:
        obj = {
            "id": product.id,
            "category": get_category_by_id(product.category.id),
            "brand": get_brand_by_id(product.brand.id),
            "name": product.name,
            "usual_price": product.usual_price,
            "listing_price": product.listing_price,
            "description": product.description,
            "picture": product.picture.name,
            "sizes": get_sizes_by_product(product),
            "colors": get_colors_by_product(product),
            "reviews": get_reviews_by_product(product),
            "images": get_images_by_product(product)
        }
    return obj
def get_products_by_brand(brand):
    productList = []
    try:
        products = Product.objects.filter(brand=brand)
    except:
        productList = False
    else:
        for product in products:
            productList.append(get_product_by_id(product.id))
    return productList
#Product end