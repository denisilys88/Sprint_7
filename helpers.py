import random
import string
import json
from data import Data


class Helpers:

    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @staticmethod
    def get_payload_for_order(color):
        payload = json.dumps(Data.PAYLOAD_FOR_ORDER)
        payload = json.loads(payload)
        if color == 'black':
            payload['color'] = ['BLACK']
        elif color == 'grey':
            payload['color'] = ['GREY']
        elif color == 'both':
            payload['color'] = ['GREY', 'BLACK']
        else:
            payload.pop('color')
        return json.dumps(payload)
