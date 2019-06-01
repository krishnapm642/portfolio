from django.shortcuts import render
from django.views.generic import ListView
from .models import posts

# Create your views here.

class IndexView(ListView):
	queryset = posts.objects.all()
	template_name = 'posts/index.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context


def contactview(request):
	if(request.method == 'POST'):
		email = request.POST['email']
		name = request.POST['name']
		content = request.POST['message']
		print(email+" "+name+" "+content)
		context = {
			'success' : "The mesage has been send",
		}
		return render(request, 'posts/contact.html', context)

	return render(request, 'posts/contact.html')
