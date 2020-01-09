import unittest
from unittest.mock import patch
from dice import Die
import dice

class Test_Roll_Dice(unittest.TestCase) :
    
    def setUp(self):
        self.die = Die(6)
        self.die_1 = Die(6)
        self.die_2 = Die(6)
        
    def test_six_sided_die(self) :
        with patch('random.randint') as mocked_randint:
            mocked_randint.return_value = 3
            self.assertEqual(self.die.roll(), 3)
            
        #test snake eyes and craps
            mocked_randint.return_value = 1
            self.assertEqual(dice.checkSnakeEyes(self.die_1.roll(), self.die_2.roll()), "Snake Eyes!")
            self.assertEqual(dice.checkCraps(self.die_1.roll(), self.die_2.roll()), "Crapped out!")
            
        #test craps continued
            mocked_randint.return_value = 1
            result_1 = self.die_1.roll()
            mocked_randint.return_value = 2
            result_2 = self.die_2.roll()
            
            self.assertEqual(dice.checkCraps(result_1, result_2), "Crapped out!")
            
            mocked_randint.return_value = 6
            self.assertEqual(dice.checkCraps(self.die_1.roll(), self.die_2.roll()), "Crapped out!")
        
        #test box cars
            mocked_randint.return_value = 6
            self.assertEqual(dice.checkBoxCars(self.die_1.roll(), self.die_2.roll()), "Box Cars!")
            
            
        

if __name__ == '__main__':
    unittest.main()
