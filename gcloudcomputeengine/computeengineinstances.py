#!/usr/bin/python
# -*- coding: utf-8 -*-
# computeengineinstances.py
# It is an example of how to handle Google Cloud Compute Engine VM instances.

import sys
import computeenginehelper

def print_menu():
    print('\nMENU')
    print('0 = Quit')
    print('1 = List all VM instances')
    print('2 = Create VM instance')
    print('3 = List VM instance')
    print('4 = Start instance')
    print('5 = Stop instance')
    print('6 = Reset instance')
    print('7 = Delete instance')
    return


def main():
    instance_id = ''
    option = -1

    while option != 0:
        print_menu()
        try:
            option = int(input('\nEnter an option? '))
            if option == 0:
                print('Bye')
            elif option == 1:
                computeenginehelper.list_instances()
            elif option == 2:
                instance_id = computeenginehelper.create_instance()
            elif option == 3:
                computeenginehelper.list_instance(instance_id)
            elif option == 4:
                computeenginehelper.start_instance(instance_id)
            elif option == 5:
                computeenginehelper.stop_instance(instance_id)
            elif option == 6:
                computeenginehelper.reset_instance(instance_id)
            elif option == 7:
                computeenginehelper.delete_instance(instance_id)
            else:
                print('\nERROR: Enter a valid option!!')
        except ValueError:
            print('\nERROR: Enter a valid option!!')

    return


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
