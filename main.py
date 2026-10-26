
from personajes import Guerrero, Mago, Arquero, Combate, Personaje


def prueba_creacion():
    guerrero = Guerrero("Arthas", 100, 30, 20)
    mago = Mago("Gandalf", 80, 40, 10)
    arquero = Arquero("Legolas", 90, 35, 15)

    assert guerrero.nombre == "Arthas"
    assert mago.vida == 80
    assert arquero.ataque == 35

    guerrero.mostrar_estado()
    mago.mostrar_estado()
    arquero.mostrar_estado()


def prueba_clase_abstracta():
    try:
        Personaje("Prueba", 100, 20, 10)
    except TypeError:
        return

    raise AssertionError("Se permitió crear directamente la clase abstracta Personaje.")


def prueba_vida_invalida():
    for vida in (-1, 101):
        try:
            Guerrero("Arthas", vida, 30, 20)
        except ValueError:
            continue

        raise AssertionError(f"Se aceptó una vida inválida: {vida}")


def prueba_nombre_vacio():
    for nombre in ("", "   "):
        try:
            Mago(nombre, 80, 40, 10)
        except ValueError:
            continue

        raise AssertionError("Se aceptó un nombre vacío.")


def prueba_ataque_defensa_invalidos():
    try:
        Guerrero("Arthas", 100, 0, 20)
    except ValueError:
        pass
    else:
        raise AssertionError("Se aceptó un ataque inválido.")

    try:
        Guerrero("Arthas", 100, 30, -1)
    except ValueError:
        pass
    else:
        raise AssertionError("Se aceptó una defensa inválida.")


def prueba_ataques_especiales():
    guerrero = Guerrero("Arthas", 100, 30, 20)
    enemigo1 = Mago("Gandalf", 80, 40, 10)
    assert guerrero.atacar(enemigo1) == 26

    mago = Mago("Merlin", 80, 40, 10)
    enemigo2 = Guerrero("Boromir", 100, 25, 20)
    assert mago.atacar(enemigo2) == 40

    arquero = Arquero("Robin", 90, 35, 15)
    enemigo3 = Guerrero("Conan", 100, 25, 20)
    assert arquero.atacar(enemigo3) == 30

    arquero_debil = Arquero("Flecha", 90, 10, 5)
    enemigo4 = Guerrero("Escudo", 100, 25, 20)
    assert arquero_debil.atacar(enemigo4) == 0


def prueba_vida_no_negativa():
    guerrero = Guerrero("Arthas", 10, 30, 20)

    danio = guerrero.recibir_danio(50)

    assert danio == 10
    assert guerrero.vida == 0
    assert guerrero.vida >= 0


def prueba_danio_invalido():
    guerrero = Guerrero("Arthas", 100, 30, 20)

    try:
        guerrero.recibir_danio(-5)
    except ValueError:
        return

    raise AssertionError("Se aceptó daño negativo.")


def prueba_personaje_derrotado():
    guerrero = Guerrero("Arthas", 10, 30, 20)
    enemigo = Mago("Gandalf", 80, 40, 10)

    guerrero.recibir_danio(10)

    try:
        guerrero.atacar(enemigo)
    except ValueError:
        return

    raise AssertionError("Un personaje derrotado pudo atacar.")


def prueba_objetivo_derrotado():
    guerrero = Guerrero("Arthas", 100, 30, 20)
    enemigo = Mago("Gandalf", 0, 40, 10)

    try:
        guerrero.atacar(enemigo)
    except ValueError:
        return

    raise AssertionError("Se atacó a un personaje derrotado.")


def prueba_combate_completo():
    guerrero = Guerrero("Arthas", 100, 30, 20)
    mago = Mago("Gandalf", 80, 40, 10)

    combate = Combate(guerrero, mago)
    ganador = combate.iniciar()

    assert ganador is not None
    assert ganador.esta_vivo()
    assert combate.rondas <= 50


def prueba_empate_tecnico():
    guerrero = Guerrero("Arthas", 100, 1, 100)
    arquero = Arquero("Legolas", 100, 1, 100)

    combate = Combate(guerrero, arquero)
    ganador = combate.iniciar()

    assert ganador is None
    assert combate.empate is True
    assert guerrero.vida == 100
    assert arquero.vida == 100


def prueba_personajes_iguales():
    guerrero = Guerrero("Arthas", 100, 30, 20)

    try:
        Combate(guerrero, guerrero)
    except ValueError:
        return

    raise AssertionError("Se permitió usar el mismo personaje dos veces.")


def ejecutar_pruebas():
    pruebas = [
        ("Creación de personajes", prueba_creacion),
        ("Clase abstracta", prueba_clase_abstracta),
        ("Vida inválida", prueba_vida_invalida),
        ("Nombre vacío", prueba_nombre_vacio),
        ("Ataque y defensa inválidos", prueba_ataque_defensa_invalidos),
        ("Habilidades especiales", prueba_ataques_especiales),
        ("Vida nunca negativa", prueba_vida_no_negativa),
        ("Daño inválido", prueba_danio_invalido),
        ("Personaje derrotado no puede atacar", prueba_personaje_derrotado),
        ("No atacar a un personaje derrotado", prueba_objetivo_derrotado),
        ("Combate completo y ganador", prueba_combate_completo),
        ("Empate técnico", prueba_empate_tecnico),
        ("Participantes diferentes", prueba_personajes_iguales),
    ]

    superadas = 0
    fallidas = 0

    print("=" * 50)
    print("GUARDIANS OF THE ANCIENT KINGDOM")
    print("EJECUCIÓN DE CASOS DE PRUEBA")
    print("=" * 50)

    for titulo, funcion in pruebas:
        print(f"\n--- {titulo} ---")

        try:
            funcion()
            print("PRUEBA SUPERADA")
            superadas += 1
        except Exception as error:
            print(f"PRUEBA FALLIDA: {error}")
            fallidas += 1

    print("\n" + "=" * 50)
    print("RESUMEN DE PRUEBAS")
    print("=" * 50)
    print(f"Pruebas ejecutadas: {len(pruebas)}")
    print(f"Pruebas superadas: {superadas}")
    print(f"Pruebas fallidas: {fallidas}")

    if fallidas == 0:
        print("\nTodas las pruebas se ejecutaron correctamente.")
    else:
        print("\nRevisa los errores de las pruebas fallidas.")


if __name__ == "__main__":
    ejecutar_pruebas()
