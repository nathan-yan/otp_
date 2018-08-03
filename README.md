<p align='center'>
  <img src = "https://gradebook-space-1.nyc3.digitaloceanspaces.com/Miscellaneous/__.png">
</p>

# OTP_
A command line based one-time password manager that allows you to easily retreive and store one-time passwords. Secrets are stored using the operating system's keyring, so sensitive information is encrypted.
![](https://gradebook-space-1.nyc3.digitaloceanspaces.com/Miscellaneous/demo.gif)

# Contents
* [Installing](#installing)
* [Commands](#commands)
  * [Show](#show)
  * [Write](#show)
  * [Update](#update)
  * [Delete](#delete)
* [Dependencies](#dependencies) 
* [Future improvements](#future-improvements)

# Installing
Installation is really simple, just run `pip install otp-cli` and you're ready to go! Alternatively, you can install the application by cloning the repository and running `python setup.py install` in the `src` directory.

If you're just testing locally, you can try it without installing by cloning the repository and running `python otp.py [OPTIONS]`.

# Commands
### Show
The show command shows a stored one-time password:
<p align='center'>
  <img src = "https://gradebook-space-1.nyc3.digitaloceanspaces.com/Miscellaneous/otp_show1.png"/>
</p>

Names are case-insensitive to help prevent typos involving case. If you want to quickly get a one-time password for a secret, for testing or development purposes, just run `otp show --secret [SECRET]` to see its corresponding TOTP code.

Codes are updated in real-time, and they are hidden upon exit (`CTRL-C` or `q`).

### Write
The write command allows you to store new one-time passwords:
<p align='center'>
  <img src = "https://gradebook-space-1.nyc3.digitaloceanspaces.com/Miscellaneous/otp_write2.png">
</p>
Most of the features here roughly follow the Google Authenticator application, allowing you to store issuers and emails to distinguish multiple one-time passwords from the same website.

### Update
The update command allows you to amend or change details of a one-time password. Changing the secret will prompt you to confirm, as it is a potentially dangerous action.
<p align='center'>
  <img src = "https://gradebook-space-1.nyc3.digitaloceanspaces.com/Miscellaneous/otp_update1.png">
</p>

### Delete
The delete command deletes saved one-time passwords:
<p align='center'>
  <img src = "https://gradebook-space-1.nyc3.digitaloceanspaces.com/Miscellaneous/otp_delete1.png">
</p>

# Dependencies
OTP_ is made in Python, and requires the following dependencies: 

1. click>=6.7
2. pyotp>=2.2.6
3. keyring>=13.2.1
4. colorama>=0.3.9
5. pyperclip>=1.6.4

As of now, OTP_ works only on Python 3 and above, but I'm looking into getting it to work with older Python versions.

Pyperclip allows one-time passwords to be copy pasted to the clipboard for easy access. According to its documentation (https://pypi.org/project/pyperclip/), `xclip` should be installed for anyone using a Linux based operating system, by running `sudo apt-get install xclip`

# Future Improvements
Here are a list of things I'd like to add in future versions of this package.

- [ ] Support for Python 2.
- [ ] Support for counter based one-time passwords. 
- [ ] Support for different kinds of one-time passwords (different period, different number of digits, etc.)
- [ ] Refactoring code and establishing best-practices.
- [ ] Use a less fragile database for storing non-sensitive information like sqlite. 
