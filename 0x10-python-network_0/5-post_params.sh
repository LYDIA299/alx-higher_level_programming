#!/bin/bash
#takes in URL, sends a POST request and the response body is displayed.
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
