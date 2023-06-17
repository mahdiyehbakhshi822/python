import random

print('**************rook_paper_scisior***************')


lap =  int(input("pleas return ypur lap : "))
print("//////////////////////////")

user_score = 0
player_score = 0

for num in range (1,lap+1):
    number = random.randint(1,3)

    playet = ""
    user = input('please return your choise : ')
    if number == 1:
        player = 'rook'
        print('player choise rook')
        
    elif number == 2:
        player ='paper'
        print('player choise paper')
       
    elif number == 3 :
        player = 'scisior'
        print('player choise scisior')
        

    if player == 'rook' and user =='paper':
        print('user win')
        user_score +=1
        print("******************")

    elif player == 'rook' and user == 'scisior':
        print('player win')
        player_score +=1
        print("******************")

    elif player == 'paper' and user == 'rook':
        print('player win')
        player_score +=1
        print("******************")

    elif player == 'paper' and user == 'scisior':
        print('user win')
        user_score +=1
        print("******************")
    elif player == 'scisior' and user == 'paper':
        print('player win')
        player_score +=1
        print("******************")
    elif player == 'scisior' and user == 'rook':
        print('user win')
        user_score +=1
        print("******************")
    else:
        print('equal')
        player_score +=0.5
        user_score +=0.5
        print("******************")
        
print("=============================")
print(f"user score : {user_score}")

print(f"player score : {player_score}")

if user_score > player_score:
    print('user is final win')

elif player_score > user_score:
    print('player is final win')
# else:
#     print('no win')