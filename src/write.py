import click
import keyring

import otp
import uuid

def write(information, name, secret, email, issuer, description, force, hotp):
    key = str(uuid.uuid4())

    info  = {
                        "type" : "hotp" * hotp + "totp" * (1 - hotp),
                        "email" : email,
                        "issuer" : issuer,
                        "description" : description,
                        "name" : name,
                        "ref" : key
                    }

    if (hotp):
        info['counter'] = 0
    
    # set name to case agnostic name to prevent typos
    information[name.lower()] = info

    # Write secret into key
    keyring.set_password("otp-cli", key, secret)

def cli(name, secret, email, issuer, description, force, hotp):
    if otp.validateSecret(secret):
        click.echo("Invalid secret! Valid secrets contain only the letters A-Z and digits 2-7")
        return
        
    information, s = otp.getInformation() 
    # keyring.get_password("otp-cli", name)    

    try:
        if name in information:
            if force:
                write(information, name, secret, email, issuer, description, force, hotp)

            force = input("This name already exists. Overwrite anyway? [Y/n] ")

            if (force == 'Y'):
                write(information, name, secret, email, issuer, description, force, hotp)

            else:
                return 
        else:
            write(information, name, secret, email, issuer, description, force, hotp)
    finally:
        print("Cleaning up...")
        s.close()

if __name__ == "__main__":
    cli()