from django.shortcuts import render, redirect
from .models import Post
from django.views import generic
from .forms import PostForm

#def index(request):
    #posts = Post.objects.all()
    #return render(request, "django_girls/index.html", {'post_list': posts, 'title': 'The main PAGE'})

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index') 

    else:
        form = PostForm()

    return render(request, 'create_post.html', {'form': form})



