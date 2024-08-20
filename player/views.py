from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import PlayerForm
from django.http import JsonResponse
from django.db.models import Q

# Create your views here.
def getPlayerDashboard(request):
    return render(request,'player_dashboard.html')

def getAllPlayersByUserId(request):
    players = Player.objects.filter(createdBy = request.user)
    return render(request,'all_players.html',{'players':players})

def getPlayerById(request,player_id):
    user_id = request.user.id
    player = get_object_or_404(Player,pk=player_id)
    if player.createdBy.id == user_id:
        return render(request,'player_portfolio.html',{'player':player})
    else:
        return redirect('home')
    
def addPlayer(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            player = form.save(commit=False)
            player.createdBy = request.user
            player.save()
        return redirect('getAllPlayersByUserId')
    else:
        nationalities = Nationality.objects.all()
        height_types = HeightType.objects.all()
        bowling_types = BowlingType.objects.all()
        batting_types = BattingType.objects.all()
        bowler_types = BowlerType.objects.all()

        # Pass the data to the template
        context = {
            'nationalities': nationalities,
            'height_types': height_types,
            'bowling_types': bowling_types,
            'batting_types': batting_types,
            'bowler_types': bowler_types,
        }

        return render(request, 'add_player.html', context)


def updatePlayer(request,player_id):
    player = get_object_or_404(Player,pk=player_id)
    if player.createdBy == request.user:
        if request.method == 'POST':
            try:
                form = PlayerForm(request.POST,instance=player)
                if form.is_valid():
                    form.save()
                return redirect('getAllPlayersByUserId')

            except:
                return JsonResponse({'error':'Something went wrong'})
            return redirect('getAllPlayersByUserId')
        else:
            nationalities = Nationality.objects.all()
            height_types = HeightType.objects.all()
            bowlingTypes = BowlingType.objects.all()
            bowlerTypes = BowlerType.objects.all()
            battingType = BattingType.objects.all()
            return render(request,'update_player.html',{
                'player':player,
                'nationalities':nationalities,
                'height_types':height_types,
                'bowling_types': bowlingTypes,
                'bowler_types': bowlerTypes,
                'batting_types': battingType
                })
    else:
        return redirect('getAllPlayersByUserId')
    
def deletePlayer(request,player_id):
    player = get_object_or_404(Player,pk=player_id)
    if player.createdBy == request.user:
        if request.method == 'POST':
            player.delete()
            return redirect('getAllPlayersByUserId')
        else:
            return render(request,'delete_player.html',{'player':player})
    else:
        return redirect('getAllPlayersByUserId')


def getAllUmpiresByUserId(request):
    umpires = Umpire.objects.filter(createdBy = request.user)
    return render(request,'all_umpire.html',{'umpires':umpires})

def addUmpire(request):
    if request.method == 'POST':
        name = request.POST['name']
        nationality = Nationality.objects.get(pk= request.POST['nationality'])
        createdBy = request.user
        umpire = Umpire(name=name,nationality=nationality,createdBy=createdBy)
        try:
            umpire.save()           
        except:
            return redirect('getAllUmpiresByUserId')
        return redirect('getAllUmpiresByUserId')            
        
    else:
        nationalities = Nationality.objects.all()
        return render(request,'add_umpire.html',{'nationalities':nationalities})
    
def deleteUmpire(request,umpire_id):
    umpire = get_object_or_404(Umpire,pk=umpire_id)
    if umpire.createdBy == request.user:
        if request.method == 'POST':
            umpire.delete()
            return redirect('getAllUmpiresByUserId')
        else:
            return render(request,'delete_umpire.html',{'umpire':umpire})
    else:
        return redirect('getAllUmpiresByUserId')

def searchPlayers(request):
    search_query = request.GET.get('q')
    players = Player.objects.filter(
        Q(firstName__icontains=search_query) |
        Q(middleName__icontains=search_query) |
        Q(lastName__icontains=search_query) |
        Q(nickName__icontains=search_query),
        createdBy = request.user
    )
    
    # Select only the fields you need
    players = players.values('pk', 'firstName', 'middleName', 'lastName', 'nickName','dob')
    
    return JsonResponse({'search_results': list(players)})