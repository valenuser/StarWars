import random

class Nave:
    def __init__(self,nombre,habilidad,velocidad = 0):
        self.piloto = (nombre,habilidad)
        self.velocidad = velocidad


    def aceleracion(self,aceleracion):
        
        if self.velocidad != 0:
            if aceleracion > 0  and aceleracion <= 100:
                numero ='1.'+str(aceleracion)
                numAceleracion = float(numero)
                self.velocidad = int(self.velocidad*numAceleracion)
                return 'Velocidad alcanzada:{}'.format(self.velocidad)
            else:
                return 'La aceleracion debe ser mayor que 0 y menor o igual a 100'
        else:
            self.velocidad = 1
            return 'Motor en marcha!'



    def frenado(self,frenado):
        if self.velocidad != 0:
            if frenado > 0  and frenado <= 100:
                numero ='1.'+str(frenado)
                numFrenado = float(numero)
                self.velocidad = int(self.velocidad/numFrenado)
                return 'Velocidad fue reducida:{}'.format(self.velocidad)
            else:
                return 'La aceleracion debe ser mayor que 0 y menor o igual a 100'
        else:
            return 'Para frenar primero debes encender la nave!'


    def velocidad_en_combate(self):
            return self.velocidad * self.piloto[1]
    


a = Nave('hola',20,50)
b = Nave('chau',30,20)
c = Nave('chau',40)

print('a -------------------')
print(a.aceleracion(10))
print(a.aceleracion(50))
print(a.frenado(20))
print(a.velocidad_en_combate())
print(a.frenado(20))
print(a.velocidad_en_combate())

print('b -------------------')
print(b.aceleracion(10))
print(b.aceleracion(40))
print(b.frenado(20))
print(b.velocidad_en_combate())
print(b.frenado(20))
print(b.velocidad_en_combate())

print('c -------------------')
print(c.aceleracion(60))
print(c.aceleracion(60))
print(c.frenado(20))
print(c.velocidad_en_combate())
print(c.frenado(20))
print(c.velocidad_en_combate())