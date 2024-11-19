from flask import current_app as app, render_template, redirect, url_for
from .models import db, Player, PlayerStats, GoalieStats, Team

@app.route('/')
def home():
    return render_template('BaseLayout.html', navbar_color="Default")

@app.route('/Canucks)')
def Canucks():
    team = Team.query.filter_by(TeamName='Canucks').all()
    forwards = Player.query.filter(Player.idTeam==1, Player.Role=='Forwards').all()
    defence = Player.query.filter(Player.idTeam==1, Player.Role=='Defensemen').all()
    goalies = Player.query.filter(Player.idTeam==1, Player.Role=='Goalies').all()
    print (defence)
    return render_template('Canucks.html', 
                           team=team, 
                           forwards=forwards,
                           defence=defence,
                           goalies = goalies,
                           navbar_color='Canucks')

@app.route('/Oilers')
def Oilers():
    team = Team.query.all()
    return render_template('Oilers.html', team=team, navbar_color='Oilers')

