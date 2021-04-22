import requests
import sendEmail
import datetime

def firmwareCheck(deviceName):
    response = requests.get('https://api.ipsw.me/v4/device/{}'.format(deviceName))
    r = response.json()
    return r['firmwares'][0]['version']


if __name__ == '__main__':
    # this should be changed to the newest apple device on the market.
    # Can be found at https://ipsw.me/product/iPhone
    # Click on the newest device in the top left corner and the New_Device name is in the URL (EX: /iphone13,3)
    newDevice = 'iphone13,3'

    # mailList = config.emailList
    fileObj = open('firmwareVersion.txt', 'r')
    currentVersion = fileObj.readline()
    fileObj.close()

    newVersion = firmwareCheck(newDevice)

    if newVersion != currentVersion:
        fileObj = open('firmwareVersion.txt', 'w')
        fileObj.write(newVersion)
        fileObj.close()
        sendEmail.email(newVersion)
    else:
        filed = open('logging.txt', 'w')
        filed.write(str(datetime.datetime.now()) + '\n')
        filed.close()
        