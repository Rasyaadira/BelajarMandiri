import time 

age = input("seller : how old are u? ")
time.sleep(2)
price = 19.95
first_name = input("seller : who are u? ")
is_online = False
endprice = price - price*(int(age)/100)
print("seller : because we have sale which you get a discount depend of ur age soooo congrats")
print("seller : The name is buyer is "  +first_name+ " and its his birth day, today he gonna be " +str(age)+ 
    "years old and the price of the cake is " +str(endprice)+ "$" ", ur normal price is " +str(price)+ "$") 