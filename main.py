"""
Numeros divisibles 3 = Fizz 
Numeros divisibles 5 = Buzz
Numeros divisibles 2 y 5 = Fizzbuzz"
"""
""" Se utliza la función range que me permite introducir parametro de inicio y parametro final,
sin embargo, siempre llega hasta un numero antes del parametro final, por ende se le debe poner un numero mas."""

for num in range(1,1001):
    if num % 3 == 0 and num % 5 == 0:
        print("Fizzbuzz")
    elif num % 3 == 0:
        print("Fizz")  
    elif num % 5 == 0:
        print("Buzz") 
    else:
        print(num)         

