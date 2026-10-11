from flask import Flask, render_template,Response, jsonify, make_response, request, redirect, url_for
import os, time
from imagineFiles import *



# Flask is our web GI
app = Flask(__name__)

@app.route("/",methods=["GET", "POST"])
def home():

    toRender = render_template('summoner.html')



    
    if request.method == "POST":
        requestForQuantumSearch = request.form.get("request")


        
        sortedList = sortList(requestForQuantumSearch)
        sortedFileNames = ""
        for i in sortedList:
            sortedFileNames = sortedFileNames+("<tr><td>"+str(i[0])+"</td></tr>")

        toRender = toRender+"<script>document.getElementById('userRequest').innerHTML = 'You Searched: "+str(requestForQuantumSearch)+"';       \
                                    document.getElementById('filesToSort').innerHTML = ' <thead> \
                                                                                            <tr> \
                                                                                            <th>Sorted by Similarity</th> \
                                                                                            </tr> \
                                                                                            </thead> \
                                                                                            <tbody>"+sortedFileNames+"\
                                                                                            </tbody>\
                                                                                            ';</script>"         


        

    return toRender+"</html>"



# Luv u geeksforgeeks
# https://www.geeksforgeeks.org/python/how-to-use-web-forms-in-a-flask-application/

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)