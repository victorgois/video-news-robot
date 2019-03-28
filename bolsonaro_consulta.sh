#!/bin/bash    
# put all your commands her

curl https://newsapi.org/v2/everything -G \
    -d q=Bolsonaro \
    -d from=2019-03-11 \
    -d sortBy=popularity \
    -d apiKey=2de5d157d448424db4574be570b492d4  \
    -o new_output.json
