from setuptools import setup
import sys

with open("README.md", 'r') as markdown:
    long_description = markdown.read()

# Check that python is greater than 3
if sys.version_info[0] < 3:
    raise Exception("To install this package you must have Python 3 or above")
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
        version = "0.5.3",
        description = "A CLI one-time password application that manages one-time passwords elegantly and with tons of customization.",
        long_description_content_type = "text/markdown",
        long_description = long_description,
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
