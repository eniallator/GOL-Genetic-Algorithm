from Population import Population
from Creature import Creature


class GOL_Simulation(object):

    def __init__(self, size, width=6, height=6, iterations=30):
        self.population = Population(size, width, height)
        self.iterations = iterations

    def _find_dead_neighbours(self, cycle, curr_index):
        dead_neighbours = []
        for x in range(-1, 2):
            for y in range(-1, 2):
                if x or y:
                    next_cell = [cycle[curr_index][0] + x,
                                 cycle[curr_index][1] + y]
                    try:
                        cycle.index(next_cell)
                    except:
                        dead_neighbours.append(next_cell)
        return dead_neighbours

    def _stack_neighbours(self, total, neighbours):
        for neighbour in neighbours:
            for pos in total:
                if pos[0] == neighbour[0] and pos[1] == neighbour[1]:
                    pos[2] += 1
                    break
            else:
                total.append(neighbour + [1])

    def _spawn_new_cells(self, next_cycle, total_dead_neighbours):
        for pos in total_dead_neighbours:
            if pos[2] == 3:
                next_cycle.append(pos[0:2])

        return next_cycle

    def _apply_rules(self, prev_cycle):
        next_cycle = list(prev_cycle)
        total_dead_neighbours = []

        for index in range(len(prev_cycle) - 1, 0, -1):
            dead_neighbours = self._find_dead_neighbours(prev_cycle, index)
            self._stack_neighbours(total_dead_neighbours, dead_neighbours)

            if len(dead_neighbours) > 6 or len(dead_neighbours) < 5:
                del next_cycle[index]

        return self._spawn_new_cells(next_cycle, total_dead_neighbours)

    def evaluate(self):
        for creature in self.population:
            alive_cells = self.population.gen_points(creature)

            for i in range(self.iterations + 1):
                alive_cells = self._apply_rules(alive_cells)

            creature.score = len(alive_cells)

    def stats(self):
        highest = None
        lowest = None
        total = 0

        for creature in self.population:
            total += creature.score
            highest = creature if not highest or highest < creature.score else highest
            lowest = creature.score if not lowest or lowest > creature.score else lowest

        print 'Total score: ' + str(total) + ' Highest score: ' + str(highest.score) + ' Lowest score: ' + str(lowest) + ' Best DNA:'

        for i in range(highest.height):
            print highest.dna[i * highest.height : (i + 1) * highest.height]

    def evolve_population(self):
        new_population = self.population.evolve()
        del self.population
        self.population = new_population
