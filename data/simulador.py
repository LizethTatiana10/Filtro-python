#construir un codigo de python que genere 
#1000 datos asociados a las ventas de un local del ropa 

#MOCK

from datetime import datetime, timedelta
import random

def generar_ventas():


    productos=[
        {"nombre":"camiseta polo","precio":150000},
        {"nombre":"pantalon jean","precio":250000},
        {"nombre":"chaqueta","precio":300000},
        {"nombre":"zapatos","precio":200000},
        {"nombre":"bufanda","precio":50000},
        {"nombre":"falda","precio":180000},
        {"nombre":"blusa","precio":120000},
        {"nombre":"sueter","precio":220000},
        {"nombre":"abrigo","precio":350000},
        {"nombre":"pijama","precio":90000},
    ]

    tallas=["S","M","L","XL"]
    vendedores=["Ana Montoya","Luis Padilla","Dulce Rivas","Marta Osorio","Lizeth Palacios"]

    tiendas=["Centro Comercial Unicentro","Centro Comercial Santafe","Centro Comercial Andino","Centro Comercial Titan","Centro Comercial Gran Estacion","Centro Comercial Plaza de las Americas","Centro Comercial Calima","Centro Comercial Viva Envigado"]

    fechaInicio=datetime(2025,1,1)

    #generando 1000 ventas 
    ventas=[]
    for _ in range(1000):
        productos=random.choice(productos)
        cantidad=random.randint(1,8)
        fecha=fechaInicio + timedelta(days=random.randint(0,90))
        ventas.append(
          {
                "producto":productos["nombre"],
                "precioUnitario":productos["precio"],
                "talla":random.choice(tallas),
                "tienda":random.choice(tiendas),
                "cantidad":cantidad,
                "vendedor":random.choice(vendedores),
                "total":cantidad*productos["precio"]
           
            }
        )
    return(ventas)

#llamando la funcion generadora de datos
generar_ventas()