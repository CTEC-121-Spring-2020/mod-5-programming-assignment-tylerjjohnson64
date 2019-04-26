# Programming Assignment 5 - Problem 2

**General Description**

Write a function that calculates the change from a transaction and prints out the number of each denomination for the change.

**Function Specification**

- The function has two inputs, the total cost of the transaction and the amount tendered.
- For the purposes of this assignment, the amounts are less than $20.00.
- The function should output a summary line listing the total cost, amount tendered and the change.
- Subsequent output lines should list how many of each denomination should be used to create the change   
    For example if the cost was 2 cents and a dime was tendered the output would look like:   
    ```
    Cost: $0.02, Tendered: $0.10, Change: $0.08
    1 nickel
    3 penney
    ```

**Other Specifications**
    
- Write a main routine that will ask the user for the cost and amount tendered and call the function to calculate the change.

**Hints**

- It might be useful to convert the calculated change value to an int representing the number of pennies, then use integer division to calculate the counts of each denomination
- After each output line you will need to recalculate the amount of change due. For example:   
    if the change due is $5.99, then after I have calculated one 5 dollar bill, the new value for change due is $0.99
- Make sure you run some tests before you turn this in.