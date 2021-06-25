from django.views.generic import DetailView, ListView
from blog.models import Post

class PostListView(ListView):
    model = Post
    ordering = "-created_at"
    template_name = "post_list.html"
    context_object_name = "posts"

class PostDetailView(DetailView):
    model = Post
    pk_url_kwarg = "post_id"
    template_name = "post_detail.html"
    context_object_name = "post"


# # from django.http import Http404
# from django.shortcuts import get_object_or_404
# from django.template.response import TemplateResponse
# from blog.models import Post

# # Create your views here.
# def post_list(request):
#     return TemplateResponse(
#         request, "post_list.html",
#         {"posts": Post.objects.all()}
#     )

# def post_detail(request, post_id):
#     post = get_object_or_404(Post, id=post_id)
#     return TemplateResponse(
#         request, "post_detail.html",
#         {"post": post}
#     )