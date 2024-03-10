import logging
from app.commands import Command


class GreetCommand(Command):
    def execute(self):
        logging.info("Hello, World!")

        mylist_tuple = (1,2,3,4)
        mylist = [1,2,3,4]

        

        print("Hello, World!")