# 🦜 `caique`

## A unique 8-bit concatenative stack machine based on LC-3 specs
**caique** is a bytecode stack machine and a **concatenative stack language** that uses combinator composition to build subroutines (functions). It employs a very simple syntax that supports algebraic manipulation of programs. Subroutines operate on a shared data structure.

Key aspects of **caique**:
*   *Stack-based operation:* **caique** uses a stack to pass values between combinators. Values are pushed onto the stack, and operations perform computations.
*   *Compositional semantics:* The syntax and semantics is inherently compositional. The reduction of any expression simplifies one function into another, without needing to apply functions.
*   *Point-free style:* **caique** is **point-free**, meaning functions don't explicitly name the data they operate on.
*   *ASCII only:* **caique** only operates over ASCII characters as unsigned integers (from 0 to 127).

**caique** is defined by the following EBNF:

```EBNF
(* Program structure *)
program = expression | definition | program, program ;

(* Basic expressions *)
expression = quotation | combinator | operator | expression, expression ;

(* Definitions *)
definition = identifier, ":=", expression ;

(* Quotations *)
quotation = "[", expression*, "]" ;

(* Built-in combinators *)
combinator = "cat" | "swp" | "dup" | "quo" | "unq" | "del" | identifier ;

(* Built-in operators *)
operator = "in" | "out" | "add" ;
```


### Definitions:
```
      quotation  -->  []
    equivalence  -->  ==
    expressions  -->  A B
      define as  -->  :=
in-line comment  -->  #
```

### Built-in combinators:

```
[B] [A] cat ==  # [B A]    Concatenate
[B] [A] swp ==  # [A] [B]  Alternate / swap
    [A] dup ==  # [A] [A]  Idem / duplicate
    [A] quo ==  # [[A]]    Quote
    [A] unq ==  # A        Unquote
    [A] del ==  #          Erase / delete
```

### Built-in operators:

```
in  # read a ASCII char as input and push the corresponding integer into the stack
out  # given a number output the corresponding ASCII character
add  # add two numbers and push to stack
```

### Defining new combinators

```
 dip  :=  alt qte cat unq   # [B] [A] dip == A [B]
cons  :=  alt qte alt cat   # [B] [A] cons == [[B] A]    
```

### Examples

```
[alt] [idm] cons ==   # result: [[alt] idm]
[alt] [idm] dip  ==   # result: idm [alt]
```

## More info

Concatenative languages --> [https://en.wikipedia.org/wiki/Concatenative_programming_language](https://en.wikipedia.org/wiki/Concatenative_programming_language)

This repo is for the implementation of an LC-3 Virtual Machine with an assembly in C --> [https://en.wikipedia.org/wiki/Little_Computer_3](https://en.wikipedia.org/wiki/Little_Computer_3)

LC-3 VM implementation! --> [https://www.jmeiners.com/lc3-vm/](https://www.jmeiners.com/lc3-vm/)

This book teaches how the LC-3 works (chapters 5 to 10) including architecture, OS, I/O, etc...

Link to the [book](https://www.amazon.com/Introduction-Computing-Systems-Gates-Beyond-dp-1260150534/dp/1260150534/ref=dp_ob_title_bk)
