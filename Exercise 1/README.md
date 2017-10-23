# Excercise 1
The original code didn't work because of a scoping problem.  

While at first glance, the code in function remoteMathService(cb) looks fine, the variables set in callOneService and callTwoService don't affect the global variables defined at the start of the function. They each just see a copy of the global variables. 

To fix this, I moved callTwoService inside callOneService's callback function so that callTwoService would be able to see the one = num set in callOneService's callback function.  

I moved the return statement for remoteMathService into callTwoService's callback function so it would be able to access both callOneService's one variable and callTwoService's two variable and do math on them.