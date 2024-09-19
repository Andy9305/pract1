'''
Practica1
Problema 1
estudiante: Andrea Sofía Figueroa López
Fecha: 19/09/2024
'''
class Figueroa_Persona:
    def __init__(self, Figueroa_nombre, Figueroa_distancia_recorrida):
        self.Figueroa_nombre=Figueroa_nombre
        self.Figueroa_distancia_recorrida=Figueroa_distancia_recorrida
    def caminar(self):
        self.Figueroa_distancia_recorrida+=2

class Figueroa_Atleta(Figueroa_Persona):
    def __init__(self, Figueroa_nombre, Figueroa_distancia_recorrida, Figueroa_calorias_consumidas):
        super(). __init__(Figueroa_nombre, Figueroa_distancia_recorrida)
        self.Figueroa_calorias_consumidas=Figueroa_calorias_consumidas
    def Figueroa_entrenar(self):
        self.Figueroa_distancia_recorrida+=10
    def Figueroa_competir(self):
        self.Figueroa_distancia_recorrida+=20
    def __str__(self):
        return ('Figueroa_Atleta(Figueroa_nombre:{}, Figueroa_distancia_recorrida:{}, Figueroa_Figueroa_calorias_consumidas)'.format(self.Figueroa_nombre, self.Figueroa_distancia_recorrida, self.Figueroa_calorias_consumidas))


#Prueba
Per1= Figueroa_Atleta('Julieta',10 ,40)
Per1.Figueroa_entrenar()
Per1.Figueroa_entrenar()
Per1.Figueroa_competir()
print('Per1:  '+ Per1.Figueroa_nombre + '  Distancia Recorrida:'+ str(Per1.Figueroa_distancia_recorrida))