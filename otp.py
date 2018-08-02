import click
import pyotp
import re
import os
import json

valid_secret_pattern = re.compile(b"^([A-Z][2-7]+)+$")

def validateSecret(secret):
    return valid_secret_pattern.match(secret.encode())

def showCode(secret, totp = True, counter = None):
    if validateSecret(secret):
        return "Invalid secret! Valid secrets only contain the letters A-Z and digits 2-7"
    
    if (totp):
        generator = pyotp.TOTP(secret)
        return generator.now()
