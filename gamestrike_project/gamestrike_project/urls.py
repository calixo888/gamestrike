"""gamestrike_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from gamestrike_app.models import Game
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

handler404 = 'gamestrike_app.views.handler404'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('', include('gamestrike_app.urls')),
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

filenames = ["DeathRow.PNG", "EscapeThePrison.PNG", "VisionTest.PNG", "IdiotTest6.PNG", "BathroomSimulator.PNG", "Holeio.PNG",
             "Agario.PNG", "Scooperia.PNG", "Bakeria.PNG", "Donuteria.PNG", "Burgeria.PNG", "Sushiria.PNG", "Cupcakeria.PNG",
             "Wingeria.PNG", "Pancakeria.PNG", "Freezeria.PNG", "Pizzeria.PNG", "Cheeseria.PNG", "Pastaria.PNG", "HotDoggeria.PNG",
             "Taco Mia.PNG", "Milionaire2018.PNG", "Paperio.PNG", "Slitherio.PNG", "ZombsRoyaleio.PNG", "Wormateio.PNG", "Survivio.PNG"]

games = ["death-row/", "escape-the-prison/", "the-vision-test/", "the-idiot-test/", "bathroom-simulator/", "hole_io/", "agar_io",
         "papas_scooperia", "papas_bakeria", "papas_donuteria", "papas_burgeria", "papas_sushiria", "papas_cupcakeria",
         "papas_wingeria", "papas_pancakeria", "papas_freezeria", "papas_pizzeria", "papas_cheeseria", "papas_pastaria",
         "papas_hotdoggeria", "papas_tacomia", "milionaire_2018", "paper_io", "slither_io", "zombsroyale_io", "wormate_io",
         "surviv_io"]

keyval_dict = dict(zip(games, filenames))

domain = "http://127.0.0.1:8000/"

for i in keyval_dict.keys():
    game = Game.objects.get(image_url=keyval_dict[i])
    game.url = domain + i
    game.save()
