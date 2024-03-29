from django.shortcuts import render, HttpResponse, redirect
from .models import Contestants
import os

# Create your views here.

adminpassword = "hello"

def index(request):
    return render(request, "index.html")


def login(request):

    if request.method == "POST":
        password = request.POST.get("password")

        if password == adminpassword:
            request.session["logged-in"] = True
            return redirect("/admin")

        else:
            return render(request, "admin.html", {"wrong":True})

    if request.session.get("logged-in"):
        return redirect("/admin")

    return render(request, "admin-login.html")


def admin(request):

    if not request.session.get("logged-in"):
        return redirect("/admin/login")

    contestants = Contestants.objects.all()

    return render(request, "admin.html", {"contestants":contestants, "open":request.session.get("open")})



def addContenstant(request):

    if request.method == "POST":
        name = request.POST.get("name").title()
        position = request.POST.get("position").title()
        photo = request.FILES.get("image")

        try:
            res = Contestants.objects.get(name=name)
            return render(request, "add.html", {"exists":True})

        except:
            pass

        last = None

        try:
            last = Contestants.objects.all().last().id + 1
        except:
            last = 1

        contestant = Contestants.objects.create(id=last, name=name, position=position, votes=0)

        contestant.save()

        contestantinst = Contestants.objects.get(id=last)

        contestantinst.photo = photo

        contestantinst.save()

        return render(request, "add.html", {"added":True})


    if not request.session.get("logged-in"):
        return redirect("/admin")

    return render(request, "add.html")

def delete(request):
    if request.method == "POST":
        id = int(request.POST.get('id'))

        res = Contestants.objects.get(id=id)

        current = os.getcwd()

        print(current)

        os.remove(current + res.photo.url)

        res.delete()

        return redirect("/admin")


def votingForm(request):
    headboys = Contestants.objects.all().filter(position="Headboy")
    headgirls = Contestants.objects.all().filter(position="Headgirl")
    sportsboys = Contestants.objects.all().filter(position="Sports Captain Boy")
    sportsgirls = Contestants.objects.all().filter(position="Sports Captain Girl")
    dheadboys = Contestants.objects.all().filter(position="Deputy Headboy")
    dheadgirls = Contestants.objects.all().filter(position="Deputy Headgirl")
    dsportsboys = Contestants.objects.all().filter(position="Deputy Sports Captain Boy")
    dsportsgirls = Contestants.objects.all().filter(position="Deputy Sports Captain Girl")

    return render(request, "vote.html", {"headboys" : headboys, "headgirls" : headgirls, "sportsboys" : sportsboys, "sportsgirls" : sportsgirls, "dheadboys" : dheadboys, "dheadgirls" : dheadgirls, "dsportsboys" : dsportsboys, "dsportsgirls" : dsportsgirls})

def votingFormMobile(request):
    headboys = Contestants.objects.all().filter(position="Headboy")
    headgirls = Contestants.objects.all().filter(position="Headgirl")
    sportsboys = Contestants.objects.all().filter(position="Sports Captain Boy")
    sportsgirls = Contestants.objects.all().filter(position="Sports Captain Girl")
    dheadboys = Contestants.objects.all().filter(position="Deputy Headboy")
    dheadgirls = Contestants.objects.all().filter(position="Deputy Headgirl")
    dsportsboys = Contestants.objects.all().filter(position="Deputy Sports Captain Boy")
    dsportsgirls = Contestants.objects.all().filter(position="Deputy Sports Captain Girl")

    return render(request, "vote-mobile.html", {"headboys" : headboys, "headgirls" : headgirls, "sportsboys" : sportsboys, "sportsgirls" : sportsgirls, "dheadboys" : dheadboys, "dheadgirls" : dheadgirls, "dsportsboys" : dsportsboys, "dsportsgirls" : dsportsgirls})

def submitVote(request):
    if request.method == 'POST':
        headboy = request.POST.get("headboy")
        headgirl = request.POST.get("headgirl")
        sportsboy = request.POST.get("sportsboy")
        sportsgirl = request.POST.get("sportsgirl")
        dheadboy = request.POST.get("dheadboy")
        dheadgirl = request.POST.get("dheadgirl")
        dsportsboy = request.POST.get("dsportsboy")
        dsportsgirl = request.POST.get("dsportsgirl")

        if not headboy or not headgirl or not sportsboy or not sportsgirl or not dheadboy or not dheadgirl or not dsportsboy or not dsportsgirl:
            return render(request, "message.html")

        if not request.session.get("open"):
            return render(request, "message.html", {"error":"closed"})

        headboyinst = Contestants.objects.get(name=headboy)
        headgirlinst = Contestants.objects.get(name=headgirl)
        sportsboyinst = Contestants.objects.get(name=sportsboy)
        sportsgirlinst = Contestants.objects.get(name=sportsgirl)
        dheadboyinst = Contestants.objects.get(name=dheadboy)
        dheadgirlinst = Contestants.objects.get(name=dheadgirl)
        dsportsboyinst = Contestants.objects.get(name=dsportsboy)
        dsportsgirlinst = Contestants.objects.get(name=dsportsgirl)

        headboyinst.votes += 1
        headgirlinst.votes += 1
        sportsboyinst.votes += 1
        sportsgirlinst.votes += 1
        dheadboyinst.votes += 1
        dheadgirlinst.votes += 1
        dsportsboyinst.votes += 1
        dsportsgirlinst.votes += 1

        headboyinst.save()
        headgirlinst.save()
        sportsboyinst.save()
        sportsgirlinst.save()
        dheadboyinst.save()
        dheadgirlinst.save()
        dsportsboyinst.save()
        dsportsgirlinst.save()

        return render(request, "thank you.html")

    return HttpResponse("Invalid request")


def resetVotes(request):
    if request.method == "POST":
        res = Contestants.objects.all()

        for i in res:
            i.votes = 0
            i.save()

        return redirect("/admin")

    return redirect("/admin")


def deleteAll(request):
    if request.method == "POST":
        res = Contestants.objects.all()

        current = os.getcwd()

        for i in res:
            os.remove(current + i.photo.url)
            i.delete()

        return redirect("/admin")

def openVoting(request):
    request.session["open"] = True

    return redirect("/admin")

def closeVoting(request):
    request.session["open"] = False

    return redirect("/admin")


def logout(request):
    del request.session["logged-in"]

    return redirect("/admin/login")

