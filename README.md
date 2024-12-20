﻿# 🎯 **Sudoku Solver using DPLL SAT Algorithm**

This repository contains a **Sudoku solver** implemented by encoding the Sudoku puzzle as a **Boolean Satisfiability Problem (SAT)** and solving it using the **Davis-Putnam-Logemann-Loveland (DPLL)** algorithm. 

---

## 🌟 **Features**

- **Efficient SAT Encoding**: Transforms Sudoku constraints into CNF clauses suitable for SAT solving.
- **DPLL Algorithm Implementation**: Utilizes a recursive DPLL algorithm with unit propagation and backtracking.
- **Customizable Puzzles**: Easily input and solve any standard 9x9 Sudoku puzzle.

---


## 🧩 Usage
Input Puzzle 

Modify the puzzle variable in the main() function of sudoku_solver.py to solve a different Sudoku puzzle:

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

    # Rest of the code remains the same

Running the Solver
Execute the script: python sudoku_solver.py

Example Output
Sudoku solution:[
       
        [8, 1, 2,   7, 5, 3,    6, 4, 9],
        [9, 4, 3,   6, 8, 2,    1, 7, 5],
        [6, 7, 5,   4, 9, 1,    2, 8, 3],

        [1, 5, 4,   2, 3, 7,    8, 9, 6],
        [3, 6, 9,   8, 4, 5,    7, 2, 1],
        [2, 8, 7,   1, 6, 9,    5, 3, 4],

        [5, 2, 1,   9, 7, 4,    3, 6, 8],
        [4, 3, 8,   5, 2, 6,    9, 1, 7],
        [7, 9, 6,   3, 1, 8,    4, 5, 2]

]

---


## 📖 How It Works
- Encoding the Puzzle: Each possible cell value is represented as a Boolean variable. The Sudoku constraints are encoded into Conjunctive Normal Form (CNF) clauses suitable for SAT solving.

- Solving with DPLL Algorithm: The solver uses the DPLL algorithm, which includes:

    - Process unit clauses: Simplifies clauses based on current assignments.

    - Backtracking: Explores different variable assignments upon encountering conflicts.

    - Recursive Search: Continues until a satisfying assignment is found or all possibilities are exhausted.

- Decoding the Solution: The satisfying assignment is decoded back into a 9x9 grid format representing the solved Sudoku puzzle.
---


## 🛠 Code Overview
- hash_mapping(row, col, val): Maps each (row, col, val) triplet to a unique integer variable.
- only_one_true(values): Ensures that exactly one variable in a list is true.
- initialize_limitations(): Sets up the Sudoku rules as CNF clauses.
- encode_sudoku(puzzle): Incorporates the initial puzzle clues into the clause set.
- process_unit_clauses(clauses, assignment): Performs unit clause propagation.
- select_variable(clauses, assignment): Chooses the next variable to assign.
- DPLL(clauses, assignment): The core recursive function implementing the DPLL algorithm.
- decode_sudoku(assignment): Converts the final variable assignments back into the Sudoku grid.

---


## 📚 Detailed Explanation

# Variable Mapping
 Each cell-value assignment (row, col, val) is represented by a unique variable.
This mapping allows the solver to use SAT techniques to handle Sudoku constraints.

# Constraints Encoding
- Cell Constraints: Each cell contains exactly one value.
- Row Constraints: Each number appears exactly once in each row.
- Column Constraints: Each number appears exactly once in each column.
- Block Constraints: Each number appears exactly once in each 3x3 subgrid.

# DPLL Algorithm Steps
- Unit Propagation: Simplify clauses with unit literals.
- Conflict Detection: Identify and handle contradictions.
- Variable Selection: Pick an unassigned variable for branching.
- Recursive Search: Try assignments recursively and backtrack as needed.
