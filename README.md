# Meaningful Quantum Search _MQS_

How MQS Works

**1st)** A user (You) types a search request for some type of document.

**2nd)** A classical computer uses a semantic embedding model to get "vectors of semantic meaning" of the documents you're searching through and the search request you've given. 
_(Also saves the semantic embedding vectors of documents already searched)_

**3rd)** Then each document's semantic vector compared to the search requests' semantic vector. _The comparison is done with a quantum circuit and then results in a similarity/likeness score of 0.0-1.0. _

# THIS EFFORT IS SUPPORTED BY QOLLAB & QION


# IMPORTANT NOTE:
  The github contains the code that can run on local hardware but due to time constraints the "files" are the strings (This could easily be changed to read files in a directory if given time). 
  We do however calculate embeddings in the github code and provide a GUI

  Our website also shows an online GUI running whats in the github

# HUGE THANKS TO THIS RESEARCH PAPER

https://arxiv.org/abs/2512.02619v1

THESE PEOPLE ARE AMAZING WE LOVE YOU THIS PAPER HELPED A LOT WITH UNDERSTANDING WHAT'S GOING ON

# USAGE
  Install all requirements and then run main.py
  then go to http://localhost:8080 and enjoy!
