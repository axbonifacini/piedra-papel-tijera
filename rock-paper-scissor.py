import random
f=open("puntaje.txt","a",encoding="utf8")
wc=0
wu=0
for i in range(1,4):
    user_action= input ("Seleccione (piedra-papel-tijera)")
    possible_actions= ["piedra","papel","tijera"]
    computer_action= random.choice(possible_actions)  
    # print(computer_action)
    print ("\n Usted eligio : ", user_action,",  la computadora eligio : ",computer_action,"\n")

    if user_action==computer_action:
        print("Empate",user_action)
        f.write("Empate \n")
    elif user_action=="piedra" and computer_action=="papel":
        print("Gano la compu. \n") 
        f.write("Gano la compu \n")
        wc+=1
    elif user_action=="piedra" and computer_action=="tijera":
        print("Usted gano. \n")
        f.write("Usted gano \n")
        wu+=1 
    elif user_action=="papel" and computer_action=="piedra":
        print("Usted gano. \n")
        f.write("Usted gano \n")
        wu+=1
    elif user_action=="papel" and computer_action=="tijera":
        print("Gano la compu. \n")
        f.write("Gano la compu \n")
        wc+=1
    elif user_action=="tijera" and computer_action=="piedra":
        print("Gano la compu. \n")
        f.write("Gano la compu \n")
        wc+=1
    elif user_action=="tijera" and computer_action=="papel":
        print("Usted gano. \n") 
        f.write("Usted gano \n")
        wu+=1
    else:
        print("Error gramatical.\n")
        f.write("Error gramatical \n")


if wc > wu:
    print("\n La partida la gano la compu")
else:
    print("\n La partida la gano usted")

if wc==wu:
    print("\n La partida finalizo empatada")
     
