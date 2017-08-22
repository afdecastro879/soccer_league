import fileinput
import sys


class SoccerLeague:
    """
    Class to process a soccer league
    """

    def __init__(self):
        """
        Constructor method. It initializes an empty dictionary to hold the results
        """
        self.results = {}

    def add_result(self, match):
        """
        Adds a result of a match to the results dictionary
        :param match: A string with the format <team 1> <goals>, <team 2> <goals>
        :type match str
        """

        team1, team2 = match.split(',')
        name1, pt1 = map(str.strip, team1.rsplit(' ', 1))
        name2, pt2 = map(str.strip, team2.rsplit(' ', 1))

        int1, int2 = int(pt1), int(pt2)

        if name1 not in self.results.keys():
            self.results[name1.strip()] = 0
        if name2 not in self.results.keys():
            self.results[name2.strip()] = 0

        if int1 > int2:
            self.results[name1] += 3
        elif int2 > int1:
            self.results[name2] += 3
        else:
            self.results[name1] += 1
            self.results[name2] += 1

    def get_results_list(self):
        """
        Returns the results list sorted descendant by number of points.
        If two teams have the same number of points returns this subset in a descendant lexicographic order
        :return: The results list with the specific order
        :rtype list
        """

        return sorted(self.results.items(), key=lambda x: (-x[1], x[0]))

    def __str__(self):
        """
        Prints the to results
        Prints the league results in the following format:
            <position>. <team name>, <points> pts
            ...
            <position>. <team name>, <points> pts
        """

        print_list = []

        for idx, item in enumerate(self.get_results_list(), start=1):
            baseformat = '{}. {}, {} '
            baseformat += 'pts' if item[1] != 1 else 'pt'
            print_list.append(baseformat.format(idx, item[0], item[1]))

        return '\n'.join(print_list)


if __name__ == '__main__':

    # Extract the argument
    args = sys.argv[1:]

    soccer = SoccerLeague()

    # Read the file
    for line in fileinput.input(args):
        soccer.add_result(line)

    fileinput.close()

    # Prints the result
    print(soccer)
