Write a complete class called GasPump to represent a gas pump. 

The class should have a constructor to set the amount of available gas supply (in liters) and the price of gas per liter. 
A method to add fuel to the gas supply. Note that the maximum capacity of the pump is 5000 liters. If we try to add too much fuel, once the maximum capacity is reached, no more fuel can be added.
A method that sells a specific amount of gas. This method should reduce the supply of available gas by the amount sold and return the total cost of the gas sold. If the supply of the available gas is less than the amount requested, then only the existing supply should be sold. 

Using the class defined in top, write a driver program that: 
Creates an object called shell of the class GasPump and initializes it to 3000 liters and 78.5 cents a liter 
Asks the user how much gas he/she wants to buy 
Sells this amount of gas from shell; 
Adds 500 liters of gas to shell; 
Displays the content of gas supply left in shell.