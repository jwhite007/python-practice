#! /usr/bin/env python

class LogicGate(object):
    def __init__(self, n):
        self.name = n
        self.output = None

    def get_name(self):
        return self.name

    def get_output(self):
        return self.perform_gate_logic()


class BinaryGate(LogicGate):
    def __init__(self, n):
        LogicGate.__init__(self, n)
        self.pinA = None
        self.pinB = None

    def get_pinA(self):
        return self.pinA.get_from().get_output()

    def get_pinB(self):
        return self.pinB.get_from().get_output()

    def set_next_pin(self, source):
        if self.pinA is None:
            self.pinA = source
        elif self.pinB is None:
            self.pinB = source
        else:
            return 'Cannot connect... no empty pins'


class AndGate(BinaryGate):
    def __init__(self, n, a = None, b = None):
        BinaryGate.__init__(self, n)
        self.a = a
        self.b = b

    def perform_gate_logic(self):
        if self.a is None:
            self.a = self.get_pinA()
        if self.b is None:
            self.b = self.get_pinB()
        if self.a == 1 and self.b == 1:
            return 1
        else:
            return 0

class NAndGate(BinaryGate):
    def __init__(self, n, a = None, b = None):
        BinaryGate.__init__(self, n)
        self.a = a
        self.b = b

    def perform_gate_logic(self):
        if self.a is None:
            self.a = self.get_pinA()
        if self.b is None:
            self.b = self.get_pinB()
        if self.a == 1 and self.b == 1:
            return 0
        else:
            return 1

class OrGate(BinaryGate):
    def __init__(self, n, a = None, b = None):
        BinaryGate.__init__(self, n)
        self.a = a
        self.b = b

    def perform_gate_logic(self):
        if self.a is None:
            self.a = self.get_pinA()
        if self.b is None:
            self.b = self.get_pinB()
        if self.a == 1 or self.b == 1:
            return 1
        else:
            return 0

class NOrGate(BinaryGate):
    def __init__(self, n, a = None, b = None):
        BinaryGate.__init__(self, n)
        self.a = a
        self.b = b

    def perform_gate_logic(self):
        if self.a is None:
            self.a = self.get_pinA()
        if self.b is None:
            self.b = self.get_pinB()
        if self.a == 1 or self.b == 1:
            return 0
        else:
            return 1

class XOrGate(BinaryGate):
    def __init__(self, n, a = None, b = None):
        BinaryGate.__init__(self, n)
        self.a = a
        self.b = b

    def perform_gate_logic(self):
        if self.a is None:
            self.a = self.get_pinA()
        if self.b is None:
            self.b = self.get_pinB()
        if (self.a == 1) ^ (self.b == 1):
            return 1
        else:
            return 0

class UnaryGate(LogicGate):
    def __init__(self, n):
        LogicGate.__init__(self, n)
        self.pin = None

    def get_pin(self):
        if self.pin is None:
            return self.pin.get_from().get_output()

    def set_next_pin(self, source):
        if self.pin is None:
            self.pin = source
        else:
            return 'Cannot connect... pin is not empty'

class NotGate(UnaryGate):
    def __init__(self, n, a = None):
        UnaryGate.__init__(self, n)
        self.pin = a

    def perform_gate_logic(self):
        if self.pin is None:
            self.pin = self.get_pin()
        if self.pin:
            return 0
        else:
            return 1


class Connector(object):
    def __init__(self, fgate, tgate):
        self.from_gate = fgate
        self.to_gate = tgate

        tgate.set_next_pin(self)

    def get_from(self):
        return self.from_gate

    def get_to(self):
        return self.to_gate

if __name__ == '__main__':
    # g1 = AndGate('G1', 0, 0)
    # g2 = AndGate('G2', 1, 1)
    # g3 = XOrGate('G3')
    # g4 = NotGate('G4')
    # c1 = Connector(g1, g3)
    # c2 = Connector(g2, g3)
    # c3 = Connector(g3, g4)
    # print(g4.get_output())

    g1 = AndGate('G1', 1, 1)
    g2 = AndGate('G2', 1, 1)
    g3 = XOrGate('G3')
    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    g4 = NAndGate('G4', 1, 1)
    g5 = NAndGate('G5', 1, 1)
    g6 = OrGate('G6')
    c3 = Connector(g4, g6)
    c4 = Connector(g5, g6)
    print(g3.get_output() == g6.get_output())
