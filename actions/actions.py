#This files contains your custom actions which can be used to run
#custom Python code.

#See this guide on how to implement these action:
#https://rasa.com/docs/rasa/custom-actions


#This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from urllib.parse import urlencode


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_retrieve_work_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

    	    contract_type_french = {'CDI': 'permanent', 'Temps plen': 'fulltime', 'CDD': 'contract', 'Intérim': 'temporary',
                 'parttime': 'Temps partiel',
                 'stage': 'internship', 'Apprentissage': 'apprenticeship', 'Contrat pro': 'custom_1',
                 'Freelance': 'subcontract'}
			remote_type = {'remote': '032b3046-06a3-4876-8dfd-474eb5e7ed11',
						'remote while COVID-19': '7e3167e4-ccb4-49cb-b761-9bae564a0a63'}

			place = 'New York'
			job = 'data scientist'
			contract = 'fulltime'
			remote = 'remote while COVID-19'
			BASE_URL = 'https://www.indeed.com'
			path = '/jobs?'
			params = (('q', job), ('l', place), ('jt', contract), ('remotejob', remote_type[remote]))
			url = BASE_URL + path + urlencode(params)
			print(url)

			headers = {
						'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
						'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,/;q=0.8',
						'Connection': 'keep-alive',
						'Upgrade-Insecure-Requests': '1',
						'Cache-Control': 'max-age=0',
						'TE': 'Trailers',
						'If-Modified-Since': 'Sat, 03 Apr 2021 18:56:51 GMT',
						'If-None-Match': "6068ba73-6314"
					}

	    page = requests.get(url, headers=headers)

	    soup = BeautifulSoup(page.content, 'html.parser')
	    links = soup.find_all(class_ = 'jobsearch-SerpJobCard')
	    print(f'I found {len(links)} results that fit your search criteria')

	    for i, card in enumerate(links):
	        print(f'Result {i+1}:')
	        job_title = card.find('a').get('title')
	        print(f'Job title: {job_title}')
	        company = card.find(class_="sjcl").find(class_="company").contents[0]
	        print(f'Company name: {company}')
	        resultUrl = card.find('a').get('href')
	        print(f'Intrested? visit this link: {BASE_URL+""+urllib.parse.quote(resultUrl)}')


	     dispatcher.utter_message(text='I found {len(links)} results that fit your search criteria')

	     return []
