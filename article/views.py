from django.shortcuts import render

import models
from django.contrib.syndication.views import Feed

# Create your views here.
def home(request):
    post_list = models.Article.objects.all()
    return render(request, 'home.html', {'post_list' : post_list})
def about(request):
	return render(request, 'about.html')
def detail(request, id):
    try:
        post = models.Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    print "detail", id
    return render(request, 'post.html', {'post' : post})
def archives(request):
	try:
		post_list = models.Article.objects.all()
	except models.Article.DoesNotExist:
		return Http404
	return render(request, 'archives.html', {'post_list':post_list,
		'error':False})
def search_tag(request, tag) :
    try:
        post_list = models.Article.objects.filter(category__iexact = tag) #contains
    except models.Article.DoesNotExist :
        raise Http404
    return render(request, 'tag.html', {'post_list' : post_list})

def blog_search(request):
	if 's' in request.GET:
		s = request.GET['s']
		if not s:
			return render(request, 'home.html')
		else:
			post_list = models.Article.objects.filter(title=s)
			status = True
			if len(post_list) > 0:
				status = False
			return render(request, 'archives.html', {'post_list':post_list, 'error':status})
		return redirect('/')

class RSSFeed(Feed) :
    title = "RSS feed - article"
    link = "feeds/posts/"
    description = "RSS feed - blog posts"

    def items(self):
        return models.Article.objects.order_by('-date_time')

    def item_title(self, item):
        return item.title

    def item_pubdate(self, item):
        return item.date_time

    def item_description(self, item):
        return item.content