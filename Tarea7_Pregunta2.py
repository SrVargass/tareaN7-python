lista=[]

N=input("ingrese un nombre:")
while N!="":
   lista.append(N)
   N=input("ingrese un nombre:") 
print(lista)

for caracter in lista:
    cont=0
    cont1=0
    for x in caracter:
        if x=="a":
         cont+=1
        if x=="A":
         cont1+=1
    print("la palabra",caracter,"tiene (a):",cont,"caracteres y (A):",cont1)
            
