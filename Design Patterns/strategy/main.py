class PrimeiroCalculo:
    def calcula(self, valor: int) -> int:
        return valor ** 2

class SegundoCalculo:
    def calcula(self, valor: int) -> int:
        return valor ** 5

class TerceiroCalculo:
    def calcula(self, valor: int) -> int:
        return valor // 3

class Calculadora:
    def efetuar_calculo(self, valor, regra) -> int:
        return regra.calcula(valor)

if __name__ == '__main__':
    calculadora = Calculadora()
    calc_1 = calculadora.efetuar_calculo(5, PrimeiroCalculo())
    calc_2 = calculadora.efetuar_calculo(5, SegundoCalculo())
    calc_3 = calculadora.efetuar_calculo(5, TerceiroCalculo())

    print(calc_1, calc_2, calc_3, sep=" || ")