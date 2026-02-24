# CutePy Compiler

Compiler for the **CutePy programming language**, implemented in Python.  
  
The compiler translates CutePy programs into intermediate code and finally into **RISC-V assembly**, executable using the RARS simulator.  
  
> Developed as part of the *Compilers* course at the Department of Computer Science and Engineering, University of Ioannina.
> 
## Features

-   Lexical Analysis (token recognition)
    
-   Recursive Descent Syntax Parser
    
-   Semantic Analysis
    
-   Symbol Table Management
    
-   Intermediate Code Generation (Quadruples)
    
-   Final Code Generation
    
-   Syntax and Semantic Error Detection

## Compilation Pipeline

CutePy Source (.cpy) -> Lexical Analysis -> Syntax Analysis -> Semantic Analysis -> Intermediate Code (.int) -> Symbol Table (.symb) -> RISC-V Assembly (.asm)


## Project Structure

cutePy-compiler/
├── cutePy-compiler.py      # Main compiler implementation
├── run_tests.py            # Test runner for all examples
├── examples/
│   ├── valid/              # Fully supported CutePy programs
│   ├── syntax_errors/      # Programs containing syntax errors
│   └── semantic_errors/    # Programs containing semantic errors
├── demo/
│   ├── test.cpy            # Example CutePy source program
│   ├── test.int            # Generated intermediate code
│   ├── test.symb           # Generated symbol table
│   └── test.asm            # Generated RISC-V assembly
├── report(greek)/
│   └── report.docx         # Project report (Greek)
└── README.md

## Known Limitations

This compiler follows the CutePy specification used in the course assignment.

-   Functions must be declared before they are used (no forward declarations).
    
-   Only the CutePy grammar defined in the assignment is supported.
    
-   The project is intended for educational purposes.
## How to Run
Compile a CutePy program:
- py cutepy-compiler.py examples/valid/while_sum.cpy

Run all example programs:
- py run_tests.py


## Authors

Stalikas Dimitrios , Voutsinas Andreas 
>Department of Computer Science and Engineering
>University of Ioannina
