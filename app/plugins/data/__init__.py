import logging
from app.commands import Command


class DataCommand(Command):
    def execute(self):
        # Demonstrating Lists
        my_list = ['apple', 'banana', 'cherry']
        logging.info(f'List example: {my_list}')
        # Lists are ordered and mutable, making them ideal for storing a collection of items that may change over time.
        logging.info(f'I pick an {my_list[0]}')
        my_list.append('date')  # Adding an item to the list
        logging.info(f'List after adding an item: {my_list}')

        # Demonstrating Tuples
        my_tuple = (1, 2, 3, 4)
        logging.info(f'Tuple example: {my_tuple}')
        # Tuples are ordered and immutable, suitable for storing a collection of items that should not change.
        logging.debug(f'My Tuple is {my_tuple[0]}')
        # Demonstrating Sets
        my_set = {1, 2, 3, 4}
        my_set2 = {2,3,4,5}
        logging.info(f'Set example: {my_set}')
        logging.info(f'whats different {my_set.difference(my_set2)}')
        # Sets are unordered, mutable, and do not allow duplicate values, ideal for unique collection without specific order.
        
        my_set.add(5)  # Adding an item to the set
        logging.info(f'Set after adding an item: {my_set}')
        
        # Demonstrating Dictionaries
        states_abbreviations = {
            'CA': 'California',
            'NJ': 'New Jersey',
            'TX': 'Texas',
            'FL': 'Florida',
            'IL': 'Illinois'
        }
        
        logging.info(f'Dictionary example: {states_abbreviations}')
        # Dictionaries store data in key-value pairs. They are mutable and unordered. Ideal for fast lookups where each value is associated with a unique key.
        
        states_abbreviations['NY'] = 'New York'  # Adding a new key-value pair
        logging.info(f'Dictionary after adding a state: {states_abbreviations}')
        
        # Demonstrating dictionary iteration
        for abbreviation, full_name in states_abbreviations.items():
            logging.info(f"State Abbreviation: {abbreviation} for: {full_name}")

        # Advanced use case: Nested Dictionaries
        states_info = {
            'CA': {
                'capital': 'Sacramento',
                'population': 39538223,  # As of the latest estimates
                'great': 'No'
            },
            'TX': {
                'capital': 'Austin',
                'population': 29145505,  # As of the latest estimates
                'great': 'Yes'
            },
            'NJ': {
                'capital': 'Trenton',
                'population': 50,  # As of the latest estimates
                'great': 'Yes',
                'good hot dogs': 'yes',
                'where': 'Rutts hutt'
            }
        }
        for state, info in states_info.items():
            # Log the state abbreviation
            logging.info(f"State: {state}")
            print(f"State: {state}")
        
            # Iterate through each property of the state and print/log it
            for property_name, property_value in info.items():
                property_info = f"    {property_name.capitalize()}: {property_value}"
                print(property_info)
                logging.info(property_info)