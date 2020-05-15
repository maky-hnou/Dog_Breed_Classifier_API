from rest_framework.routers import DefaultRouter

from .views import ImageModelViewSet

router = DefaultRouter()
router.register(r'Dog_Breed_Classifier', ImageModelViewSet)
urlpatterns = router.urls
# urlpatterns = [
#     url(r'', include(router.urls)),
# ]
# from django.conf.urls import url, include
