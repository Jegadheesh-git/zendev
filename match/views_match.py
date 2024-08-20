from django.shortcuts import render, get_object_or_404, redirect
from tournament.models import Competition, MatchType, CompetitionSquad
from .models import Match,Stadium,Knockout,PlayingEleven
from team.models import Team
from player.models import Umpire,Player

# Create your views here.
def getAllMatchesByCompetition(request, competition_id):
    competition = get_object_or_404(Competition, pk=competition_id)
    
    if competition.createdBy == request.user:
        matches = Match.objects.filter(competition=competition)
        
        # List to hold match details with additional fields
        matches_with_details = []
        
        for match in matches:
            # Check if toss details are fully updated
            has_toss_updated = all([
                match.tossWonBy,
                match.optTo,
                match.fisrtInningsCondition,
                match.secondInningsCondition,
                match.teamBattingFirst,
                match.teamBattingSecond
            ])
            
            # Check if any playing eleven entries exist for the match
            has_playing_eleven = PlayingEleven.objects.filter(match=match).exists()
            
            # Add the match along with the new fields to the list
            matches_with_details.append({
                'match': match,
                'hasTossUpdated': has_toss_updated,
                'hasPlayingEleven': has_playing_eleven
            })
        
        # Render the response with the new data structure
        return render(request, 'all_matches.html', {
            'matches': matches_with_details,  # Pass matches_with_details as 'matches'
            'competition': competition
        })
    
    # Redirect if the user is not the creator of the competition
    return redirect('getAllTournaments')

def deleteMatch(request,match_id):
    match = get_object_or_404(Match,pk=match_id)
    if match.createdBy == request.user:
        if request.method == 'POST':
            match.delete()
            return redirect('getAllTournamentsByUserId')
        else:
            return render(request,'delete_match.html',{'match':match})
    else:
        return redirect('getAllStadiumsByUserId')
    
def addMatch(request,competition_id):
    competition = get_object_or_404(Competition,pk=competition_id)
    if competition.createdBy == request.user:
        if request.method == 'POST':
            stadium = Stadium.objects.get(pk=request.POST['stadium'])
            date = request.POST['date']
            matchType = MatchType.objects.get(pk=request.POST['matchType'])
            dayOrNight = request.POST['dayOrNight']
            fisrtInningsCondition = request.POST['fisrtInningsCondition']
            secondInningsCondition = request.POST['secondInningsCondition']
            team1 = Team.objects.get(pk=request.POST['team1'])
            team2 = Team.objects.get(pk=request.POST['team2'])
            knockout = Knockout.objects.get(pk=request.POST['knockout'])
            try:
                match = Match(
                    competition=competition,
                    stadium = stadium,
                    date = date,
                    matchType = matchType,
                    dayOrNight = dayOrNight,
                    fisrtInningsCondition=fisrtInningsCondition,
                    secondInningsCondition = secondInningsCondition,
                    team1 = team1,
                    team2 = team2,
                    knockout = knockout,
                    createdBy = request.user
                )
                match.save()
                match_id = match.pk
                print(match_id)
                return redirect('updateMatchToss',match.id)
            except Exception as e:
                print(e)
                return redirect('getAllTournamentsByUserId')
        else:
            stadiums = Stadium.objects.filter(createdBy=request.user)
            knockouts = Knockout.objects.all()
            teams = competition.teams.all()
            match_types = MatchType.objects.all()
            competitions = Competition.objects.filter(createdBy=request.user)

            context = {
                'selected_competition': competition,
                'competitions':competitions,
                'stadiums': stadiums,
                'knockouts': knockouts,
                'teams': teams,
                'match_types': match_types
            }
            
            return render(request,'add_match_setup.html',context)
    else:
        return redirect('getAllCompetitions')

