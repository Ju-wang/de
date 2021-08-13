from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm

def main(request):
    return render(request, 'main.html')

def visiter(request): #all visiter
    visiters = Post.objects.all()
    return render(request, 'visiter.html', {'visiters':visiters})

def detail(request, id): #each visiter
    visit = get_object_or_404(Post, pk=id)
    comment_form = CommentForm()
    return render(request, 'detail.html', {'visit':visit, 'comment_form':comment_form})

# def new(request):
#     if request.method == 'GET':
#         form = PostForm()

#     elif request.method == 'POST':
#         form = PostForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.save()
#             return redirect('visiter')
#     return render(request, 'new.html', {
#         'form':form,      
#     })

def new(request):
    if request.method == 'GET':
        form = PostForm()

    elif request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()         
            return redirect('visiter')

    return render(request, 'new.html', {
        'form': form,
    })

# def add_comment(request, id):
#     visit = get_object_or_404(Post, pk=id)
#     if request.method == "POST":
#         visit = CommentForm(request.Post, instance=post)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.post = visit
#             comment.save()
#             return redirect('detail', post_id=visit.id)
#         else:
#             form = CommentForm()
#         return render(request, 'add_comment.html', {
#             'form':form,
#         })
        
def add_comment(request, id):
    visit = get_object_or_404(Post, pk=id)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = visit
            comment.save()
            return redirect('detail', id)
        else:
            form = CommentForm(request.POST)
    return render(request, 'add_comment.html', {
        'form':form,
    })
