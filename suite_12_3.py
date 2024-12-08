import unittest
from tests_12_3 import RunnerTest
from tests_12_3 import TournamentTest

nameRN = unittest.TestSuite()
nameRN.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
nameRN.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(nameRN)
