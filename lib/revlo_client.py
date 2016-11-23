import requests
from math import ceil
import json
from time import sleep

VERSION = 1
API_BASE = 'https://api.revlo.co'
MAX_RETRIES = 10

class RevloClient(object):

  def __init__(self, api_key=""):
    self.headers = {'content-type': 'application/json', \
                    'x-api-key'   : api_key}

  def handle_errors(self, response):
    if response.status_code >= 500:
      raise RevloAPIServiceError("Something went wrong")
    else:
      raise RevloAPIClientError(json.loads(response.text)['error'])

  def _is400(self, code):
    return code >= 400 and code < 500

  def _get(self, endpoint):
    response = None
    for i in range(0,MAX_RETRIES):
      response = requests.get("{}{}".format(API_BASE,endpoint), headers=self.headers)
      if response.ok:
        break
      elif is400(response.status_code):
        handle_errors(self,response)
      sleep(min(2**i,10))
    if not response.ok:
      self.handle_errors(response)
    return response.json()

  def _post(self, endpoint, payload):
    response = None
    for i in range(0, MAX_RETRIES):
      response = requests.post("{}{}".format(API_BASE, endpoint), headers=self.headers, data=payload)
      if response.ok:
        break
      elif is400(response.status_code):
        handle_errors(self,response)
      sleep(min(2**i,10))
    if not response.ok:
      self.handle_errors(response)
    return response.json()

  def get_rewards(self):
    response = self._get('/{}/rewards'.format(VERSION))
    total = response['total']
    page_size = response['page_size']
    number_of_pages = int(ceil((total+0.0)/page_size))
    p = 1
    while p <= number_of_pages:
      redemptions = self._get('/{}/rewards?page={}'.format(VERSION, p))['rewards']
      yield redemptions
      p += 1

  def get_redemptions(self):
    response = self._get('/{}/redemptions'.format(VERSION))
    total = response['total']
    page_size = response['page_size']
    number_of_pages = int(ceil((total+0.0)/page_size))
    p = 1
    while p <= number_of_pages:
      redemptions = self._get('/{}/redemptions?page={}'.format(VERSION, p))['redemptions']
      yield redemptions
      p += 1

class RevloAPIServiceError(IOError):
  pass

class RevloAPIClientError(IOError):
  pass
