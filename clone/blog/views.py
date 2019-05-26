from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from blog.models import Post,comment
from blog.forms import postform,commentform
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import  login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.
class about(TemplateView):
    template_name="blog/about.html"

class postlist(ListView):
    context_object_name='postlist'
    model=Post
    template_name="blog/postlist.html"

    def get_queryset(self):
        return Post.objects.filter(pub_time__lte=timezone.now()).order_by('-pub_time')

class postdetail(DetailView):
    context_object_name='postdetail'
    model=Post
    template_name="blog/postdetail.html"

class postcreate(LoginRequiredMixin,CreateView):
    login_url='/login/'
    redirect_field_name='blog/postdetail.html'
    form_class = postform
    model=Post
    template_name="blog/postnew.html"

class postupdate(LoginRequiredMixin,UpdateView):
    login_url='/login/'
    redirect_field_name='blog/postdetail.html'
    form_class= postform
    model=Post
    template_name="blog/postnew.html"

class postdelete(DeleteView):
    model=Post
    success_url=reverse_lazy('blog:postlist')
    template_name='blog/postdelete.html'

class draftlist(LoginRequiredMixin,ListView):
    context_object_name='draftlist'
    login_url='/login/'
    redirect_field_name='blog/postlist.html'
    model=Post
    template_name='blog/draftlist.html'

    def get_queryset(self):
        return Post.objects.filter(pub_time__isnull=True).order_by('-create_time')

@login_required
def add_comment_to_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = commentform(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post
            comment.save()
            return redirect('blog:postdetail',pk=post.pk)
    else:
        form=commentform()
    return render(request,'blog/commentform.html',{'form':form})


@login_required
def comment_approve(request,pk):
    com=get_object_or_404(comment,pk=pk)
    com.approve()
    return redirect('blog:postdetail',pk=com.post.pk)

@login_required
def comment_remove(request,pk):
    com=get_object_or_404(comment,pk=pk)
    post_pk=com.post.pk
    com.delete()
    return redirect('blog:postdetail',pk=post_pk)

@login_required
def post_publish(request,pk):
    pos=get_object_or_404(Post,pk=pk)
    Post.publish(pos)
    return redirect('blog:postdetail',pk=pk)
