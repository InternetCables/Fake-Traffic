# KB
from urllib.request import urlretrieve
import random
import datetime
from colorama import Fore, Back, Style
from tqdm import tqdm
import fade
import platform , sys ,os
import time
import shutil

# START Program
system = platform.uname()[0]
if system != "Windows":
    os.system("clear")
else:
    os.system("cls")

banner = f'''
Program Started.                                                             
'''

faded_banner = fade.water(banner)

# START Page
def manual():
    if system != "Windows":
        os.system("clear")
    else:
        os.system("cls")
    print(
    "This script makes fake trafic with downloading files.\n"
    "You can put urls in url.txt file and script will download them.\n"
    "For control download speed put ::x at the end of each url you want to limit , for example:\n"
    "http://download.com/file.iso::1 \neach number you put it will *1024 , in this case we limite up to 1Mb\n" 
    "After each download it will loged in log.txt so you can monitor when witch files are downloaded\n" + Fore.YELLOW +
    "This script is the first version , if you want add any feature , bug ... please contact to programers.\n" + Fore.GREEN + 
    "Coded by @internetCables" + Fore.RESET
    )
    c = input("Back to menu press 0 :")
    if c == '0':
        menu()
    else:
        print(Fore.RED + "Invalid input" + Fore.RESET)
        time.sleep(1.5)
        manual()

# START Download
def download_iso(url_file):
# START Read to time
    date_download = "time-" + datetime.datetime.now().strftime("%Y-%m-%d--%H-%M-%S")
# START Import to logfile
    with open(url_file) as f, open("log.txt", "a") as log_file:
        for i, line in enumerate(f, 1):
# START Call data on url file
            line_parts = line.strip().split("::")
            url = line_parts[0]
# START Convert to bytes
            speed_limit = int(line_parts[1]) * 1024 if len(line_parts) > 1 else None 
# START Random numbers to save files
            ranum = random.randint(1, 1000)
# START Saving file name
            filename = f"dl/{date_download}--{ranum}.iso"
# START Main
            try:
                with tqdm(unit='B', unit_scale=True, desc=filename, ncols=80, mininterval=0, dynamic_ncols=True) as progress:
                    def report(count, block_size, total_size):
                        progress.update(block_size)
                        if progress.n == total_size:
                            progress.close()
                    log_file.write(f"{filename}\n")
                    urlretrieve(url, filename, reporthook=report, data=None)
            except Exception as e:
                print(f"Error Downloading {url}: {str(e)}")
# START Console and controler
if __name__ == "__main__":
    
    def menu():
        url_file = "url.txt"
        print(faded_banner)
        print()
        print(Fore.YELLOW, "Hello. my name is Fake Traffic.")
        print(Fore.GREEN, "\n\t0.Exit\n\t1.Once Download\n\t2.Unlimited Download\n\t3.Readme")
        print()
        a = input("Please Enter : " + Fore.RESET)
        b = 0
        if a == '0':
            print(Fore.CYAN + "See you")
            time.sleep(1)
            exit()
        elif a == '1':
            download_iso(url_file)
            print(Fore.CYAN + "Done")
            time.sleep(1)
# Remove dl
            shutil.rmtree('dl', ignore_errors=True)
# Create dl
            os.mkdir('dl')
            menu()
        elif a == '2':
            print(Fore.YELLOW + "Unlimited Download Start , Press Ctrl + c to Stop" + Fore.RESET)
            time.sleep(3)
            while b < 1:
# Remove dl
                shutil.rmtree('dl', ignore_errors=True)
# Create dl
                os.mkdir('dl')
                download_iso(url_file)
        elif a == '3':
            manual()
        else:
            print(Fore.RED, "Invalid input." + Fore.RESET)
            menu()
menu()