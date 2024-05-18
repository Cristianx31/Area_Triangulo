import math

class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        # Verificar si los lados forman un triángulo válido
        if self.es_triangulo_valido():
            # Calcular el semiperímetro
            s = (self.a + self.b + self.c) / 2
            # Calcular el área usando la fórmula de Herón
            area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
            return area
        else:
            print("Los lados ingresados no forman un triángulo válido.")
            return None

    def es_triangulo_valido(self):
        # Verificar la desigualdad triangular
        return self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a

