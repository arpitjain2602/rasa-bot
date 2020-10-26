## happy path
* greet
  - utter_greet
* mood_great
  - action_check_date

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## New Story
* check_date
    - action_check_date

## New Story

* greet
    - utter_greet
* mood_great
    - utter_happy
* check_date
    - action_check_date
