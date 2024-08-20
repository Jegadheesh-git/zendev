from django.shortcuts import render,redirect, get_object_or_404
from .models import Team
from player.models import Player
from django.http import JsonResponse

def getAllTeamsByUserId(request):
    teams = Team.objects.filter(createdBy = request.user)
    return render(request,'all_teams.html',{'teams':teams})

def addTeam(request):
    if request.method == 'POST':
        name = request.POST['name']
        shortName = request.POST.get('shortName')
        try:
            team = Team(name=name,shortName=shortName,createdBy = request.user)
            team.save()
            return redirect('getAllTeams')
        except Exception as e:
            print(e)
            return redirect('getAllTeams')
    else:
        return render(request,'add_team.html')


def updateTeam(request,team_id):
    team = get_object_or_404(Team,pk=team_id)
    if request.user == team.createdBy:
        if request.method == 'POST':
            name = request.POST['name']
            shortName = request.POST.get('shortName')
            team.name = name
            team.shortName = shortName
            team.save()
            return redirect('getAllTeams')
        else:
           
            return render(request,'update_team.html',{'team':team})
    else:
        return redirect('getAllTeams')
            
            


def deleteTeam(request,team_id):
    team = get_object_or_404(Team,pk=team_id)
    if team.createdBy == request.user:
        if request.method == 'POST':
            team.delete()
            return redirect('getAllTeams')
        else:
            return render(request,'delete_team.html',{'team':team})
    else:
        return redirect('getAllTeams')
    

def searchTeams(request):
    search_query = request.GET.get('q', '')
    teams = Team.objects.filter(name__icontains=search_query,createdBy=request.user)
    teams = teams.values('pk', 'name', 'shortName')
    return JsonResponse({'search_results': list(teams)})
