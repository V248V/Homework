import unittest
import runner_and_tournament


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        test1 = runner_and_tournament.Runner('T1')
        for _ in range(10):
            test1.walk()
        self.assertEqual(test1.distance, 50)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        test2 = runner_and_tournament.Runner('T2')
        for _ in range(10):
            test2.run()
        self.assertEqual(test2.distance, 100)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        obj1 = runner_and_tournament.Runner('OBJ1')
        obj2 = runner_and_tournament.Runner('OBJ2')
        for _ in range(10):
            obj1.run()
            obj2.walk()
        self.assertNotEqual(obj1.distance, obj2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        runner_and_tournament.Tournament.all_results = {}

    def setUp(self):
        self.usein = runner_and_tournament.Runner('Усэйн', speed=10)
        self.andrey = runner_and_tournament.Runner('Андрей', speed=9)
        self.nick = runner_and_tournament.Runner('Ник', speed=3)

    @classmethod
    def tearDownClass(cls):
        for element in runner_and_tournament.Tournament.all_results.values():
            print(element)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_tournament_1(self):
        tourn = runner_and_tournament.Tournament(90, self.usein, self.nick)
        runner_and_tournament.Tournament.all_results['test_1'] = tourn.start()
        self.assertTrue(runner_and_tournament.Tournament.all_results[max(runner_and_tournament.Tournament.all_results)],
                        'Ник')

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_tournament_2(self):
        tourn = runner_and_tournament.Tournament(90, self.andrey, self.nick)
        runner_and_tournament.Tournament.all_results['test_2'] = tourn.start()
        self.assertTrue(runner_and_tournament.Tournament.all_results[max(runner_and_tournament.Tournament.all_results)],
                        'Ник')

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_tournament_3(self):
        tourn = runner_and_tournament.Tournament(90, self.usein, self.andrey, self.nick)
        runner_and_tournament.Tournament.all_results['test_3'] = tourn.start()
        self.assertTrue(runner_and_tournament.Tournament.all_results[max(runner_and_tournament.Tournament.all_results)],
                        'Ник')
