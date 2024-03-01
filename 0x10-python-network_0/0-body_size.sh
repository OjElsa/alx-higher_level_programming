#!/bin/bash
# Bash that Sends a request to that URL & displays size of the body of response
curl -sL "$1" | wc -c
