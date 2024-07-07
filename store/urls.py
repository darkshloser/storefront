from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter
from . import views

# If we use DefaultRouter instead of SimpleRouter we'll have also response for ...../store/ 
# containing the URLs for products and collections
# {
#  "products": "htp://127.0.0.1:8000/store/products/",
#  "collections": "htp://127.0.0.1:8000/store/collections/"
# }
# Additional feature is if we call for example "htp://127.0.0.1:8000/store/collections.json"
# we'll get all the data in JSON format 


router = DefaultRouter()
router.register('products', views.ProductViewSet)  # first argument is the value we're using for the url and the ssecond is  
router.register('collections', views.CollectionViewSet)


urlpatterns = [
    path('', include(router.urls))
]

