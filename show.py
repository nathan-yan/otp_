import click
import os
import json
import otp
import getch

import sys
import time

import colorama
from colorama import Fore, Back, Style

colorama.init()

@click.command()
@click.option("--secret", "-s", help = 'The secret used to generate a one-time password')
#@click.option("--")
@click.argument("name", required = True)
def cli(name, secret):
    credentials_path = os.path.expanduser("~\otp-cli\credentials.json")

    with open(credentials_path, 'r') as credentials:
        secrets = json.loads(credentials.read())

        secret_group = secrets.get(name)

        issuer = secret_group.get('issuer')
        email = secret_group.get('email')

        if issuer:
            click.echo("\n%s" % issuer, nl = False)
        if email:
            click.echo(" (%s)" % email, nl = True)
            
        if name:
            while True:
                char = getch.getch()

                if (char == 'q'):
                    break;

                seconds_until_next_period = -int(time.time()) % 30

                secret = secrets.get(name)['secret']
                if (not secret):
                    click.echo("%s is not a valid name!" % name)
                    return

                click.echo('\r' +\
                Fore.RED + "[ " + Fore.CYAN +\
                "%s" % str(seconds_until_next_period) +\
                Fore.RED + " ] " +\
                Style.RESET_ALL + Fore.GREEN + otp.showCode(secret) + "    ", nl = False)

                
                sys.stdout.flush()

                time.sleep(1)
        else:
            click.echo(otp.showCode(secret))

if __name__ == "__main__":
    cli()