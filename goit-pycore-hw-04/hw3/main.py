import os
import sys
from pathlib import Path
from colorama import Fore, Style, init

# Initiation colorama
init(autoreset=True)

def print_directory_structure(path: Path, indent: str = ""):
    # check which way is the same as the directory
    if not path.exists():
        print(Fore.RED + f"Error: Path '{path}' does not exist.")
        return
    if not path.is_dir():
        print(Fore.RED + f"Error: Path '{path}' is not a directory.")
        return
    
    # Looping through directory
    for entry in path.iterdir():
        # What is this subdirectory?
        if entry.is_dir():
            print(Fore.CYAN + f"{indent}📂 {entry.name}")
            # Recursively click for subdirectories
            print_directory_structure(entry, indent + "  ")
        # If file
        elif entry.is_file():
            print(Fore.GREEN + f"{indent}📜 {entry.name}")

# Main part of the script
if __name__ == "__main__":
    # Checking the validity of a command line argument
    if len(sys.argv) != 2:
        print(Fore.RED + "Usage: python hw03.py <path_to_directory>")
        sys.exit(1)

    directory_path = sys.argv[1]
    directory = Path(directory_path)

    # The directory structure is displayed
    print_directory_structure(directory)
