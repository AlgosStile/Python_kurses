lst = [param * param for param in range(5)]
for el in lst:
    print(el)
# ++++++++++++++++++ #
generator = (param * param for param in range(5))
for el in generator:
      print(el)
# Генератор итерируемый объект в котором значения не хранятся в памяти,
# а формируются эти значения в процессе обращения к ним!