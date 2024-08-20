from django.shortcuts import render,redirect, get_object_or_404
from .models import Stadium
from player.models import Nationality

def getAllStadiumsByUserId(request):
    stadiums = Stadium.objects.filter(createdBy=request.user)
    return render(request,'all_stadiums.html',{'stadiums':stadiums})

def addStadium(request):
    if request.method == 'POST':
        try:
            nationality = get_object_or_404(Nationality,pk=request.POST.get('nationality'))
            stadium = Stadium(name=request.POST['name'], nationality=nationality, createdBy=request.user)
            stadium.save()
            return redirect('getAllStadiumsByUserId')
        except:
            return redirect('getAllStadiumsByUserId')
    else:
        nationalities = Nationality.objects.all()
        return render(request,'add_stadium.html',{'nationalities':nationalities})

def deleteStadium(request,stadium_id):
    stadium = get_object_or_404(Stadium,pk=stadium_id)
    if stadium.createdBy == request.user:
        if request.method == 'POST':
            stadium.delete()
            return redirect('getAllStadiumsByUserId')
        else:
            return render(request,'delete_stadium.html',{'stadium':stadium})
    else:
        return redirect('getAllStadiumsByUserId')
