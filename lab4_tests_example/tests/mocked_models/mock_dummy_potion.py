import unittest
from src.app.combat_system import CombatSystem
from src.models.character import Character
from tests.mocked_models.dummy_potion import DummyPotion  

class TestTestPotion(unittest.TestCase):

    def test_test_potion_in_combat_system(self):
        """Test que CombatSystem acepta TestPotion como Potion válida"""
        combat = CombatSystem(object())
        target = Character("Sesshomaru", 50)
        test_potion = DummyPotion  ()

        # CombatSystem debe tratar a TestPotion como cualquier Potion
        result = combat.perform_use_potion(test_potion, target)

        # Verificamos que se comporta como una Potion en el sistema
        self.assertIn("posion", result)
        self.assertEqual(target.health, 50) 

