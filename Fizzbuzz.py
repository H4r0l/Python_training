# This problem prints Fizz for every number divisible by 3 and Buzz if is divisible by 5

for i in range (1, 100):
    if i % 3==0 and i % 5 == 0:
        print("FizzBuzz")
    if i % 3 == 0:
        print("Fizz")
    if i % 5 == 0: 
        print("Buzz")
    if i % 3 !=0 and i % 5 != 0:
        print(i)

    