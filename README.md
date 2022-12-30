# Build-our-own-Compiler (Custom Compiler)
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

## Entire grammar for this Compiler.

<img width="452" alt="image" src="https://user-images.githubusercontent.com/78562069/210045712-2423d8ef-ebc2-49c3-b6cf-f3d7bd5b30c9.png">

## Our parser will generate trees similar to:- 

<img width="452" alt="image" src="https://user-images.githubusercontent.com/78562069/210045787-c9d82c1e-0eb2-409f-87bc-c4b92b554470.png">

## PARSER:- 
Data is broken down into smaller components by a parser, a component of a compiler or interpreter, to make it easier to translate it into another language. A parser receives input in the form of a series of tokens, interactive commands, or computer instructions and separates it into pieces that may be utilised by other programming components. 
 
 
## Token: 
It is essentially a group of characters that are handled as a whole since it cannot be further divided. Strings may be regarded as tokens in programming languages like C++ language since they are used as keywords (int, char, float, const, etc.), identifiers (user-defined names), operators (+, -, *, /, >, <, >=, <=), delimiters/punctuators like comma (,), semicolon(;);, braces ({} ), etc. 


For this work, the tokens used (refer to Fig1) 
### Control Character 
1.	END_OF_FILE 
2.	NEWLINE 
 
###	Keywords 
1.	PRINT 
2.	INPUT 
3.	LET 
4.	IF 
5.	THEN 
6.	ENDIF 
 
###	Operators 
1.	EQUAL_TO 
2.	PLUS 
3.	MINUS 
4.	ASTERISK 
5.	SLASH 
6.	EQUAL_TO_EQUAL_TO 
7.	NOT_EQUAL_TO 
8.	LESS_THEN 
9.	LESS_THEN_EQUAL_TO 
10.	GRATER_THEN 
11.	GRATER_THEN_EQUAL_TO 
 
###	Types 
1.	STRING 
2.	NUMBER 
 
###	IDENTIFIER 

<img width="452" alt="image" src="https://user-images.githubusercontent.com/78562069/210045947-03f89d59-c568-49ec-92b0-06c2e37470d8.png"> Fig1 – (TokenTypes) 
 
 
A Token class has been defined. The token class consists of the token text and token kind.  
And then class also check the keywords. (refer to Fig2) 

<img width="452" alt="image" src="https://user-images.githubusercontent.com/78562069/210045969-263aff1b-a735-4294-b7fc-fb8f5a391c6e.png"> Fig2 – (Token Class)

After Token Class,  Lexer Class has been define and consists entire source code of the program. To make it easier to lex/parse the final token/statement, append a newline.,  current_character in the String, current_position  in the String and next_character in the String. 

<img width="452" alt="image" src="https://user-images.githubusercontent.com/78562069/210046019-de70e0f4-965d-4118-8364-e530c44f6feb.png"> Fig3 – ( Lexer Class)

The lexer class consists of following methods: 
1. next_character() - Process the next character 
 
<img width="452" alt="image" src="https://user-images.githubusercontent.com/78562069/210046053-670cf6ee-617f-4067-a79d-66408a2189e3.png"> Fig4 – (next_character method)

2. peek() - Return the lookahead character.

<img width="452" alt="image" src="https://user-images.githubusercontent.com/78562069/210046132-c79efdd3-4f97-47d3-8ca9-68979404542d.png"> Fig5 – (peek method) 
 
3. abort() - Found an invalid token; print message, Lexing error. 

<img width="452" alt="image" src="https://user-images.githubusercontent.com/78562069/210046154-f469519a-1bf2-441f-b263-0105ca4c4ca0.png"> Fig6 – (abort method) 
 
4. skipWhiteSpace() - Skip all whitespace besides the newlines we'll use to denote the conclusion of a statement. 

<img width="452" alt="image" src="https://user-images.githubusercontent.com/78562069/210046189-4510802a-2339-4d6e-8d6c-33d44886941a.png"> Fig 7 – (skipWhiteSpace method) 
 
5. skipComment() – Skip comments in the code. 
 
 <img width="452" alt="image" src="https://user-images.githubusercontent.com/78562069/210046211-b9d96416-b3a3-4fcc-9431-607fe1c10034.png"> Fig8 – (skipComment method) 
 
 
6. getToken() - Identify the token and then return the token object. 

<img width="443" alt="image" src="https://user-images.githubusercontent.com/78562069/210046229-99fa76e5-dd72-4ba2-8bdb-491ebfce1188.png">
<img width="452" alt="image" src="https://user-images.githubusercontent.com/78562069/210046256-6275956c-f395-4fe2-8318-e678159b0711.png">
<img width="452" alt="image" src="https://user-images.githubusercontent.com/78562069/210046266-26329402-1a0a-4565-a188-a9b91be13ded.png">
Fig9 –(getToken) 
 
 
Parser class has been define after Lexer, The parser object maintains track of the current token and verifies that the code follows grammatical rules and consists lexer, code_generator, symbols, curToken, peekToken, nextToken  

<img width="452" alt="image" src="https://user-images.githubusercontent.com/78562069/210046290-6485a19e-ca1c-4f23-838d-402dc1168296.png"> Fig10 – (Parser Class) 
 
