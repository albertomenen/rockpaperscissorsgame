import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


game_images = [rock, paper, scissors]

gamer_1 = int(input(f" Que eliges rock paper or scissors? escribe 0 para rock, 1 para paper y 2 para Scissors.\n"))



if gamer_1 >= 3 or gamer_1 < 0:
  print("Ese numero no es valido tio")
else:

  print (game_images[gamer_1])



  gamer_2= random.randint(0,2)
  print(f"El ordenador eligió")
  print(game_images[gamer_2])




  if gamer_1 == 0 and gamer_2 == 2:
    print("Tu ganas!")
  elif gamer_2 == 0 and gamer_1 ==2:
    print("Tu pierdes!")
  elif  gamer_2 > gamer_1:
    print ("Tu pierdes!")
  elif gamer_1 > gamer_2:
    print("Tu ganas!")
  elif gamer_1 == gamer_2:
    print(" es un empate")
