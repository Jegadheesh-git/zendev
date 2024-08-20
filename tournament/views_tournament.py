from django.shortcuts import render, get_object_or_404, redirect
from .models import Tournament
from django.http import JsonResponse

# Create your views here.
def getAllTournamentsByUserId(request):
    tournaments = Tournament.objects.filter(createdBy=request.user)
    return render(request,'all_tournaments.html',{'tournaments':tournaments})

def addTournament(request):
    if request.method == 'POST':
        name = request.POST['tournament_name']
        try:
            tournament = Tournament(name = name, createdBy = request.user)
            tournament.save()
            return redirect('getAllTournamentsByUserId')
        except:
            return redirect('getAllTournamentsByUserId')
    else:
        return render(request,'add_tournament.html')

def updateTournament(request,tournament_id):
    tournament = get_object_or_404(Tournament,pk=tournament_id)

    if request.user == tournament.createdBy:
        if request.method == 'POST':
            name = request.POST['name']
            tournament.name = name
            tournament.save()
            return redirect('getAllTournamentsByUserId')
        else:
            return render(request,'update_tournament.html',{'tournament':tournament})
    else:
        return redirect('getAllTournamnetsByUserId')
    
def deleteTournament(request,tournament_id):
    tournament = get_object_or_404(Tournament,pk=tournament_id)

    if request.user == tournament.createdBy:
        if request.method == 'POST':
            tournament.delete()
            return redirect('getAllTournamentsByUserId')
        else:
            return render(request,'delete_tournament.html',{'tournament':tournament})
    else:
        return redirect('getAllTournamentsById')
    
def searchTournaments(request):
    search_query = request.GET.get('q', '')
    tournaments = Tournament.objects.filter(name__icontains=search_query,createdBy=request.user)
    tournaments = tournaments.values('pk', 'name')
    return JsonResponse({'search_results': list(tournaments)})