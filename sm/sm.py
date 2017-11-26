from sm.utility import *

class MySM:
    def start(self):
        self.state = self.startState
        self.halted = False
    
    def getNextValues(self, state, inp, verbose=False):
        nextState = self.getNextState(state, inp)
        return (nextState, nextState)
    
    def step(self, inp, verbose=False, compact=False):
        (s, o) = self.getNextValues(self.state, inp, verbose)
        self.state = s

        if verbose:
            print ('output of sm: ', o)
        
        return o
    
    def transduce(self, inputs, verbose=False, compact=False):
        self.start()

        if verbose:
            print ('Start state: ' + str(self.startState) + ' .. inputs: ' + str(inputs))
        
        return [self.step(inp, verbose, compact) for inp in inputs if not self.done(self.state)]
    
    def run(self, n=10, verbose=False):
        return self.transduce([undef]*n, verbose)

    def go(self, verbose=False, compact=False):
        self.start()
        
        while(not self.done(self.state)):
            self.step(undef, verbose, compact)
    
    def resume(self, verbose=False, compact=False):
        self.halted = False
        while(not self.done(self.state)):
            self.step(undef, verbose, compact)

    def done(self, state):
        return False