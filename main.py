 #COMO USAR PANDAS PARA CREAR FILTROS

#1. importarlo
import pandas as pd # type: ignore
#2. traer los datos 
from data.simulador import generar_ventas
#3. convertir los datos a un DATAFRAME 
dataframe=pd.DataFrame(generar_ventas())
#4. aplicar los filtros(5)
#print(dataframe)
#yo como administrador de la tienda quiero obtener las ventas de enero 
FiltroUno=dataframe.query("vendedor == 'Dulce Rivas'")
#print(FiltroUno)
#yo como administrador de la tienda quiero ver ventas con mas de tres productos
FiltroDos=dataframe.query("cantidad >= 3")
#print(FiltroDos)
#yo como administrador de la tienda quiero ver ventas por valores de mas de 900 mil
FiltroTres=dataframe.query("total >= 900000")
print(FiltroTres)
#yo como administrador de la tienda quiero ver las ventas de las camisetas polo
FiltroCuatro=dataframe.query("producto == 'camiseta polo'")
#print(FiltroCuatro)
#yo como administrador de la tienda quiero ver las ventas de los productos que menos venden
FiltroCinco=dataframe.query("producto == 'pijama'")
print(FiltroCinco)