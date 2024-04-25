import json

desired_names = ['Top|NA', 'Jungle|NA','Mid|NA','ADC|NA','Support|NA',
                 'Top|EUW', 'Jungle|EUW','Mid|EUW','ADC|EUW','Support|EUW',
                 'Top|EUNE', 'Jungle|EUNE', 'Mid|EUNE', 'ADC|EUNE', 'Support|EUNE']


na_desired_names = ['Top|NA', 'Jungle|NA','Mid|NA','ADC|NA','Support|NA']
euw_desired_names = ['Top|EUW', 'Jungle|EUW','Mid|EUW','ADC|EUW','Support|EUW']
eune_desired_names = ['Top|EUNE', 'Jungle|EUNE', 'Mid|EUNE', 'ADC|EUNE', 'Support|EUNE']


desired_servers = ['EUW','NA','EUNE']



def clean(name_list):
    players = []
    encountered_numbers = {}
    for item in name_list:
        number = item[0]
        if number in encountered_numbers:
            index = encountered_numbers[number]
            players.pop(index)
        encountered_numbers[number] = len(players)
        players.append(item)
    return players

def getTeams(players):
    matching_names = []
    counter = {name: 0 for name in desired_names}
    for record in players:
        name = record[1]
        if name in desired_names and counter[name] < 2:
            matching_names.append(record)
            counter[name] += 1
            if all(count == 2 for count in counter.values()):
                break
    return matching_names

def splitTeams(players):

    if(len(players) == 10):
        team1 = []
        counter = {name: 0 for name in desired_names}
        for record in players:
            name = record[1]
            if name in desired_names and counter[name] < 1:
                team1.append(record)
                counter[name] += 1
                if all(count == 1 for count in counter.values()):
                    break
        for x in team1:
            players.remove(x)
        team2 = players
        teaming = team1 + team2
        return teaming

def getPlayer(list):
    seen = {}
    result = []
    for tuple in list:
        if tuple[1] in seen:
            result.append(seen[tuple[1]])
            result.append(tuple)
            break
        seen[tuple[1]] = tuple

    return result

def countNAPlayers(list):
    role_counts = {role: 0 for role in na_desired_names}
    for role in list:
        if role in role_counts:
            role_counts[role] += 1
    return role_counts

def countEUWPlayers(list):
    role_counts = {role: 0 for role in euw_desired_names}
    for role in list:
        if role in role_counts:
            role_counts[role] += 1
    return role_counts

def countEUNEPlayers(list):
    role_counts = {role: 0 for role in eune_desired_names}
    for role in list:
        if role in role_counts:
            role_counts[role] += 1
    return role_counts

def getdiscordUser(list):
    users = []
    for i in list:
        users.append(i[0])
    return users

def decoration(list):
    result = ''
    for item in list:
        message = str(item[1])
        result += f"{item[0]} ==> {message.rsplit('|')[0]}\n"
    return result

def splitMessage(first:str,second:str):
    final  = ''
    final += "Team 1 \n" + first +'\t \t ' + second
    return final

def solo_decoration(list):
    result = f'{list[0][0]} VS {list[1][0]}'
    return result




