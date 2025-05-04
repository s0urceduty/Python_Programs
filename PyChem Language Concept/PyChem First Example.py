# Import the necessary classes from the PyChem module
from pychem import Substance, Reaction, ChemicalEquationParser

def main():
    # Initialize the chemical equation parser
    parser = ChemicalEquationParser()

    # Ask the user to input a chemical equation
    equation_input = input("Enter a chemical equation to parse and balance (e.g., '2 H2 + O2 -> 2 H2O'): ")

    # Parse the chemical equation
    parsed_reaction = parser.parse(equation_input)

    # Check if the parsing was successful
    if parsed_reaction:
        print("Parsed Reaction:", parsed_reaction)
        # Assuming a balance function exists (if not, use manual or other balancing methods here)
        # balanced_reaction = balance_reaction(parsed_reaction)
        # print("Balanced Reaction:", balanced_reaction)
    else:
        print("Failed to parse the equation. Please ensure it is formatted correctly.")

if __name__ == "__main__":
    main()

