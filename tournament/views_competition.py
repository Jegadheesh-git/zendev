from django.shortcuts import render, get_object_or_404, redirect
from .models import Tournament, MatchType, Competition, CompetitionSquad
from team.models import Team
from .forms import CompetitionForm
from datetime import datetime
from django.http import JsonResponse
from player.models import Player
from django.db.models import Exists, OuterRef

def getAllCompetitions(request):
    competitions = Competition.objects.filter(createdBy = request.user)
    competitions_with_details = []
    for competition in competitions:
        has_competition_squad = CompetitionSquad.objects.filter(competition=competition).exists()
        competitions_with_details.append({
            'competition': competition,
            'has_competition_squad': has_competition_squad
        })
    return render(request, 'all_competitions.html', {'competitions':competitions_with_details})

def getAllCompetitionsByTournament(request,tournamentId):
    tournament = get_object_or_404(Tournament,pk=tournamentId)
    competitions = Competition.objects.filter(createdBy = request.user,tournament=tournament)
    competitions_with_details = []
    for competition in competitions:
        has_competition_squad = CompetitionSquad.objects.filter(competition=competition).exists()
        competitions_with_details.append({
            'competition': competition,
            'has_competition_squad': has_competition_squad
        })
    return render(request, 'all_competitions.html', {'competitions':competitions_with_details})


def getCompetitionById(request,competition_id):
    competition = get_object_or_404(Competition,pk=competition_id)
    if competition.createdBy == request.user:
        return render(request,'competition_profile.html',{'competition':competition})
    else:
        return redirect('getAllCompetitions')


def addCompetition(request):
    if request.method == 'POST':
        try:
            name = request.POST['name']
            displayName = request.POST['displayName']
            year = request.POST['year']
            matchType = MatchType.objects.get(pk=request.POST['matchType'])
            tournament = Tournament.objects.get(pk=request.POST['tournament'])
            fromDate = request.POST['fromDate']
            toDate = request.POST['toDate']
            matchCount = request.POST['matchCount']
            gender = request.POST['gender']

            competition = Competition(
                name=name,
                displayName=displayName,
                year=year,
                matchType=matchType,
                tournament=tournament,
                fromDate=fromDate,
                toDate=toDate,
                matchCount=matchCount,
                gender=gender,
                createdBy = request.user
            )
            competition.save()
    
            return redirect('addCompetitionTeams',competition.id)
        except Exception as e:
            print(e)
            return redirect('getAllCompetitions')
    else:
        match_types = MatchType.objects.all()
        tournaments = Tournament.objects.filter(createdBy=request.user)
        teams = Team.objects.filter(createdBy=request.user)
        return render(request,'add_competition.html',{'match_types':match_types,'tournaments':tournaments,'teams':teams})


def updateCompetition(request,competition_id):
    competition = get_object_or_404(Competition,pk=competition_id)
    if competition.createdBy == request.user:
        if request.method == 'POST':
            competition.name = request.POST['name']
            competition.displayName = request.POST['displayName']
            competition.year = request.POST['year']
            competition.matchType = get_object_or_404( MatchType ,pk=request.POST['matchType'] )
            competition.tournament = get_object_or_404( Tournament,pk=request.POST['tournament'])
            competition.fromDate = request.POST['fromDate']
            competition.toDate = request.POST['toDate']
            competition.matchCount = request.POST['matchCount']
            competition.gender = request.POST['gender']
            competition.save()
            return redirect('updateCompetitionTeams',competition.id)
            
        else:
            match_types = MatchType.objects.all()
            tournaments = Tournament.objects.filter(createdBy=request.user)
            selected_teams = competition.teams.all()
            available_teams = Team.objects.filter(createdBy=request.user)
            available_teams = available_teams.exclude(id__in=selected_teams.values_list('id',flat=True))
            fromDate = competition.fromDate.strftime("%Y-%m-%d")
            toDate = competition.toDate.strftime("%Y-%m-%d")

            context = {
                'competition': competition,
                'tournaments': tournaments,
                'match_types': match_types,
                'selected_teams': selected_teams,
                'available_teams': available_teams,
                'genders': ['Male','Female','Third gender'],
                'from_date': fromDate,
                'to_date': toDate
            }
            return render(request,'update_competition.html',context)
    else:
        return redirect('getAllCompetitions')


