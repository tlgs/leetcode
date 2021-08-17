"""1925. Count Square Sum Triples

Using Euclid's formula to generate candidate primitive triplets
and then using k to check for multiples.
In all fairness, pythagorean triples are a well studied subject and
with a constraint such as n <= 250, this can be solved in O(1).


Useful links:
  - <https://en.wikipedia.org/wiki/Pythagorean_triple>
  - <https://en.wikipedia.org/wiki/Coprime_integers#Generating_all_coprime_pairs>

difficulty: easy
tags: mathematics
runtime: 99.07
memory: 52.28
"""


class Solution:
    def coprimes(self, m, n, t):
        if m * m + n * n > t:
            return []

        return (
            [(m, n)]
            + self.coprimes(2 * m - n, m, t)
            + self.coprimes(2 * m + n, m, t)
            + self.coprimes(m + 2 * n, n, t)
        )

    def countTriples(self, n: int) -> int:
        pt = 0
        for a, b in self.coprimes(2, 1, n):
            k = 1
            while k * (a * a + b * b) <= n:
                pt += 2
                k += 1

        return pt
