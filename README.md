# Laboratorio 4
# Diseño de Software
# James Araya Rodríguez - B70528
---

Para este la boratorio:
> Se desarrollo una funcionalidad extra llamada Posion.

> Se integraron diferentes test a la funcionalidad implementada. 

> Se integro un pipeline a git.

> Se crearon mock_dummy para la funcionalidad.

> Se creo un repositorio para subir los archivos. 

> Se implemento un gitignore para descartar archivos inecesarios.


Potion: Clase abstracta que define el contrato que deben implementar todas las pociones (healing(target)).

Elixir: Clase  que hereda de Potion e implementa healing; restaura una cantidad fija de salud al objetivo (llama target.heal(HP)). 

dummy_potion: Cumple el contrato pero no altera la vida; sirve para comprobar polimorfismo y sustituibilidad.

mock_dummy_weapon: Permite trabajar con cualquier Potion porque solo depende del contrato healing.

Test: 
    * test_character_is_healed: Verifica que un personaje vivo con 20 de vida, al recibir heal(40), aumenta su salud a 60 y sigue vivo.
    * test_character_is_not_healed_if_dead: Verifica que si un personaje está muerto, al llamar heal(100) no cambia su vida (sigue en 0) y permanece muerto. 
    * DummyPotion(Potion): Permite probar que se pueden crear otros constructores de posiones. 
    * test_test_potion_in_combat_system: confirma que CombatSystem acepta cualquier Potion válida (como DummyPotion) y la ejecuta sin errores;