def deleteCompetition(request,competition_id):
    competition = get_object_or_404(Competition,pk=competition_id)
    if competition.createdBy == request.user:
        if request.method == 'POST':
            competition.delete()
            return redirect('getAllCompetitions')
        else:
            return render(request,'delete_competition.html',{'competition':competition})
    else:
        return redirect('getAllCompetitions')
    
def addCompetitionTeams(request,competitionId):
    competition = get_object_or_404(Competition,pk=competitionId)
    if request.user != competition.createdBy:
        return redirect('getAllTournaments')
    if request.method == 'POST':
        selectedTeams = request.POST.get('teams')
        selectedTeams = selectedTeams.split(',')
        for selectedTeam in selectedTeams:
            team = get_object_or_404(Team,pk=int(selectedTeam))
            competition.teams.add(team)
            competition.save()
        return redirect('getAllCompetitions')
    teams = Team.objects.filter(createdBy = request.user)
    return render(request,'addCompetitionTeams.html',{'teams':teams,'competition':competition})

def updateCompetitionTeams(request,competitionId):
    competition = get_object_or_404(Competition,pk=competitionId)
    if request.user != competition.createdBy:
        return redirect('getAllTournaments')
    if request.method == 'POST':
        selectedTeams = request.POST.get('teams')
        selectedTeams = selectedTeams.split(',')
        competition.teams.clear()

        for selectedTeam in selectedTeams:
            team = get_object_or_404(Team,pk=int(selectedTeam))
            competition.teams.add(team)
            competition.save()
        return redirect('getAllCompetitions')
    teams = Team.objects.filter(createdBy = request.user)
    return render(request,'updateCompetitionTeams.html',{'teams':teams,'competition':competition})

def addCompetitionSquad(request,competitionId):
    competition = Competition.objects.get(pk=competitionId)
    if request.user != competition.createdBy:
        return redirect('getAllTournaments')
    if competition.createdBy == request.user:
        if request.method == 'POST':
            if request.method == 'POST':
                teamId = request.POST.get('teamName')
                team = get_object_or_404(Team,pk=teamId)
                competitionSquads = CompetitionSquad.objects.filter(competition=competition, team=team)
                if(len(competitionSquads)==0):
                    competitionSquad = CompetitionSquad(competition=competition,team=team)
                    competitionSquad.save()
                else:
                    competitionSquad = competitionSquads[0]
                competitionSquad.players.clear()
                selectedPlayers = request.POST.get('players')
                selectedPlayers = selectedPlayers.split(',')
                for selectedPlayer in selectedPlayers:
                    player = get_object_or_404(Player,pk=int(selectedPlayer))
                    competitionSquad.players.add(player)
                    competitionSquad.save()
        return render(request,'addCompetitionSquad.html',{'competition':competition})
    
def updateCompetitionSquad(request):
    competitionId = request.GET.get('competitionId')
    teamId = request.GET.get('teamId')
    try:
        competition = get_object_or_404(Competition, pk=competitionId)
        team = get_object_or_404(Team, pk=teamId)

        if competition.createdBy != request.user:
            return JsonResponse({'error':'action resricted'})
        # Assuming there's only one CompetitionSquad per competition and team
        competitionSquad = get_object_or_404(CompetitionSquad, competition=competition, team=team)
        
        # Access the players directly from the CompetitionSquad object
        players = competitionSquad.players.values('pk', 'firstName', 'middleName', 'lastName', 'nickName','dob')
        
        return JsonResponse({'players': list(players)})
    
    except Exception as e:
        return JsonResponse({'error': str(e)})
    
def searchCompetition(request):
    search_query = request.GET.get('q', '')

    # Annotate competitions with a boolean indicating whether a related CompetitionSquad exists
    competitions = Competition.objects.filter(name__icontains=search_query,createdBy=request.user).annotate(
        has_competition_squad=Exists(CompetitionSquad.objects.filter(competition=OuterRef('pk')))
    ).values('pk', 'name', 'fromDate', 'toDate', 'has_competition_squad')

    return JsonResponse({'search_results': list(competitions)})

