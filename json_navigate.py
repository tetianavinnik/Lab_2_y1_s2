"This program will help you to navigate through json file"

import json
import pprint


def read_file(file: str) -> dict:
    """
    Return information from file.
    """
    with open(file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def navigate(file):
    """
    Navigation through file.
    """
    data = read_file(file)
    def recursion(data):
        """
        Recursional navigation.
        """
        if isinstance(data, dict):
            if data != {} and len(list(data.keys())) != 1:
                pprint.pprint(list(data.keys()))
                inp = input('Enter key: ')
                if isinstance(data[inp], dict):
                    print('This is a dictionary')
                    recursion(data[inp])
                elif isinstance(data[inp], list):
                    print('This is a list')
                    recursion(data[inp])
                else:
                    print('The value is: ', data[inp])    
            else:
                print('The value is: ', data)
            
        if isinstance(data, list):
            if data != [] and len(data) != 1:
                inp = int(input('Enter index(0-' + str(len(data)-1) + '): '))
                if isinstance(data[inp], dict):
                    print('This is a dictionary')
                    recursion(data[inp])
                elif isinstance(data[inp], list):
                    print('This is a list')
                    recursion(data[inp])
                else:
                    print('The value is: ', data[inp])
            else:
                print('The value is: ', data[0])
            
    recursion(data)


if __name__ == '__main__':
    file = input('Path to file: ')
    navigate(file)
