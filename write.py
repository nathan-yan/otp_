import click
import os
import json
import otp

def write(secrets, name, secret, email, issuer, description, force, hotp):
    secrets[name] = {
                        "secret" : secret,
                        "type" : "hotp" * hotp + "totp" * (1 - hotp),
                        "email" : email,
                        "issuer" : issuer,
                        "description" : description
                    }

    if (hotp):
        secrets[name]['counter'] = 0
    
    return secrets

@click.command()
@click.option("--email", "-e", help = 'The email address this one-time password belongs to')
@click.option("--issuer", "-i", help = 'The issuer of this one-time password')
@click.option("--description", "-d", help = 'The description of this one-time password')
@click.option("--force/--no-force", default = False)
@click.option("--hotp/--no-hotp", default = False)
@click.argument("name", required = True)
@click.argument("secret", required = True)
def cli(name, secret, email, issuer, description, force, hotp):
    credentials_path = os.path.expanduser("~\otp-cli\credentials.json")

    with open(credentials_path, 'r') as credentials:
        secrets = json.loads(credentials.read())

        exists = secrets.get(name)

        if exists:
            if force:
                secrets = write(secrets, name, secret, email, issuer, description, force, hotp)

            force = input("This name already exists. Overwrite anyway? [Y/n] ")

            if (force == 'Y'):
                secrets = write(secrets, name, secret, email, issuer, description, force, hotp)

            else:
                return 
        else:
            secrets = write(secrets, name, secret, email, issuer, description, force, hotp)

        newFile = open(credentials_path, 'w')
        newFile.write(json.dumps(secrets))
        newFile.close()

if __name__ == "__main__":
    cli()