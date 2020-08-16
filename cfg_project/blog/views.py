from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User
# Create your views here.
'''
posts = [
    {
        'author' : 'Ankit',
        'title' : 'Blog Post 1',
        'content' : 'First post content',Lo
        'date_posted' : '1 Dec 2000'
    },
    {
        'author' : 'Vishal',
        'title' : 'Blog Post 2',
        'content' : 'Second post content',
        'date_posted' : '8 May 1995'
    }

'''

def home(request):
    #a = 5
    #b= 7
    #return HttpResponse('<h1> Sum: '+ str(a+b) + '</h1>')
    #return HttpResponse('<h1>Blog Home</h1>')
    context = {
    'posts' : Post.objects.all()
    }
    return render(request,'blog/home.html',context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #<app><model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html' #<app><model>_<viewtype>.html
    context_object_name = 'posts'
    #ordering = ['-date_posted']
    paginate_by = 3
    
    def get_queryset(self):
        post = Post.objects.filter(title = self.kwargs.get('title'))
        #a = post.objects.all()
        return post  


class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','Lane_name','WasteIn','WasteOut','site_image']
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','Lane_name','WasteIn','WasteOut','site_image']
    
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostGraphView(ListView):
    model = Post
    context_object_name = 'posts'

def mati(request):
    if request.method == 'POST':
        c = request.POST["c"]
    v=Post.objects.all()
    lanel=[]
    wasteinl=[]
    for i in v:
        if(i.title==str(c)):
            lanel.append(i.Lane_name)
            wasteinl.append(i.WasteIn)

    print(lanel)
    print(wasteinl)
    
    plt.bar(lanel,wasteinl, color ='maroon',  width = 0.1) 
    
    plt.xlabel("Lane Numbers") 
    plt.ylabel("Waste collected in kgs") 
    plt.title("Collected in a particular city") 
    #plt.show()
    plt.savefig("media/img.png")
    return render(request,'about.html')

def about(request):
    #return HttpResponse('<h1>Blog About</h1>')
    return render(request,'blog/about.html',{'title' : 'About'})