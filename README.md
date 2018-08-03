<center>[![](https://gradebook-space-1.nyc3.digitaloceanspaces.com/Miscellaneous/__.png)](https://gradebook-space-1.nyc3.digitaloceanspaces.com/Miscellaneous/__.png)</center>

#OTP_
A command line based one-time password manager that allows you to easily retreive and store one-time passwords. Secrets are stored using the operating system's keyring, so sensitive information is encrypted. 
![](https://gradebook-space-1.nyc3.digitaloceanspaces.com/Miscellaneous/demo.gif)

##Commands
### Show
The show command shows a stored one-time password:
<center>![](https://gradebook-space-1.nyc3.digitaloceanspaces.com/Miscellaneous/otp_show1.png)</center>
Names are case-__insensitive__ to help prevent typos involving case.  If you want to quickly get a one-time password for a secret, for testing or development purposes, just run `opt show --secret [SECRET]` to see its corresponding TOTP code.

Codes are updated in real-time, and they are hidden upon exit (`CTRL-C` or `q`).

### Write
The write command allows you to store new one-time passwords:
<center>[![](https://gradebook-space-1.nyc3.digitaloceanspaces.com/Miscellaneous/otp_write2.png)](https://gradebook-space-1.nyc3.digitaloceanspaces.com/Miscellaneous/otp_write2.png)</center>
Most of the features here follow roughly the Google Authenticator application, allowing you to store issuers and emails to distinguish multiple one-time passwords from the same website.

### Update
The update command allows you to amend or change details of a one-time password. Changing the secret will prompt you to confirm, as it is a potentially dangerous action.
<center>![](https://gradebook-space-1.nyc3.digitaloceanspaces.com/Miscellaneous/otp_update1.png)</center>

### Delete
The delete command deletes saved one-time passwords:
<center>![](https://gradebook-space-1.nyc3.digitaloceanspaces.com/Miscellaneous/otp_delete1.png)</center>
