import click
import pyotp
import re
import os
import json
import shelve

import show as show_
import delete as delete_
import write as write_
import update as update_

valid_secret_pattern = re.compile(b"^([A-Z][2-7]+)+$")
information_path = os.path.expanduser(os.path.join("~", "otp-cli", "information.db"))

def validateSecret(secret):
    return valid_secret_pattern.match(secret.encode())

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
    except:
        os.makedirs(os.path.dirname(information_path), exist_ok = True)
        s = shelve.open(information_path, writeback = True)

    try:
        ret = s['information']
    except:
        ret = {}
    
    return ret, s

@click.group()
def cli():
    pass

@cli.command()
@click.option("--secret", "-s", help = 'The secret used to generate a one-time password')
@click.option("--all", "-a", is_flag = True)
#@click.option("--")
@click.argument("name", required = False)
def show(name, secret, all):
    show_.cli(name, secret, all)

@cli.command()
@click.option("--email", "-e", help = 'The email address this one-time password belongs to')
@click.option("--issuer", "-i", help = 'The issuer of this one-time password')
@click.option("--description", "-d", help = 'The description of this one-time password')
@click.option("--force/--no-force", default = False)
@click.option("--hotp/--no-hotp", default = False)
@click.argument("name", required = True)
@click.argument("secret", required = True)
def write(name, secret, email, issuer, description, force, hotp):
    write_.cli(name, secret, email, issuer, description, force, hotp)

@cli.command()
@click.option("--email", "-e", help = 'The email address this one-time password belongs to')
@click.option("--issuer", "-i", help = 'The issuer of this one-time password')
@click.option("--description", "-d", help = 'The description of this one-time password')
@click.option("--force/--no-force", default = False)
@click.option("--hotp/--no-hotp", default = False)
@click.option("--secret", "-s")
@click.option("--name", "-n")
@click.argument("name_", required = True)
def update(name_, name, secret, email, issuer, force, description, hotp):
    update_.cli(name_, name, secret, email, issuer, force, description, hotp)

@cli.command()
@click.argument("name", required = True)
def delete(name):
    delete_.cli(name)

if __name__ == "__main__":
    cli()