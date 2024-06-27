from typing import Any, Dict

from django.views.generic import TemplateView

from .models import Post

"""
    Function Based Views of detail.html

    def detailPage(request, id):
        post = Post.objects.get(id = id)
        context = {
            "post": post,
            "title": post.title
        }
        return render(request, "posts/detail.html", context)
"""


# Create your views here.
# Class Based Views (CBVs)
class PostPageView(TemplateView):
    template_name = "posts/index.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()
        return context


class DetailsPageView(TemplateView):
    template_name = "posts/detail.html"

    def get_context_data(self, **kwargs) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        post_id = self.kwargs.get("id")
        post = Post.objects.get(id=post_id)
        context.update(
            {
                "post": post,
                "title": post.title,
            }
        )
        return context
