# Pairer
Given two sets of entities, pair them up based on similarity

## Implementation
Each entity, or character, is assigned values for attributes.
These attributes then act as a vector for a point in Cartesian space.
Distances are calculated for each possible point pairing between the two sets.
The Hungarian Algorithm is used to find a full set of pairs minimizing distance between paired entities
