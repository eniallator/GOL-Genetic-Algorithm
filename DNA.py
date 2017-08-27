from random import random, randrange


class DNA(object):

    def __init__(self, size=None):
        if type(size) == int:
            self._dna = []
            self.size = size
            for index in range(size):
                self._dna.append(randrange(0, 2))
        else:
            dna = size
            self._dna = dna
            self.size = len(dna)

    def __iter__(self):
        return iter(self._dna)

    def __len__(self):
        return len(self._dna)

    def __setitem__(self, index, val):
        self._dna[index] = val

    def __getitem__(self, index):
        return self._dna[index]

    def splice(self, other_dna):
        if len(other_dna) != len(self):
            print 'Tried splicing DNA with length ' + str(len(self)) + ' with another of length ' + str(len(other_dna))
            return

        splice_point = randrange(len(self) - 1)
        new_dna_sequence = self[0:splice_point] + other_dna[splice_point:len(other_dna)]
        new_dna = DNA(new_dna_sequence)

        return new_dna

    def mutate(self, mutation_chance):
        for i in range(len(self)):
            if random() < mutation_chance:
                self[i] = 0 if self[i] else 1

    def get_dna(self):
        return self._dna
