from Hologram.HologramCloud import HologramCloud
import psutil #sudo apt-get install python-psutil
import socket, time, math

# Setup Hologram
deviceKey = {'devicekey': 'abcd1234'}
hologram = HologramCloud(deviceKey, network = 'cellular', authentication_type = 'csrpsk')

startTime = time.time()
smsFrom = None

def sendSMS(message):
    phone = "+" + smsFrom.replace('F','') # format senders phone number
    hologram.sendSMS(phone, message) # send SMS answer

def answerQuestion(sms):
    # save phone number of who sent the question
    global smsFrom
    smsFrom = sms.sender

    # determine which answer to send back
    if "name" in sms.message:
        # If I'm asked what my name is
        name = socket.gethostname().replace('.local','')
        sendSMS("My name is " + name + ", it is nice to meet you! :)")

    elif "old" in sms.message:
        # If I'm asked how old I am
        age = math.ceil((time.time() - startTime) / 1000)
        sendSMS("I'm " + str(age) + " seconds old, to be exact.")

    elif "smart" in sms.message:
        # If asked what I'm doing
        numProcesses = len(psutil.pids())
        sendSMS("Currently I'm thinking about " + str(numProcesses) + " things right now. I'm a genius!")

    elif "body" in sms.message:
        # If I'm asked anything about my body
        sendSMS("Sniffle :(  I do not have a body, will you make one for me?")

    else:
        # default answer if I have no idea what was asked
        sendSMS("Sorry, I do not have an answer for that question.")

# Connect to the Hologram Global Network
hologram.network.connect()

try:
    print "Listening for incoming SMS..."
    while True:
        # Start listening for incoming SMS questions
        hologram.enableSMS()
        time.sleep(5)
        hologram.disableSMS()

        # check if we recieved a new question
        sms = hologram.popReceivedSMS()
        if sms is not None:
            print "GOT MESSAGE"
            print sms
            answerQuestion(sms) # try to answer the question and send a response
finally:
    print "Closing cell connection"
    hologram.network.disconnect()
