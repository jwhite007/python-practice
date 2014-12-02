#! /usr/bin/env python

import unittest
from python_practice.practice_modules.animal_shelter import AnimalShelter

class TestAnimalShelter(unittest.TestCase):
    def setUp(self):
        self.shelter = AnimalShelter()
        self.shelter.enqueue('dog', 'Bear')
        self.shelter.enqueue('cat', 'Buffy')
        self.shelter.enqueue('cat', 'Yoda')

    def test_enqueue_cat(self):
        shelter = AnimalShelter()
        shelter.enqueue('cat', 'Yoda')
        self.assertEqual("You have adopted a cat named Yoda.",
                         shelter.dequeue('cat'))

    def test_enqueue_dog(self):
        shelter = AnimalShelter()
        shelter.enqueue('dog', 'Bear')
        self.assertEqual("You have adopted a dog named Bear.",
                         shelter.dequeue('dog'))

    def test_dequeue_cat(self):
        self.assertEqual("You have adopted a cat named Buffy.",
                         self.shelter.dequeue('cat'))

    def test_dequeue_dog(self):
        self.assertEqual("You have adopted a dog named Bear.",
                         self.shelter.dequeue('dog'))

    def test_dequeue_any(self):
        self.assertEqual("You have adopted a dog named Bear.",
                         self.shelter.dequeue())

    def test_dequeue_cat_twice(self):
        self.shelter.dequeue('cat')
        self.assertEqual("You have adopted a cat named Yoda.",
                         self.shelter.dequeue('cat'))

    def test_no_dogs(self):
        shelter = AnimalShelter()
        shelter.enqueue('cat', 'Yoda')
        self.assertEqual("The animal shelter currently has no dogs.",
                         shelter.dequeue('dog'))

    def test_no_cats(self):
        shelter = AnimalShelter()
        shelter.enqueue('dog', 'Bear')
        self.assertEqual("The animal shelter currently has no cats.",
                         shelter.dequeue('cat'))

    def test_is_empty(self):
        shelter = AnimalShelter()
        self.assertEqual("The animal shelter currently has no animals for adoption.",
                         shelter.dequeue())

if __name__ == '__main__':
    unittest.main()
