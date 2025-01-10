# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import time

def print_hi(name):

    start_time = time.time()

    for i in range(5):
        time.sleep(1)
    execution_time = time.time() - start_time

    print(f"Execution time: {execution_time:.2f} seconds")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
