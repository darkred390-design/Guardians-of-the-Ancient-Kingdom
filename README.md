

# Guardians of the Ancient Kingdom

## 1. Descripción del proyecto

En este proyecto desarrollé una aplicación en Python que simula un combate por turnos entre personajes de un reino antiguo. El sistema permite crear diferentes tipos de personajes, aplicar sus habilidades especiales, calcular el daño de los ataques y determinar el ganador del combate.

Para desarrollar el proyecto utilicé programación orientada a objetos (POO), aplicando conceptos como encapsulamiento, abstracción, herencia y polimorfismo.

## 2. Autor del proyecto

- Nombre del estudiante: Vicente Ortega

## 3. Estructura del proyecto

El proyecto contiene los siguientes archivos:

- `personajes.py`: contiene las clases de los personajes, sus atributos, validaciones, habilidades y la lógica del combate.
- `main.py`: ejecuta los casos de prueba y muestra los resultados en la terminal.
- `README.md`: contiene la documentación y las instrucciones de ejecución.
- `diagrama_uml.puml`: contiene el código fuente del diagrama UML de las clases del proyecto.

## 4. Descripción de las clases

### 4.1. Clase Personaje

Es una clase abstracta que define las características comunes de los personajes.

**Atributos:**
- Nombre.
- Vida.
- Ataque.
- Defensa.

**Métodos principales:**
- `recibir_danio(cantidad)`: aplica el daño recibido sin permitir que la vida sea negativa.
- `esta_vivo()`: comprueba si el personaje continúa con vida.
- `mostrar_estado()`: muestra los atributos actuales del personaje.
- `atacar(objetivo)`: método abstracto que debe implementarse en cada tipo de personaje.

### 4.2. Clase Guerrero

Hereda de `Personaje`. Su ataque utiliza un multiplicador de 1.2 sobre el valor de ataque y resta la defensa del objetivo. El daño no puede ser negativo y se convierte a entero.

### 4.3. Clase Mago

Hereda de `Personaje`. Su ataque ignora la defensa del objetivo y causa un daño igual a su atributo de ataque.

### 4.4. Clase Arquero

Hereda de `Personaje`. Si su ataque supera la defensa del objetivo, calcula el daño restando la defensa al ataque y multiplicando el resultado por dos. Si no supera la defensa, no causa daño.

### 4.5. Clase Combate

Administra el enfrentamiento entre dos personajes.

**Sus funciones principales son:**
- `iniciar()`: ejecuta el combate por turnos.
- `cambiar_turno()`: alterna el personaje que debe atacar.
- `verificar_ganador()`: comprueba si uno de los participantes ha sido derrotado.
- `mostrar_resultado()`: muestra el ganador o el empate y el estado final de los personajes.

El combate termina cuando un personaje es derrotado, cuando se produce un empate técnico por una ronda sin daño o cuando se alcanza el límite de 50 rondas.

## 5. Conceptos de programación orientada a objetos

### Encapsulamiento

Los atributos de `Personaje` se manejan mediante atributos privados y propiedades que validan los valores asignados. La vida debe ser un entero entre 0 y 100, el ataque debe ser un entero positivo, la defensa debe ser un entero no negativo y el nombre no puede estar vacío.

### Abstracción

La clase `Personaje` define las características y comportamientos comunes de todos los personajes. El método `atacar()` es abstracto porque cada tipo de personaje implementa su propia forma de atacar.

### Herencia

Las clases `Guerrero`, `Mago` y `Arquero` heredan los atributos y métodos comunes de `Personaje`.

### Polimorfismo

Cada clase implementa el método `atacar()` de manera diferente. El combate puede invocar este método sin necesitar una lógica de ataque distinta para cada clase.

## 6. Relaciones entre las clases

- **Herencia:** `Guerrero`, `Mago` y `Arquero` heredan de `Personaje`.
- **Agregación:** `Combate` administra dos personajes que participan en el enfrentamiento.
- **Asociación:** los personajes interactúan entre sí cuando uno ataca a otro y recibe el daño correspondiente.

## 7. Reglas del combate

1. Cada personaje debe tener un nombre válido y atributos dentro de los límites permitidos.
2. Un personaje derrotado no puede atacar.
3. No se puede atacar a un personaje derrotado.
4. La vida nunca puede ser negativa.
5. El daño aplicado no puede ser negativo.
6. Los personajes se alternan los turnos de ataque.
7. Después de cada ataque se muestran los estados de los participantes.
8. El combate termina al determinar un ganador, al producirse un empate técnico o al alcanzar 50 rondas.

## 8. Requisitos para ejecutar el proyecto

- Tener Python instalado.
- Contar con los archivos del proyecto en una misma carpeta.
- Utilizar una terminal o Visual Studio Code para ejecutar el programa.

No se requieren bibliotecas externas para ejecutar las pruebas incluidas en `main.py`.

## 9. Instrucciones de ejecución

1. Abrir la carpeta `Guardians-of-the-Ancient-Kingdom` en Visual Studio Code.
2. Abrir una terminal desde el menú Terminal.
3. Verificar que la terminal esté ubicada en la carpeta del proyecto.
4. Ejecutar el siguiente comando:

```bash
python main.py
```

5. Revisar los resultados que aparecen en la terminal.

El programa ejecuta los casos de prueba y muestra el número de pruebas superadas y fallidas.

## 10. Resultados de las pruebas

Durante la verificación del programa ejecuté 13 casos de prueba.

Los resultados obtenidos fueron:

- Pruebas ejecutadas: 13.
- Pruebas superadas: 13.
- Pruebas fallidas: 0.

Comprobé la creación de personajes, la clase abstracta, las validaciones de atributos, las habilidades especiales, el control de la vida, la restricción de ataques de personajes derrotados, el combate completo, la determinación del ganador y el empate técnico.

## 11. Diagrama UML

El archivo `diagrama_uml.puml` contiene el código fuente del diagrama UML del proyecto. En él se representan las clases, sus atributos, sus métodos y las relaciones de herencia y agregación.

Para visualizarlo se puede utilizar la extensión PlantUML de Visual Studio Code, con los requisitos necesarios para generar la vista previa.

## 12. ¿Por qué atacar() es abstracto y recibir_danio() es concreto?

El método `atacar()` es abstracto porque cada tipo de personaje tiene una mecánica de ataque diferente. Así, cada clase debe implementar su propia versión del método.

En cambio, `recibir_danio()` es concreto porque todos los personajes comparten la misma regla general para recibir daño: restar el daño a la vida disponible sin permitir que el resultado sea negativo.

## 13. Conclusión

Con este proyecto apliqué los principios fundamentales de la programación orientada a objetos en Python. Implementé una estructura de clases reutilizable, validaciones de atributos, diferentes mecánicas de ataque y un sistema de combate por turnos.

Mediante las pruebas realizadas, comprobé el funcionamiento de las funcionalidades implementadas. Los 13 casos de prueba finalizaron correctamente, sin errores.
