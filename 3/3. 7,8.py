import math
import random

class Particle:
    def __init__(self, initial_pos):
        self.position = initial_pos

    def set_position(self, new_pos):
        self.position = new_pos

    def distance_to_mass_center(self):
        distance_squared = sum([pos ** 2 for pos in self.position])
        return math.sqrt(distance_squared)

    def distance_between_particles(self, other_particle):
        # Calculate distance between two particles
        distance_squared = sum([(self.position[i] - other_particle.position[i]) ** 2 for i in range(len(self.position))])
        return math.sqrt(distance_squared)

# Creating 10 electrons
electrons = []
for i in range(10):
    # random positions for electrons
    electron_pos = [random.uniform(0, 10), random.uniform(0, 10), random.uniform(0, 10)]

    # Creating electrons with given positions
    electron = Particle(electron_pos)
    electrons.append(electron)

    # Calculating distance of electron 'i' to the nucleus
    distance_to_nucleus = electron.distance_to_mass_center()
    print(f"Distance of electron {i + 1} to nucleus: {distance_to_nucleus}")

# relative distance between two electrons
electron_1 = electrons[0]
electron_2 = electrons[1]

distance_between_electrons = electron_1.distance_between_particles(electron_2)
print(f"Modulus of relative distance between electron 1 and electron 2: {distance_between_electrons}")
