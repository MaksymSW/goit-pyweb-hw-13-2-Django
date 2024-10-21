from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Count

from .models import Author, Tag, Quote
from .forms import TagForm, AuthorForm, QuoteForm

from django.contrib.auth.decorators import login_required

def main(request, page = 1):
    quotes = Quote.objects.all()
    top_tags = Tag.objects.annotate(num_posts=Count('posts')).order_by('-num_posts')[:10]
    print(top_tags)
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
   
    return render(request,'quotes/index.html', context={'quotes':quotes_on_page, 'top_tags': top_tags})

def detail(request, quote_id):
    author = get_object_or_404(Author, pk=quote_id)
    return render(request, 'quotes/detail.html', {"author": author})

def tags(request, tag_id):
    tag = get_object_or_404(Tag, pk=tag_id)
    quotes = Quote.objects.filter(tags=tag)
    return render(request, 'quotes/tags.html', context={"quotes": quotes, "tag": tag})

@login_required
def addtag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotes:root')
        else:
            return render(request, 'quotes/addtag.html', {'form': form})

    return render(request, 'quotes/addtag.html', {'form': TagForm()})

@login_required
def addauthor(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotes:root')
        else:
            return render(request, 'quotes/addauthor.html', {'form': form})

    return render(request, 'quotes/addauthor.html', {'form': AuthorForm()})


@login_required
def addquote(request):
    tags = Tag.objects.all()
    authors = Author.objects.all()

    if request.method == 'POST':
        form = QuoteForm(request.POST)

        if form.is_valid():
            new_note = form.save()

            choice_tags = Tag.objects.filter(name__in=request.POST.getlist('tags'))
            choice_author = Author.objects.filter(fullname__in=request.POST.getlist('authorid'))
            for tag in choice_tags.iterator():
                print(tag)
                new_note.tags.add(tag)
            print(choice_author)
            for author in choice_author.iterator():
                print(author)
                print(author.id)
                print(new_note.author)
                new_note.author = author
                print(new_note.author)
                print(new_note.author_id)


            return redirect(to='quotes:root')
        else:
            return render(request, 'quotes/addquote.html', {"tags": tags, "authors": authors, 'form': form})

    return render(request, 'quotes/addquote.html', {"tags": tags, "authors": authors,'form': QuoteForm()})
