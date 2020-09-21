# Problem 1: Square root of integer

I decided to use the bisection method to find the root of the function __y = x^2 - S__ where __x__ is the square root of __S__ .

Time complexity: __O(log S)__ since the interval __[1,S]__ is halved at each iteration

Space complexity: "space complexity of recursive algorithm is proportinal to maximum depth of recursion tree generated. In the case of this problem, each call uses O(1) space, the maximum depth of the recursive tree is O(logn) so the space complexity is __O(logn)__"

Although I agree with about statement, the memory use in my implementation is independent to the input - each loop is running independently. Thus, I still believe the space complexity __O(1)__ as I'm not using a recurvive function.
