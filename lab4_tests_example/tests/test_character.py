import unittest
from src.models.character import Character

class TestCharacter(unittest.TestCase):

    def test_character_starts_alive_with_full_health(self):
        """Test que un personaje nuevo tiene salud completa y está vivo"""
        warrior = Character("Conan")
        self.assertEqual(warrior.health, 100)
        self.assertTrue(warrior.is_alive)

    def test_take_damage_reduces_health_and_can_kill(self):
        """Test que el daño reduce salud y puede matar al personaje"""
        mage = Character("Gandalf")
        mage.take_damage(30)
        self.assertEqual(mage.health, 70)
        
        mage.take_damage(70)
        self.assertFalse(mage.is_alive)

    def test_attacked_character_is_healed(self):
        """Test que un personaje con 20 de vida se cura 40 (queda en 60)."""
        healty = Character("Kirito", 20)
        self.assertEqual(healty.health, 20)
        self.assertTrue(healty.is_alive)

        healty.heal(40)

        self.assertEqual(healty.health, 60)
        self.assertTrue(healty.is_alive)

    def test_attacked_character_is_healed_when_target_is_dead(self):
        """Si el target está muerto, no se aplica la poción y no cambia la vida."""
        healty = Character(" Noor", 0)
        healty.is_alive = False   
        
        self.assertEqual(healty.health, 0)
        self.assertFalse(healty.is_alive)

        healty.heal(100)

        self.assertEqual(healty.health, 0)
        self.assertFalse(healty.is_alive)