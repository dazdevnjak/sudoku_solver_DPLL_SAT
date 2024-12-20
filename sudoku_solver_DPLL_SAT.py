import sys
import copy

RECURSION_LIMIT = 100000
sys.setrecursionlimit(RECURSION_LIMIT)

subgrid_dimensions = 3
grid_dimensions = subgrid_dimensions ** 2

DIGITS = [i for i in range(1, grid_dimensions + 1)]

def hash_mapping(row, col, val):
    return row * grid_dimensions * grid_dimensions + col * grid_dimensions + val

def only_one_true(values):
    clauses = [values[:]]  # At least one must be true
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            clauses.append([-values[i], -values[j]])  # No two values can be true simultaneously
    return clauses

def initialize_limitations():
    clauses = []

    # Cell constraints
    for row in range(grid_dimensions):
        for col in range(grid_dimensions):
            values = [hash_mapping(row, col, val) for val in DIGITS]
            clauses.extend(only_one_true(values))

    # Row constraints
    for row in range(grid_dimensions):
        for val in DIGITS:
            values = [hash_mapping(row, col, val) for col in range(grid_dimensions)]
            clauses.extend(only_one_true(values))

    # Column constraints
    for col in range(grid_dimensions):
        for val in DIGITS:
            values = [hash_mapping(row, col, val) for row in range(grid_dimensions)]
            clauses.extend(only_one_true(values))

    # Block constraints
    for block_row in range(subgrid_dimensions):
        for block_col in range(subgrid_dimensions):
            for val in DIGITS:
                values = []
                for row in range(block_row * subgrid_dimensions, (block_row + 1) * subgrid_dimensions):
                    for col in range(block_col * subgrid_dimensions, (block_col + 1) * subgrid_dimensions):
                        values.append(hash_mapping(row, col, val))
                clauses.extend(only_one_true(values))
                
    return clauses

def encode_sudoku(puzzle):
    clauses = []
    for row in range(grid_dimensions):
        for col in range(grid_dimensions):
            val = puzzle[row][col]
            if val != 0:
                clauses.append([hash_mapping(row, col, val)])
    return clauses

def process_unit_clauses(clauses, assignment):
    assignment = assignment.copy()
    while True:
        unit_clauses = [clause for clause in clauses if len(clause) == 1]
        if not unit_clauses:
            break  # No more unit clauses to process

        for unit in unit_clauses:
            literal = unit[0]
            variable = abs(literal)
            value = literal > 0

            if variable in assignment:
                if assignment[variable] != value:
                    return False  # Conflict detected
            else:
                assignment[variable] = value

            new_clauses = []
            for clause in clauses:
                if literal in clause:
                    continue  # Clause is satisfied
                if -literal in clause:
                    new_clause = [lit for lit in clause if lit != -literal]
                    if not new_clause:
                        return False  # Conflict detected
                    new_clauses.append(new_clause)
                else:
                    new_clauses.append(clause)
            clauses = new_clauses

    return clauses, assignment

def select_variable(clauses, assignment):
    unassigned_vars = set()
    for clause in clauses:
        for literal in clause:
            variable = abs(literal)
            if variable not in assignment:
                unassigned_vars.add(variable)
    if not unassigned_vars:
        return None
    return next(iter(unassigned_vars))  # Return any unassigned variable

def DPLL(clauses, assignment):
    result = process_unit_clauses(clauses, assignment)
    if result == False:
        return None  # Conflict detected
    clauses, assignment = result
    if not clauses:
        return assignment  # All clauses satisfied

    variable = select_variable(clauses, assignment)
    if variable is None:
        return assignment

    for value in [True, False]:
        new_assignment = assignment.copy()
        new_assignment[variable] = value
        new_clauses = copy.deepcopy(clauses)  # Deep copy of clauses

        # Add the new assignment as a unit clause
        if value:
            new_clauses.append([variable])
        else:
            new_clauses.append([-variable])

        result = DPLL(new_clauses, new_assignment)
        if result is not None:
            return result  # Solution found

    return None  # No solution found

def decode_sudoku(assignment):
    grid = [[0 for _ in range(grid_dimensions)] for _ in range(grid_dimensions)]
    for variable, value in assignment.items():
        if value:
            v = variable - 1
            row = v // (grid_dimensions * grid_dimensions)
            v %= grid_dimensions * grid_dimensions
            col = v // grid_dimensions
            val = v % grid_dimensions + 1
            if grid[row][col] != 0:
                print(f"Error: Cell ({row}, {col}) assigned multiple values.")
            else:
                grid[row][col] = val
    return grid

def main():
    puzzle = [
        [8, 0, 0,   0, 0, 0,    0, 0, 0],
        [0, 0, 3,   6, 0, 0,    0, 0, 0],
        [0, 7, 0,   0, 9, 0,    2, 0, 0],

        [0, 5, 0,   0, 0, 7,    0, 0, 0],
        [0, 0, 0,   0, 4, 5,    7, 0, 0],
        [0, 0, 0,   1, 0, 0,    0, 3, 0],  

        [0, 0, 1,   0, 0, 0,    0, 6, 8],
        [0, 0, 8,   5, 0, 0,    0, 1, 0],
        [0, 9, 0,   0, 0, 0,    4, 0, 0]
    ]

    clauses = initialize_limitations()
    clues = encode_sudoku(puzzle)
    clauses.extend(clues)
    assignment = {}
    result = DPLL(clauses, assignment)

    if result is not None:
        solution = decode_sudoku(result)
        print("Sudoku solution:")
        for row in solution:
            print(" ".join(str(d) for d in row))
    else:
        print("No solution exists.")

if __name__ == "__main__":
    main()
