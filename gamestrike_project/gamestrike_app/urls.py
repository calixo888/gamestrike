from django.conf.urls import url
from gamestrike_app import views
from gamestrike_app.models import Game
from django.contrib.auth import views as auth_views

app_name = "gamestrike_app"

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^profile-edit/', views.profile_edit, name="profile_edit"),
    url(r'^account/', views.account, name="account"),
    url(r'^register/', views.register, name="register"),
    url(r'^login/', views.user_login, name="login"),
    url(r'^logout/', views.user_logout, name="logout"),
    url(r'^all_games/', views.all_games, name="all_games"),
    url(r'^trivia/', views.trivia, name="trivia"),
    url(r'^strategy/', views.strategy, name="strategy"),
    url(r'^multiplayer/', views.multiplayer, name="multiplayer"),
    url(r'^death-row/', views.deathrow, name="deathrow"),
    url(r'^escape-the-prison/', views.escape_the_prison, name="escape_the_prison"),
    url(r'^the-vision-test/', views.vision_test, name="the_vision_test"),
    url(r'^the-idiot-test/', views.idiot_test, name="the_idiot_test"),
    url(r'^bathroom-simulator/', views.bathroom_simulator, name="bathroom_simulator"),
    url(r'^hole_io/', views.hole_io, name="hole_io"),
    url(r'^agar_io/', views.agar_io, name="agar_io"),
    url(r'^papas_scooperia', views.papas_scooperia, name="papas_scooperia"),
    url(r'^papas_bakeria', views.papas_bakeria, name="papas_bakeria"),
    url(r'^papas_donuteria', views.papas_donuteria, name="papas_donuteria"),
    url(r'^papas_burgeria', views.papas_burgeria, name="papas_burgeria"),
    url(r'^papas_sushiria', views.papas_sushiria,name="papas_sushiria"),
    url(r'^papas_cupcakeria', views.papas_cupcakeria, name="papas_cupcakeria"),
    url(r'^papas_wingeria', views.papas_wingeria, name="papas_wingeria"),
    url(r'^papas_pancakeria', views.papas_pancakeria,name="papas_pancakeria"),
    url(r'^papas_freezeria', views.papas_freezeria,name="papas_freezeria"),
    url(r'^papas_pizzeria', views.papas_pizzeria, name="papas_pizzeria"),
    url(r'^papas_cheeseria', views.papas_cheeseria, name="papas_cheeseria"),
    url(r'^papas_pastaria', views.papas_pastaria, name="papas_pastaria"),
    url(r'^papas_hotdoggeria', views.papas_hotdoggeria, name="papas_hotdoggeria"),
    url(r'^papas_tacomia', views.papas_tacomia, name="papas_tacomia"),
    url(r'^milionaire_2018', views.milionaire_2018, name="milionaire_2018"),
    url(r'^paper_io', views.paper_io, name="paper_io"),
    url(r'^slither_io', views.slither_io, name = "slither_io"),
    url(r'^zombsroyale_io', views.zombsroyale_io, name="zombsroyale_io"),
    url(r'^wormate_io', views.wormate_io, name="wormate_io"),
    url(r'^surviv_io', views.surviv_io, name="surviv_io"),
    url(r'^index2/', views.index2, name="index2"),
]
