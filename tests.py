import fileinput
import unittest

from main import SoccerLeague


def get_file_content(filename):
    """
    Reads a file with filename
    :param filename: the path of a file
    :return: The string read from the file
    """

    result = ''
    for line in fileinput.input(filename):
        result += line
    fileinput.close()
    return result


class TestSoccerLeague(unittest.TestCase):
    """
    Test Case class
    """

    def setUp(self):
        """
        Set up the environment for each test
        """
        self.soccer = SoccerLeague()

    def calculate_results(self, filename):
        """
        Reads a file and calculate the result of the soccer league
        :param filename: The path of the file to read
        """
        for line in fileinput.input(filename):
            self.soccer.add_result(line)
        fileinput.close()

    def check_points_order(self, result_list):
        """
        Checks if result_list numbers are in descendant order
        :param result_list: The result list containing the number of points
        """
        length = len(result_list)
        for i in range(length - 1):
            self.assertGreaterEqual(result_list[i][1], result_list[i + 1][1])

    def check_alphabetical_order(self, result_list):
        """
        Checks if result_list names are order Alphabetically
        :param result_list: The result list containing the team names
        """
        length = len(result_list)
        for i in range(length - 1):
            self.assertLessEqual(result_list[i][0], result_list[i + 1][0])

    def test_points_order_1(self):
        """
        Tests that the result list returned by the soccer league class is order by points
        """

        self.calculate_results('tests/test1.txt')
        self.check_points_order(self.soccer.get_results_list())

    def test_points_order_2(self):
        """
        Tests that the result list returned by the soccer league class is order by points
        """

        self.calculate_results('tests/test2.txt')
        self.check_points_order(self.soccer.get_results_list())

    def test_alphabetical_order(self):
        """
        Tests that the result list returned by the soccer league class is order alphabetically
        in the case the teams have the same number of points
        """
        self.calculate_results('tests/test2.txt')
        self.check_alphabetical_order(self.soccer.get_results_list())

    def test_print_1(self):
        """
        Tests that the result string is equals to the expected one
        """

        self.calculate_results('tests/test1.txt')
        test = get_file_content('tests/test1_result.txt')
        self.assertEqual(test, self.soccer.__str__())

    def test_print_2(self):
        """
        Tests that the result string is equals to the expected one
        """

        self.calculate_results('tests/test2.txt')
        test = get_file_content('tests/test2_result.txt')
        self.assertEqual(test, self.soccer.__str__())

    def test_print_3(self):
        """
        Tests that the result string is equals to the expected one
        """
        self.calculate_results('tests/test3.txt')
        test = get_file_content('tests/test3_result.txt')
        self.assertEqual(test, self.soccer.__str__())


if __name__ == '__main__':
    unittest.main()
