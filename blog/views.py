from django.shortcuts import render
from .models import Post,Category,Comment
from taggit.models import Tag
from .forms import CommentForm
from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here.
def post_list(request):
    post_list = Post.objects.all()

    ##Search
    search_query = request.GET.get('q')
    if search_query :
        post_list = post_list.filter(
            Q(title__icontains = search_query)|
            Q(content__icontains = search_query)|
            Q(tags__name__icontains = search_query)
        ).distinct()

    paginator = Paginator(post_list,2)
    page_number = request.GET.get('page')
    post_list = paginator.get_page(page_number)
    context = {
        'post_list':post_list,
    }
    return render(request,"blog/post_list.html",context)

def post_detail(request,id):
    post_detail = Post.objects.get(id=id)
    categories = Category.objects.all()
    all_tags = Tag.objects.all()
    comments = Comment.objects.filter(post=post_detail)
    comment_form = CommentForm()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.user = request.user
            new_comment.post = post_detail
            new_comment.save()

    context = {
        'post_detail':post_detail,
        'categories':categories,
        'all_tags':all_tags,
        'comments':comments,
        'comment_form':comment_form,
    }
    return render(request,"blog/post_detail.html",context)

def post_by_tag(request,tag):
    post_by_tag = Post.objects.filter(tags__name__in=[tag])
    context = {
        'post_list':post_by_tag,
    }
    return render(request,"blog/post_list.html",context)

def post_by_category(request,category):
    post_by_category = Post.objects.filter(category__category_name=category)
    context={
        'post_list':post_by_category,
    }
    return render(request, "blog/post_list.html",context)
   