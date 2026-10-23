health = int(input("enter your heart rn : "))
healthbar = round(health/float(10))
Maxhp = 100
Minhp = 0

if health < Minhp :
    print("Anda sudah lama mati")
elif health == 0 :
    print("Anda mati")
elif health > Maxhp :
    print("Error")
elif health >= Minhp and health <= Maxhp :   
    healthbarVisual = "#"*healthbar
    healthbarKosong = ("-"*(10-healthbar))
    print("Hp : [" +healthbarVisual+ healthbarKosong+"] " +str(health)+"%")
    
