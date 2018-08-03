import click
import pyotp
import re
import os
import sys
import shelve
import signal
import pyperclip

import colorama
from colorama import Fore, Back, Style

import show as show_
import delete as delete_
import write as write_
import update as update_

valid_secret_pattern = re.compile(b"^([A-Z]|[2-7]+)+$")
information_path = os.path.expanduser(os.path.join("~", "otp-cli", "information.db"))

def validateSecret(secret):
    notValid = not valid_secret_pattern.match(secret.upper().encode())

    try:
        pyotp.TOTP(secret).now()
    except:
        return True
    
    return notValid

def copyCode(code):
    pyperclip.copy(code)

def showCode(secret, totp = True, counter = None, split = True):
    if validateSecret(secret):
        return "Invalid secret! Valid secrets only contain the letters A-Z and digits 2-7"
    
    if (totp):
        generator = pyotp.TOTP(secret)
        code = generator.now()

        if split:
            return code[0: int(len(code) / 2)] + " " + code[int(len(code) / 2) : ]
        else:
            return code

def updateInformation(key, value):
    try:
        s = shelve.open(information_path)
    except:
        os.makedirs(information_path, exist_ok = True)
        s = shelve.open(information_path)

    try:
        s['information'][key] = value
    finally:
        s.close()

def removeInformation(key, value):
    try:
        s = shelve.open(information_path)
    except:
        os.makedirs(information_path, exist_ok = True)
        s = shelve.open(information_path)

    try:
        del s['information'][key]
    finally:
        s.close()

def getInformation():
    try:
        s = shelve.open(information_path, writeback = True)
    except Exception as e:
        print(e)
        os.makedirs(os.path.dirname(information_path), exist_ok = True)
        s = shelve.open(information_path, writeback = True)

    try:
        ret = s['information']
        
    except:
        s['information'] = {}
        ret = {}
    
    return ret, s

def handleSigint(sig, frame):
    click.echo('\r' +\
            Fore.RED + "[ " + Fore.CYAN +\
            "-" +\
            Fore.RED + " ] " +\
            Style.RESET_ALL + Fore.GREEN + "--- ---" + "    " + Style.RESET_ALL, nl = False)      # Quit gracefully 

    click.echo(Style.RESET_ALL)

    sys.exit(0)

# Set handler
signal.signal(signal.SIGINT, handleSigint)

@click.group()
def cli():
    pass

@cli.command()
@click.option("--secret", "-s", help = 'The secret used to generate a one-time password')
@click.option("--all", "-a", is_flag = True, help = 'Show information of all stored one-time passwords')
@click.option("--copy", "-c", is_flag = True, help = 'Copy one-time password to clipboard')
@click.argument("name", required = False)
def show(name, secret, all, copy):
    show_.cli(name, secret, all, copy)

@cli.command()
@click.option("--email", "-e", help = 'The email address this one-time password belongs to')
@click.option("--issuer", "-i", help = 'The issuer of this one-time password')
@click.option("--description", "-d", help = 'The description of this one-time password')
@click.option("--force", is_flag = True, help = 'Force the write even if name exists', default = False)
@click.option("--hotp", is_flag = True, help = 'This one-time password is counter based', default = False)
@click.argument("name", required = True)
@click.argument("secret", required = True)
def write(name, secret, email, issuer, description, force, hotp):
    write_.cli(name, secret, email, issuer, description, force, hotp)

@cli.command()
@click.option("--email", "-e", help = 'The new email address this one-time password belongs to')
@click.option("--issuer", "-i", help = 'The new issuer of this one-time password')
@click.option("--description", "-d", help = 'The new description of this one-time password')
@click.option("--force", is_flag = True, help = 'Force the update of secret', default = False)
@click.option("--hotp", is_flag = True, help = 'This one-time password is counter based', default = False)
@click.option("--secret", "-s", help = 'The new secret of this one-time password')
@click.option("--name", "-n", help = 'The new name of the one-time password')
@click.argument("name_", required = True)
def update(name_, name, secret, email, issuer, force, description, hotp):
    update_.cli(name_, name, secret, email, issuer, force, description, hotp)

@cli.command()
@click.argument("name", required = True)
def delete(name):
    delete_.cli(name)

if __name__ == "__main__":
    cli()
