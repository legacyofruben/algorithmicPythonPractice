import unittest

def nextPrime(lastPrime):
    div = 1
    num = lastPrime + 1
    while True:
        for j in range(2 , num):
            if num % j == 0:
                div += 1
            if div >= 2:
                break

        if div >= 2:
            div = 1
            num += 1
        else:
            break

    return num

def solution(input):
    if input < 0:
        return 0
    if input == 1:
        return 2

    primes = [[1, 2]]
    input -= 1
    while input != 0:
        primes.append([
            primes[-1][0] + 1,
            nextPrime(primes[-1][1])
        ])
        input -= 1

    return primes[-1][1]


class Test(unittest.TestCase):
    def test_01(self):
        self.assertEqual(solution(6), 13)

    def test_02(self):
        self.assertEqual(solution(10001), 104743)

# # Función para encontrar el siguiente número primo
# def siguiente_primo(num):
#     def es_primo(n):
#         if n < 2:
#             return False
#         for i in range(2, int(n ** 0.5) + 1):
#             if n % i == 0:
#                 return False
#         return True
#
#     num += 1
#     while not es_primo(num):
#         num += 1
#     return num
#
# # Lista inicial para almacenar primos
# primes = [[1, 2]]  # Inicialización similar a `primes.getLast()` en el primer caso
# input = 5          # Número de iteraciones (cambiar según necesidad)
#
# # Bucle while
# while input != 0:
#     last = primes[-1]  # Equivalente a `primes.getLast()`
#     primes.append([
#         last[0] + 1,          # Incrementar el primer valor
#         siguiente_primo(last[1])  # Encontrar el siguiente primo
#     ])
#     input -= 1
#
# # Imprimir el resultado
# print(primes)
