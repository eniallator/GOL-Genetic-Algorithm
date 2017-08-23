from random import random, randrange
from DNA import DNA


class Creature(object):

    def __init__(self, width, height, dna=None, mutation_chance = 0.025):
        self.dna = DNA(width * height, dna)
        self.width = width
        self.height = height
        self.mutation_chance = mutation_chance
        self.score = 0

    def gen_coords_from_dna(self):
        dna_size = len(self.dna)
        alive_cells = []

        for index in range(len(self.dna)):
            if self.dna[index]:
                alive_cells.append([int(index / self.width),
                                    int(index % self.height)])

        return alive_cells

    def mate(self, other):
        if self.width != other.width or self.height != other.height:
            print 'tried mating the following creature sizes\'s:'
            print str(self.width) + ' by ' + str(self.height)
            print str(other.width) + ' by ' + str(other.height)
            return

        splice_point = randrange(len(self.dna) - 1)
        new_dna = self.dna[0:splice_point] + other.dna[splice_point:len(other.dna)]

        for i in range(len(new_dna)):
            if random() <= self.mutation_chance:
                self.dna[i] = 0 if self.dna[i] else 1

        return Creature(self.width, self.height, new_dna)
