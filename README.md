# Guardians of the Ancient Kingdom

## 1. Descripción del proyecto

Guardians of the Ancient Kingdom es una aplicación desarrollada en Python que simula un sistema de combate entre personajes de un reino antiguo. El proyecto aplica los principios de la programación orientada a objetos (POO), incluyendo abstracción, encapsulamiento, herencia y polimorfismo.

El sistema permite crear diferentes tipos de personajes, ejecutar ataques con habilidades particulares, administrar los puntos de vida y realizar combates hasta determinar un ganador o un empate técnico.

## 2. Estructura del proyecto

El proyecto está organizado en los siguientes archivos:

- `personajes.py`: contiene las clases de los personajes, sus habilidades y la lógica del combate.
- `main.py`: contiene la ejecución del programa y los casos de prueba.
- `README.md`: contiene la documentación del proyecto.
- `diagrama_uml.puml`: contiene el código fuente del diagrama UML.

## 3. Clases principales

### Personaje

Es una clase abstracta que define las características y comportamientos comunes de todos los personajes. Administra el nombre, la vida, el ataque y la defensa mediante propiedades que validan los datos.

También implementa los métodos `recibir_danio()`, `esta_vivo()` y `mostrar_estado()`. El método `atacar()` es abstracto y debe implementarse en cada clase derivada.

### Guerrero

Representa un personaje especializado en ataques físicos. Su daño se calcula multiplicando el ataque por 1.2, redondeando hacia abajo y restando la defensa del objetivo, sin permitir daños negativos.

### Mago

Representa un personaje que realiza ataques mágicos. Su daño corresponde al valor de ataque y no se reduce por la defensa del objetivo.

### Arquero

Representa un personaje especializado en ataques a distancia. Si su ataque supera la defensa del objetivo, causa el doble de la diferencia entre ambos valores. De lo contrario, no causa daño.

### Combate

Administra los enfrentamientos entre dos personajes. Controla los turnos, verifica si existe un ganador, muestra los estados de los participantes y finaliza el combate cuando un personaje es derrotado, se produce un empate técnico o se alcanza el límite de 50 rondas.

## 4. Principios de programación orientada a objetos

El proyecto aplica los siguientes principios:

- **Abstracción:** la clase `Personaje` establece una estructura común y define el método abstracto `atacar()`.
- **Encapsulamiento:** los atributos se protegen mediante atributos privados y propiedades con validaciones.
- **Herencia:** las clases `Guerrero`, `Mago` y `Arquero` heredan de `Personaje`.
- **Polimorfismo:** cada tipo de personaje implementa su propia versión del método `atacar()`.

## 5. Relaciones entre clases

- **Herencia:** `Guerrero`, `Mago` y `Arquero` heredan de `Personaje`.
- **Agregación:** la clase `Combate` administra dos personajes que participan en el enfrentamiento.
- **Asociación:** los personajes interactúan entre sí cuando uno ejecuta un ataque contra otro.

## 6. Validaciones implementadas

El sistema valida los datos ingresados para evitar estados incorrectos. Entre las validaciones implementadas se encuentran:

- El nombre no puede estar vacío.
- La vida debe ser un número entero entre 0 y 100.
- El ataque debe ser un número entero positivo.
- La defensa debe ser un número entero no negativo.
- No se permite aplicar daño negativo.
- La vida de un personaje nunca puede ser inferior a cero.
- Un personaje derrotado no puede atacar.
- No se puede atacar a un personaje derrotado.
- Los participantes de un combate deben ser personajes válidos y diferentes.

## 7. Lógica del combate

El combate comienza con el primer personaje y continúa alternando los turnos entre los participantes. Cada personaje utiliza su propia implementación del método `atacar()`.

Después de cada ataque, el programa muestra el estado de ambos personajes. El combate termina cuando uno de ellos queda sin vida. También contempla el empate técnico cuando una ronda completa no produce daño y establece un límite máximo de 50 rondas.

## 8. Cómo ejecutar el proyecto

### Requisitos

- Tener Python instalado.
- Disponer de los archivos del proyecto en una misma carpeta.

### Pasos de ejecución

1. Abrir la carpeta del proyecto en Visual Studio Code.
2. Abrir una terminal desde el menú **Terminal > Nueva terminal**.
3. Ejecutar el siguiente comando:

```bash
python main.py
```

4. Revisar la salida en la terminal, donde se muestran los casos de prueba y sus resultados.

Si el comando `python` no funciona, se puede intentar con:

```bash
py main.py
```

## 9. Pruebas realizadas

Se implementaron 13 casos de prueba para verificar el funcionamiento del sistema:

1. Creación de personajes.
2. Clase abstracta.
3. Validación de vida inválida.
4. Validación de nombre vacío.
5. Validación de ataque y defensa.
6. Verificación de habilidades especiales.
7. Verificación de que la vida nunca sea negativa.
8. Rechazo de daño inválido.
9. Impedir que un personaje derrotado ataque.
10. Impedir atacar a un personaje derrotado.
11. Ejecución completa del combate y determinación del ganador.
12. Verificación del empate técnico.
13. Validación de participantes diferentes.

**Resultado de las pruebas:** 13 pruebas superadas y 0 pruebas fallidas.

## 10. Diagrama UML

El archivo `diagrama_uml.puml` contiene el código fuente del diagrama UML del proyecto. En él se representan las clases principales, sus atributos, métodos y las relaciones de herencia y agregación.

## 11. Importancia de la abstracción

El método `atacar()` se define como abstracto porque cada tipo de personaje debe implementar su propia forma de atacar. Esto permite establecer una estructura común sin obligar a que todos los personajes tengan la misma lógica de daño.

En cambio, el método `recibir_danio()` es concreto porque todos los personajes comparten la misma lógica para recibir daño, reducir sus puntos de vida y evitar que estos sean negativos.

## 12. Conclusión

Con el desarrollo de este proyecto se aplicaron los conceptos fundamentales de la programación orientada a objetos en Python. La implementación permite representar distintos tipos de personajes, validar sus atributos y simular combates mediante una estructura organizada, reutilizable y fácil de mantener.
