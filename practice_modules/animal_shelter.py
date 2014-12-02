#! /usr/bin/env python

"""This program implements the Animal-Shelter inverview question outlined in
the chapter "Stacks and Queues" in "Cracking the Coding Interview" by Gayle
Laakman McDowell"""

from Queue import Queue

class AnimalShelter(object):
    """Uses two queues to model an animal shelter in which an adopted pet is
    always the pet which has been in the animal shelter the longest of the type
    'kind'."""

    def __init__(self):
        # super(animalShelter, self).__init__()
        self.queue1 = Queue()
        self.queue2 = Queue()
        self.current_queue = self.queue1
        self.next_queue = self.queue2

    def enqueue(self, kind, name):
        """Places an animal into the animal shelter.
        Two arguments, kind and name, are required"""
        self.current_queue.put((kind, name))

    def dequeue(self, kind='any'):
        """Used when someone adopts a pet. If the animal selection is 'any',
        the pet gets dequeued from the current queue. If the first pet dequeued
        from the current queue is of type 'kind', that pet is returned otherwise
        the current queue gets dequeued into the next queue until the desired
        'kind' is encountered. This pet gets dequeued for adoption and the
        rest of the queue is dequeued into the next queue. At this point the
        next queue becomes the current queue which becomes the next_queue."""

        if self.current_queue.empty():
            return "The animal shelter currently has no animals for adoption."
        if kind == 'any':
            animal, name = self.current_queue.get()
            return "You have adopted a " + animal + " named " + name + "."
        else:
            adopted = False
            name = None
            while not self.current_queue.empty():
                pet = self.current_queue.get()
                if adopted is False and pet[0] == kind:
                    adopted = True
                    name = pet[1]
                    if self.next_queue.empty():
                        break
                else:
                    self.next_queue.put(pet)
            if self.current_queue.empty():
                self.current_queue, self.next_queue = self.next_queue, self.current_queue
            if adopted is False:
                return "The animal shelter currently has no " + kind + "s."
            else:
                return "You have adopted a " + kind + " named " + name + "."


if __name__ == '__main__':
    shelter = AnimalShelter()
    shelter.enqueue('dog', 'Bear')
    shelter.enqueue('cat', 'Buffy')
    shelter.enqueue('cat', 'Yoda')
    print shelter.dequeue('cat')
    print shelter.dequeue('cat')
    shelter.enqueue('cat', 'Chelsea')
    print shelter.dequeue('any')
    print shelter.dequeue('dog')
    shelter.enqueue('cat', 'Oscar')
    print shelter.dequeue('cat')
