class Cuenta_bancaria:
    def __init__(self, ID, nombre_titular, fecha_apertura, numero_cuenta, saldo):
        self.ID=ID
        self.nombre_titular=nombre_titular
        self.fecha_apertura=fecha_apertura
        self.numero_cuenta=numero_cuenta
        self.saldo=saldo
    
    def retirar_dinero(self, cantidad):
        if cantidad>self.saldo:
            print("No tienes suficiente dinero en tu cuenta")
        else:
            self.saldo-=cantidad
            print("Se ha retirado la siguiente cantidad de euros:", cantidad)

    def ingresar_dinero(self, cantidad):
        self.saldo+=cantidad
        print("Se ha ingresado la siguiente cantidad de euros:", cantidad)

    def transferir_dinero(self, cantidad, otra_cuenta):
        if cantidad>self.saldo:
            print("No tienes suficiente dinero en tu cuenta")
        else:
            self.saldo-=cantidad
            otra_cuenta.saldo+=cantidad
            print("Se han transferido:", cantidad, "euros a la siguiente cuenta:", otra_cuenta)


class Cuenta_plazo_fijo(Cuenta_bancaria):
    def __init__(self, ID, nombre_titular, fecha_apertura, numero_cuenta, saldo, fecha_actual, fecha_vencimiento):
        super().__init__(ID, nombre_titular, fecha_apertura, numero_cuenta, saldo)
        self.fecha_actual=fecha_actual
        self.fecha_vencimiento=fecha_vencimiento

    def retirar(self, cantidad):
        if self.fecha_actual<self.fecha_vencimiento:
            penalizacion=cantidad*0,5
            cantidad_total=cantidad+penalizacion
            self.retirar_dinero(cantidad_total)
        else:
            self.retirar_dinero(cantidad)


class Cuenta_Vip(Cuenta_bancaria):
    def __init__(self, ID, nombre_titular, fecha_apertura, numero_cuenta, saldo, saldo_negativo_maximo):
        super().__init__(ID, nombre_titular, fecha_apertura, numero_cuenta, saldo)
        self.saldo_negativo_maximo=saldo_negativo_maximo
    
    def retirar(self, cantidad):
        cantidad_puede_retirar=self.saldo+self.saldo_negativo_maximo
        if cantidad>cantidad_puede_retirar:
            print("No tienes suficiente dinero en tu cuenta")
        else:
            self.saldo-=cantidad
        
