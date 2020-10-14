import math

def distancia_euclidiana(x_1, y_1, x_2, y_2):
    return math.sqrt((x_2 - x_1)*(x_2 - x_1) + (y_2 - y_1)*(y_2 - y_1))

print(distancia_euclidiana(7, 5, 4, 1), '\n')
print(distancia_euclidiana(100, 200, 200, 1), '\n')
print(distancia_euclidiana(500, 500, 200, 200), '\n')
