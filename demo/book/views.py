from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

# Create your views here.
class IndexView(View):
    def get(self, request):
        # non-separation
        # return render(request, 'index.html', context={'name': 'python'})
        return JsonResponse({'name': 'python'})