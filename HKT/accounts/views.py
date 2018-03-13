from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import View
from django.views import generic
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .forms import RegistrationForm


def index(request):
    return HttpResponse("its the front page")
# here u have to return a template as front page.


class RegisterView(View):
	form_class = RegistrationForm
	template_name = 'register.html'

	def get(self, request):
		form = self.form_class(None)
		print("hbf")
		return render(request, self.template_name, {'form': form})

	def post(self,request):
		form=self.form_class(request.POST)
		if form.is_valid():
			uid=form.save(commit=False)
		return render(request, self.template_name, {'form': form})









