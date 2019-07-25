# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from gamestrike_app.models import Game, UserProfile
from django.contrib.auth.models import User
from gamestrike_app import forms
from gamestrike_app import models
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from PIL import Image
import os

def crop_images():
    for file in os.listdir(os.path.abspath("media/profile_pictures")):
        try:
            filepath = os.path.abspath("media/profile_pictures") + "/" + file
            img = Image.open(filepath)
            width, height = img.size
            crop_size = min(img.size)
            left = (width - crop_size)/2
            top = (height - crop_size)/2
            right = (width + crop_size)/2
            bottom = (height + crop_size)/2

            img = img.crop((left, top, right, bottom))
            img.save(filepath)
        except Exception as e:
            print(e)
#################
## ERROR PAGES ##
#################

def handler404(request, exception, template_name="404.html"):
    response = render_to_response("404.html")
    response.status_code = 404
    return response

###############
## FUNCTIONS ##
###############

def add_point(name):
    game = Game.objects.get(name=name)
    game.points += 1
    game.save()

def popular():
    game_objects = Game.objects.all()
    game_points = [i.points for i in game_objects]
    game_objects_copy = list(game_objects)[:]
    most_popular = []
    for i in range(5):
        most_popular.append(game_objects_copy[game_points.index(max(game_points))])
        game_points.remove(max(game_points))
    most_popular_images = ["/static/gamestrike_app/thumbnails/" + most_popular[i].image_url for i in range(len(most_popular))]
    most_popular_names = [most_popular[i].name for i in range(len(most_popular))]
    most_popular_descriptions = [most_popular[i].description for i in range(len(most_popular))]
    most_popular_urls = [most_popular[i].url for i in range(len(most_popular))]
    most_popular = {"most_popular": [list(a) for a in zip(most_popular_names, most_popular_images, most_popular_descriptions, most_popular_urls)]}
    return most_popular

def recent():
    game_objects = Game.objects.all()
    game_objects_copy = list(game_objects)[:]
    date = [int(x) for x in datetime.datetime.today().strftime('%Y-%m-%d').split("-")]
    days = [datetime.date(date[0], date[1], date[2]) - i.date for i in game_objects]
    days = [i.days for i in days]
    most_recent = []
    for i in range(5):
        most_recent.append(game_objects_copy[days.index(min(days))])
        game_objects_copy.remove(game_objects_copy[days.index(min(days))])
        days.remove(min(days))
    most_recent_images = ["/static/gamestrike_app/thumbnails/" + most_recent[i].image_url for i in range(len(most_recent))]
    most_recent_names = [most_recent[i].name for i in range(len(most_recent))]
    most_recent_descriptions = [most_recent[i].description for i in range(len(most_recent))]
    most_recent_urls = [most_recent[i].url for i in range(len(most_recent))]
    most_recent = {"most_recent": [list(a) for a in zip(most_recent_names, most_recent_images, most_recent_descriptions, most_recent_urls)]}
    return most_recent

def feature():
    featured = Game.objects.all()[:5]
    featured_images = ["/static/gamestrike_app/thumbnails/" + featured[i].image_url for i in range(len(featured))]
    featured_names = [featured[i].name for i in range(len(featured))]
    featured_descriptions = [featured[i].description for i in range(len(featured))]
    featured_urls = [featured[i].url for i in range(len(featured))]
    featured = {"featured": [list(a) for a in zip(featured_names, featured_images, featured_descriptions, featured_urls)]}
    return featured

def all():
    objects = Game.objects.all()
    images = ["/static/gamestrike_app/thumbnails/" + objects[i].image_url for i in range(len(objects))]
    names = [objects[i].name for i in range(len(objects))]
    descriptions = [objects[i].description for i in range(len(objects))]
    urls = [objects[i].url for i in range(len(objects))]
    objects = {"objects": [list(a) for a in zip(names, images, descriptions, urls)]}
    return objects

