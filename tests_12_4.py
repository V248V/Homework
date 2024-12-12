import logging
import unittest
import rt_with_exceptions

logger = logging.getLogger('runner_logger')
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler('runner_tests.log', mode='w', encoding='UTF-8')
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


class RunnerTest(unittest.TestCase):
    is_frozen = False

    def test_walk(self):
        try:
            test1 = rt_with_exceptions.Runner('T1', speed=-5)
            logger.info('"test walk" выполнен успешно')
            for _ in range(10):
                test1.walk()
            self.assertEqual(test1.distance, 50)
        except ValueError as err:
            logger.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            test2 = rt_with_exceptions.Runner(222)
            logger.info('"test run" выполнен успешно')
            for _ in range(10):
                test2.run()
            self.assertEqual(test2.distance, 100)
        except TypeError as err:
            logger.warning('Неверный тип данных для объекта Runner', exc_info=True)


    def test_challenge(self):
        obj1 = rt_with_exceptions.Runner('OBJ1')
        obj2 = rt_with_exceptions.Runner('OBJ2')
        for _ in range(10):
            obj1.run()
            obj2.walk()
        self.assertNotEqual(obj1.distance, obj2.distance)
