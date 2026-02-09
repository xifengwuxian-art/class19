import requests
import colorama
from colorama import Fore, init
init(autoreset=True)

def getjoke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    if response.status_code == 200:
        print(f"{Fore.CYAN}\nFull JSON Response: {response.json()}")
        joke_data = response.json()
        return f"\n{Fore.MAGENTA}{joke_data['setup']}-{joke_data['punchline']}\n"
    else:
        return "Fail to get joke"

def main():
    print(f"\n{Fore.YELLOW}Welcome to random joke generator!\n")
    while True:
        user_input = input(f"{Fore.GREEN}Please press enter to get a new joke or press 'q/, exit ' to quit: ").strip().lower()
        if user_input in ("q", "exit"):
            print("Good bye")
            break
        joke = getjoke()
        print(joke)
        
if __name__ == "__main__":
    main()