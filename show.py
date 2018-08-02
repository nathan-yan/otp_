import click
import os
import json
import otp
import getch_

import sys
import time

import keyring

import colorama
from colorama import Fore, Back, Style

colorama.init()

def stream_otp(secret):
    while True:
        char = getch_.getch()

        if (char == 'q'):
            break;

        seconds_until_next_period = -int(time.time()) % 30

        click.echo('\r\r' +\
        Fore.RED + "[ " + Fore.CYAN +\
        "%s" % str(seconds_until_next_period) +\
        Fore.RED + " ] " +\
        Style.RESET_ALL + Fore.GREEN + otp.showCode(secret, split = True) + "    ", nl = False)

        sys.stdout.flush()

@click.command()
@click.option("--secret", "-s", help = 'The secret used to generate a one-time password')
#@click.option("--")
@click.argument("name", required = False)
def cli(name, secret):
    if secret:
        stream_otp(secret)

    else:
        information = keyring.get_password("otp-cli", name)
        if not information:
            click.echo("'%s' does not exist! Use 'otp write [name] [secret]' to create a new one-time password." % name)
            return

        information = json.loads(information)

        secret = information.get('secret')
        issuer = information.get('issuer')
        email = information.get('email')

        if issuer:
            click.echo("\n%s" % issuer, nl = False)
        if email:
            click.echo(" (%s)" % email, nl = True)
            
        if name:
            stream_otp(secret)
        
if __name__ == "__main__":
    cli()