# This files contains your custom actions which can be used to run
# custom Python code.

# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction

import requests
import json
#from bs4 import BeautifulSoup
from urllib.parse import urlencode

import time


class ActionHelloWorld(Action):
    def name(self) -> Text:
        return "action_retrieve_work_info"

    @staticmethod
    def get_chat_id(string: Text):
        time.sleep(3)
        return Text

    def get_algo(self, string: Text):
        return Text

    @staticmethod
    def get_jobs(dispatcher: CollectingDispatcher, tracker: Tracker) -> bool:
        """Check if a string is an integer."""

        try:
            contract_type_french = {
                "CDI": "permanent",
                "Temps plen": "fulltime",
                "CDD": "contract",
                "Intérim": "temporary",
                "parttime": "Temps partiel",
                "stage": "internship",
                "Apprentissage": "apprenticeship",
                "Contrat pro": "custom_1",
                "Freelance": "subcontract",
            }
            remote_type = {
                "remote": "032b3046-06a3-4876-8dfd-474eb5e7ed11",
                "remote while COVID-19": "7e3167e4-ccb4-49cb-b761-9bae564a0a63",
            }
            job = tracker.slots.get("work_type")
            place = tracker.slots.get("place")
            contract = "fulltime"
            remote = "remote while COVID-19"
            BASE_URL = "https://www.indeed.com"
            path = "/jobs?"
            params = (
                ("q", job),
                ("l", place),
                ("jt", contract),
                ("remotejob", remote_type[remote]),
            )
            url = BASE_URL + path + urlencode(params)
            dispatcher.utter_message(url)
            headers = {
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,/;q=0.8",
                "Connection": "keep-alive",
                "Upgrade-Insecure-Requests": "1",
                "Cache-Control": "max-age=0",
                "TE": "Trailers",
                "If-Modified-Since": "Sat, 03 Apr 2021 18:56:51 GMT",
                "If-None-Match": "6068ba73-6314",
            }

            page = requests.get(url, headers=headers)

            soup = BeautifulSoup(page.content, "html.parser")
            links = soup.find_all(class_="jobsearch-SerpJobCard")
            return "I found " + str(len(links)) + " jobs for you"
        except ValueError:
            return "False"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        result = self.get_jobs(dispatcher, tracker)
        dispatcher.utter_message(result)
        time.sleep(3.0)

        return []



class ValidateWorkForm(FormValidationAction):
    """Example of a form validation action."""

    def name(self) -> Text:
        return "validate_work_form"

    @staticmethod
    def place_db() -> List[Text]:
        """Database of supported cuisines."""
        return open('cityDb.txt', 'r').read().splitlines()
        

    # @staticmethod
    # def is_int(string: Text) -> bool:
    #     """Check if a string is an integer."""

    #     try:
    #         int(string)
    #         return True
    #     except ValueError:
    #         return False



    def validate_place(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate place value."""

        if value.lower() in self.place_db():
            # validation succeeded, set the value of the "place" slot to value
            return {"place": value}
        else:
            dispatcher.utter_message(response="utter_wrong_place")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"place": None}



    # def validate_num_people(
    #     self,
    #     value: Text,
    #     dispatcher: CollectingDispatcher,
    #     tracker: Tracker,
    #     domain: Dict[Text, Any],
    # ) -> Dict[Text, Any]:
    #     """Validate num_people value."""

    #     if self.is_int(value) and int(value) > 0:
    #         return {"num_people": value}
    #     else:
    #         dispatcher.utter_message(response="utter_wrong_num_people")
    #         # validation failed, set slot to None
    #         return {"num_people": None}

    # def validate_outdoor_seating(
    #     self,
    #     value: Text,
    #     dispatcher: CollectingDispatcher,
    #     tracker: Tracker,
    #     domain: Dict[Text, Any],
    # ) -> Dict[Text, Any]:
    #     """Validate outdoor_seating value."""

    #     if isinstance(value, str):
    #         if "out" in value:
    #             # convert "out..." to True
    #             return {"outdoor_seating": True}
    #         elif "in" in value:
    #             # convert "in..." to False
    #             return {"outdoor_seating": False}
    #         else:
    #             dispatcher.utter_message(response="utter_wrong_outdoor_seating")
    #             # validation failed, set slot to None
    #             return {"outdoor_seating": None}

    #     else:
    #         # affirm/deny was picked up as True/False by the from_intent mapping
    #         return {"outdoor_seating": value}

