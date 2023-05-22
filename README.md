**Magic Square:** 

A magic square is a nxn matrix filled with distinct numbers where the sum of each row, column and diagonal will be equal to the same number.  

For example:  [[8,3,4],
               [1,5,9],
               [6,7,2]]
               
 n this 3x3 matrix, the summation of each row, column and diagonal is 15. Therefore, this is a magic square. 

Generating all odd array magic squares: 
3x3, 5x5, 7x7 etc are all odd array magic squares. 

Trick: 
i) Start with the middle grid of the first row and put the first number in that grid. 
ii) After that, go to its right-upper grid.
    => If there is an empty grid, then put the next value;
    => If there is no grid to hold an element, then go to the last grid of that 
         column and put the next value.
    => If there is a value, then back go to the grid below the current grid and
         put the next value.  
**Note:**  If the current value is in the last grid of the first row, then insert the next value in the lower grid of the current value. 

**1) All 3x3 magic squares:** 

There are 1 to 9 numbers and we have put these 9 numbers in such a way that the sum of each row, column and diagonal is equal to 15. 

Step 1: Put the first number in the middle grid of the first row.  
Step 2: Go to the right-upper grid. As there is no grid, we will put the next value in the last grid of the third column. 

Step 3: Again, will go to the right-upper grid. But there is no grid there. So, the next value will be inserted in the last grid of the row where no grid is found.

Step 4: Now, check the right-upper grid. There is a value or the current value is the last value of the first row, then we will come back to the current grid and insert the next value in the grid below the value. 

Step 5: We will continue the process till the last remaining grid. 

A visualization of forming 3x3 square matrix is given below: 


![Magic square drawio](https://github.com/Alisha-Khan-Mridula/Problem-Solving/assets/124449169/48ef4dd3-830f-46b5-b432-edcb2d679268)

If we exchange first row and last row and frist column and last column, we will get other magric squares.  
