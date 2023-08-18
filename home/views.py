from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

class BookListView(TemplateView):

    def get(self, *args, **kwargs):
        self.users = []
        self.context = {'users':self.users}
        return render( self.request, 'index.html', self.context )