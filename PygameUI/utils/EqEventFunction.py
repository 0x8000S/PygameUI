from typing import Any, Callable


class EqEventFunction:
    def __init__(self, Func:Callable, Variable:Any):
        self.call = Func
        self.var = Variable
    def __call__(self, *args, **kwds):
        return self.var
    def __setattr__(self, name, value):
        print("aa")
        self.var = value
        self.call(value)
