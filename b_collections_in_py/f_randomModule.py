"""
===========================================================
                 RANDOM MODULE(DEEP NOTES)
===========================================================

CORE IDEA:
----------
The random module is used to generate pseudo-random numbers.

IMPORTANT WORD:
- NOT truly random
- PSEUDO-random

Why?
Because computers are deterministic machines.
They use algorithms to *simulate* randomness.

-----------------------------------------------------------
WHERE IS random USED?
-----------------------------------------------------------
- Games (dice, cards, shuffling)
- Simulations (Monte Carlo methods)
- Machine Learning (train-test split)
- Cryptography (but NOT with random module)
- Testing & debugging
"""

import random


# =========================================================
# PSEUDO-RANDOMNESS EXPLAINED (VERY IMPORTANT)
# =========================================================
"""
Python uses the Mersenne Twister algorithm internally.

Properties:
- Deterministic
- Period: 2^19937 - 1 (huge)
- Fast
- Good statistical randomness

BUT:
- Not cryptographically secure
- Never use random for passwords or tokens
"""

# =========================================================
# RANDOM INTEGER
# =========================================================
"""
randint(a, b):
- Returns integer between a and b
- BOTH a and b are inclusive
- Internally uses uniform distribution
"""

rand_int = random.randint(1, 10)
print("Random Integer [1, 10]:", rand_int)

"""
Time Complexity:
O(1)
"""


# =========================================================
# RANDOM FLOAT
# =========================================================
"""
random():
- Returns float in range [0.0, 1.0)
- 1.0 is EXCLUDED
"""

rand_float = random.random()
print("Random Float [0.0, 1.0):", rand_float)


# =========================================================
# RANDOM CHOICE
# =========================================================
"""
choice(iterable):
- Picks ONE random element
- Iterable must be non-empty
"""

choices = ['apple', 'banana', 'cherry', 'date']
rand_choice = random.choice(choices)
print("Random choice:", rand_choice)

"""
Internally:
- Generates random index
- Fetches element
Time Complexity: O(1)
"""


# =========================================================
# SHUFFLING
# =========================================================
"""
shuffle(list):
- Shuffles list IN PLACE
- Modifies original list
- Returns None

Algorithm:
- Fisher-Yates shuffle
- Time Complexity: O(n)
"""

random.shuffle(choices)
print("Shuffled list:", choices)

"""
IMPORTANT:
shuffle() works ONLY on mutable sequences (lists)
"""


# =========================================================
# RANDOM SAMPLE
# =========================================================
"""
sample(population, k):
- Returns k UNIQUE random elements
- Does NOT modify original iterable
- Population can be list, tuple, set
"""

rand_sample = random.sample(choices, 2)
print("Random sample:", rand_sample)

"""
Difference between choice() and sample():
- choice(): single element, repetition allowed, means same element can be picked multiple times
- sample(): multiple elements, NO repetition, means unique elements only, if you try to sample more elements than available, it raises a ValueError, if you choose 2 elements from a list of 4, you will get 2 unique elements each time you call sample()
"""


# =========================================================
# RANDOM SEED (VERY IMPORTANT)
# =========================================================
"""
seed(value):
- Initializes the random number generator 
- Fixes the starting point of randomness 
- in simple language, it helps to reproduce the same sequence of random numbers

Same seed → Same sequence
Different seed → Different sequence
"""

random.seed(42)

print("Random with seed 42:", random.randint(1, 10))

"""
WHY seed() MATTERS?

1. Debugging
2. Unit testing
3. Reproducible experiments
4. ML model consistency

Mental Model:
Think of random numbers as a movie.
seed() decides where the movie starts.
"""


# =========================================================
# COMMON MISTAKES (EXAM GOLD)
# =========================================================
"""
1. Thinking random is truly random ❌
2. Using random for passwords ❌
3. Expecting shuffle() to return list ❌
4. Using seed() incorrectly in production ❌
"""


# =========================================================
# WHAT NOT TO USE random FOR
# =========================================================
"""
❌ Passwords
❌ Tokens
❌ Security keys

Use instead:
- secrets module
- os.urandom()
"""


# =========================================================
# WHEN TO USE random MODULE?
# =========================================================
"""
Use random when:
- You need fast randomness
- Security is NOT a concern
- Reproducibility matters
"""

print("END OF RANDOM MODULE")
