from setuptools import setup
import sys

# Check that python is greater than 3
if sys.version_info[0] < 3:
    print("To install this package you must have Python 3.0.0 or above")
else:
    requirements = [
        "click>=6.7",
        "pyotp>=2.2.6",
        "keyring>=13.2.1",
        "colorama>=0.3.9",
        "pyperclip>=1.6.4"
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
