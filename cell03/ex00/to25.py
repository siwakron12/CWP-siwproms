number = int(input("Enter a number less than 25\n"))
if number > 25:
    print("Eror")
else:
    while number < 25:
        print(f"Inside the loop, my variable is {number}")
        number += 1