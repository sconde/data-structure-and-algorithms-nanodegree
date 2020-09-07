# Problem 1: Square root of integer

I decided to use the bisection method to find the root of the function __y = x^2 - S__ where __x__ is the square root of __S__ .

Time complexity: __O(log S)__ since the interval __[1,S]__ is halved at each iteration

Space complexity: __O(1)__ only 3 temporary/local scalar variables are used
