import unittest
from src.AreaT import Triangulo


class TestTriangulo(unittest.TestCase):
    def test_area_valido(self):
        a = float(input("Ingrese la longitud del lado a del triángulo: "))
        b = float(input("Ingrese la longitud del lado b del triángulo: "))
        c = float(input("Ingrese la longitud del lado c del triángulo: "))

        triangulo = Triangulo(a, b, c)
        area_calculada = triangulo.area()
        area_esperada = 6.0
        self.assertAlmostEqual(area_esperada, area_calculada,
                               msg=f"El área calculada ({area_calculada}) no coincide con el área esperada ({area_esperada})")

    def test_area_invalido(self):
        a = float(input("Ingrese la longitud del lado a del triángulo: "))
        b = float(input("Ingrese la longitud del lado b del triángulo: "))
        c = float(input("Ingrese la longitud del lado c del triángulo: "))

        triangulo = Triangulo(a, b, c)
        area_calculada = triangulo.area()
        self.assertIsNone(area_calculada, msg="Se esperaba que el área fuera None para un triángulo inválido")


if __name__ == '__main__':
    unittest.main()
