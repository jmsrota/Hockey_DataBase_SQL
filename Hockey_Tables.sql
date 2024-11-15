USE hockey_database;
/* PlayerStats Table */
CREATE TABLE PlayerStats (
	idPlayerStats INT AUTO_INCREMENT,
    Goals INT,
    Assists INT,
    Points INT,
    
    PRIMARY KEY (idPlayerStats)
);
/* GoalieStats Table */
CREATE TABLE GoalieStats (
	idGoalieStats INT AUTO_INCREMENT,
    GAA DECIMAL(5,2),
    Save_Percentage DECIMAL(5,2),
    ShutOuts INT,
    
    PRIMARY KEY (idGoalieStats)
);
/* Team Table */
CREATE TABLE Team (
	idTeam INT AUTO_INCREMENT,
    TeamName VARCHAR(45),
    Wins INT,
    Losses INT,
    OT INT,
    Points INT,
    
    PRIMARY KEY (idTeam)
);
/* Player Table */
CREATE TABLE Player (
	idPlayer INT AUTO_INCREMENT,
    playerName VARCHAR(45) UNIQUE,
    idPlayer_Stats INT,
    idGoalie_Stats INT,
    idTeam INT,
    
	PRIMARY KEY (idPlayer),
    FOREIGN KEY (idPlayer_Stats) REFERENCES PlayerStats(idPlayerStats),
    FOREIGN KEY (idTeam) REFERENCES Team(idTeam),
    FOREIGN KEY (idGoalie_Stats) REFERENCES GoalieStats(idGoalieStats)
);

