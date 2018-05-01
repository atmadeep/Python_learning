from operator import itemgetter
import sys
indexOf={'Best_Of_5':0, 'Best_Of_3':1, 'Sets_Won':2, 'Games_Won':3, 'Sets_Lost':4, 'Games_Lost':5}

def score_Calculator(dictionary_Of_Players,line):
    # Score variables
    score_list_1=[0,0,0,0,0,0]
    score_list_2=[0,0,0,0,0,0]
    player_1_set=0
    player_2_set=0
     #loop over every line read.
    Name1 = line[0:line.index(':')] #extract name of player one
    Name2=line[line.index(':')+1:line.rindex(':')]  # extract name of player 2

    if not(Name1 in dictionary_Of_Players):
        dictionary_Of_Players[Name1]=[0,0,0,0,0,0]

    score_list_1 = dictionary_Of_Players[Name1]

    if not(Name2 in dictionary_Of_Players):
        dictionary_Of_Players[Name2]=[0,0,0,0,0,0]

    score_list_2 = dictionary_Of_Players[Name2]

    values = line[line.rindex(":")+1:len(line)].split(',')
    game_score=[]
    for val in values:
        game_score.append(val.split('-'))

    #This is used to decide whether the set of 3 or 5 games in total.
    no_of_sets = len(game_score)

    for game in game_score:
        #print(game)

        if(game[0] > game[1]):
            #update score of sets
            player_1_set+=1
            score_list_2[indexOf['Sets_Lost']] +=1
            score_list_1[indexOf['Sets_Won']]+=1


        else:
            player_2_set+=1
            score_list_1[indexOf['Sets_Lost']]+=1
            score_list_2[indexOf['Sets_Won']]+=1

        #update score of games for player 1
        score_list_1[indexOf['Games_Won']]+=int(game[0])
        score_list_1[indexOf['Games_Lost']]+=int(game[1])

        #update score of games for player 2
        score_list_2[indexOf['Games_Won']]+=int(game[1])
        score_list_2[indexOf['Games_Lost']]+=int(game[0])
        #print(Name1,player_1_set,Name2,player_2_set)
    if player_1_set > player_2_set:
            if (no_of_sets<5):
                score_list_1[indexOf['Best_Of_3'] ]+= 1
            else:
                score_list_1[indexOf['Best_Of_5']]+=1
    else:
            if (no_of_sets < 5):
                score_list_1[indexOf['Best_Of_3']] += 1
            else:
                score_list_1[indexOf['Best_Of_5']] += 1


    dictionary_Of_Players[Name1]=score_list_1
    dictionary_Of_Players[Name2]=score_list_2
   # print(dictionary_Of_Players)
    return dictionary_Of_Players


def print_Dictionary_Of_Players(dictionary_Of_Players):
    temp_list=[]
    keys = dictionary_Of_Players.keys()
    for i in range(len(keys)):
        list2=[]
        list2.append(([dictionary_Of_Players[keys[i]][0],dictionary_Of_Players[keys[i]][1],dictionary_Of_Players[keys[i]][2]],i))
        temp_list.append(list2)
    temp_list.sort(reverse=True)
    for i in range(len(temp_list)):
        name = keys[temp_list[i][0][1]]
        print name, dictionary_Of_Players[name][0],dictionary_Of_Players[name][1], dictionary_Of_Players[name][2], dictionary_Of_Players[name][3],  dictionary_Of_Players[name][4], dictionary_Of_Players[name][5]

dictionary={}
lines=sys.stdin.readline()
while lines != '\n':
    dictionary=score_Calculator(dictionary_Of_Players=dictionary,line=lines)
    lines = sys.stdin.readline()

print_Dictionary_Of_Players(dictionary)
