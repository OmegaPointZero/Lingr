# Lingr

Lingr is a programming language in it's infancy, it's first version being written in Python3. 


## Lexer 

It has a basic lexer that can tokenize the following:

+ INT integers (ie, `18`)
+ OPERATORS including `= + - * /`
+ STRINGS enclosed by double quotes `"`
+ Parenthesis and braces: `() and []` 
+ END OF LINE identifier `;`

### Next to include

+ Modulus (`%`)
+ Braces (`{}`)
+ Increment and decrement (`++` and `--`)
+ Arrays
+ Objects

## Abstract Syntax Tree

The AST is finally starting to take shape, and with the rewriting of it, shaping the direction of the project. So far, the file gets parsed into individual tokens, as long as they match the above criteria. The lexed tokens are then passed to the AST. The AST then takes said tokens (in a list), and returns a list of lists. The contained lists are modified lists of tokens, where anything within a line of code contained within parenthesis is replaced with a variable, RESOLVABLEi. All arrays after the first one should begin with an object identifying the beginning of a RESOLVABLE variable, as well as it's ID. The last item should end with an object identifying the end of that RESOLVABLE variable. The tokens in between are the contents of those parenthesis. So, 1 + ( 2 + 3) becomes `[1 + RESOLVABLE0], [START_RESOLVABLE0 2 + 3 END_RESOLVABLE0]` The order is then reversed, to start resolving from the bottom up (so that nested parentheses are correctly parsed and resolved).

Due to scrapping the old AST logic, the next objectives have changed

## Development objectives

### Primary

+ Rewrite the lexer to scrutinze whitespace seperated items harder. `1 + (2 + 3)` would be parsed correctly, `1 + (2+3)` wouldn't. 
+ Create a function to create tree leaves, and break everything down into pseudo-assembly: An operation, a source, and a destination. 1 + 2 becomes `[{'TYPE': 'INT', 'TOKEN': '1'}, {'TYPE': 'OPERATOR', 'TOKEN': '+'}, {'TYPE': 'INT', 'TOKEN': '2'}]`, which should then become `ADD 1 2`, which is, of course, much easier to translate into asm, the next step before translating into machine code directly. 

### Tertiary

+ Once whitespace seperated items are parsed better, identify the increment and decrement operators. Lex braces in the same way, and add a symbol for the modulus.
+ Add a "print" function. An identifier, so that I can print shit to the console. May come before or after the first compiler version.

## Looking ahead

Once the tree has leaves in statements that can be digested into pseudoassembly, I'll start on the compiler to make ELF files. 32-bit to start, with a 64-bit option added after I work out the kinks in the rudimentary 32 bit one. Print'll be fun to figure out, and highlights that I'll need to work out how to find the right syscall numbers. 

Once I can compile an executable, run it without error, and have it add, subtract, divide, and multiply, and print out what it calculates, I can start looking into how to hold variables, objects and arrays in memory, and access them. 
