from enum import Enum 
import sys
from tkinter import *


class TokenType(Enum):

    END_OF_FILE = -1
    NEWLINE = 0     #\n
    NUMBER = 1      #1,2,3,4....
    IDENTIFIER = 2       #IDENTIFIERifier variables
    STRING = 3      #string variables

    # Keywords.     
    PRINT = 100    # "cout"
    INPUT = 101 
    LET = 102        # "Variable"
    IF = 103
    THEN = 104
    ENDIF = 105

	# Operators.
    EQUAL_TO = 201       # "="
    PLUS = 202          # "+"
    MINUS = 203          # "-"
    ASTERISK = 204       # "*"
    SLASH = 205         # "/"
    EQUAL_TO_EQUAL_TO = 206  # "=="
    NOT_EQUAL_TO = 207     # "!="
    LESS_THEN = 208         # "<"
    LESS_THEN_EQUAL_TO = 209     # "<="
    GREATER_THEN = 210          # ">"
    GREATER_THEN_EQUAL_TO = 211    # ">="


class Lexer:
    
    def __init__(self,input):
        self.source = input + '\n'
        self.current_character = ''
        self.current_position = -1
        self.next_character()
    
    
    def next_character(self):
        self.current_position += 1
        if self.current_position >= len(self.source):
            self.current_character = '\0'
        else:
            self.current_character = self.source[self.current_position]
    
    def peek(self):
        if self.current_position + 1 >= len(self.source):
            return '\0'
        
        return self.source[self.current_position + 1]
    

    # Invalid token found, print error message and exit.
    def abort(self,message):
        print(self.current_character)
        sys.exit("Lexing error: " + self.peek())
    
    
    # Skip whitespace except newlines, which we will use to indicate the end of a statement.
    def skipWhiteSpace(self):
        while self.current_character == ' ' or self.current_character == '\t' or self.current_character == '\r':
            self.next_character()
    
    def skipComment(self):
        if self.current_character == '#':
            while self.current_character != '\n':
                self.next_character()
    
    
    
    #detects a specific token
    def getToken(self):
        self.skipWhiteSpace()
        token = None
        
        if self.current_character == '+':
            token = Token(self.current_character, TokenType.PLUS)
        elif self.current_character == '-':
            token = Token(self.current_character, TokenType.MINUS)
        elif self.current_character == '*':
            token = Token(self.current_character, TokenType.ASTERISK)
        elif self.current_character == '/':
            token = Token(self.current_character, TokenType.SLASH)
        elif self.current_character == '\n':
            token = Token(self.current_character, TokenType.NEWLINE)
        elif self.current_character == '\0':
            token = Token('', TokenType.END_OF_FILE)
            
        elif self.current_character == '=':
            token = Token('=', TokenType.EQUAL_TO)

 #------ For > or >=           
        elif self.current_character == '>':
            if(self.peek() == "="):
                last_character = self.current_character
                self.next_character()
                token = Token(last_character + self.current_character, TokenType.GREATER_THEN_EQUAL_TO)
            else:
                token = Token(self.current_character, TokenType.GREATER_THEN)
                
#------For < or <=
        elif self.current_character == '<':
            if(self.peek() == "="):
                last_character = self.current_character
                self.next_character()
                token = Token(last_character + self.current_character, TokenType.LESS_THEN_EQUAL_TO)
            else:
                token = Token(self.current_character, TokenType.LESS_THEN)
                
#------ For !=
        elif self.current_character == '!':
            if(self.peek() =='='):
                last_character = self.current_character
                self.next_character()
                token = Token(last_character + self.current_character, TokenType.NOT_EQUAL_TO)
            else:
                self.abort("Unexpected Error"+self.peek())
                
        elif self.current_character.isalpha():
            start_position = self.current_position
            while self.peek().isalpha():
                self.next_character()
                
            tokText = self.source[start_position: self.current_position + 1]
            Keywords = Token.checkIfKeyword(tokText)
            if(Keywords == None):
                token = Token(tokText, TokenType.IDENTIFIER)
            else:
                token = Token(tokText, Keywords)
        
        #----For string------------
        elif self.current_character == '\"':
            self.next_character()
            start_position = self.current_position
            while(self.current_character != '\"'):
                if (self.current_character == '\n' or self.current_character == '\t'):
                    print("abort by 6")
                    self.abort("The Formate of String is Illegal...")
                self.next_character()
                
            tokText = self.source[start_position:self.current_position]
            token = Token(tokText, TokenType.STRING)
        
        #------For Digits-------------
        elif self.current_character.isdigit():
            start_position = self.current_position
            while(self.peek().isdigit()):
                self.next_character()
                
            tokText = self.source[start_position : self.current_position +1]
            token = Token(tokText, TokenType.NUMBER)
                    
                    
             
        else:
            #print("abort by 5")
            self.abort("Unknown token: " + self.current_character)
        
        self.next_character()
        return token
    
