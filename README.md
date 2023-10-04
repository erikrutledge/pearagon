# Challenge project for Pearagon interview
created by Erik Rutledge 
10/3/2023

--- 

Contained in this repository is the main.py file which holds the main function of the program. Upon executing the program it does the following:
* Prompts the user for a string input
* Pings the /books/search endpint with the string as the title value
* If the book is located it Pings the /authors/:authorId endpoint for the full names of each of the listed authors
* Displays the book title, description, and full name of every author
* On completion or error finding book, the user is prompted for another book title
* Loop repeats until interrupted by submitting "exit"

# Notes

--- 

* The only implemented title is "The Lord Of The Flies" which will return a valid output
* Any random string inputted has a 50% chance to return gibberish or fail
* The /authors.:authorId will return a random author name for any authorId

# Development Environment

---

* Created in python 3.11.5 using the requests library to handle API calls
* Used Visual Studio Code as my IDE
