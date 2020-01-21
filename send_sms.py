import requests
import json

URL = 'https://www.sms4india.com/api/v1/sendCampaign'

# get request
def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey': '0G7YEX56M3U5DNS53DCCFJIHJH2D86IL',
  'secret':'WH8WYMEMSAEH0RH5',
  'usetype':'useType',
  'phone': '8376016424',
  'message':'textMessage',
  'senderid':'SMSIND'
  }
  return requests.post(reqUrl, req_params)

# get response
response = sendPostRequest(URL, 'provided-api-key', 'provided-secret', 'prod/stage', 'valid-to-mobile', 'active-sender-id', 'message-text' )
"""
  Note:-
    you must provide apikey, secretkey, usetype, mobile, senderid and message values
    and then requst to api
"""
# print response if you want
print(response.text)