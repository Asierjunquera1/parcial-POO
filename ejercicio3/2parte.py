from clases import Cuenta_bancaria
from clases import Cuenta_plazo_fijo
from clases import Cuenta_Vip
import random
from datetime import datetime, timedelta


ID_cuenta1=int(input("Escriba aqui su ID (debe ser un numero entero incremental):"))
nombre_titular_cuenta1=input("Escriba el nombre del titular:")
fecha_aperura_cuenta1=datetime.now()- timedelta(days=random.randint(1, 365))
fecha_vencimiento_cuenta1=datetime.now() + timedelta(days=random.randint(1, 365))
numero_cuenta_cuenta1=random.randint(100000000000, 999999999999)
saldo_cuenta1=10000

ID_cuenta2=int(input("Escriba aqui su ID (debe ser un numero entero incremental):"))
nombre_titular_cuenta2=input("Escriba el nombre del titular:")
fecha_aperura_cuenta2=datetime.now()- timedelta(days=random.randint(1, 365))
fecha_vencimiento_cuenta2=datetime.now() + timedelta(days=random.randint(1, 365))
numero_cuenta_cuenta2=random.randint(100000000000, 999999999999)
saldo_cuenta2=10000

ID_cuenta3=int(input("Escriba aqui su ID (debe ser un numero entero incremental):"))
nombre_titular_cuenta3=input("Escriba el nombre del titular:")
fecha_aperura_cuenta3=datetime.now()- timedelta(days=random.randint(1, 365))
fecha_vencimiento_cuenta3=datetime.now() + timedelta(days=random.randint(1, 365))
numero_cuenta_cuenta3=random.randint(100000000000, 999999999999)
saldo_cuenta3=10000
saldo_negativo_maximo=int(input("Cual es el saldo maximo negativo?"))


cuenta1=Cuenta_bancaria(ID_cuenta1, nombre_titular_cuenta1, fecha_aperura_cuenta1, numero_cuenta_cuenta1, saldo_cuenta1)
cuenta2=Cuenta_plazo_fijo(Cuenta_bancaria(ID_cuenta2, nombre_titular_cuenta2, fecha_aperura_cuenta2, numero_cuenta_cuenta2, saldo_cuenta2, datetime.now(), fecha_vencimiento_cuenta2))
cuenta3=Cuenta_Vip(Cuenta_bancaria(ID_cuenta3, nombre_titular_cuenta3, fecha_aperura_cuenta3, numero_cuenta_cuenta3, saldo_cuenta3, saldo_negativo_maximo))



cuenta1.ingresar_dinero(575)
cuenta2.retirar_dinero(78)
cuenta3.transferir_dinero(2000, cuenta1)
