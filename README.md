# Most-typical-computer-store
welcome to the most typical computer store 

When selecting option 1:
1. Prompt the computer store owner to input their password. 
Ensure the existence of a constant variable containing the password "password" — refrain from
employing any other password for ease of assessment. The computer store owner is granted three
attempts to input the correct password. Upon the third unsuccessful attempt, the main menu depicted
in Figure 1 is redisplayed.
2. If the correct password is successfully entered, inquire about the number of computers the
owner intends to input. Verify the availability of adequate space in the computer store
(represented by an array of Computers) to accommodate the specified quantity. If sufficient
space is available, proceed with the addition; otherwise, notify the owner that the array can
only accommodate the remaining available slots. The method by which the user inputs/enters
computer information is at your discretion.

When selecting option 2:
i. Request the computer store owner's password, ensuring the presence of a constant containing
the password "password" — use only this constant for ease of evaluation. The computer store
owner is granted three attempts to input the correct password. Following the third unsuccessful
attempt, the main menu depicted in figure 1 is redisplayed.

ii. Inquire about the specific computer number the user wishes to update. The computer number
corresponds to the index in the array inventory. If there is no Computer object at the specified 
index, prompt the user to either choose another computer or exit this operation and return to the
main menu. If the entered index corresponds to a valid computer, display the current information
of that computer in the following format:
Computer # X
Brand: [Brand of this computer] 
Model: [Model of computer]
SN: [Serial number (SN) of this computer] 
Price: $[Price]

Then, display the following menu to ask the user which attribute they wish to change:
What information would you like to change?
1.	brand
2.	model
3.	SN
4.	price
5.	Quit
Enter your choice >

When selecting option 3: 
Initiate a prompt for the user to input a brand name. Subsequently, Display the information
of all computers associated with the specified brand.

When option 4 is entered: 
Prompt the user to enter a value (representing a price). Then display all 
computers that have a value smaller than that entered value. 

When option 5 is entered:
Display a closing message and end the driver.


