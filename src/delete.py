import click
import otp
import keyring

def cli(name):
    click.echo("Deleting a one-time password is permanent and irreversable. If this is your only copy of a one-time password, deleting it WILL lock you out of your account.")
    delete = input("Delete your one-time password? [Y/n] ")

    if (delete == 'y' or delete == 'Y'):
        information, s = otp.getInformation() 
        
        try:
            if name not in information:
                click.echo("'%s' does not exist! Use 'otp write [name] [secret]' to create a new one-time password." % name)
            else:
                del information[name]

        finally:
            click.echo("Cleaning up...")
            s.close()
            

if __name__ == "__main__":
    cli()