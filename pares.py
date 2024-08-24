print ("----- NÚMEROS PARES ------")
#i = int (input ("Até qual número quer percorrer? "))

for x in range (201): #use range (i) para dar opção para o usuario de escolher o número
    if x % 2 == 1:
        continue
    print (x)
