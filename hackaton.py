from black import out


hackathon_1 = ["Team Kenzie", "Team Ateliware", "Team VHSYS", "Team Mirum"]
hackathon_2 = ["Team Ateliware", "Team Kenzie", "Team VHSYS", "Team Mirum"]
hackathon_3 = ["Team Mirum", "Team Ateliware","Team VHSYS", "Team Kenzie"]




def get_score(team_name,team):
    output=''
    for i in range (len(team)):
        if team[i]==team_name:
            output='A '+team[i]+' ficou classificada em '+str(i+1)
            return output
