# This files contains your custom actions which can be used to run
# custom Python code.
# code for your custom actions. In-case you want Rasa to call external server via REST API or API call, 
# you can define your Custom Actions here. Remember you can create multiple Python Script for Rasa Custom Action.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

# This is the most real-world example of your chatbot. Suppose in your chatbot you want to add 
# a feature where your bot can tell you latest weather report of a specified city, how you will 
# do it? The answer is “Rasa Custom Action”

# An action can run any code you want. Custom actions can turn on the lights, 
# add an event to a calendar, check a user’s bank balance, or anything else you can imagine.

# Rasa will call an endpoint you can specify when a custom action is predicted. 
# This endpoint should be a web server that reacts to this call, runs the code 
# and optionally returns information to modify the dialogue state.


# This is a simple example for a custom action which utters "Hello World!"


#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


# Step-1 — Define a Method called “ActionCheckWeather” in “actions.py”
# Step-2 — Link this custom action with your Chatbot. Open “domain.yml”.
# actions:
# - utter_greet
# - utter_cheer_up
# - utter_did_that_help
# - utter_happy
# - utter_goodbye
# - action_check_weather

# Step-3 - Now in the stories, add this custom action as your flow. Open “stories.md” file 
#         and this new custom action “action_check_weather” as part of happy path flow.
# ## happy path
# * greet
# - utter_greet
# * mood_great
# - action_check_weather

# Step-4 Tell rasa to use Custom Action Server
# Open “endpoints.yml” and add the following line to enable custom action server
# action_endpoint:
#    url: "http://localhost:5055/webhook"
# https://towardsdatascience.com/create-chatbot-using-rasa-part-1-67f68e89ddad

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from datetime import date
from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

global today
today = date.today()

# class ActionCheckWeather(Action):
#    def name(self) -> Text:
#       return "action_check_weather"

#    def run(self,
#            dispatcher: CollectingDispatcher,
#            tracker: Tracker,
#            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#       dispatcher.utter_message("Hello World! from custom action")
#       return []

class ActionCheckDate(Action):
   def name(self) -> Text:
      return "action_check_date"

   async def run(self,
           dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

      dispatcher.utter_message("Today is " + str(today))
      # dispatcher.utter_message(attachment = "https://rasa.com/docs/rasa-x/installation-and-setup/install/local-mode/")

      # dispatcher.utter_messsage(buttons = [
      #           {"payload": "/affirm", "title": "Yes"},
      #           {"payload": "/deny", "title": "No"},])

      # date_picker = {
      # "blocks":[
      # {"type": "section","text":{
      #   "text": "Make a bet on when the world will end:",
      #   "type": "mrkdwn"},
      # "accessory":
      # {"type": "datepicker",
      #   "initial_date": "2019-05-21",
      #   "placeholder":
      #   {"type": "plain_text",
      #     "text": "Select a date"}}}]}
      # dispatcher.utter_message(json_message = date_picker)

      # dispatcher.utter_message(image = "https://i.imgur.com/nGF1K8f.jpg")
      return []



# class ActionCheckRestaurants(Action):
#    def name(self) -> Text:
#       return "action_check_restaurants"

#    def run(self,
#            dispatcher: CollectingDispatcher,
#            tracker: Tracker,
#            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#       cuisine = tracker.get_slot('cuisine')
#       q = "select * from restaurants where cuisine='{0}' limit 1".format(cuisine)
#       result = db.query(q)

#       return [SlotSet("matches", result if result is not None else [])]


# the state tracker for the current user. You can access slot values using tracker.get_slot(slot_name), 
# the most recent user message is tracker.latest_message.text and any other rasa_sdk.Tracker property. 
# See the documentation for the tracker.

# You can see, you are getting a reply from custom action which is written in python. 
# In the same python script, you can connect to your backend database and return a response. 
# Also, you can call an external API using additional python packages.
# Also, you can develop Custom action Server in C#, NodeJS and Java.


# data/nlu.md ‘*’your NLU training data. Here you can define Intent. Like Order Pizza or Book Uber. 
# You need to add related Sentences for that Intent. Remember if you are using Rasa-X, your training 
# Intent and Data will be added automatically.

# data/stories.md ‘*’your stories. This is required for Rasa Core. There is something called “Dialog Flow 
# in Rasa” where Rasa Core controls the flow of the conversation between you and chatbot, so for that 
# flow, you need to train chatbot using these stories. So in case you want your chatbot to be very perfect 
# on different context (stories) you can add those stories here.

# domain.yml ‘*’your assistant’s domain. This file combines Different Intent which chatbot can 
# detect and list of Bot replies. Remember you can define your Custom Action Server Python method 
# name here (in underscore format), so that Rasa will call that python method for you.

# endpoints.ymldetails for connecting to channels like FB messenger. This is mainly used for 
# production setup. You can configure your Database like Redis so that Rasa can store 
# tracking information.