In order to run this app you need to install python3 on your Windows 10 machine.
You will also need the following python packages installed:
    * flask
    * dotenv-python

Additional software needed in order to run the application on system startup:
    * nvm (https://github.com/coreybutler/nvm-windows)
    * pm2-installer (https://github.com/jessety/pm2-installer)

Next step is to create a .env file located in root directory of the project.
Add the following values (or change if you want. 0.0.0.0 makes it possible however to access this server from any computer in the local network):
    * HOST=0.0.0.0
    * PORT=6424

Start and save the server process in PM2:
    * `pm2 start server.py --name windows-shutdowner`
    * `pm2 save`

Now the server should be up and running in the background. Vetify this by running `pm2 status`.
If you want to be able to run this remotely (over internet), you must allow port 6424 for TCP in the Windows Firewall configuration. Also, your router configuration must be updated with a port forward rule for the same port and TCP.

When this is set up, you simply create a POST request using Postman or Insomnia as example.
From local networt:
http://yourcomputerslocalip:6424/poweroff

From remote network:
http(s)://yourpublicip:6424/poweroff

Enjoy shutting down your PC without leaving the couch or bed!