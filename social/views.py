from django.shortcuts import render
from social.models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.filter().order_by('published_date')
    return render(request, 'social/post_list.html', {'posts': posts})