#----------Parser ---------------------------------

class Parser:
    def __init__(self, lexer, code_generator):
        self.lexer = lexer
        
        self.code_generator = code_generator
        
        self.symbols = set()
        
        self.curToken = None
        self.peekToken = None
        
        self.nextToken()
        self.nextToken()            #call this twicw to initialize current and peek
    
    def checkToken(self, kind):             #return true if the current token match
        return kind == self.curToken.kind
    
    def checkpeek(self, kind):              #return true if the next token match
        return kind == self.peekToken.kind
    
    def match(self, kind):                  
        if not self.checkToken(kind):
            #print("abort by 4")
            self.abort("Expected " +kind.name + " got " + self.curToken.kind.name)
        self.nextToken()
    
    def nextToken(self):
        self.curToken = self.peekToken
        self.peekToken = self.lexer.getToken()
        
    
    def abort(self, message):
        sys.exit("Error: " + message)


    def program(self):
        #print("Program")
        self.code_generator.headerLine("#include <iostream>")
        self.code_generator.headerLine("using namespace std;")
        self.code_generator.headerLine("int main()")
        self.code_generator.headerLine("{")
        
        while self.checkToken(TokenType.NEWLINE):
            self.nextToken()
        
        while not self.checkToken(TokenType.END_OF_FILE):
            self.statement()
            
        self.code_generator.CodeLine("return 0;")
        self.code_generator.CodeLine("}")            
            
#---------- comparison oprators
#             i.e, >, <, >=, <=, ==, !=

    def isComparisonOperator(self):
        return self.checkToken(TokenType.GREATER_THEN) or self.checkToken(TokenType.LESS_THEN) or self.checkToken(TokenType.GREATER_THEN_EQUAL_TO) or self.checkToken(TokenType.LESS_THEN_EQUAL_TO) or self.checkToken(TokenType.EQUAL_TO_EQUAL_TO) or self.checkToken(TokenType.NOT_EQUAL_TO)
    
#---------- Expression Operators
#              i.e., --> + , -

    def expression(self):
        #print("EXPRESSION")

#-----------Example: a*b+c/d
#           after apply term condition
#              -> (a*b) + (c/d) 
        self.term()
        while(self.checkToken(TokenType.PLUS) or self.checkToken(TokenType.MINUS)):
            self.code_generator.Code(self.curToken.text)
            self.nextToken()
            self.term()

#-------- term are divide into Unary
#           i.e,  * , /
    def term(self):
        print("Term")
        self.unary()
        while(self.checkToken(TokenType.ASTERISK) or self.checkToken(TokenType.SLASH)):
            self.code_generator.Code(self.curToken.text)
            self.nextToken()
            self.unary()
            
            
    def unary(self):
        #print("Unary")
        
#------ Unary Operators -> + or -
        if(self.checkToken(TokenType.PLUS) or self.checkToken(TokenType.MINUS)):
            self.code_generator.Code(self.curToken.text)
            self.nextToken()
        self.primary()
        
    def primary(self):
        #print("Primary -> " + self.curToken.text)
        if(self.checkToken(TokenType.NUMBER)):
            self.code_generator.Code(self.curToken.text)
            self.nextToken()
        elif(self.checkToken(TokenType.IDENTIFIER)):
            if(self.curToken.text not in self.symbols):
                self.abort("The referecing variables before assignment: " +self.curToken.text)
            self.code_generator.Code(self.curToken.text)
            self.nextToken()
            
        else:
            #print("abort by 3")
            self.abort("Error!! Token are Unexpected : " + self.curToken.text) 
               
        
#------------statement -> PRINT {expression | string } and then new line -----------------
    def statement(self):
#---------"PRINT" {(expression | string)}
        if(self.checkToken(TokenType.PRINT)):
            #print("Statement-PRINT")
            self.nextToken()
            
            if self.checkToken(TokenType.STRING):
                #self.code_generator.CodeLine("cout << \"" + self.curToken.text +  " \\n\";")
                self.code_generator.CodeLine("cout << \"" + self.curToken.text +  " \";")
                self.nextToken()
            elif self.checkToken(TokenType.IDENTIFIER):
                self.code_generator.CodeLine("cout << " + self.curToken.text + ";")
                self.nextToken()
            else:
                #self.code_generator.CodeLine("cout << " + self.curToken.text + ";")
                self.expression()
                
