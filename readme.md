## SMS example with Raspberry Pi and Hologram Nova

In this example we making a Pi talk back to us through cellular SMS. From your phone you can ask questions and get a intelligent response back.

Prerequisites:
  - [RaspberryPi w/Raspbian running](https://www.raspberrypi.org/products/)
  - [Hologram Nova w/activated SIM](https://hologram.io/nova/)
  - Allocated phone number through device configuration page form Hologram's dashboard.

To get started, from the Pi, install dependancies and clone this repo.
```
$ sudo apt-get install python-psutil
$ curl -L hologram.io/python-install | bash
$ git clone https://github.com/benstr/TUT-ask-pi-sms.git
```

Modify the `deviceKey` variable with your device's CSR key from the Hologram device configuration page.
```
$ cd TUT-ask-pi-sms
$ sudo nano askPiSMS.py
```

Run the script and send it a question.
```
$ sudo python askPiSMS.py
```

Send one of the following questions to your allocated Hologram phone number.
  - What is your name?
  - How old are you?
  - Do you have a body?
  - How smart are you?
