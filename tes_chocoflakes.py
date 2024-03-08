import random

# Lista de preguntas y respuestas
preguntas = [
    (
    "¿Qué es el control PWM?",
    [
        "a) Sistema que controla, mediante pulsos, la velocidad del ventilador de la CPU, de esa manerase puede ajustar dicha velocidad a la temperatura del microprocesador.",
        "b) Sistema que controla, mediante impulsos magnéticos, la velocidad del ventilador de la CPU, de esa manerase puede ajustar dicha velocidad a la temperatura del microprocesador.",
        "c) Sistema que controla, mediante pulsos, la velocidad del ventilador de la RAM, de esa manerase puede ajustar dicha velocidad a la temperatura del microprocesador.",
        "d) Sistema que controla, mediante pulsos, el Power Motor de la CPU.",
    ],
    "a"
),
    (
    "Cuando elmicroprocesador esté más caliente,...",
    [
        "a) ..., dará menos vueltas, y cuando esté más frío, dará más.De esa manera también se reduce el ruido del equipo.",
        "b) ..., dará más vueltas, y cuando esté más frío, dará menos.De esa manera también se reduce el ruido del equipo.",
        "c) ..., dará más vueltas, y cuando esté más frío, dará más aún.De esa manera también se reduce el ruido del equipo.",
        "d)...girará sin parar hasta explotar, pero se reducirá el ruido del equipo",
    ],
    "b"
),
    (
    "¿Qué es el chipset?",
    [
        "a) Conjunto de chips situados en el microprocesador de un equipo como el control de la memoria, el procesador, los puertos USB, PCIe, etc., que realizan funciones de la misma.",
        "b) Conjunto de chips situados en la placa base de un equipo como el control de la memoria, el procesador, sin incluir los puertos USB, PCIe, etc., que realizan funciones de la misma.",
        "c) Conjunto de chips situados en la placa base de un equipo como el control de la memoria, el procesador, los puertos USB, PCIe, etc., que realizan funciones de la misma.",
        "d) Conjunto de chips situados en el microprocesador base de un equipo como el control de la memoria, el procesador, los puertos USB, PCIe, etc., que realizan funciones de la misma.",
    ],
    "c"
),
    (
    "¿Qué es Fan?",
    [
        "a) Ventilador.",
        "b) Tu amiga de la infancia.",
        "d) Fan-ática",
        "c) Disipador",
    ],
    "a"
),
    (
    "¿Qué es el FSB?",
    [
        "a) Un FAKIN USB",
        "b) Front Side Bus",
        "c) Frontal System Bus",
        "d) Fastest Security Balance",
    ],
    "b"
),
    (
    "¿Cuál es la función principal del FSB?",
    [
        "a) Une el Front Side Bus con la memoria volátil RAM o VRAM",
        "b) Conecta el Bus del Sistema con el microprocesador.",
        "c) Conecta los elementos del sistema (microprocesador,memoria, chipset y PCI x 16).",
        "d) Conecta los elementos más rápidos del sistema (microprocesador,memoria, chipset y PCI x 16).",
    ],
    "d"
),
    (
    "En relación a la pasta térmica...",
    [
        "a) Sustancia que se coloca entre el microprocesador u otro chip y el disipador para eliminar cualquier hueco que pueda haber entre ambos.",
        "b) Sustancia que se coloca entre el microprocesador y el disipador.",
        "c) Se puede sustituir por otras pastas más baratas, incluso la dental, aunque no son tan eficientes",
        "d) Se puede sustituir por otras pastas más baratas, como la pasta cerámica, aunque no son tan eficientes",
    ],
    "a"
),
    (
    "La pasta térmica, al ser más conductiva que el aire, refrigerará más el circuito integrado.",
    [
        "v) Verdadero",
        "f) Falso",
    ],
    "v"
),
    (
    "La pasta térmica, al ser menos conductiva que el aire, refrigerará menos el circuito integrado.",
    [
        "v) Verdadero",
        "f) Falso",
    ],
    "f"
),
    (
    "¿Qué es un slot?",
    [
        "a) Un ventilador.",
        "b) Ranura o espacio para insertar un componente.",
        "c) Zócalo donde se introduce el microprocesador.",
        "d) Hueco donde se introducen las Memorias RAM.",
    ],
    "b"
),
    (
    "¿Qué es una Workstation?",
    [
        "a) Ranura o espacio para insertar un componente.",
        "b) Equipo de sobremesa con alta capacidad.",
        "d) Equipo que se encuentra a caballo entre un servidor y un equipo de sobremesa.",
        "c) Sistema que controla, mediante pulsos, la velocidad del ventilador de la CPU, de esa manerase puede ajustar dicha velocidad a la temperatura del microprocesador.",
    ],
    "d"
),
    (
    "¿Cuál de las siguientes afirmaciones, en relación con las Workstations, es verdadera?",
    [
        "a) Se diferencia de los servidores por tener unos procesadores ni una memoria específicos. ",
        "b) Al igual que los servidores, no tiene unos procesadores ni una memoria específicos.",
        "c) Se diferencia de los servidores por no tener unos procesadores ni una memoria específicos.",
        "d) Al igual que los servidores, tiene unos procesadores y una memoria específicos",
    ],
    "c"
),
    (
    "¿Qué significan las siglas “ZIF”?",
    [
        "a) Zero Inertial Force",
        "b)  Zero Interference Factor",
        "c) Zero Impact Frequency",
        "d) Zero Insertion Force",
    ],
    "d"
),
    (
    "¿Los zócalos ZIF perminten instalar el procesador sin hacer fuerza sobre el mismo?",
    [
        "v) Verdadero",
        "f) Falso",

    ],
    "v"
),
    (
    "¿Los zócalos ZIF perminten instalar el procesador haciendo presión sobre el mismo para que quede perfectamente anclado?",
    [
        "v) Verdadero",
        "f) Falso",

    ],
    "f"
),
    (
    "¿Cual de las siguientes afirmaciones es correcta?",
    [
        "a) Mantener los componentes organizados y limpios mejora la eficiencia.",
        "b) La limpieza es importante solo en un lugar trabajo.",
        "c) El desorden no afecta la productividad.",
        "d) No es necesario limpiar regularmente los equipos informáticos.",
    ],
    "a"
),
    (
    "¿Cuál es la recomendación para limpiar equipos del cliente que llegan con polvo?",
    [
        "a) Limpiarlos en cualquier lugar, sin importar la ventilación.",
        "b) Aspirar o limpiarlos fuera de la instalación, en un sitio ventilado.",
        "c) Dejar el polvo tal como está.",
        "d) Utilizar los productos adecuados para eliminar el polvo.",
    ],
    "b"
),
    (
    "¿Cuál de las siguientes afirmaciones es correcta en relación con las herramientas y componentes en un entorno de trabajo?",
    [
        "a) El etiquetado no es relevante para las herramientas.",
        "b) Las herramientas y componentes deben estar donde el trabajador desee.",
        "c) Es importante mantener las herramientas y componentes organizados y etiquetados.",
        "d) No es necesario etiquetar las herramientas y componentes si los tienes perfectamente organizados",
    ],
    "c"
),
    (
    "¿Cuál de las siguientes afirmaciones es correcta en relación con la seguridad en el lugar de trabajo?",
    [
        "a)  Bloquear las salidas de incendio es aceptable en situaciones de emergencia.",
        "b)  Tapar los extintores no afecta la seguridad contra incendios.",
        "c)  No es obligatorio prestar atención a las salidas de incendio.",
        "d)  No bloquear las zonas de paso con material es importante para la seguridad.",
    ],
    "d"
),
    (
    "¿Cual de las siguentes afirmaciones no es importante en un puesto de montaje?",
    [
        "a) No bloquear las salidas de incendio",
        "b) No bloquear las zonas de paso con material",
        "c) No tapar los extintores u otro sistema contraincendios.",
        "d) Todas las anteriores se consideran importantes",
    ],
    ""
),
    (
    "¿?",
    [
        "a) ",
        "b) ",
        "c) ",
        "d) ",
    ],
    ""
),
    (
    "¿?",
    [
        "a) ",
        "b) ",
        "c) ",
        "d) ",
    ],
    ""
),
    (
    "¿?",
    [
        "a) ",
        "b) ",
        "c) ",
        "d) ",
    ],
    ""
),


    ]


