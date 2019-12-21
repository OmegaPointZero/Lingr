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

Still working out how to build the AST; I think it's appropriate to start out evaluating 2-token statements, and from there reading ahead to evaluate what needs to be done in what order. 

## State of Development - Current Sprint Objectives

### Primary objective: pass these lingr .lr files to the interpreter:

File 1:

```
9 + 18;
9 + (3 * 9);
```

Such that `9+18` is identified as an ADD expression, and will be passed to the interpreter as an {`ADD 0x09 0x12`} set of instructions. `9 + (3*9)` Should be passed as  {`MULT 03 09 VAR1 ADD 09 VAR1`}, or something along those lines. I don't know how the AST will format the information being passed along to the interpreter or the compiler, but I think it would be efficient to figure out how to create a class recursively to evaluate this kind of thing in an optimized way. Ultimately, I want to be able to compile 9+18 in machine code with the compiler, but also be able to optimize it in the AST before passing it along to an interpreter or the compiler. 

File 2:

```
_string = "Hello, world!"
_string + " Longr livr lingr!"
_string + 1
```

It should have _string equal to "Hello, world!", "Hello, world! Longr livr lingr!" and "Hello, world! Longr livr lingr!1". Whatever you do in lingr, it does. If the AST can parse all of these successfully, making something like {`[SET _string STRING "Hello, world"] [ADD _string " Longr livr lingr!"] [ADD _string 1] (<-- but make it the text, not the char at 0x01)`}, then all of the present cases for + are handled!
