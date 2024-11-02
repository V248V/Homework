import runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        test1 = runner.Runner('T1')
        for _ in range(10):
            test1.walk()
        self.assertEqual(test1.distance, 50)

    def test_run(self):
        test2 = runner.Runner('T2')
        for _ in range(10):
            test2.run()
        self.assertEqual(test2.distance, 100)

    def test_challenge(self):
        obj1 = runner.Runner('OBJ1')
        obj2 = runner.Runner('OBJ2')
        for _ in range(10):
            obj1.run()
            obj2.walk()
        self.assertNotEqual(obj1.distance, obj2.distance)


if __name__ == "__main__":
    unittest.main()
