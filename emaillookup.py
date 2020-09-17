from enum import IntEnum
import requests

class Protocol(IntEnum):
  POP3=0,
  IMAP=1,
  SMTP=2

class Info:
  def __init__(self, protocol, address, port, secure, username):
    self.protocol = protocol
    self.address = address
    self.port = port
    self.secure = secure
    self.username = username

class LookUp:
    @staticmethod
    def search(domain, protocol):
        response = requests.get(f'https://emailsettings.firetrust.com/settings?q={domain}')
        jobj = response.json()['settings'][int(protocol)]
        return Info(jobj['protocol'], jobj['address'], jobj['port'], jobj['secure'], jobj['username'])

#data = LookUp().search('@gmail.com', Protocol.POP3)