from flask import current_app as app, render_template, redirect, url_for
from .models import db, Player, PlayerStats, GoalieStats, Team

@app.route('/')
def home():
    return render_template('BaseLayout.html')

@app.route('/canucks)')
def canucks():
    player = Player.query.all()
    return render_template('Canucks.html',player=player)
