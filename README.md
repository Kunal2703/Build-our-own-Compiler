# Build-our-own-Compiler
A compiler converts computer code from one language to another without altering the program's meaning. It is also assumed that a compiler would produce space and time efficient, effective target code. The compilation process is divided into steps. Each step of the compiler receives input from the stage before it, has its own representation of the source code, and feeds its output to the stage after. The compiler examines the source code, separates it into its component components, and then does a lexical, grammar, and syntax check. Assembly Language Code, which is also known as intermediate code, is produced during the analysis phase.
## STRUCTURE OF THE COMPILER DESIGN
Phases of the Compiler: A compiler operates in stages. A phase is an operation that logically connects two representations by taking a source programme from one and producing an output in the other.


<img width="309" alt="image" src="https://user-images.githubusercontent.com/78562069/210045410-ecace9e3-7ea8-4a37-ac04-be6a26e19b23.png">

### Lexical Analysis: 
Tokens are created using a lexical analyser from a stream of input string characters. Tokens are then broken down into smaller parts to create meaningful expressions. The smallest unit in a programming language with meaning (such as +, -, *, or "function") is called a token. 
 
<img width="188" alt="image" src="https://user-images.githubusercontent.com/78562069/210045507-1274dbd3-c15b-4169-bc2a-6b72b4bb9cbb.png">
