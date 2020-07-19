from django.shortcuts import render, redirect
from article.forms import ArticleForm
from article.models import Article


def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    else:
        form = ArticleForm()

    return render(request, 'article/create.html', {'form': form})


def update(request, id):
    pass


def delete(request, id):
    article = Article.objects.get(id = id)
    article.delete()
    return redirect('article.view')