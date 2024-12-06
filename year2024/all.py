import os
from subprocess import run

SEPARATOR = "---------------"
SOLUTION = "python3 solution.py"

def run_solutions(directory):
    for _, folders, _ in os.walk(directory):
        for index, folder in enumerate(sorted(folders)):
            os.chdir(f"{directory}/{folder}")
            print(f"{SEPARATOR} day{index + 1:02} {SEPARATOR}")
            run(SOLUTION.split(" "))
            os.chdir(f"{directory}")

current_directory = os.getcwd()
try:
    run_solutions(current_directory)
except FileNotFoundError:
    print("ERROR LOADING SOLUTION SCRIPTS")
