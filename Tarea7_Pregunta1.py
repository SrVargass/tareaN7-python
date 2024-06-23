lista=[]
x=0
while x!=10:
    numero=int(input("ingrese un numero:"))
    lista.append(numero)
    x=x+1
    
print("la lista original:",lista)     
lista.reverse()
print("la lista invertida es:",lista)