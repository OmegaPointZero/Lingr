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

+ Braces (`{}`)
+ Increment and decrement (`++` and `--`)
+ Arrays
+ Objects

## Abstract Syntax Tree

Still working out how to build the AST; I think it's appropriate to start out evaluating 2-token statements, and from there reading ahead to evaluate what needs to be done in what order. 
