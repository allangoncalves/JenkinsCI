# -*- coding: utf-8 -*-


class Calculator():
    def add(self, a, b):
        if(self.valid_types([a, b])):
            return a + b
        else:
            raise NotImplementedError(
                    "Sorry, we have not implemented this funcionality yet."
                )

    def sub(self, a, b):
        if(self.valid_types([a, b])):
            return a - b
        else:
            raise NotImplementedError(
                    "Sorry, we have not implemented this funcionality yet."
                )

    def valid_types(self, variables):
        return all(
                isinstance(variable, int) or isinstance(variable, float)
                for variable in variables
            )
