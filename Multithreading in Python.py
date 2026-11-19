import threading
import time


def count_numbers(limit=5):
    print("Task 1: Starting number counting...")
    for i in range(1, limit + 1):
        print(f"[Count]: {i}")
        time.sleep(0.5)  # Simulate delay
    print("Task 1: Counting finished.")

def calculate_squares(numbers):
    print("Task 2: Starting square calculation...")
    for num in numbers:
        print(f"[Square]: {num}^2 = {num ** 2}")
        time.sleep(0.7)  # Simulate delay
    print("Task 2: Squares finished.")

def calculate_cubes(numbers):
    print("Task 3: Starting cube calculation...")
    for num in numbers:
        print(f"[Cube]: {num}^3 = {num ** 3}")
        time.sleep(0.6)  # Simulate delay
    print("Task 3: Cubes finished.")

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]

    thread1 = threading.Thread(target=count_numbers, args=(5,))
    thread2 = threading.Thread(target=calculate_squares, args=(data,))
    thread3 = threading.Thread(target=calculate_cubes, args=(data,))

    print("--- Starting All Threads ---")

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()

    print("--- All tasks executed concurrently and finished! ---")

