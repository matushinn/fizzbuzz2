number = int(input("一つの自然数を入れてね:"))

if number % 15 == 0:
    output = "fizzbuzz"
elif number % 3 == 0:
    output = "Fizz"
elif number % 5 == 0:
    output = "Buzz"

else:
    output = str(number)

print(output)
