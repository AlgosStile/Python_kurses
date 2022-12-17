weight = float(input('Какой у вас вес: '))
height = float(input('Какой у вас рост: '))
x = weight // (height ** 2)
if x < 18.5:
    print("Underweight")
elif x >= 18.5 and x < 25:
    print("Normal")
elif x >= 25 and x < 30:
    print("Overweight")
elif x >= 30:
    print("Obesity")