def updateMatchToss(request,match_id):
    match = get_object_or_404(Match,pk=match_id)
    if match.createdBy == request.user:
        if request.method == 'POST':
            tossWonById = request.POST['tossWonBy']
            optTo = request.POST['optTo']
            umpire1 = request.POST['umpire1']
            umpire2 = request.POST['umpire2']
            umpire3 = request.POST['umpire3']

            try:
                match.tossWonBy = Team.objects.get(pk=tossWonById)
                match.optTo = optTo

                match.umpire1 = get_object_or_404(Umpire,pk=umpire1)
                match.umpire2 = get_object_or_404(Umpire,pk=umpire2)
                match.umpire3 = get_object_or_404(Umpire,pk=umpire3)

                tossWonBy = Team.objects.get(pk=tossWonById)
                tossLostBy = match.team1 if match.tossWonBy==match.team2 else match.team2

                if(optTo == 'Batting'):
                    match.teamBattingFirst = tossWonBy
                    match.teamBattingSecond = tossLostBy
                else:
                    match.teamBattingFirst = tossLostBy
                    match.teamBattingSecond = tossWonBy
                match.save()
                return redirect('addPlayingXI',match.pk)
            except Exception as e:
                print(e)
                return redirect('getAllTournamentsByUserId')

        else:
            competition = match.competition
            stadiums = Stadium.objects.filter(createdBy=request.user)
            knockouts = Knockout.objects.all()
            teams = competition.teams.all()
            match_types = MatchType.objects.all()
            competitions = Competition.objects.filter(createdBy=request.user)
            umpires = Umpire.objects.filter(createdBy=request.user)

            context = {
                'selected_competition': competition,
                'competitions':competitions,
                'stadiums': stadiums,
                'knockouts': knockouts,
                'teams': teams,
                'match_types': match_types,
                'match': match,
                'umpires': umpires,
            }
            return render(request,'update_match_toss.html',context)
    else:
        return redirect('getAllTournamentsByUserId')
    
def addPlayingXI(request,match_id):
    match = get_object_or_404(Match,pk=match_id)
    if request.user == match.createdBy:
        
        has_toss_updated = all([
                match.tossWonBy,
                match.optTo,
                match.fisrtInningsCondition,
                match.secondInningsCondition,
                match.teamBattingFirst,
                match.teamBattingSecond
            ])

        if not has_toss_updated:
            return redirect('updateMatchToss',match.id)

        competitionSquadTeam1 = CompetitionSquad.objects.filter(competition=match.competition,team=match.team1)
        competitionSquadTeam2 = CompetitionSquad.objects.filter(competition=match.competition,team=match.team2)

        if request.method == 'POST':

            PlayingEleven.objects.filter(match=match).delete()

            team1_player_count = competitionSquadTeam1[0].players.count()
            team2_player_count = competitionSquadTeam2[0].players.count()
            
            try:
                for id in range(1,match.matchType.activePlayersPerTeam+1):
                    t1_player = get_object_or_404(Player,pk=request.POST.get('t1p'+str(id)))
                    t2_player = get_object_or_404(Player,pk=request.POST.get('t2p'+str(id)))
                    t1_playing_xi = PlayingEleven(
                        match=match,battingOrder = id,team=match.team1,player=t1_player
                    )
                    t2_playing_xi = PlayingEleven(
                        match=match, battingOrder = id, team=match.team2, player=t2_player
                    )
                    t1_playing_xi.save()
                    t2_playing_xi.save()
                for id in range(1,max(team1_player_count,team2_player_count)-1):
                    t1_player_id = request.POST.get('t1s'+str(id))
                    t2_player_id = request.POST.get('t2s'+str(id))
                    if t1_player_id:
                        t1_player = get_object_or_404(Player,pk=t1_player_id)
                        t1_playing_xi = PlayingEleven(
                        match=match,battingOrder = 11+id,team=match.team1,player=t1_player,substitute=True
                        )
                        t1_playing_xi.save()
                    if t2_player_id:
                        t2_player = get_object_or_404(Player,pk=t2_player_id)
                        t2_playing_xi = PlayingEleven(
                        match=match,battingOrder = 11+id,team=match.team2,player=t2_player,substitute=True
                        )
                        t2_playing_xi.save()
                
                match.captain1 = get_object_or_404(Player,pk=request.POST.get('captain1'))
                match.captain2 = get_object_or_404(Player,pk=request.POST.get('captain2'))
                match.wicketKeeper1 = get_object_or_404(Player,pk=request.POST.get('wicketkeeper1'))
                match.wicketKeeper2 = get_object_or_404(Player,pk=request.POST.get('wicketkeeper2'))
                match.save()
                 
            except Exception as e:
                print(e)
            
            
            return redirect('addBall',match.pk)
        else:
            if(len(competitionSquadTeam1)==0 or len(competitionSquadTeam2)==0):
                return redirect('addCompetitionSquad',match.competition.pk)
            competitionSquadTeam1 = competitionSquadTeam1[0]
            competitionSquadTeam2 = competitionSquadTeam2[0]

            return render(request,'add_playing_xi.html',{'match':match,'team1':competitionSquadTeam1,'team2':competitionSquadTeam2})
    else:
        return redirect('getAllTournamentsByUserId')
