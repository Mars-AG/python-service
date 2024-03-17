import os
from colorama import Fore

class Env:
    @staticmethod
    def get(name):
        if os.getenv(name):
            return os.getenv(name)
        else:
            print(f"\n\n{Fore.RED}Env: {Fore.WHITE}{name}{Fore.RED} not exist{Fore.WHITE}\n\n")