def urls():
    objects = Game.objects.all()
    return {"urls": {objects[i].name: objects[i].url for i in range(len(objects))}}

#################
## INDEX PAGES ##
#################

def profile_edit(request):
    edited = False
    profile = models.UserProfile.objects.get(user=User.objects.get(username=request.user.username))

    if request.method == "POST":
        user_form = forms.ProfileEditForm(request.POST)
        profile_form = forms.UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = request.user

            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.email = request.POST.get('email')
            user.save()

            profile.description = request.POST.get('description')
            profile.user = user
            profile.place = user

            if 'profile_picture' in request.FILES: # checking if they provided picture
                profile.profile_picture = request.FILES['profile_picture']

            profile.save()

            edited = True
            crop_images()
            return HttpResponseRedirect("/")

        else:
            print("Profile edit error")
            print(user_form.errors)
            print(profile_form.errors)
            return HttpResponse("You must fill out the form correctly")
    else:
        user_form = forms.ProfileEditForm(initial={"first_name": request.user.first_name, "last_name": request.user.last_name, "email": request.user.email})
        profile_form = forms.UserProfileForm(initial={"description": profile.description, "profile_picture": profile.profile_picture})

    return render(request, "gamestrike_app/profile_edit.html", context={'edited': edited, "user_form": user_form, "profile_form": profile_form})

def register(request):
    registered = False

    if request.method == "POST":
        user_form = forms.UserForm(request.POST)
        profile_form = forms.UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.place = user

            if 'profile_picture' in request.FILES: # checking if they provided picture
                profile.profile_picture = request.FILES['profile_picture']

            profile.save()

            registered = True
            crop_images()
            return HttpResponseRedirect("/")

        else:
            if not user_form.errors:
                return render(request, "gamestrike_app/error.html", context={"errors": profile_form.errors})
            elif not profile_form.errors:
                return render(request, "gamestrike_app/error.html", context={"errors": user_form.errors})
            else:
                return render(request, "gamestrike_app/error.html", context={"errors": user_form.errors + profile_form.errors})
    else:
        user_form = forms.UserForm()
        profile_form = forms.UserProfileForm()

    return render(request, "gamestrike_app/register.html", context={'registered': registered, "user_form": user_form, "profile_form": profile_form})

@login_required()
def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/")

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect("/")
            else:
                return HttpResponse("Your account has been deactivated. Please register again.")
        else:
            return HttpResponse("Invalid login credentails. Please try again.")
    else:
        return render(request, "gamestrike_app/login.html")

@login_required(login_url="/login/")
def account(request):
    profile = models.UserProfile.objects.get(user=User.objects.get(username=request.user.username))
    return render(request, "gamestrike_app/account.html", context={"profile": profile})

def index(request):
    most_popular = popular()
    most_recent = recent()
    featured = feature()
    return render(request, "gamestrike_app/index.html", context={"most_popular": most_popular, "most_recent": most_recent, "featured": featured})

def index2(request):
    return render(request, "gamestrike_app/index2.html", context=None)

def all_games(request):
    objects = Game.objects.all()
    game_list = [objects[i:i+5] for i in range(0, len(objects), 5)]
    return render(request, "gamestrike_app/all_games.html", context={"objects": game_list})

def base(request):
    return render(request, "gamestrike_app/base.html", context=url())

###########
## TYPES ##
###########

def trivia(request):
    trivia_games = Game.objects.filter(type="Trivia")
    game_list = [trivia_games[i:i+5] for i in range(0, len(trivia_games), 5)]
    return render(request, "gamestrike_app/trivia.html", context={"games": game_list})

def strategy(request):
    strategy_games = Game.objects.filter(type="Strategy")
    game_list = [strategy_games[i:i+5] for i in range(0, len(strategy_games), 5)]
    return render(request, "gamestrike_app/strategy.html", context={"games": game_list})

def multiplayer(request):
    multiplayer_games = Game.objects.filter(type="Multiplayer")
    game_list = [multiplayer_games[i:i+5] for i in range(0, len(multiplayer_games), 5)]
    return render(request, "gamestrike_app/multiplayer.html", context={"games": game_list})

