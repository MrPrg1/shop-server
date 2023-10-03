from django.urls import path, include
from .views import CategoryView, BrandView, ProductView, CouponView, ProductOrderView, AddressView, OrderView, CommentView, FavoritView
from rest_framework import routers

router = routers.SimpleRouter()
router.register('category', CategoryView)
router.register('brand', BrandView)
router.register('product', ProductView)
router.register('coupon', CouponView)
router.register('productorder', ProductOrderView)
router.register('address', AddressView)
router.register('order', OrderView)
router.register('comment', CommentView)
router.register('favorit', FavoritView)
urlpatterns = router.urls


# urlpatterns = [
#     path('', include(router.urls)),
    # path('category/', CategoryView.as_view()),
    # path('brand/', BrandView.as_view()),
    # path('product/', ProductView.as_view()),
    # path('coupon/', CouponView.as_view()),
    # path('productorder/', ProductOrderView.as_view()),
    # path('address/', AddressView.as_view()),
    # path('order/', OrderView.as_view()),
    # path('comment/', CommentView.as_view()),
    # path('favorit/', FavoritView.as_view()),
# ]