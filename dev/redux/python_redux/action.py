class Action:

    def __init__(self, action_type, **kwargs):
        self.type = action_type
        self.args = {}
        for arg, value in kwargs.items():
            self.args[arg] = value

    def __getattr__(self, arg):
        return self.args[arg]
