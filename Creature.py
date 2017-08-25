from random import random, randrange
from DNA import DNA


class Creature(object):

    def __init__(self, width, height, mutation_chance):
        self.dna = DNA(width * height)
        self.width = width
        self.height = height
        self._mutation_chance = mutation_chance
        self.score = 0

    def set_dna(self, new_dna):
        del self.dna
        self.dna = new_dna

    def gen_coords_from_dna(self):
        dna_size = len(self.dna)
        alive_cells = []

        for index in range(len(self.dna)):
            if self.dna[index]:
                alive_cells.append([index % self.width,
                                    int(index / self.height)])

        return alive_cells

    def _mutate_dna(self, dna):
        for i in range(len(dna)):
            if random() <= self._mutation_chance:
                dna[i] = 0 if dna[i] else 1

    def mate(self, other):
        if self.width != other.width or self.height != other.height:
            print 'tried mating the following creature sizes\'s:'
            print str(self.width) + ' by ' + str(self.height)
            print str(other.width) + ' by ' + str(other.height)
            return

        splice_point = randrange(len(self.dna) - 1)
        new_dna = DNA(self.dna[0:splice_point] + other.dna[splice_point:len(other.dna)])

        self._mutate_dna(new_dna)

        child = Creature(self.width, self.height, self._mutation_chance)
        child.set_dna(new_dna)
        return child
