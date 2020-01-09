import roll_dice
import unittest
from unittest.mock import patch

@patch('random.randint', return_value=3)
class Test_Roll_Dice(unittest.TestCase) :
    
    def _make_one(self, *args, **kw) :
        from roll_dice import Die
        return Die(*args, **kw)
        
    def test_six_sided_die(self, mocked_randint) :
        die = self._make_one(sides=6)
        result = die.roll()
        
        self.assertEqual(result, 3)
        
    def test_42_sided_die(self, mocked_randint) :
        die = self._make_one(sides=42)
        result = die.roll()
        
        self.assertEqual(result, 3)
        

if __name__ == '__main__':
    unittest.main()
