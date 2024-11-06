import unittest
import runner_and_tournament


class TournamentTest(unittest.TestCase):
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

    def test_tournament_1(self):
        tourn = runner_and_tournament.Tournament(90, self.usein, self.nick)
        runner_and_tournament.Tournament.all_results['test_1'] = tourn.start()
        self.assertTrue(runner_and_tournament.Tournament.all_results[max(runner_and_tournament.Tournament.all_results)],
                        'Ник')

    def test_tournament_2(self):
        tourn = runner_and_tournament.Tournament(90, self.andrey, self.nick)
        runner_and_tournament.Tournament.all_results['test_2'] = tourn.start()
        self.assertTrue(runner_and_tournament.Tournament.all_results[max(runner_and_tournament.Tournament.all_results)],
                        'Ник')

    def test_tournament_3(self):
        tourn = runner_and_tournament.Tournament(90, self.usein, self.andrey, self.nick)
        runner_and_tournament.Tournament.all_results['test_3'] = tourn.start()
        self.assertTrue(runner_and_tournament.Tournament.all_results[max(runner_and_tournament.Tournament.all_results)],
                        'Ник')
