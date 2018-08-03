import click
import otp
import getch_

import sys
import time

import keyring

import colorama
from colorama import Fore, Back, Style

def stream_otp(secret, copy = False):
    while True:
        char = getch_.getch()

        if (char == 'q'):
            click.echo('\r' +\
            Fore.RED + "[ " + Fore.CYAN +\
            "-" +\
            Fore.RED + " ] " +\
            Style.RESET_ALL + Fore.GREEN + "--- ---" + "    " + Style.RESET_ALL, nl = False)      # Overwrite previous line to hide the otp

            click.echo(Style.RESET_ALL)
            break;

        seconds_until_next_period = -int(time.time()) % 30

        if (copy):
            try:
                # Copy the code to clipboard
                otp.copyCode(otp.showCode(secret))
            except:
                print("If you are currently on linux, you will need to install the xclip dependency. Run \"sudo apt-get install xclip\".")
                break;

        click.echo('\r' +\
        Fore.RED + "[ " + Fore.CYAN +\
        "%s" % str(seconds_until_next_period) +\
        Fore.RED + " ] " +\
        Style.RESET_ALL + Fore.GREEN + otp.showCode(secret, split = True) + "    ", nl = False)

        sys.stdout.flush()

def cli(name, secret, all, copy):
    if all or (not name and not secret):
        information, s = otp.getInformation()
        s.close()

        for key in information:
            info = information[key]

            click.echo(Fore.YELLOW + info['name'] + Style.RESET_ALL)
            if (info.get('issuer')):
                click.echo("Issuer: %s" % info['issuer'])
            if (info.get('email')):
                click.echo("Email:  " + info['email'])
            
            if (info.get("description")):
                click.echo("\n    %s" % info['description'])
            
            click.echo("")
                
        return

    if secret:
        if otp.validateSecret(secret):
            click.echo("Invalid secret! Valid secrets contain only the letters A-Z and digits 2-7")
            return

        stream_otp(secret, copy = copy)

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
                stream_otp(secret, copy = copy)
        finally:
            s.close()

if __name__ == "__main__":
    cli()