from transporte.automovil import automovil
from transporte.vehiculo import vehiculo
from transporte.automovil import automovil

veh1 = vehiculo("123", 4, 5)
print(f"El numero de asientos es de: {veh1.getNroasientos()}")

veh1.setNroasientos(8)
print(f"El numero de asientos es de: {veh1.getNroasientos()}")

veh1.setNroruedas(1)
veh1.Arrancar()

auto1 = automovil("876", 4, 4, False, 4)
print(f"El numero de puertas es de: {auto1.getNropuertas()}")