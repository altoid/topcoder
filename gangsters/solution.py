#!/usr/bin/env python

import fileinput
from util import permute
import unittest
from pprint import pprint


def shootout(p):
    survived = [True] * len(p)
    mapper = {x[1]: x[0] for x in enumerate(p)}

    for i in xrange(len(p)):
        shooter = p[i] - 1
        shoots = (shooter + 1) % len(p)
        if not survived[mapper[shooter + 1]]:
            continue
        survived[mapper[shoots + 1]] = False

    zipped = zip(p, survived)
    result = [z[0] for z in zipped if z[1]]
    return result


def countOrderings(people, alive):
    g = [x + 1 for x in xrange(people)]
    survivor_count = {}
    for p in permute.permute(g):
        standing = shootout(p)
        print p, standing

        l = len(standing)
        if l not in survivor_count:
            survivor_count[l] = 0
        survivor_count[l] += 1

    pprint(survivor_count)


if __name__ == '__main__':
    fi = fileinput.FileInput()
    people = int(fi.readline().strip())
    alive = int(fi.readline().strip())

    countOrderings(people, alive)


class Tests(unittest.TestCase):
    def test1(self):
        g = [1, 2, 4, 3]
        result = shootout(g)
        self.assertEqual([1, 3], result)

    def test_5(self):
        countOrderings(5, 5)

    def test_6(self):
        countOrderings(6, 0)

