amount = 0
if hours <= 20:  #2 Lakh 50 thousand
    amount = amount + 500
    print("hours lost is less than 20")

else:
    amount = amount + 750
    print("hours lost is equal or more than 20")

print( amount, "AUD is paid!")
