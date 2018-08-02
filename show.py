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

def stream_otp(secret):
    while True:
        char = getch_.getch()

        if (char == 'q'):
            click.echo('\r\r' +\
            Fore.RED + "[ " + Fore.CYAN +\
            "-" +\
            Fore.RED + " ] " +\
            Style.RESET_ALL + Fore.GREEN + "--- ---" + "    ", nl = False)      # Overwrite previous line to hide the otp

            click.echo("")
            break;

        seconds_until_next_period = -int(time.time()) % 30

        click.echo('\r\r' +\
        Fore.RED + "[ " + Fore.CYAN +\
        "%s" % str(seconds_until_next_period) +\
        Fore.RED + " ] " +\
        Style.RESET_ALL + Fore.GREEN + otp.showCode(secret, split = True), nl = False)

        sys.stdout.flush()

def cli(name, secret, all):
    #if all:
    if secret:
        stream_otp(secret)

    else:
        try:
            information, s = otp.getInformation()
            s.close()

            if name not in information:
                click.echo("'%s' does not exist! Use 'otp write [name] [secret]' to create a new one-time password." % name)
                return

            info = information.get(name)

            secret = keyring.get_password("otp-cli", info.get('ref'))
            issuer = info.get('issuer')
            email = info.get('email')

            if issuer:
                click.echo("\n%s" % issuer, nl = False)
            if email:
                click.echo(" (%s)" % email, nl = True)
            else:
                click.echo("")

            if name:
                stream_otp(secret)
        finally:
            s.close()

if __name__ == "__main__":
    cli()