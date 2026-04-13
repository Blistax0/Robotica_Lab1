"""controlador_omg controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)

# Motores (para asignar nombres nomas)
left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')

# Configurar motores (modo velocidad)
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

# Variables
step_count = 0

while robot.step(timestep) != -1:
    step_count += 1

    # ===== EXPERIMENTOS =====
    
    # 1. Movimiento recto (SIRVE)
    if step_count < 200:
        vl = 3.0
        vr = 3.0

    # 2. Trayectoria curva (SIRVE)
    elif step_count < 400:
        vl = 2.0
        vr = 4.0

    # 3. Rotacion en el lugar (SIRVE)
    elif step_count < 600:
        vl = 3.0
        vr = -3.0

    # ===== Extension: perturbaciones =====
    elif step_count < 800:
        import random
        vl = 3.0 + random.uniform(-1.5, 1.5)
        vr = 3.0 + random.uniform(-1.5, 1.5)

    # ===== DESAFIO =====
    
    # 4. Linea recta (Funciona bien)
    elif step_count < 1000: 
        vl = 4.0
        vr = 4.0

    # 5. Curva (Funciona bien)
    elif step_count < 1200:
        vl = 2.0
        vr = 4.0
    
    # Pequeña pausa antes del circulo    
    elif step_count < 1250: 
        vl = 0.0
        vr = 0.0

    # 6. Circulo (Funciona bien)
    elif step_count < 1500:
        vl = 2.0
        vr = 4.0 



    # 7. Cuadrado (esto es opcional igual, pero pa probar)
    # de repente funciona, pero otras veces no, no se
    # porque :p
    
    # elif step_count < 1600:
        # if (step_count // 50) % 2 == 0:
            # vl = 4.0
            # vr = 4.0  # avanzar
        # else:
            # vl = 3.0
            # vr = -3.0  # girar 90
               
            
            
    # 7. Cuadrado v2 (Ahora si funciona, es 1795 para que
    # haga el cuadrado)
    elif step_count < 1895:
        lado_steps = 80      # duracion del avance
        giro_steps = 25      # duracion del giro (ajustar)

        ciclo = lado_steps + giro_steps
        fase = step_count % ciclo

        if fase < lado_steps:
            # avanzar recto
            vl = 4.0
            vr = 4.0
        else:
            # girar sobre su eje
            vl = 3.0
            vr = -3.0
            
    else:
        vl = 0
        vr = 0

    # Aplicar velocidades
    left_motor.setVelocity(vl)
    right_motor.setVelocity(vr)

# NO OCUPAR LO DE ACA ABAJO
# Main loop:
# - perform simulation steps until Webots is stopping the controller
# while robot.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
#     pass

# Enter here exit cleanup code.