######################################################################################

# Mezclar las preguntas en orden aleatorio
random.shuffle(preguntas)

# Función para calcular la equivalencia de la puntuación en una nota sobre 10
def calcular_equivalencia_puntuacion(puntuacion, total_preguntas):
    escala_maxima = 10.0
    equivalencia = (puntuacion / total_preguntas) * escala_maxima
    return equivalencia

# Función para realizar el test
def realizar_test():
    puntaje = 0
    total_preguntas = len(preguntas)

    for i, (pregunta, opciones, respuesta) in enumerate(preguntas, 1):
        print(f"\nPregunta {i}: {pregunta}")
        random.shuffle(opciones)
        for opcion in opciones:
            print(opcion)
        respuesta_usuario = input("\nTu respuesta: ").strip().lower()
        if respuesta_usuario == respuesta:
            print("-------------------------")
            print("¡Respuesta correcta! ✔✔✔✔✔✔✔✔✔")
            print("-------------------------\n")
            puntaje += 1
        else:
            print("-------------------------")
            print(f"✖✖✖✖✖✖✖ Respuesta incorrecta. La opción correcta es: {respuesta}\n")
            print("-------------------------\n")
    
    equivalencia = calcular_equivalencia_puntuacion(puntaje, total_preguntas)
    
    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print(f"  Has completado el test, {nombre_usuario}. Puntuación final: {puntaje}/{total_preguntas}")
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    print("                                                  ==========")
    print(f"Tu equivalencia de nota sobre 10 es ━━━━━━━━━━━━❯✷ {equivalencia:.2f}/10 ✷❮━━━━━━━━━━━━")
    print("                                                  ==========")

# Solicitar el nombre del usuario
nombre_usuario = input("Bienvenido al test de Fundamentos. Por favor, introduce tu nombre: ")

# Solicitar el número de preguntas
num_preguntas = int(input("¿Cuántas preguntas deseas en el test? "))
while num_preguntas > len(preguntas):
    print(f"Lo siento, solo hay {len(preguntas)} preguntas disponibles.")
    num_preguntas = int(input("Por favor, elige un número igual o menor: "))

# Mezclar las preguntas en orden aleatorio
random.shuffle(preguntas)
preguntas = preguntas[:num_preguntas]

# Ejecutar el test
print(f"Muy bien, {nombre_usuario}! Comencemos con tu test de Fundamentos con {num_preguntas} preguntas.")
realizar_test()
