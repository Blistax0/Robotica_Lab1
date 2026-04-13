# Laboratorio 1: Simulación de Robot Móvil Diferencial en Webots

## Descripción

En este laboratorio se implementó el control de un robot móvil diferencial (e-puck) utilizando el simulador Webots y el lenguaje Python.

El objetivo principal fue comprender cómo las velocidades de las ruedas izquierda (vl) y derecha (vr) afectan el movimiento del robot, permitiendo generar distintos tipos de trayectorias como movimiento recto, curvas y rotaciones.

El modelo cinemático del robot está dado por:

- v = (vr + vl) / 2
- ω = (vr - vl) / L

donde:

- v es la velocidad lineal
- ω es la velocidad angular
- L es la distancia entre ruedas

## Implementación

Se utilizó el controlador `controlador_omg.py` , en el cual se controlan directamente los motores del robot:

- Motor izquierdo → vl
- Motor derecho → vr

El control se realizó mediante la asignación de velocidades en función del tiempo (step_count), permitiendo ejecutar distintos experimentos de forma secuencial.

## Cómo ejecutar la simulación

1. Abrir Webots
2. Cargar el mundo que contiene el robot e-puck
3. Asignar el controlador `controlador_epuck_lab1.py` al robot
4. Ejecutar la simulación

## Experimentos realizados

### 1. Movimiento recto

Se configuró la velocidad de la rueda izquierda a la misma que la de la rueda derecha:

- vl = vr

Resultado:
El robot se desplazó en línea recta sin desviaciones.

### 2. Trayectoria curva

Se configuró a mayor velocidad la rueda derecha a comparacion de la rueda izquierda para simular una curva:

- vl ≠ vr

Resultado:
El robot describió una trayectoria curva, girando hacia el lado de la rueda con menor velocidad.

### 3. Rotación en el lugar

Se configuró:

- vl = -vr

Resultado:
El robot rotó sobre su propio eje sin desplazamiento lineal.

## Extensión: perturbaciones

Se introdujeron variaciones aleatorias en las velocidades. Para esto utilizamos la libreria random:

- vl = 3.0 ± ruido
- vr = 3.0 ± ruido

Resultado:
La trayectoria dejó de ser perfectamente recta, mostrando desviaciones que simulan errores en actuadores reales y/o terrenos irregulares. Esto solo se probo para una trayectoria recta para comparar los resultados entre un tramo ideal y otro con variaciones.

## Desafíos implementados

Luego realizamos algunos desafios utilizando lo que ya probamos en los experimentos realizados, siendo estos una trayectoria en linea recta, una curva, un circulo y por ultimo un cuadrado:

### Línea recta

Movimiento estable con velocidades constantes iguales.

### Curva

Trayectoria controlada mediante diferencia de velocidades.

### Círculo

Se mantuvo una diferencia constante entre velocidades, generando una trayectoria circular.

### Cuadrado (opcional)

Se implementó un control basado en ciclos de:

- Avance recto
- Giro en el lugar

Resultado:
El robot, aunque no funcione a la perfeccion esta funcion, intenta aproximar un cuadrado, ajustando los tiempos de giro para acercarse a 90°.

## Resultados obtenidos

En esta sección se presentan los resultados observados durante la ejecución de los distintos experimentos en el simulador Webots. A partir de la variación en las velocidades de las ruedas, fue posible analizar cómo cambia el comportamiento del robot y verificar empíricamente el modelo cinemático.

- Se verificó el comportamiento esperado del modelo cinemático del robot diferencial.
- Las trayectorias coinciden con la teoría:
  - velocidades iguales → línea recta
  - velocidades distintas → curva
  - velocidades opuestas → rotación

- Las perturbaciones afectan directamente la precisión del movimiento.
- Las figuras (círculo y cuadrado) dependen fuertemente del ajuste de tiempos y velocidades.

## Preguntas de análisis

En esta sección, como grupo analizamos los resultados obtenidos durante la simulación, relacionando lo observado con el comportamiento esperado de un robot diferencial. A partir de los experimentos realizados, pudimos notar que, en general, el modelo teórico se cumple bastante bien, aunque en algunos casos aparecen pequeñas variaciones debido a la simulación y al ajuste de parámetros.

### ¿Qué ocurre cuando ambas ruedas tienen la misma velocidad?

El robot se mueve en línea recta, ya que no existe velocidad angular.

### ¿Cómo cambia la trayectoria cuando las velocidades son diferentes?

Se genera una trayectoria curva, cuyo radio depende de la diferencia entre velocidades.

### ¿Qué ocurre cuando una rueda gira en sentido opuesto a la otra?

El robot rota sobre su eje, generando movimiento angular sin desplazamiento lineal.

### ¿Qué tipo de movimiento permite dibujar un círculo?

Velocidades distintas pero constantes en ambas ruedas permiten generar una trayectoria circular.

## Video del robot

A continuacion se muestra un video del funcionamiento del robot utilizando el controlador que programamos.

### [Link del video](https://drive.google.com/file/d/1uyaXayvmDTJUAyOrqlM-JMtuuYFQL6r9/view?usp=sharing)

## Conclusión

El laboratorio nos permitió comprender de manera práctica el comportamiento de un robot diferencial, evidenciando la relación directa entre las velocidades de las ruedas y la trayectoria generada.

Además, se observó cómo pequeñas perturbaciones pueden afectar significativamente el movimiento, lo cual es relevante en sistemas reales.
