# application/models.py
from . import db

class PlayerStats(db.Model):
    __tablename__ = 'PlayerStats'
    
    idPlayerStats = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Goals = db.Column(db.Integer)
    Assists = db.Column(db.Integer)
    Points = db.Column(db.Integer)

    # Relationship back to Player
    player = db.relationship("Player", back_populates="player_stats", uselist=False)

    def __repr__(self):
        return f"<PlayerStats (Goals={self.Goals}, Assists={self.Assists}, Points={self.Points})>"


class GoalieStats(db.Model):
    __tablename__ = 'GoalieStats'
    
    idGoalieStats = db.Column(db.Integer, primary_key=True, autoincrement=True)
    GAA = db.Column(db.Numeric(5, 2))
    Save_Percentage = db.Column(db.Numeric(5, 2))
    ShutOuts = db.Column(db.Integer)

    # Relationship back to Player
    player = db.relationship("Player", back_populates="goalie_stats", uselist=False)

    def __repr__(self):
        return f"<GoalieStats (GAA={self.GAA}, Save Percentage={self.Save_Percentage}, ShutOuts={self.ShutOuts})>"


class Team(db.Model):
    __tablename__ = 'Team'
    
    idTeam = db.Column(db.Integer, primary_key=True, autoincrement=True)
    TeamName = db.Column(db.String(45))
    Wins = db.Column(db.Integer)
    Losses = db.Column(db.Integer)
    OT = db.Column(db.Integer)
    Points = db.Column(db.Integer)

    # Relationship to Player
    players = db.relationship("Player", back_populates="team")

    def __repr__(self):
        return f"<Team (Name={self.TeamName}, Wins={self.Wins}, Losses={self.Losses}, Points={self.Points})>"


class Player(db.Model):
    __tablename__ = 'Player'
    
    idPlayer = db.Column(db.Integer, primary_key=True, autoincrement=True)
    playerName = db.Column(db.String(45))
    
    Position = db.Column(db.String(2), nullable=True)
    Role = db.Column(db.String(45), nullable=True)
    idPlayer_Stats = db.Column(db.Integer, db.ForeignKey('PlayerStats.idPlayerStats'), nullable=True)
    idGoalie_Stats = db.Column(db.Integer, db.ForeignKey('GoalieStats.idGoalieStats'), nullable=True)
    idTeam = db.Column(db.Integer, db.ForeignKey('Team.idTeam'), nullable=True)
    
    # Relationships to PlayerStats, GoalieStats, and Team
    player_stats = db.relationship("PlayerStats", back_populates="player")
    goalie_stats = db.relationship("GoalieStats", back_populates="player")
    team = db.relationship("Team", back_populates="players")

    def __repr__(self):
        return f"<Player (Name={self.playerName}, Team ID={self.idTeam})>"