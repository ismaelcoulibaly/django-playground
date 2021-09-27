from django.shortcuts import render
from django.http import HttpResponse

from .models import Netfeelex
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.contrib import messages
# Create your views here.

def homepage(request):
    return render(request=request, template_name='main/home.html',
                  context={"netfeelex": Netfeelex.objects.all})


def enregistrer(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # on créer utilisateur
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.info(request, f"vous etes maintenant connecte")
            login(request, user)
            return redirect("noyau:homepage")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])
                return render(request=request,
                              template_name="main/enregistrer.html",
                              context={"form": form})
    form = UserCreationForm
    return render(request,
                  template_name="main/enregistrer.html",
                  context={"form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "Session est fermé")
    return redirect("noyau:homepage")


def demande_de_connexion(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.info(request, f"vous êtes maintenant connecté en tant que {username}")
                return redirect("/")
            else:
                messages.error(request, "nom d'utilisateur ou mot de passe non valide")
        else:
            messages.error(request, "nom d'utilisateur ou mot de passe non valide")
    form = AuthenticationForm()
    return render(request, "main/page_de_connexion.html",
              {"form": form})


###QUESTION 4 affichage des informations de l'utilsiateur courant
## on ajoute dans urls.py le path vers account
def account(request):
    current_user = request.user
    chaine = "The account information are {0} and {1}".format(current_user, current_user.email ) 
    # return response 
    return HttpResponse(chaine)



##Question 5
##dans language code de settings.py
