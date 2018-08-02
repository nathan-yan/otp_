from setuptools import setup

setup(
    name = "otp",
    version = "0.1",
    py_modules = ["otp"],
    install_requires = ["Click", "pyotp"],
    entry_points = '''
    [console_scripts]
    otp=otp:cli
    '''
)
