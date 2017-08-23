import random


class DNA(object):

    def __init__(self, size=None, dna=None):
        if dna:
            self._dna = dna
            self.size = len(dna)
        else:
            self._dna = []
            self.size = size
            for index in range(size):
                self._dna.append(random.randrange(0, 2))

    def __iter__(self):
        return iter(self._dna)

    def __len__(self):
        return len(self._dna)

    def __setitem__(self, index, val):
        if (val == 1 or val == 0) and type(val) is int:
            self._dna[index] = val
        else:
            print 'Tried setting ' + str(self._dna) + ' at index ' + str(index) + ' to value: ' + str(val)

    def __getitem__(self, index):
        return self._dna[index]

    def get_dna(self):
        return self._dna
