from GOL_Simulation import GOL_Simulation

newSim = GOL_Simulation(50, 3, 3, 50, 0.1, 4)
for i in range(50):
    print '\nIteration #' + str(i + 1)
    newSim.evaluate()
    newSim.stats()
    newSim.evolve_population()
