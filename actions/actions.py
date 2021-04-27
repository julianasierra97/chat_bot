# This files contains your custom actions which can be used to run
# custom Python code.

# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import requests
import json
from bs4 import BeautifulSoup
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
