from django.views.generic import ListView, DetailView, FormView, UpdateView
from .models import Announce
from .form import AnnounceForm, ContactForm, EditForm
from .utility import *
from django.urls import resolve, reverse_lazy
from django.shortcuts import render, redirect

# ------------------------------------------------

class HomeView(ListView):
    template_name = 'goodcorner/home.html'
    context_object_name = 'announce_list'

    def get_queryset(self):
        return Announce.objects.order_by('-creation_date')

# ------------------------------------------------

class AnnounceView(DetailView):
    template_name = 'goodcorner/announce.html'
    model = Announce

class CreateAnnounceView(FormView):
    template_name = 'goodcorner/create.html'
    form_class = AnnounceForm
    success_url = '/'
    
    def form_valid(self, form):
        username = form.cleaned_data['surname']
        email = form.cleaned_data['email']
        title = form.cleaned_data['title']
        description = form.cleaned_data['description']

        user = createOrGetUser(username, email)
        announce = createAnnounce(title, description, user)
        sendCreationMail(user, announce)

        return super(CreateAnnounceView, self).form_valid(form)

# ------------------------------------------------

def contact(request, pk):
    announce = Announce.objects.get(pk = pk)
    if(request.method == 'GET'):
        form = ContactForm
        return render(request, 'goodcorner/contact.html', {'announce': announce, 'form': form})
    else:
        if(request.method == 'POST'):
            email = request.POST['email']
            message = request.POST['message']
            sendContactMail(email, message, announce)
            return redirect('goodcorner:announce', pk)
    redirect('goodcorner:home')

# ------------------------------------------------

def edit(request, hashurl):
    announce = Announce.objects.get(hashurl = hashurl)
    if(request.method == 'GET'):
        form = EditForm(initial={'title':announce.title, 'description':announce.description})
        return render(request, 'goodcorner/edit.html', {'announce': announce, 'form': form})
    else:
        if(request.method == 'POST'):
            newTitle = request.POST['title']
            newDescription = request.POST['description']
            updateAnnounce(announce.pk, newTitle, newDescription)
            return redirect('goodcorner:announce', announce.pk)
    return redirect('goodcorner:home')

# ------------------------------------------------

def delete(request, hashurl):
    announce = Announce.objects.filter(hashurl=hashurl).delete()
    return redirect('goodcorner:home')
