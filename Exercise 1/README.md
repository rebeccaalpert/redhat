# Excercise 1
Please see exercise1.js for working Javascript.  

The original code didn't work because of a scoping problem.  

While at first glance, the code in function remoteMathService(cb) looks fine, the variables set in callOneService and callTwoService don't affect the global variables defined at the start of the function. They each just see and set values for a copy of a global variable.

To fix this, I moved callTwoService inside callOneService's callback function so that callTwoService would be able to see the one = num set in callOneService's callback function.  

I moved the return statement for remoteMathService into callTwoService's callback function so it would be able to access both callOneService's one variable and callTwoService's two variable and do math on them. The program now works.