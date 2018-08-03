import click
import keyring

import otp

def update_(information, name, secret, email, issuer, description, hotp):
    d = {
        'name' : name, 
        'email' : email,
        'issuer' : issuer,
        'description' : description,
        'hotp' : hotp
    }

    for key in d:
        value = d.get(key)
        if value:
            information[key] = value
    
    if secret:
        keyring.set_password("otp-cli", information['ref'], secret)
    
    return information

def cli(name_, name, secret, email, issuer, force, description, hotp):
    if (secret):
        if otp.validateSecret(secret):
            click.echo("Invalid secret! Valid secrets contain only the letters A-Z and digits 2-7")
            return
            
        if(input("Are you sure you want to change your secret for %s? [Y/n] " % name_) not in ['Y', 'y']):
            return 
    try:
        information, s = otp.getInformation() 

        if name_ not in information:
            click.echo("'%s' does not exist! Use 'otp write [name] [secret]' to create a new one-time password." % name_)
            return

        new_information = update_(information[name_], name, secret, email, issuer, description, hotp)

        if name:
            del information[name_]
            name_ = name

        information[name_.lower()] = new_information
    finally:
        s.close()

if __name__ == "__main__":
    update()