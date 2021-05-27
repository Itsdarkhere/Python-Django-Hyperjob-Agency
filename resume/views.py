from django.shortcuts import render
from django.views import View


class Main(View):
    def get(self, request):
        return render(request, 'resume/main.html')


class Resumes(View):
    def get(self, request):
        return render(request, 'resume/resumes.html')