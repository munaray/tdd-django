from django.urls import path

from .views import DetailsPageView, PostPageView

urlpatterns = [
    path("", PostPageView.as_view(), name="homepage"),
    path("post/<int:id>/", DetailsPageView.as_view(), name="post_detail"),
]
