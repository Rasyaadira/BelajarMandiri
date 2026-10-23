import random 
import time

Player_health = int(100)
Monster_Health = int(100)
MaxHp = 100
MinHp = 0
def RNGNumAttack():
     return random.randint(10,35)
def RNGNumAttackMonster():
     return random.randint(25,35)
def RNGNumHeal():
     return random.randint(10,25)
def RNGNumHealMonster():
     return random.randint(15,25)
# def Get_HealthBarVisualPlayer():
#     return round(Player_health / 10)
# def Get_HealthBarVisualMonster():
#     return round(Monster_Health / 10)
# def VisualMakerPlayer():
#     HealthBarVisual = Get_HealthBarVisualPlayer()
#     HealthBarVisual = "#" * Get_HealthBarVisualPlayer
#     HealthBarVisual2Kosong = "-" * (10-Get_HealthBarVisualPlayer)
# def VisualMakerMonster():
#     HealthBarVisual = Get_HealthBarVisualMonster()
#     HealthBarVisual = "#" * Get_HealthBarVisualMonster
#     HealthBarVisualKosong = "-" * (10-Get_HealthBarVisualMonster)
def PrintHealthBar():
    # VisualMakerPlayer()
    # VisualMakerMonster()
    print("Current Enemy Health: " +str(Monster_Health)+"\nCurrent Health : " +str(Player_health)+ "\n")
def Get_NRGEnemy():
    return random.choices([1,2,3], weights=[70, 20, 10])[0]




while Player_health > 0 and Monster_Health > 0:
    PlayerInput = int(input("1. Attack \n2. Heal\n3. Exit \nSelect option : "))
    if PlayerInput == 1 :
        print("\033[H\033[J", end="") 
        Attack = RNGNumAttack() 
        Monster_Health -= Attack
        PrintHealthBar()   

    elif PlayerInput == 2 :
        print("\033[H\033[J", end="")  
        heal = RNGNumHeal()
        if Player_health >= 100 :
            print("Health player sudah maximal")
        elif Player_health < 100 :
            Player_health += heal
            if Player_health > 100 :
                Player_health = 100
        PrintHealthBar()

    elif PlayerInput == 3 :
        print("\033[H\033[J", end="")  
        print("Terima kasih sudah bermain")
        break

    else :
        print("pilihan tidak valid")

    if Monster_Health < 0 :
        print("pahlawan telah menaklukan monster")
        break

    
    time.sleep(1)
    print("Monster Melawan!!!")
    RNGEnemy = Get_NRGEnemy()

    if RNGEnemy == 1:
        print("\033[H\033[J", end="")  
        print("Monster menyerang !!!\n")
        Attack = RNGNumAttackMonster()
        Player_health -= Attack
        PrintHealthBar()

    elif RNGEnemy == 2:
        print("\033[H\033[J", end="")  
        print("Monster heal dirinya sendiri\n")
        Heal = RNGNumHealMonster()
        if Monster_Health >= 100 :
            print("Health Monster sudah maximal")
        elif Monster_Health < 100 :
            Monster_Health += Heal
            if Monster_Health > 100 :
                Monster_Health = 100
        PrintHealthBar()

    elif RNGEnemy == 3:
        print("\033[H\033[J", end="")  
        print("Monster tidak melakukan apa apa\n")
        PrintHealthBar()

    if Player_health < 0:
        print("monster telah mengalahkan sang pahlawan")
        break

        # setelah blok if PlayerInput == 1/2/3
    

    
    

    
# monster menyerang

    


