import re
from collections import defaultdict

class Substance:
    def __init__(self, formula, name=None):
        self.formula = formula
        self.name = name if name else formula

    def __repr__(self):
        return f"Substance('{self.formula}', '{self.name}')"

class Reaction:
    def __init__(self, reactants, products):
        self.reactants = reactants  # Expected as a dictionary {Substance: coefficient}
        self.products = products    # Expected as a dictionary {Substance: coefficient}

    def __repr__(self):
        reactants_str = ' + '.join([f"{coef} {sub.formula}" for sub, coef in self.reactants.items()])
        products_str = ' + '.join([f"{coef} {sub.formula}" for sub, coef in self.products.items()])
        return f"{reactants_str} -> {products_str}"

class ChemicalEquationParser:
    def __init__(self):
        # Regular expression to correctly parse chemical formulas
        self.pattern = re.compile(r"(\d*)\s*([A-Z][a-z]?)(\d*)")

    def parse_substance(self, term):
        """ Parse a single term to extract coefficient and substance formula. """
        matches = self.pattern.findall(term.strip())
        if matches:
            overall_coefficient = int(matches[0][0]) if matches[0][0] else 1
            formula_parts = []
            for match in matches:
                element = match[1]
                count = int(match[2]) if match[2] else 1
                if count > 1:
                    formula_parts.append(f"{element}{count}")
                else:
                    formula_parts.append(f"{element}")
            formula = ''.join(formula_parts)
            sub = Substance(formula)
            return overall_coefficient, sub
        return None, None

    def parse(self, equation):
        """ Parse a full chemical equation into a Reaction object. """
        if '->' in equation:
            left_side, right_side = equation.split('->')
            reactants = {}
            products = {}
            
            for term in left_side.split('+'):
                coef, sub = self.parse_substance(term)
                if sub and coef:
                    reactants[sub] = coef
            
            for term in right_side.split('+'):
                coef, sub = self.parse_substance(term)
                if sub and coef:
                    products[sub] = coef
            
            return Reaction(reactants, products)
        return None
