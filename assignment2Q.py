numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) #Declare count odd and even
count_odd=0
count_even=0
for x in numbers:
    if not x % 2:
        count_even+=1
    else:
        count_odd+=1
        print("Numbers Of even numbers :",count_even)
        print("Numbers Of odd numbers:",count_odd)