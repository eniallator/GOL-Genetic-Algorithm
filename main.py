from GOL_Simulation import GOL_Simulation

newSim = GOL_Simulation(10, 5, 5, 100)
for i in range(6):
    print '\nIterations: ' + str(i)
    newSim.evaluate()
    newSim.stats()
    newSim.evolve_population()
