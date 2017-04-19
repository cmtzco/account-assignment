# AccountManager
A program written to keep track of credit card accounts and their balances.

## Info

- Language: Python

- Tools:
    - Virtualenv: Used for isolating the environment I was working with in regards to dependencies.

- Dependencies: fileinput, PyDAL
    - fileinput: Used to allow for reading file input.
    - PyDAL: Database ORM used to abstract from writing raw SQL and aid in simple schema creation.


### Installation

** **NOTE:** *Some of these steps may require elevated privileges to run.  Prefix the command with sudo if your account does not have the correct permission set.*

- Ensure that Python 2.7 and Pip are installed on the device this will be used on.

- Clone repo to your desired run location

        git clone https://github.com/cmtzco/account-assignment.git

- Change directory to repo folder (Following command will work if cloned into default folder name)

        cd account-assignment

- Install Dependencies

        pip install -r requirements.txt


### Usage

- Edit input.txt, file that will house your operations (Ex. Account additions, charges, credits)

- Run

        python run.py < input.py


### Design Patterns

