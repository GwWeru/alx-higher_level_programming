#!/bin/bash
# script that takes url and sends POST req to display the response
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
