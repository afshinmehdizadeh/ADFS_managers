from django.shortcuts import render, loader, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext
from models import Player, Team, Stadium, Match, Tournament, MatchInLeague
import datetime

import serializers

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response

# Views for REST-API
@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def player_list(request):
    if request.method == 'GET':
        players = Player.objects.all()
        serializer = serializers.PlayerSerializer(players, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = serializers.PlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Views for Web-Service

def player(request, id):
    template = loader.get_template('teamlogic/player.html')
    players = get_object_or_404(Player, pk=id)
    context = RequestContext(request, {
        'player': players,
        'user': request.user,
    })
    return HttpResponse(template.render(context))


def players(request):
    template = loader.get_template('teamlogic/players.html')
    players = Player.objects.all()
    context = RequestContext(request, {
        'players': players,
        'user': request.user
    })
    return HttpResponse(template.render(context))


def team(request, id):
    template = loader.get_template('teamlogic/team.html')
    teams = get_object_or_404(Team, pk=id)
    context = RequestContext(request, {
        'team': teams,
        'nows': datetime.datetime.today(),
        'user': request.user,
    })
    return HttpResponse(template.render(context))


def teams(request):
    template = loader.get_template('teamlogic/teams.html')
    teams = Team.objects.all()
    context = RequestContext(request, {
        'teams': teams
    })
    return HttpResponse(template.render(context))


def stadion(request, id):
    template = loader.get_template('teamlogic/stadion.html')
    stadion = get_object_or_404(Stadium, pk=id)
    context = RequestContext(request, {
        'stadion': stadion,
        'user': request.user,
    })
    return HttpResponse(template.render(context))


def stadions(request):
    template = loader.get_template('teamlogic/stadions.html')
    stadions = Stadium.objects.all()
    context = RequestContext(request,{
        'stadions': stadions,
        'user': request.user
    })
    return HttpResponse(template.render(context))


def match(request, id=None):
    template = loader.get_template('teamlogic/match.html')
    matchs = get_object_or_404(Match, pk=id)
    context = RequestContext(request, {
        'match': matchs,
        'nows': datetime.datetime.now(),
        'user': request.user,
    })
    return HttpResponse(template.render(context))


def league(request, id=None):
    if request.method == "GET":
        template = loader.get_template('teamlogic/league.html')
        leagues = get_object_or_404(Tournament, pk=id)
        context = RequestContext(request, {
            'league': leagues,
            'nows': datetime.datetime.now(),
        })
    return HttpResponse(template.render(context))


def calendar(request, id=id):
    template = loader.get_template('teamlogic/calendar.html')
    t = get_object_or_404(Tournament, pk=id)
    t.refresh()
    calend = t.get_calendar()
    context = RequestContext(request, {
        'matches': calend,
        'all_team_matches': Match.objects.all().last().all_team_matches(Team.objects.all().last()),
        'user': request.user,
    })
    return HttpResponse(template.render(context))


def team_matches(request, id=1):
    template = loader.get_template('teamlogic/matches.html')
    t = get_object_or_404(Team, pk=id)
    context = RequestContext(request, {
        'all_team_matches': MatchInLeague.objects.all().last().all_team_matches(t),
        'team': t,
        'user': request.user,
    })
    return HttpResponse(template.render(context))


def bombardiers(request, id=1):
    template = loader.get_template('teamlogic/bombardiers.html')
    t = get_object_or_404(Tournament, pk=id)
    context = RequestContext(request, {
        'all_bombardiers': t.get_bombardiers_table(),
        'league': t,
        'user': request.user,
    })
    return HttpResponse(template.render(context))
