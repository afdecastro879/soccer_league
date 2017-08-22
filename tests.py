import fileinput
import unittest

from main import SoccerLeague


class TestSoccerLeague(unittest.TestCase):
    def setUp(self):
        self.soccer = SoccerLeague()

    def calculate_results(self, filename):
        for line in fileinput.input(filename):
            self.soccer.add_result(line)
        fileinput.close()

    def get_file_content(self, filename):
        result = ''
        for line in fileinput.input(filename):
            result += line
        fileinput.close()
        return result

    def check_points_order(self, result_list):
        length = len(result_list)
        for i in range(length - 1):
            self.assertGreaterEqual(result_list[i][1], result_list[i+1][1])

    def check_alphabetical_order(self, result_list):
        length = len(result_list)
        for i in range(length - 1):
            self.assertLessEqual(result_list[i][0], result_list[i+1][0])

    def test_points_order(self):
        self.calculate_results('tests/test1.txt')
        self.check_points_order(self.soccer.get_results_list())
        # print(self.soccer)

    def test_alphabetical_order(self):
        self.calculate_results('tests/test2.txt')
        self.check_alphabetical_order(self.soccer.get_results_list())
        # print(self.soccer)

    def test_print_1(self):
        self.calculate_results('tests/test1.txt')
        test = self.get_file_content('tests/test1_result.txt')
        self.assertEqual(test, self.soccer.__str__())

    def test_print_2(self):
        self.calculate_results('tests/test2.txt')
        test = self.get_file_content('tests/test2_result.txt')
        self.assertEqual(test, self.soccer.__str__())

    def test_print_3(self):
        self.calculate_results('tests/test3.txt')
        test = self.get_file_content('tests/test3_result.txt')
        self.assertEqual(test, self.soccer.__str__())


if __name__ == '__main__':
    unittest.main()