###########
## GAMES ##
###########

@login_required(login_url="/login/")
def deathrow(request):
    name = "Death Row"
    most_popular = popular()
    add_point(name)
    return render(request, "gamestrike_app/games/deathrow.html", context={"most_popular": most_popular, "game": Game.objects.get(name=name)})

@login_required(login_url="/login/")
def escape_the_prison(request):
    name = "Escape the Prison"
    most_popular = popular()
    add_point(name)
    return render(request, "gamestrike_app/games/escape_the_prison.html", context={"most_popular": most_popular, "game": Game.objects.get(name=name)})

@login_required(login_url="/login/")
def vision_test(request):
    name = "The Vision Test"
    most_popular = popular()
    add_point(name)
    return render(request, "gamestrike_app/games/vision_test.html", context={"most_popular": most_popular, "game": Game.objects.get(name=name)})

@login_required(login_url="/login/")
def idiot_test(request):
    name = "The Idiot Test 6"
    most_popular = popular()
    add_point(name)
    return render(request, "gamestrike_app/games/idiot_test.html", context={"most_popular": most_popular, "game": Game.objects.get(name=name)})

@login_required(login_url="/login/")
def hole_io(request):
    name = "Hole.io"
    most_popular = popular()
    add_point(name)
    return render(request, "gamestrike_app/games/hole_io.html", context={"most_popular": most_popular, "game": Game.objects.get(name=name)})

@login_required(login_url="/login/")
def agar_io(request):
    name = "Agar.io"
    most_popular = popular()
    add_point(name)
    return render(request, "gamestrike_app/games/agar_io.html", context={"most_popular": most_popular, "game": Game.objects.get(name=name)})

@login_required(login_url="/login/")
def papas_scooperia(request):
    name = "Papa's Scooperia"
    most_popular = popular()
    add_point(name)
    return render(request, "gamestrike_app/games/papas_scooperia.html", context={"most_popular": most_popular, "game": Game.objects.get(name=name)})

@login_required(login_url="/login/")
def papas_bakeria(request):
    name = "Papa's Bakeria"
    most_popular = popular()
    add_point(name)
    return render(request, "gamestrike_app/games/papas_bakeria.html", context={"most_popular": most_popular, "game": Game.objects.get(name=name)})

@login_required(login_url="/login/")
def papas_donuteria(request):
    name = "Papa's Donuteria"
    most_popular = popular()
    add_point(name)
    return render(request, "gamestrike_app/games/papas_donuteria.html",context={"most_popular": most_popular, "game": Game.objects.get(name=name)})

@login_required(login_url="/login/")
def papas_burgeria(request):
    name = "Papa's Burgeria"
    most_popular = popular()
    add_point(name)
    return render(request, "gamestrike_app/games/papas_burgeria.html", context={"most_popular": most_popular, "game": Game.objects.get(name=name)})

@login_required(login_url="/login/")
def papas_sushiria(request):
    name = "Papa's Sushiria"
    most_popular = popular()
    add_point(name)
    return render(request, "gamestrike_app/games/papas_sushiria.html", context={"most_popular": most_popular, "game": Game.objects.get(name=name)})

@login_required(login_url="/login/")
def papas_cupcakeria(request):
    name = "Papa's Cupcakeria"
    most_popular = popular()
    add_point(name)
    return render(request, "gamestrike_app/games/papas_cupcakeria.html", context={"most_popular": most_popular, "game": Game.objects.get(name=name)})

@login_required(login_url="/login/")
def papas_wingeria(request):
    name = "Papa's Wingeria"
    most_popular = popular()
    add_point(name)
    return render(request, "gamestrike_app/games/papas_wingeria.html", context={"most_popular": most_popular, "game": Game.objects.get(name=name)})

