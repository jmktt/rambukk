import argparse
import requests
from colorama import Fore, Style
import time

banner = """
 ██▀███   ▄▄▄       ███▄ ▄███▓ ▄▄▄▄    █    ██  ██ ▄█▀ ██ ▄█▀
▓██ ▒ ██▒▒████▄    ▓██▒▀█▀ ██▒▓█████▄  ██  ▓██▒ ██▄█▒  ██▄█▒ 
▓██ ░▄█ ▒▒██  ▀█▄  ▓██    ▓██░▒██▒ ▄██▓██  ▒██░▓███▄░ ▓███▄░ 
▒██▀▀█▄  ░██▄▄▄▄██ ▒██    ▒██ ▒██░█▀  ▓▓█  ░██░▓██ █▄ ▓██ █▄ 
░██▓ ▒██▒ ▓█   ▓██▒▒██▒   ░██▒░▓█  ▀█▓▒▒█████▓ ▒██▒ █▄▒██▒ █▄
░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▒░   ░  ░░▒▓███▀▒░▒▓▒ ▒ ▒ ▒ ▒▒ ▓▒▒ ▒▒ ▓▒
  ░▒ ░ ▒░  ▒   ▒▒ ░░  ░      ░▒░▒   ░ ░░▒░ ░ ░ ░ ░▒ ▒░░ ░▒ ▒░
  ░░   ░   ░   ▒   ░      ░    ░    ░  ░░░ ░ ░ ░ ░░ ░ ░ ░░ ░ 
   ░           ░  ░       ░    ░         ░     ░  ░   ░  ░   
                                    ░    """

class Enumerator:
    def __init__(self, target, wordlist_path):
        self.target = target
        self.wordlist_path = wordlist_path

    def load_wordlist(self):
        try:
            with open(self.wordlist_path, "r") as wordlist_file:
                return [line.strip() for line in wordlist_file]
        except FileNotFoundError:
            print(f"{Fore.RED}[ERROR] Wordlist not found.{Style.RESET_ALL}")
            exit(1)

    def enumerate(self):
        wordlist = self.load_wordlist()

        for item in wordlist:
            target = f"{self.target}/{item}"
            response = requests.get(target)
            if response.status_code == 200:
                print(f"{Fore.GREEN}[SUCCESS] Found: {target}{Style.RESET_ALL}")

def main():
    parser = argparse.ArgumentParser(description="Brute force tool for directories or passwords")
    parser.add_argument("-t", "--target", help="Target URL or IP address", required=True)
    parser.add_argument("-w", "--wordlist", help="Path to wordlist file", required=True)
    parser.add_argument("-m", "--mode", choices=["dir", "pass"], help="Mode: 'dir' for directory brute force, 'pass' for password brute force", required=True)
    args = parser.parse_args()

    if args.mode == "dir":
        if not args.target.startswith(("http://", "https://")):
            args.target = f"http://{args.target}"
        enumerator = Enumerator(args.target, args.wordlist)
        print(banner)
        print("=" * 50)
        print("RAMBUKK BRUTE FORCE TOOL", end="      ")
        print("John Prizrak(jmktt)")
        print("=" * 50)

        print(f"[*] Mode: {args.mode}")
        print(f"[*] Starting enumeration on: {args.target}")
        print(f"[*] Wordlist: {args.wordlist}")
        print("=" * 50)

        enumerator.enumerate()

    elif args.mode == "pass":
        print("Password brute force mode is not available.")
    else:
        print("Invalid mode. Use 'dir' for directory brute force or 'pass' for password brute force.")

if __name__ == "__main__":
    main()
