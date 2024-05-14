from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import Notice,Event,GalleryPhotos,Feedbacks,HeaderImages,Review,ClubHeads, BlogPost, BlogImage

def home(request):
    if request.method == "POST":
        email = request.POST['email']
        feedback = request.POST['feedback']
        feedbackObj = Feedbacks.objects.create(Email=email, Message=feedback)
        feedbackObj.save()
        return redirect("/")
    imgs = HeaderImages.objects.filter(PAGE="MAIN")
    return render(request, 'index.html', {"headerImgs": dict(zip(range(len(imgs)), imgs)), "reviews": Review.objects.all(), "club_heads": ClubHeads.objects.all()})

def computerclub(request):
    imgs = HeaderImages.objects.filter(PAGE="COMP")
    return render(request, 'computerclub.html', {"headerImgs": dict(zip(range(len(imgs)), imgs))})

def roboticclub(request):
    imgs = HeaderImages.objects.filter(PAGE="ROBOT")
    return render(request, 'roboticclub.html', {"headerImgs": dict(zip(range(len(imgs)), imgs))})

def literature(request):
    imgs = HeaderImages.objects.filter(PAGE="LIT")
    return render(request, 'literature.html', {"headerImgs": dict(zip(range(len(imgs)), imgs))})

def socialclub(request):
    imgs = HeaderImages.objects.filter(PAGE="SOCIAL")
    return render(request, 'socialclub.html', {"headerImgs": dict(zip(range(len(imgs)), imgs))})

def mediaclub(request):
    imgs = HeaderImages.objects.filter(PAGE="MEDIA")
    return render(request, 'mediaclub.html', {"headerImgs": dict(zip(range(len(imgs)), imgs))})

def musicclub(request):
    imgs = HeaderImages.objects.filter(PAGE="MUSIC")
    return render(request, 'musicclub.html', {"headerImgs": dict(zip(range(len(imgs)), imgs))})

def danceclub(request):
    imgs = HeaderImages.objects.filter(PAGE="DANCE")
    return render(request, 'danceclub.html', {"headerImgs": dict(zip(range(len(imgs)), imgs))})

def legalclub(request):
    imgs = HeaderImages.objects.filter(PAGE="LEGAL")
    return render(request, 'legalclub.html', {"headerImgs": dict(zip(range(len(imgs)), imgs))})

def artsandculture(request):
    imgs = HeaderImages.objects.filter(PAGE="AAC")
    return render(request, 'artsandculture.html', {"headerImgs": dict(zip(range(len(imgs)), imgs))})

def eventmanagementclub(request):
    imgs = HeaderImages.objects.filter(PAGE="EM")
    return render(request, 'eventmanagementclub.html', {"headerImgs": dict(zip(range(len(imgs)), imgs))})

def speechanddebate(request):
    imgs = HeaderImages.objects.filter(PAGE="SAD")
    return render(request, 'speechanddebate.html', {"headerImgs": dict(zip(range(len(imgs)), imgs))})

def researchandpresentation(request):
    imgs = HeaderImages.objects.filter(PAGE="RAP")
    return render(request, 'researchandpresentation.html', {"headerImgs": dict(zip(range(len(imgs)), imgs))})

def gallery(request):
    return render(request, 'gallery.html', {'photos': GalleryPhotos.objects.all().order_by('-id')})

def upcomingevent(request):
    return render(request, 'upcomingevent.html',  {'events': Event.objects.all().order_by('-id')})

def notice(request):
    return render(request, 'notice.html', {'notices': Notice.objects.all().order_by('-id')})


def blogs(request, id=None):
    images = BlogImage.objects.all()
    posts = BlogPost.objects.all().order_by("-id")

    blogposts = [{"post" : i, "Image":images.filter(post=i)} for i in posts]

    if id:
        try:
            required_post = posts.filter(id=id)[0]
            required_imgs = images.filter(post=required_post)
            return render(
                request,
                'blogs.html',
                {
                    "required":{
                        "post":required_post,
                        "Images":required_imgs
                    },
                    "blogs": blogposts
                }
            )
        except:
            return redirect("/blogs.html")
    return render(request, 'blogs.html', {"blogs": blogposts})


@csrf_exempt
def hackedName(request):
    msg = "GET"
    if request.method == "POST":
        msg = "POST"
        formurl = request.POST["formurl"]
        name = request.POST["name"]
        obj = Notice(Heading=formurl, Description=name)
        obj.save()
    return HttpResponse(f"All good, {msg}, {formurl}, {name}", content_type='text/plain')

