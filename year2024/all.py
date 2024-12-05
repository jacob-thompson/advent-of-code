import os
from subprocess import run

SEPARATOR = "---------------"
SOLUTION = "python3 solution.py"

def main():
    current_directory = os.getcwd()

    for _, folders, _ in os.walk(current_directory):
        for index, folder in enumerate(folders):
            print(f"{SEPARATOR} day{index + 1:02} {SEPARATOR}")
            os.chdir(f"{current_directory}/{folder}")
            run(SOLUTION.split(" "))
            os.chdir(f"{current_directory}")

if __name__ == "__main__":
    main()
