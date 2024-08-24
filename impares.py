print ("----- NÚMEROS IMPARES ------")

i = int (input ("Até qual número que analisar? "))

for x in range (i):
    if x % 2 == 0:
        continue
    print (x)