inventory = ["Sword", "Pickaxe", "Axe", "steak", "Torch", "Block", "Bow", "arrow", "arrow"]

i = 0 
arrow = 0
while i < len(inventory): 
    if inventory[i] == "arrow":
        arrow += 1
    i += 1
print("Jumlah Arrow : " +str(arrow))

CleanInventory = []
i = 0 