The Parser class consists of following methods: 
1. checkToken() - If the current token matches, return true. 

<img width="452" alt="image" src="https://user-images.githubusercontent.com/78562069/210046330-76ee8aff-5429-4ef8-a107-d947bbebe9d0.png"> Fig11 – (checkToken method) 
 

2. checkpeek() – If next token matched, return true 

<img width="452" alt="image" src="https://user-images.githubusercontent.com/78562069/210046362-9622ec6c-bc53-454b-a686-3a279c56b02c.png"> Fig12 – (checkpeek method) 
 
3. match() - Check to see whether the token matches. Error if not. 

<img width="452" alt="image" src="https://user-images.githubusercontent.com/78562069/210046395-1d67c9ec-0eb9-4885-af3e-079169ebf950.png"> Fig13 - (match method) 
 
4. nextToken() - the current token is advanced. 

<img width="452" alt="image" src="https://user-images.githubusercontent.com/78562069/210046411-8f670f34-34b6-44c0-a59f-a59cf06b6771.png"> Fig14 – (nextToken method) 
 
 
5. isComparisonOperator() - If a comparison operator is present in the current token, return true. 

<img width="452" alt="image" src="https://user-images.githubusercontent.com/78562069/210046443-0afccdb2-9fd6-4c52-9212-276fb9565ce4.png"> Fig15 – (isComparisonOperator method) 
 
 
6. expression() - expression ::= term {( "-" | "+" ) term} 

<img width="452" alt="image" src="https://user-images.githubusercontent.com/78562069/210046467-2d210bde-c04b-4571-890c-fc1947cedb49.png"> Fig16 – (experession method) 
 
7. term() - term ::= unary {( "/" | "*" ) unary} 

<img width="452" alt="image" src="https://user-images.githubusercontent.com/78562069/210046508-78b42c47-b083-44e1-a666-26c3aab85f1d.png"> Fig17 – (trem method) 
 
8. unary() - unary ::= ["+" | "-"] primary 

<img width="452" alt="image" src="https://user-images.githubusercontent.com/78562069/210046526-7045df49-1e12-4c99-b9a1-e526e76900c7.png"> Fig18 – (unary method) 
 
9. primary() - primary ::= number | ident. If the token is invalid then give Error 

<img width="452" alt="image" src="https://user-images.githubusercontent.com/78562069/210046547-ae19e249-ac78-4e32-bfbd-764b1bfbd9e7.png"> Fig19 – (primary method) 
 
10. statement() – This function handles statements. It checks for the following cases- 
 
a.	If the current token is PRINT, then it checks if the next token is a string or an identifier, otherwise it checks for expression. At the same time, the CodeLine function writes the “cout” statement in the generated code. 

<img width="452" alt="image" src="https://user-images.githubusercontent.com/78562069/210046568-a61fb251-7b3a-4b9c-9190-27d121faafe2.png">

b.	If the current token is IF, then it checks for a comparison. After comparison it checks for THEN keyword. After that all the statements are checked until ENDIF is encountered. The CodeLine function writes the “if” statement in the generated code. 

<img width="452" alt="image" src="https://user-images.githubusercontent.com/78562069/210046595-d8358a7c-2329-4295-a932-6517c89dc338.png">


c.	If the current token is INPUT, then it checks for an identifier. If identifier is then checked with symbol table. If the identifier is not present in the table, then it is added to the symbol table. The CodeLine function defines the identifier if it was not present in the symbol table using “int”. 
 
If the current token is LET, then it checks for an identifier. If identifier is then checked with symbol table. If the identifier is not present in the table, then it is added to the symbol table. Then it checks for “=” and then for an expression. The CodeLine function defines the identifier if it was not present in the symbol table using “int”. 

<img width="452" alt="image" src="https://user-images.githubusercontent.com/78562069/210046617-ba59c4fc-726f-4af9-935f-7e36b0d7b24d.png">

d.	If no statement is found, error is generated.

<img width="452" alt="image" src="https://user-images.githubusercontent.com/78562069/210046649-b0e8320b-27a6-49c2-8b4e-93142e23ff3e.png">


### GUI of the compiler. 
 
<img width="452" alt="image" src="https://user-images.githubusercontent.com/78562069/210046676-1a26fb46-7af4-4679-ae5b-28728f54cbdc.png">


## Final GUI of the Compiler
Positive Execution Report:- 
 
1.	Addition of two number 

<img width="452" alt="image" src="https://user-images.githubusercontent.com/78562069/210046711-624eefb0-689e-4c17-9131-cba5f86a2270.png">

2.	Test whether “a” is greater than “b” (using the > operator). And if condition is true, print “a is greater than b”.

<img width="452" alt="image" src="https://user-images.githubusercontent.com/78562069/210046748-746df90e-e786-46ea-8509-157fcc8f37cf.png">


Negative Execution Report:- 
 
Lexing Error 

<img width="452" alt="image" src="https://user-images.githubusercontent.com/78562069/210046798-e4b2cb05-70e6-4495-9fd8-39f43a781045.png">


IDENTIFIER Error !

<img width="452" alt="image" src="https://user-images.githubusercontent.com/78562069/210046819-5d03f127-fd9d-426e-9519-b684daf93905.png">


