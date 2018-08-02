import click
import os
import json
import keyring

import otp

def write(name, secret, email, issuer, description, force, hotp):
    information  = {
                        "secret" : secret,
                        "type" : "hotp" * hotp + "totp" * (1 - hotp),
                        "email" : email,
                        "issuer" : issuer,
                        "description" : description,
                        "name" : name 
                    }

    if (hotp):
        information['counter'] = 0
    
    # set name to case agnostic name to prevent typos
    keyring.set_password("otp-cli", name.lower(), json.dumps(information))

def cli(name, secret, email, issuer, description, force, hotp):
    information = keyring.get_password("otp-cli", name)    

    if information:
        if force:
            write(name, secret, email, issuer, description, force, hotp)

        force = input("This name already exists. Overwrite anyway? [Y/n] ")

        if (force == 'Y'):
            write(name, secret, email, issuer, description, force, hotp)

        else:
            return 
    else:
        write(name, secret, email, issuer, description, force, hotp)

if __name__ == "__main__":
    cli()