from itertools import combinations

class ballanced_parentheses:
    def __init__(self, n: int) -> None:
        self.brackets = ['(', ')']
        self.n = n*2
        self.gen_brackets = self.__gen_brackets()
        self.combination_brackets = self.__bracket_combinations()

    def __gen_brackets(self) -> list:
        return [i for i in self.brackets]*self.n

    def __bracket_combinations(self) -> list:
            '''generate an unique brackets combination
            that distincts from each other'''
            return list(combinations(self.gen_brackets, self.n))
        
    def check_validity(self, brackets: list) -> bool:
        stack = []
        for i in brackets:
            if i == "(":
                stack.append(i)
            elif i in ")":
                if len(stack) == 0:
                    return False
                else:
                    stack.pop()
        if len(stack) == 0:
            return True
        else:
            return False
        
    def get_brackets(self) -> list:
        if self.n == 0:
            return ['']
        return [i for i in self.combination_brackets]


balanced_parens = lambda n: ballanced_parentheses(n).get_brackets()
print(balanced_parens(3))
