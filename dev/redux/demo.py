class Action:

    def __init__(self, type_, **kwargs):
        self.dict = {}
        self.type = type_
        for arg, value in kwargs.items():
            self.dict[arg] = value

    def __getattr__(self, arg):
        return self.dict[arg]

class Store:

    def __init__(self, reducer, initialState=None):
        self.reducer = reducer
        self.state = initialState
        self.listeners = []

    def dispatch(self, action):
        self.state = self.reducer(action, self.state)
        for listener in self.listeners:
            listener(self.state)

    def subscribe(self, listener):
        self.listeners.append(listener)

def reducer(action, state=None):
    if not state:
        state = []
    if action.type == 'ADD_NUMBER':
        new_state = state[:]
        new_state.append(action.number)
        return new_state
    else:
        return state

def listener(state):
    print('New state={}'.format(state))

store = Store(reducer, [])
store.subscribe(listener)

import time
import random

while True:
    action = Action('ADD_NUMBER', number=random.random())
    store.dispatch(action)
    time.sleep(1)