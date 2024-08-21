import math

puntos = [(1, 2), (2, 3), (0, 1), (3, 3)]


distancia_al_origen = lambda punto: math.hypot(punto[0], punto[1])

puntos_ordenados = sorted(puntos, key=distancia_al_origen)

print(puntos_ordenados)  