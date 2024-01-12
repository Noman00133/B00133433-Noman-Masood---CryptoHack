import math

vector = [4, 6, 2, 5]

# Calculating  Euclidean norm of the vector
# This function squares each vector elements, then calculates the sum of the squered vector elements.
# The square root of the sum is the magnitude of the vector.
print(math.sqrt(sum([x**2 for x in vector])))

