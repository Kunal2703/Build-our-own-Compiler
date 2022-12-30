# Build-our-own-Compiler
A compiler converts computer code from one language to another without altering the program's meaning. It is also assumed that a compiler would produce space and time efficient, effective target code. The compilation process is divided into steps. Each step of the compiler receives input from the stage before it, has its own representation of the source code, and feeds its output to the stage after. The compiler examines the source code, separates it into its component components, and then does a lexical, grammar, and syntax check. Assembly Language Code, which is also known as intermediate code, is produced during the analysis phase.
## STRUCTURE OF THE COMPILER DESIGN
Phases of the Compiler: A compiler operates in stages. A phase is an operation that logically connects two representations by taking a source programme from one and producing an output in the other.


<img width="309" alt="image" src="https://user-images.githubusercontent.com/78562069/210045410-ecace9e3-7ea8-4a37-ac04-be6a26e19b23.png">

### Lexical Analysis: 
Tokens are created using a lexical analyser from a stream of input string characters. Tokens are then broken down into smaller parts to create meaningful expressions. The smallest unit in a programming language with meaning (such as +, -, *, or "function") is called a token. 
 
<img width="188" alt="image" src="https://user-images.githubusercontent.com/78562069/210045507-1274dbd3-c15b-4169-bc2a-6b72b4bb9cbb.png">


### Syntactic Analysis: 
Determines if the resulting tokens make sense as an expression. This uses a syntax without context to specify algorithmic steps for the components. These combine to create an expression and provide the specific sequence in which tokens need to be arranged. 
 
<img width="190" alt="image" src="https://user-images.githubusercontent.com/78562069/210045560-2690d353-93f2-4e0b-a9cc-77c56b83d9b5.png">

### Semantic Parsing: 
The step of parsing where required actions are made and the meaning and implications of the approved expression are determined. 

<img width="325" alt="image" src="https://user-images.githubusercontent.com/78562069/210045588-ae99011e-a28e-40e0-a51f-7c867b4e8113.png">

### Intermediate Code Generations: 
The machine programme can be created from the source code using intermediary code. Because the compiler cannot produce machine code directly in a single pass, intermediate code is produced. As a result, it first transforms the original programme into intermediate code, which is then used to efficiently generate machine code. 

<img width="204" alt="image" src="https://user-images.githubusercontent.com/78562069/210045636-cf179e02-02a5-4aa5-a984-76291ff89e43.png">

### code optimization: 
Code optimization, a programme transformation method, is used in the synthesis phase to try to optimise the intermediate code by making it use less resources (such as CPU, Memory), which should lead to faster-running machine code. 
 
### code generation: 
The process of code generation may be thought of as the conclusion of compilation. The optimization method can be performed to the code through post code generation, although that can be considered as a component of the code creation step itself. A lower-level programming language's object code is what the compiler produces as its output. 
 
### symbol table: 
In order to record details about the existence of various things, such as variable names, function names, objects, classes, interfaces, etc., compilers constructed and maintain a crucial data structure called a symbol table. Both the analysis and synthesis components of a compiler employ symbol tables. 
 
 
This compiler accept the grammar which is define by user and the compiler follow top-down  approach. 
##Entire grammar for this Compiler.

<img width="452" alt="image" src="https://user-images.githubusercontent.com/78562069/210045712-2423d8ef-ebc2-49c3-b6cf-f3d7bd5b30c9.png">