@login_required(login_url="/login/")
def papas_pancakeria(request):
    name = "Papa's Pancakeria"
    most_popular = popular()
    add_point(name)
    return render(request, "gamestrike_app/games/papas_pancakeria.html", context={"most_popular": most_popular, "game": Game.objects.get(name=name)})

@login_required(login_url="/login/")
def papas_freezeria(request):
    name = "Papa's Freezeria"
    most_popular = popular()
    add_point(name)
    return render(request, "gamestrike_app/game.html",context={"most_popular": most_popular, "game": Game.objects.get(name=name)})

@login_required(login_url="/login/")
def papas_pizzeria(request):
    name = "Papa's Pizzeria"
    most_popular = popular()
    add_point(name)
    return render(request, "gamestrike_app/games/papas_pizzeria.html", context={"most_popular": most_popular, "game": Game.objects.get(name=name)})

@login_required(login_url="/login/")
def papas_cheeseria(request):
    name = "Papa's Cheeseria"
    most_popular = popular()
    add_point(name)
    return render(request, "gamestrike_app/games/papas_cheeseria.html", context={"most_popular": most_popular, "game": Game.objects.get(name=name)})

@login_required(login_url="/login/")
def papas_pastaria(request):
    name = "Papa's Pastaria"
    most_popular = popular()
    add_point(name)
    return render(request, "gamestrike_app/games/papas_pastaria.html", context={"most_popular": most_popular, "game": Game.objects.get(name=name)})

@login_required(login_url="/login/")
def papas_hotdoggeria(request):
    name = "Papa's Hot Doggeria"
    most_popular = popular()
    add_point(name)
    return render(request, "gamestrike_app/games/papas_hotdoggeria.html", context={"most_popular": most_popular, "game": Game.objects.get(name=name)})

@login_required(login_url="/login/")
def papas_tacomia(request):
    name = "Papa's Taco Mia!"
    most_popular = popular()
    add_point(name)
    return render(request, "gamestrike_app/games/papas_tacomia.html", context={"most_popular": most_popular, "game": Game.objects.get(name=name)})

@login_required(login_url="/login/")
def milionaire_2018(request):
    name = "Millionaire 2018"
    most_popular = popular()
    add_point(name)
    return render(request, "gamestrike_app/games/milionaire_2018.html", context={"most_popular": most_popular, "game": Game.objects.get(name=name)})

@login_required(login_url="/login/")
def paper_io(request):
    name = "Paper.io"
    most_popular = popular()
    add_point(name)
    return render(request, "gamestrike_app/game.html", context={"most_popular": most_popular, "game": Game.objects.get(name=name)})

@login_required(login_url="/login/")
def slither_io(request):
    name = "Slither.io"
    most_popular = popular()
    add_point(name)
    return render(request, "gamestrike_app/games/slither_io.html", context={"most_popular": most_popular, "game": Game.objects.get(name=name)})

@login_required(login_url="/login/")
def wormate_io(request):
    name = "Wormate.io"
    most_popular = popular()
    add_point(name)
    return render(request, "gamestrike_app/games/wormate_io.html", context={"most_popular": most_popular, "game": Game.objects.get(name=name)})

@login_required(login_url="/login/")
def surviv_io(request):
    name = "Surviv.io"
    most_popular = popular()
    add_point(name)
    return render(request, "gamestrike_app/games/surviv_io.html", context={"most_popular": most_popular, "game": Game.objects.get(name=name)})

@login_required(login_url="/login/")
def zombsroyale_io(request):
    name = "ZombsRoyale.io"
    most_popular = popular()
    add_point(name)
    return render(request, "gamestrike_app/games/zombsroyale_io.html", context={"most_popular": most_popular, "game": Game.objects.get(name=name)})

@login_required(login_url="/login/")
def bathroom_simulator(request):
    name = "Bathroom Simulator"
    most_popular = popular()
    add_point(name)
    return render(request, "gamestrike_app/games/bathroom_simulator.html", context={"most_popular": most_popular, "game": Game.objects.get(name=name)})
