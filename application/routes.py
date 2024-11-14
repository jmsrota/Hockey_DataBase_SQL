from flask import current_app as app, render_template, redirect, url_for
from .models import db, Player, PlayerStats, GoalieStats, Team

@app.route('/')
def home():
    return render_template('BaseLayout.html', navbar_color="Default")

@app.route('/Canucks)')
def Canucks():
    player = Player.query.all()
    return render_template('Canucks.html', player=player, navbar_color='Canucks')

@app.route('/Oilers')
def Oilers():
    player = Player.query.all()
    return render_template('Oilers.html', player=player, navbar_color='Oilers')

