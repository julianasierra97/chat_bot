#This files contains your custom actions which can be used to run
#custom Python code.

#See this guide on how to implement these action:
#https://rasa.com/docs/rasa/custom-actions


#This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from urllib.parse import urlencode


class ActionRetrieveWorkInfo(Action):

    def name(self) -> Text:
        return "action_retrieve_work_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

    	#     contract_type = {'CDI': 'permanent', 'Temps plein': 'fulltime', 'CDD': 'contract', 'Intérim': 'temporary',
        #              'parttime': 'Temps partiel',
        #              'stage': 'internship', 'Apprentissage': 'apprenticeship', 'Contrat pro': 'custom_1',
        #              'Freelance': 'subcontract'}
	    # remote_type = {'télétravail': '032b3046-06a3-4876-8dfd-474eb5e7ed11',
	    #                'télétravail pendat la crise COVID-19': '7e3167e4-ccb4-49cb-b761-9bae564a0a63'}
		#
	    # place = 'Paris'
	    # job = 'developper'
	    # contract = 'CDI'
	    # remote = 'télétravail'
	    # BASE_URL = 'https://fr.indeed.com'
	    # path = '/emplois?'
	    # params = (('q', job), ('l', place), ('jt', contract_type[contract]), ('remotejob', remote_type[remote]))
	    # url = BASE_URL + path + urlencode(params)
		#
	    # print(url)
	    # page = requests.get(url)
		#
	    # soup = BeautifulSoup(page.content, 'html.parser')
	    # links = soup.find_all(class_ = 'jobsearch-SerpJobCard')
	    # print(f'I found {len(links)} results that fit your search criteria')

        print("printing :")

        dispatcher.utter_message(text=tracker.slots.get("place"))

        return []
