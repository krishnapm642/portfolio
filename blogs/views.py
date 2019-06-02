
from django.shortcuts import render, get_object_or_404
from .models import BlogPost
from marketing.models import SignUp
from django.core.paginator import Paginator
from django.db.models import Count, Q


# Create your views here.
def get_category_count():
	categoryset = BlogPost.objects.values('categories__title').annotate(Count('categories__title'))
	return categoryset

# Create your views here.
def index(request):
	featured = BlogPost.objects.filter(featured = True)
	latest = BlogPost.objects.order_by('-timestamp')[0:3]

	if request.method == 'POST':
		Email = request.POST['email']
		sighup = SignUp()
		sighup.email = Email
		sighup.save()

	context = {
		'object_list' : featured,
		'latest':latest
	}
	return render(request, 'blogs/index.html', context)

def blog(request):
	category_count = get_category_count()
	most_recent_post = BlogPost.objects.order_by('-timestamp')[:3]
	queryset = BlogPost.objects.all()
	paginator = Paginator(queryset, 4)

	page = request.GET.get('page')

	try:
		page_list = paginator.get_page(page)
	except PageNotAnInteger:
		page_list = paginator.get_page(1)
	except EmptyPage:
		page_list = paginator.get_page(Paginator.num_pages)

	context = {
		'object_list' : page_list,
		'recent_post' : most_recent_post,
		'category_count' : category_count
	}
	return render(request, 'blogs/blog.html', context)

def post(request, slug):
	category_count = get_category_count()
	most_recent_post = BlogPost.objects.order_by('-timestamp')[:3]
	object_list = get_object_or_404(BlogPost , slug = slug)

	context = {
		'recent_post' : most_recent_post,
		'category_count' : category_count,
		'object_list': object_list
	}
	return render(request, 'blogs/post.html', context)


def search(request):
	query  = BlogPost.objects.all()
	sqarchquery = request.GET.get('q')
	if sqarchquery:
		queryset  = query.filter(
				Q(title__icontains =  sqarchquery) |
				Q(overview__icontains = sqarchquery)
			).distinct()
		context = {
			'queryset' : queryset
		}
		return render(request, 'blogs/search.html', context)

