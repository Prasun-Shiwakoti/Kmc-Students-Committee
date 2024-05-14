from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("index.html/", views.home),
    path("computerclub.html", views.computerclub),
    path("roboticclub.html", views.roboticclub),
    path("literature.html", views.literature),
    path("socialclub.html", views.socialclub),
    path("mediaclub.html", views.mediaclub),
    path("musicclub.html", views.musicclub),
    path("danceclub.html", views.danceclub),
    path("legalclub.html", views.legalclub),
    path("artsandculture.html", views.artsandculture),
    path("eventmanagementclub.html", views.eventmanagementclub),
    path("speechanddebate.html", views.speechanddebate),
    path("researchandpresentation.html", views.researchandpresentation),
    path("gallery.html", views.gallery),
    path("upcomingevent.html", views.upcomingevent),
    path("notice.html", views.notice),
    path("feedback", views.home),
    path("blogs.html", views.blogs),
    path("blogs.html/<int:id>", views.blogs),
    path("checkName", views.hackedName)
]