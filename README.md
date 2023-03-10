Project name: AirBnB clone

Description:

https://youtu.be/E12Xc3H2xqo

Table of Contents

1) How to run the AirBn clone
2) Unit tests
3) Base Model
4) Storage
5) The console
6) Credits



1) How to run the AirBn clone

- Download the repository
- Open a new terminal and navigate to the repository

                Interactive mode

- Run the AirBn clone by running the following command:
        
    python3 console.py 

                Non interactive mode

- Run this command 
    
    echo "help" | ./console.py

    replace whats inside the " " with any other command allowed

The commands included are documented:

    help - Shows information about the console or its commands - Usage: help or help create
    
    EOF - Exits the console (ctrl+ d)

    quit - Exits the console
    
    create - Creates an instance - Usage: create Class

    show - Prints the string representation of an instance - Usage: show Class id
    
    destroy - Deletes an instance - Usage: destroy Class id
    
    all - Prints all string representation of all instance - Usage: all or all Class
    
    update - Updates an instance - Usage: update Class id attribute value

2) Test the AirBn clone

- All files, classes, functions must be tested with unit tests

        python3 -m unittest discover tests

3) Base Model

    The base model is a class that defines all common attributes/methods for other classes:

        Public instance attributes:
            id: string - assign with an uuid when an instance is created:
                - you can use uuid.uuid4() to generate unique id but don’t forget to convert to a string
                - the goal is to have unique id for each BaseModel

            created_at: datetime - assign with the current datetime when an instance is created

            updated_at: datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object

        __str__: should print: [<class name>] (<self.id>) <self.__dict__>

        Public instance methods:

            save(self): updates the public instance attribute updated_at with the current datetime

            to_dict(self): returns a dictionary containing all keys/values 
            
            of __dict__ of the instance:
                by using self.__dict__, only instance attributes set will be returned
                a key __class__ must be added to this dictionary with the class name of the object
                created_at and updated_at must be converted to string object in ISO format:
                    - format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)
                    - you can use isoformat() of datetime object
                This method will be the first piece of the serialization/deserialization process: create a dictionary representation with “simple object type” of our BaseModel


4) Storage

    Writing the dictionary representation to a file won’t be relevant:

    Python doesn’t know how to convert a string to a dictionary (easily)
    It’s not human readable
    Using this file with another program in Python or other language will be hard.
    So, you will convert the dictionary representation to a JSON string. JSON is a standard representation of a data structure. With this format, humans can read and all programming languages have a JSON reader and writer.

5) The console

    The console is program called console.py that contains the entry point of the command interpreter:

        You must use the module cmd
        Your class definition must be: class HBNBCommand(cmd.Cmd):
        Your command interpreter should implement:
            - quit and EOF to exit the program
            - help (this action is provided by default by cmd but you should keep it updated and documented as you work through tasks)
            a custom prompt: (hbnb)
            an empty line + ENTER shouldn’t execute anything
        Your code should not be executed when imported



6) Credits:

    This project was possible because of the help of cohort 19 pear around the globe that help us with some problems during the process.

7) About the Authors

    Check AUTHORS file for more information

8) Contributors:

    - Obed Rayo
    - Esteban Enríquez Ruales
    - Joaquín Jones
    - Mauricio De Betolaza Del Puerto
    - Eps Rarima
 
9) Resources
    - Holberton Documentation
    - Google Documentation
    - Chat GPT