#------------IF comparison THEN 
#               new line i.e., newLine
#                  {STATEMENT}
#                       ENDIF
#               NEW LINE i.e., newLine

        elif self.checkToken(TokenType.IF):
            #print("Statement-IF")
            self.nextToken()
            self.code_generator.Code("if(")
            self.comparison()
            
            self.match(TokenType.THEN)
            self.newLine()
            self.code_generator.CodeLine(")")
            self.code_generator.CodeLine("{")
            
            while not self.checkToken(TokenType.ENDIF):
                self.statement()
                
            self.match(TokenType.ENDIF)
            self.code_generator.CodeLine("}") 
            
#--------INPUT -- IDENTIFIER
        elif self.checkToken(TokenType.INPUT):
            #print("Statement-INPUT")
            self.nextToken()
            if(self.curToken.text not in self.symbols):
                self.symbols.add(self.curToken.text)
                self.code_generator.headerLine("int " + self.curToken.text + ";")
            #self.code_generator.CodeLine("cout << \"" + self.curToken.text +  " \\n\";")
            self.code_generator.CodeLine("cin >>" + self.curToken.text +  ";")
            self.match(TokenType.IDENTIFIER)
            
#------- LET
        elif self.checkToken(TokenType.LET):
            self.nextToken()
            #print("Statement-LET")
            
            if(self.curToken.text not in self.symbols):
                self.symbols.add(self.curToken.text)
                self.code_generator.headerLine("int " + self.curToken.text + ";")
                
            self.code_generator.Code(self.curToken.text + " = ")
            self.match(TokenType.IDENTIFIER)
            self.match(TokenType.EQUAL_TO)
            self.expression()
            self.code_generator.CodeLine(";")
        
#-------- For invalid statement--> gives Error
        else:
            #print("abort by 2")
            self.abort("Invalid Statement at: "+self.curToken.text+ " (" + self.curToken.kind.name+")")
            
#------- New Line    
        self.newLine()

    def comparison(self):
        #print("Comparison")
        
        self.expression()
        if(self.isComparisonOperator()):
            self.code_generator.Code(self.curToken.text)
            self.nextToken()
            self.expression()
            
        while(self.isComparisonOperator()):
            self.code_generator.Code(self.curToken.text)
            self.nextToken()
            self.expression()
     
#-------------newLine -> new line i.e, '\n'+ ----------------       
    def newLine(self):
        print("NEWLINE")
        self.match(TokenType.NEWLINE)
        while self.checkToken(TokenType.NEWLINE):
            self.nextToken()
            

class Token:
    def __init__(self,tokenText, tokenKind):
        self.text = tokenText
        self.kind = tokenKind
        
    @staticmethod
    def checkIfKeyword(tokenText):
        for kind in TokenType:
            if(kind.name == tokenText and kind.value >= 100 and kind.value < 200):
                return kind
            
        return None
      
class CodeGenerator:
    def __init__(self,fullPath):
        self.fullPath = fullPath
        self.headers = ""
        self.code = ""
        
    def Code(self,code):
        self.code += code
        
    def CodeLine(self,code):
        self.code += code + '\n'
        
    def headerLine(self,code):
        self.headers += code + '\n'
        
    def writeFile(self):
        return self.headers+self.code


def compile():
    text1.delete("1.0",END)
    input=text.get("1.0",END)
    lexer = Lexer(input) 
    code_generator=CodeGenerator("result.cpp")
    parser = Parser(lexer, code_generator)

    parser.program() #Start the parser
    text1.insert(END,code_generator.writeFile())

  
#--------------GUI------------------------------
 
root = Tk()
root.title("Kunal's Compiler")
root.geometry()
#root.configure(background= 'blue')

text = Text(root,font=('Times New Roman',25), width=127, height=14, bd= 5, relief='groove', bg = 'Black', foreground="lime", insertbackground='lime')
text.pack()

button = Button(root,font=('Times New Roman',20), text = "Compile", fg='Black', command=compile)  
button.pack()

text1 = Text(root,font=('Times New Roman',25), width=127, height=16, bd= 5, relief='groove', bg = 'Black', foreground="lime",insertbackground='lime')
text1.pack()

root.mainloop()