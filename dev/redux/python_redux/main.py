import time
import random

from action import Action
from store import Store

def reducer(action, state=None):
    if not state:
        state = []
    if action.type == 'ADD_NUMBER':
        new_state = state[:]  # no mutating state
        new_state.append(action.number)
        return new_state
    else:
        return None


def listener(state):
    print('Current state={}'.format(state))         


def main():
    defaultState = []
    store = Store(reducer, defaultState)
    store.subscribe(listener)

    while True:
        store.dispatch(Action('ADD_NUMBER', number=random.random()))
        time.sleep(1)


if __name__ == '__main__':
    main()
