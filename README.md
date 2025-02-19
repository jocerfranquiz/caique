# 🦜 `caique`

## tiny concatenative stack machine based on LC-3 specs
`caique` is a bytecode stack machine and a *concatenative stack language* that uses combinator composition to build subroutines (functions). It employs a very simple syntax that supports algebraic manipulation of programs. Subroutines operate on a shared data structure.

Key aspects of `caique`:
*   **Stack-based operation** `caique` uses a stack to pass values between combinators. Values are pushed onto the stack, and operations perform computations.
*   **Compositional semantics** The syntax and semantics is inherently compositional. The reduction of any expression simplifies one function into another, without needing to apply functions.
*   **Point-free style** `caique` is *point-free*, meaning functions don't explicitly name the data they operate on.

### Definitions:

`  []` means "QUOTATION".

`  ==` means "EVALUATE EXPRESSION" / "EQUIVALENT TO".

`  A B`  are "EXPRESSIONS".

`  :=` means "DEFINED AS".

`  #`  means "INLINE COMMENT".

### Built-in combinators:

```
[B] [A] cat  # concatenate
== [B A]

[B] [A] alt  # alternate / swap
==  [A] [B]

[A] idm  # idem / dup
== [A] [A]

[A] qte  # quote
== [[A]]

[A] uqt  # unquote
== A

[A] ers  # erase / pop
==
```

### Defining new combinators

```
dip  :=  swap quote cat call   # [B] [A] dip == A [B]
cons :=  swap quote swap cat   # [B] [A] cons == [[B] A]    
sip  :=  [dup] dip dip         # [B] [A] sip   ==  [B] A [B]            
take :=  [dip] cons cons       # [B] [A] take  ==  [A [B]]             
sip2 :=  [cons sip] dup call   # [C] [B] [A] sip2  ==  [C] [B] A [C] [B]   
cake :=  [cons] sip2 take      # [B] [A] cake  ==  [[B] A] [A [B]]     
k    :=  [pop] dip call        # [B] [A] k  ==  A
```

### Examples

```

[alt] [idm] cons
== [alt] [idm] alt qte alt cat
== [idm] [alt] qte alt cat
== [idm] [[alt]] alt cat
== [[alt]] [idm] cat
== [[alt] idm]


[alt] [idm] dip
== [alt] [idm] alt qte cat call
== [idm] [alt] qte cat call
== [idm] [[alt]] cat call
== [idm [alt]] call
== idm [alt]
```

## More info
Concatenative languages --> [https://en.wikipedia.org/wiki/Concatenative_programming_language](https://en.wikipedia.org/wiki/Concatenative_programming_language)

This repo is for the implementation of an LC-3 Virtual Machine with an assembly in C --> [https://en.wikipedia.org/wiki/Little_Computer_3](https://en.wikipedia.org/wiki/Little_Computer_3)

LC-3 VM implementation! --> [https://www.jmeiners.com/lc3-vm/](https://www.jmeiners.com/lc3-vm/)

This book teaches how the LC-3 works (chapters 5 to 10) including architecture, OS, I/O, etc...

Link to the [book](https://www.amazon.com/Introduction-Computing-Systems-Gates-Beyond-dp-1260150534/dp/1260150534/ref=dp_ob_title_bk)
