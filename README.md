Magic Square: 

A magic square is a nxn matrix filled with distinct numbers where the sum of each row, column and diagonal will be equal to the same number.  

For example:  [[8,3,4],
               [1,5,9],
               [6,7,2]]
               
 In this 3x3 matrix, the summation of each row, column and diagonal is 15. Therefore, this is a magic square. 

Generating all odd array magic squares: 
3x3, 5x5, 7x7 etc are all odd array magic squares. 

Trick: 
i) Start with the middle value of the first row and put the first number in that grid. 
ii) After that, go to its right-upper grid.
    => If there is an empty grid, then put the next value;
    => If there is no grid to hold an element, then go to the last grid of that 
         column and put the next value.
    => If there is a value, then back go to the grid below the current grid and
         put the next value.  
         
1) All 3x3 magic squares:  

