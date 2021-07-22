weight = int(input("Enter your weight: "))
unit= input("(l)bs or (k)g: ")
if unit == 'k':
    converted = weight / 0.454
    print(f"{converted} Pounds")
elif unit == ('l'):
    converted = weight * 0.454
    print(f"{converted} Kilos")
else:
    print("INVALID!")



