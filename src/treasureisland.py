print('''

                                ,
                               //\
                              / | ;
                              | /_|
                            .-"`  `"-.
                          /`          `\
                         /              \
                   .-.,_|      .-""""-. |
                  |     `",_,-'  (((-. '(
                   \ (`"=._.'/   (  (o>'-`"#
        ,           '.`"-'` /     `--`  '==;
       /\\            `'--'`\         _.'~~
      / | \                  `.,___,-}
      | |  |                   )  {  }
       \ \ (.--==---==-------=' o {  }
        ",/` (_) (_)  (_)    (_)   \ /
         / ()   o   ()    ()        ^|
         \   ()  (    () o        ;  /
          `\      \         ;    / } |
            )      \       /   /`  } /
         ,-'       |=,_   |   /,_ ,'/
         |    _,.-`/   `"=\   \\   \
         | ."` \  |        \   \`\  \
         | |    \ \         `\  \ `\ \
         | |     \ \          `\ \  \ \
         | |      \ \           \ \  \ \
         | |       \ \           \ \  \ \
         | |        \ \           \ \  \ \
         | |         ) \           \ \  ) \
     jgs `) \        ^ww            ) \ ^ww
          ^ww                       ^ww 

''')

print("Welcome to Treusure Island.\nYour mission is to find the treassure.\nCan you find it?")
choice1 = input('You arrived at the island and are looking for the treasure. You are standing in front of a crossroad, where do you want to go? Type "Left" or "Right"\n').lower()

if choice1 == 'left':
    print("You choose luckily the right direction. When you looked back, while heading to the left side, you see a group of canibals with spears and bow & arrows screaming and hunting for food.")
    choice2 = input('While walking you\'ve come to a lake, There is an island in the middle of the lake. Do you want to wait or swim? Type "wait" to wait for a boat or "swim" to swim across.\n').lower()
    if choice2 == 'wait':
        print("That was the best choice, while waiting you see a lot of crocodiles in the water.")
        choice3 = input('You arrived at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n').lower()
        if choice3 == 'red':
            print('There was a hungry tiger behind that door, you woke him up, game over')
        elif choice3 == 'yellow':
            print("Congrats you found the treasure! You win the game.")
        elif choice3 == 'blue':
            print("This was a room full of explosions and you died... game over")
        else:
            print("You choose a wrong colour, game over")
    else:
        print("You have been eaten by a group of hungry crocodiles, game over")
else: 
    print("Game over, you ran into a group of cannibals")

