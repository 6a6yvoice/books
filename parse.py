import requests
import json 

response = requests.get('https://gitlab.grokhotov.ru/hr/yii-test-vacancy/-/raw/master/books.json')

response_json = json.loads(response.text)

for books in response_json:
    if books['categories'] == []:
        books['categories'] = ['new']
    print(books['title'],books['categories'])

#def resp():
#    if (
#        response.status_code != 204 and
#        response.headers["content-type"].strip().startswith("application/json")
#    ):
#        try:
#            return response.json()
#        except json.decoder.JSONDecodeError:
#            print('The string does NOT contain valid JSON')
#
#resp()

