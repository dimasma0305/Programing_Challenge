from itertools import combinations
import cProfile

class ballanced_parentheses:
    def __init__(self, n: int) -> None:
        self.brackets = ['(', ')']
        self.n = n*2
        self.combination_brackets = self.__bracket_combinations()

    def __bracket_combinations(self) -> list:
            n = set(combinations([i for i in self.brackets]*self.n, self.n))
            lst = []
            for i in n:
                if self.check_validity(i):
                    lst += [i]
            return lst
        
    def check_validity(self, brackets: list) -> bool:
        stack = []
        for i in brackets:
            if i == "(":
                stack += [i]
            elif i in ")":
                if len(stack) == 0:
                    return False
                else:
                    stack = stack[:-1]
        if len(stack) == 0:
            return True
        else:
            return False
        
    def get_brackets(self) -> list:
        if self.n == 0:
            return ['']
        return [''.join(i) for i in self.combination_brackets]



balanced_parens = lambda n: ballanced_parentheses(n).get_brackets()
print(balanced_parens(1))
# cProfile.run('balanced_parens(7)')