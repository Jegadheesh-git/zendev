from django.shortcuts import render,get_object_or_404, redirect
from match.models import Match, PlayingEleven
from ball.models import *

# Create your views here.
def addBall(request,match_id):
    match = get_object_or_404(Match,pk=match_id)
    deliveryTypes = DeliverySide.objects.all()
    creaseMovements = CreaseMovement.objects.all()
    shotConnections = ShotConnection.objects.all()
    batSubjects = BatSubject.objects.all()
    strokes = Stroke.objects.all()
    keeperActivities = KeeperActivity.objects.all()
    batsmanActivities = BatsmanActivity.objects.all()
    fieldingActivities = FieldingActivity.objects.all()
    umpireActivities = UmpireActivity.objects.all()
    if request.user == match.createdBy:
        if request.method == 'POST':
            pass
        else:
            ball_count = Ball.objects.filter(matchId=match).count()

            if ball_count==0:
                batters = PlayingEleven.objects.filter(match=match, team = match.teamBattingFirst ,dismissed=False)
                bowlers = PlayingEleven.objects.filter(match=match, team = match.teamBattingSecond)
                print(batters)
            context = {
                'match': match,
                'batters': batters,
                'bowlers': bowlers,
                'deliveryTypes': deliveryTypes, 'creaseMovements': creaseMovements,
                'shotConnections': shotConnections, 'batSubjects':batSubjects,
                'strokes':strokes, 'keeperActivities': keeperActivities,
                'batsmanActivities': batsmanActivities, 'fieldingActivities': fieldingActivities,
                'umpireActivities': umpireActivities
            }
            return render(request,'ball_zero.html',context)
    else:
        redirect('getAllTournamentsByUserId')