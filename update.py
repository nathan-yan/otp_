import click
import os
import json
import keyring

import otp

def update_(information, name, secret, email, issuer, description, hotp):
    d = {
        'name' : name, 
        'secret' : secret,
        'email' : email,
        'issuer' : issuer,
        'description' : description,
        'hotp' : hotp
    }

    for key in d:
        value = d.get(key)
        if value:
            information[key] = value
    
    return information

@click.command()
@click.option("--email", "-e", help = 'The email address this one-time password belongs to')
@click.option("--issuer", "-i", help = 'The issuer of this one-time password')
@click.option("--description", "-d", help = 'The description of this one-time password')
@click.option("--force/--no-force", default = False)
@click.option("--hotp/--no-hotp", default = False)
@click.option("--secret", "-s")
@click.option("--name", "-n")
@click.argument("name_", required = True)
def update(name_, name, secret, email, issuer, force, description, hotp):
    if (secret):
        if(input("Are you sure you want to change your secret for %s? [Y/n] " % name) not in ['Y', 'y']):
            return 
    
    information = keyring.get_password("otp-cli", name_)
    try:
        information = json.loads(information)
    except:
        click.echo("'%s' does not exist! Use 'otp write [name] [secret]' to create a new one-time password." % name_)
        return

    information = update_(information, name, secret, email, issuer, description, hotp)

    keyring.delete_password("otp-cli", name_.lower())

    if (name):
        name_ = name 

    keyring.set_password("otp-cli", name_.lower(), json.dumps(information)) 

if __name__ == "__main__":
    update()