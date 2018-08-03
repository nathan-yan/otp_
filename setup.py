from setuptools import setup
import sys

requirements = [
    "click>=6.7",
    "pyotp>=2.2.6",
    "keyring>=13.2.1",
    "colorama>=0.3.9"
]

setup(
    name = "otp-cli",
    version = "0.4.3",
	description = "A CLI one-time password application that manages one-time passwords elegantly and with tons of customization.", 
	author = "Nathan Yan",
	author_email = "nathancyan2002@gmail.com",
	url = "https://github.com/nathan-yan/otp_",
    py_modules = ["otp", "delete", "write", "show", "update", "getch_" ],
    install_requires = requirements,
    entry_points = '''
    [console_scripts]
    otp=otp:cli
    '''
)
