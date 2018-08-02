from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

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
