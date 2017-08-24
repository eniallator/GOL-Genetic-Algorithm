from random import random
from Creature import Creature


class Population(object):

    def __init__(self, size, width, height, mutation_chance):
        self._population = []
        self._width = width
        self._height = height
        self._mutation_chance = mutation_chance

        for i in range(size):
            self.add_creature(Creature(width, height, mutation_chance))

    def __iter__(self):
        return iter(self._population)

    def __len__(self):
        return len(self._population)

    def __setitem__(self, index, val):
        self._population[index] = val

    def __getitem__(self, index):
        return self._population[index]

    def add_creature(self, creature):
        self._population.append(creature)

    def _weighted_random(self, population):
        totals = []
        total_score = 0

        for creature in population:
            total_score += creature.score
            totals.append(total_score)

        rnd = random() * total_score

        for i, total in enumerate(totals):
            if rnd <= total:
                return i

    def evolve(self):
        new_population = Population(0, self._width, self._height, self._mutation_chance)

        for i in range(len(self)):
            creature_choice = list(self)

            first_index = self._weighted_random(creature_choice)
            first_creature = creature_choice.pop(first_index)

            second_index = self._weighted_random(creature_choice)
            second_creature = creature_choice.pop(second_index)

            child = first_creature.mate(second_creature)

            new_population.add_creature(child)

        return new_population
