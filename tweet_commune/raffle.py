import random


class Raffle:

    def __init__(self, multiplier=1):
        self.multiplier = multiplier

    def choices(self, choices, k=1):
        """
        Run raffle to select k items from a list of items

        :param choices: list of items to select from
        :param k: the number of items to select
        :return: a list of selected items
        """
        n = len(choices)
        weights = self._build_weights(n)
        return random.choices(
            population=choices,
            weights=weights,
            k=k
        )

    def _equation(self, n, i):
        """
        The equation used to determine the number of tickets an item receives

        :param n: total number of items
        :param i: the index of the item
        :return: number of tickets the given item receives
        """
        return (n - i) ** self.multiplier

    def _total_tickets(self, n):
        """
        Calculate total number of tickets participating in the raffle
        :param n: the total number of items
        :return: total ticket count
        """
        count = 0
        for i in range(n):
            count += self._equation(n, i)
        return count

    def _build_weights(self, n):
        """
        Generate the weight for each item

        :param n: total number of items
        :return: a list of weights
        """
        total_tickets = self._total_tickets(n)
        return [self._equation(n, i) / total_tickets for i in range(n)]





