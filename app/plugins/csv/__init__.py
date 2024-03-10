import logging
import os
from app.commands import Command
import pandas as pd


class CsvCommand(Command):
    def execute(self):
        
        # Existing code for demonstrating data structures and saving CSV...

        # Ensure the 'data' directory exists and is writable
        data_dir = './data'
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
            logging.info(f"The directory '{data_dir}' is created")

        elif not os.access(data_dir, os.W_OK):
            logging.error(f"The directory '{data_dir}' is not writable.")
            return
        
        # Convert dictionary to DataFrame and save to CSV
        states_abbreviations = {
            'CA': 'California',
            'NJ': 'New Jersey',
            'TX': 'Texas',
            'FL': 'Florida',
            'IL': 'Illinois',
            'NY': 'New York'  # Newly added state
        }
        df_states = pd.DataFrame(list(states_abbreviations.items()), columns=['Abbreviation', 'State'])
        csv_file_path = os.path.join(data_dir, 'states.csv')
        df_states.to_csv(csv_file_path, index=False)
        
        logging.info(f"States saved to CSV at '{csv_file_path}'.")
        # This is creating the path for saving the file.
        csv_file_path = os.path.join(data_dir, 'gpt_states.csv')
        logging.info(f'the relative path  to save my file is {csv_file_path}')
        # Read the CSV file back into a DataFrame
        absolute_path = os.path.abspath(csv_file_path)
        logging.info(f'the absolute path  to save my file is {absolute_path}')
        df_read_states = pd.read_csv(csv_file_path)
        
        # Print and log each state nicely
        print("States from CSV:")
        for index, row in df_read_states.iterrows():
            # First, print and log the complete record for the state
            state_info = f"{row['State Abbreviation']}: {row['State Name']}"
            print(f"Record {index}: {state_info}")
            logging.info(f"Record {index}: {state_info}")
            
            # Then, iterate through each field in the row to print and log
            for field in row.index:
                field_info = f"    {field}: {row[field]}"
                print(field_info)
                logging.info(f"Index: {index}, {field_info}")