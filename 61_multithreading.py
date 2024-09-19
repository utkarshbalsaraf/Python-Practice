# multithreading = Used to perform multiple tasks concurrently (multitasking)
#                 Good for I/O bound tasks like reading files or fetching data from APIS
#                 threading. Thread(target-my_function)

import threading
import time


def walk_dog(name):
    time.sleep(5)
    print(f"Finished walking the {name}")


def take_out_trash():
    time.sleep(8)
    print("Take out the trash")


def get_the_mail():
    time.sleep(2)
    print("Read the mail")


# walk_dog()
# take_out_trash()
# get_the_mail()

func1 = threading.Thread(target=walk_dog, args=("Scooby",))
func2 = threading.Thread(target=take_out_trash)
func3 = threading.Thread(target=get_the_mail)
func1.start()
func2.start()
func3.start()

func1.join()
func2.join()
func3.join()
print("All Tasks are completed")
