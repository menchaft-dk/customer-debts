import json
import jsonlines
import requests


class Api:

    @staticmethod
    def makeApiCall(url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json();
                return data;
            else:
                raise ApiError('GET /tasks/ {}'.format(resp.status_code))
        except requests.exceptions.HTTPError as errh:
            return "An Http Error occurred:" + repr(errh)
        except requests.exceptions.ConnectionError as errc:
            return "An Error Connecting to the API occurred:" + repr(errc)
        except requests.exceptions.Timeout as errt:
            return "A Timeout Error occurred:" + repr(errt)
        except requests.exceptions.RequestException as err:
            return "An Unknown Error occurred" + repr(err)
