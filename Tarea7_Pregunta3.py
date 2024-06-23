supermercado={}
producto=input("ingrese un producto: ")

while producto!="":
  
  valor_producto=int(input("ingrese el valor del producto:"))
  supermercado[producto]=valor_producto
  producto=input("ingrese un producto: ")
print(supermercado)

x=int(input("ingrese la cantidad a multiplicar del producto:"))
for producto in supermercado: 
    supermercado[producto]=supermercado[producto]*x
    
print(supermercado)  