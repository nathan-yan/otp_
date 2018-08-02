from setuptools import setup
import sys

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

if sys.platform != 'win32':
    requirements.append('getch==1.0')

setup(
    name = "otp",
    version = "0.2",
    py_modules = ["show", "otp", "getch_", "delete", "write", "show", "update"],
    install_requires = requirements,
    entry_points = '''
    [console_scripts]
    otp=otp:cli
    '''
)
