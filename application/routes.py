from flask import current_app as app, render_template, redirect, url_for
from .models import db, Player, PlayerStats, GoalieStats, Team

@app.route('/')
def home():
    return render_template('BaseLayout.html', navbar_color="Default")

@app.route('/Canucks)')
def Canucks():
    team = Team.query.filter_by(TeamName='Canucks').all()
    player = Player.query.filter(Player.idTeam==1).all()
    return render_template('Canucks.html', 
                           team=team, 
                           player=player,
                           navbar_color='Canucks')

@app.route('/Oilers')
def Oilers():
    team = Team.query.all()
    return render_template('Oilers.html', team=team, navbar_color='Oilers')

