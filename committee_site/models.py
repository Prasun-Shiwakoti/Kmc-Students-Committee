from django.db import models
# Create your models here.


class ClubHeads(models.Model):
    id = models.AutoField(primary_key=True)
    photo = models.ImageField(upload_to="ClubHeads")
    name = models.CharField(max_length=100, default="")
    designation = models.CharField(
        max_length=20,
        choices=[
            ("E", "Executive"),
            ("P", "Club President"),
        ],
        default="E",
    )
    club = models.CharField(max_length=100, default="")
    facebook_link = models.CharField(max_length=1000, default="", blank=True)
    instagram_link = models.CharField(max_length=1000, default="", blank=True)
    linkedin_link = models.CharField(max_length=1000, default="", blank=True)

    def __str__(self):
        return self.club


class Notice(models.Model):
    id = models.AutoField(primary_key=True)
    Heading = models.CharField(max_length=100, default="")
    Description = models.TextField(default="")
    Link = models.URLField(blank=True)

    def __str__(self):
        return self.Heading


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    Heading = models.CharField(max_length=100)
    Description = models.TextField()

    def __str__(self):
        return self.Heading


class GalleryPhotos(models.Model):
    id = models.AutoField(primary_key=True)
    Image = models.ImageField(upload_to="Photos")


class Feedbacks(models.Model):
    id = models.AutoField(primary_key=True)
    Email = models.EmailField(max_length=254)
    Message = models.TextField(default="")

    def __str__(self):
        return self.Message


class HeaderImages(models.Model):
    id = models.AutoField(primary_key=True)

    PAGE_CHOICES = [
        ("MAIN", "HOME PAGE"),
        ("AAC", "ART AND CULTURAL CLUB"),
        ("COMP", "COMPUTER CLUB"),
        ("DANCE", "DANCE CLUB"),
        ("EM", "EVENT MANAGEMENT CLUB"),
        ("LEGAL", "LEGAL CLUB"),
        ("LIT", "LITERATURE CLUB"),
        ("MEDIA", "MEDIA CLUB"),
        ("MUSIC", "MUSIC CLUB"),
        ("RAP", "RESEARCH AND PRESENTATION CLUB"),
        ("ROBOT", "ROBOTICS CLUB"),
        ("SOCIAL", "SOCIAL CLUB"),
        ("SAD", "SPEECH AND DEBATE CLUB"),
    ]

    PAGE = models.CharField(
        max_length=10,
        choices=PAGE_CHOICES,
        default="MAIN",
    )

    Image = models.ImageField(upload_to="HeaderImages")

    def __str__(self):
        return self.PAGE


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100, default="")
    Message = models.TextField(default="")
    Stars = models.IntegerField()
    Image = models.ImageField(upload_to="FeedbackImages")

    def __str__(self):
        return self.Name


class BlogPost(models.Model):
    id = models.AutoField(primary_key=True)
    Publisher = models.CharField(max_length=100, default=" ")
    Title = models.CharField(max_length=500, default=" ")
    PublishDate = models.DateField(auto_now_add=True, blank=True)
    Likes = 0
    Content = models.TextField(default=" ", blank=True)

    def __str__(self):
        return self.Title


class BlogImage(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    Image = models.ImageField(upload_to="BlogImages",blank=True)