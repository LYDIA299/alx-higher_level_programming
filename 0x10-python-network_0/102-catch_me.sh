#!/bin/bash
# makes a request to 0.0.0.0:5000/catch_me and response msg "You got me!
curl -s -X PUT -H "Origin: HolbertonSchool" --data "user_id=98" 0.0.0.0:5000/catch_me
