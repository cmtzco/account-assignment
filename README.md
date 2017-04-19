# AccountManager
A program written to keep track of credit card accounts and their balances.

## Info

- Language: Python

- Tools:
    - Virtualenv: Used for isolating the environment I was working with in regards to dependencies.

- Dependencies: fileinput, PyDAL
    - fileinput: Used to allow for reading file input.
    - PyDAL: Database ORM used to abstract from writing raw SQL and aid in simple schema creation.


## Installation

**NOTE:** *Some of these steps may require elevated privileges to run.  Prefix the command with sudo if your account does not have the correct permission set.*

- Ensure that Python 2.7 and Pip are installed on the device this will be used on.

- Clone repo to your desired run location

        git clone https://github.com/cmtzco/account-assignment.git

- Change directory to repo folder (Following command will work if cloned into default folder name)

        cd account-assignment

- Install Dependencies

        pip install -r requirements.txt


## Usage

- Edit input.txt, file that will store your operations (Ex. Account additions, charges, credits)

- Run

        python run.py < input.py


### Sample Output

        python run.py < input.txt
        John, 418889: 150
        Maddy, 318237: -750


### Example operations

- The following lines are examples that can be used in the **input.txt** file


        Add John 418889 1000
        Charge John 100
        Add Maddy 318237 1000
        Credit Maddy 300
        Credit John 50


## Design Patterns

- Behavorial

    - Command: This was used in run.py to ensure that the application could run via CLI and take the input of a file.

    - Catalog: This was used in Account.py to allow for the multiple operations that needed to be present to ensure account management.


### Tradeoffs

- The choice to do a catalog and command pattern allowed for a thicker model of the class that was built and a thinner controller/run script to execute the account functions on the input.

- A full command pattern would have allowed me to build the input directly into the class but that would not have been as clean to manage when trying to validate STDIN.

- A full Catalog would have been added more classes than are needed as well as not allowed for a clean controller/run script.

