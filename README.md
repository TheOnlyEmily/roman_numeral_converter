# Purpose
Make the storage of roman numerals more memory efficient.

# Goal
Create a library to convert between roman numerals and numbers. 

## Milestones
1. Convert the roman numerals i, v, x, l, c, d, and m to numbers. 
1. Convert the numbers 1, 5, 50, 100, 500, and 1000 into roman numerals. 
1. Implement code that indicates if a given roman numeral can be uniformly stacked. 
1. Implement code that indicates if a given uniform stacking of roman numerals is valid. 
1. Convert uniformly stacked roman numerals to numbers.
1. Implement code that indicates if a given indo-european numeral is the result of uniform stacking. 
1. Implement code that indicates which roman numeral was uniformly stacked to create a given indo-european numeral. 
1. Implement code that indicates how many roman numerals where uniformly stacked to create a given indo-european numeral. 
1. Convert a numbers numeral to a uniform stacking of roman numerals.
1. Implement code that indicates if a given non-uniform subtractive stacking of roman numerals is valid.
1. Convert a non-uniform subtractive stack of roman numerals to numbers.

# Golossary 
## Stack
In the context of this documentation, a stack refers to a roman numeral that is any combination of atomic roman numerals. 
## Minimal Stack
A stack of two atomic roman numerals.
## Atomic Roman Numerals
The roman numerals i, v, x, l, c, d, and m, written by themselves. 
## Uniform Stack
A stack that consists of the same atomic roman numeral repeated. 
## Non-uniform Stack
A stack that includes at least two different atomic roman numerals.
## Subtractive Non-uniform Stack
A non-uniform stack where there is a single or uniform stack of roman numerals that preceed an atomic roman numeral that has a greater value than that of the atomic roman numerals that make up to preceeding uniform stack.