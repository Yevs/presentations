class Store:

    def __init__(self, reducer, defaultState=None):
        self.reducer = reducer
        self.state = defaultState
        self.listeners = []

    def subscribe(self, listener):
        self.listeners.append(listener)

    def dispatch(self, action):
        self.state = self.reducer(action, self.state)
        for listener in self.listeners:
            listener(self.state)
