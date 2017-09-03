from GOL_Simulation import GOL_Simulation

NEWSIM = GOL_Simulation(50, 5, 5, 50)
for i in range(20):
    print '\nIteration #' + str(i + 1)
    NEWSIM.evaluate()
    NEWSIM.stats()
    NEWSIM.evolve_population()
