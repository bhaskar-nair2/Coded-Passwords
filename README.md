# Coded-Passwords
A possible way to secure passwords is by not storing them or sending them.
The idea behind this project is to make a encrypted hash using the username and password combination and storing it instead, while the users remember the passwords of their account.
When a user tries to log-in this hash is searched & brought using the username and is then is tested against the given username and password,
if the hash generated by the current values match the stored hash, the function returns true and the user logs in.
This is simple function and can be done on the browser itself, thus saving resources and also avoiding the stealing of passwords(Packet Sniffing).

No point hacking the cloud as the passwords aren't stored there
No point sniffing packets as there is no password being transferred.
The only way is by session hijacking, which is equal to giving away your password.

Useage:
The basic logic is in the Main.py file
To test the logic, first run the sqlmanager.py
Make a new User in process.py
Then login using process-login.py
Voila!

This is under MIT license, Enjoy using this it!