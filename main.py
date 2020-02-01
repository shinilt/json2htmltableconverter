from flask import Flask
from flask import request
import json2table
import json

app = Flask(__name__)

@app.route("/")
def home():
    return "Der Service läuft gut- vielen Dank - $#!5!|"
    
@app.route("/generatetable",methods=['GET', 'POST'])
def generatetable():
# make sure data is sent to data
    data='{"Message": "Hi there, we didnt get your message","ResponseStatus": "Waiting"}'
    data = request.json
    infoFromJson = data #since the data is json itself, we dont need to convert string to json
    #json.loads(data)
    

    build_direction = "LEFT_TO_RIGHT"
    table_attributes = {"style": "width:100%", "border":1,"border-collapse": "collapse"}
    jango=json2table.convert(infoFromJson, build_direction=build_direction, table_attributes=table_attributes)
    print(jango)
    return jango
    
if __name__ == "__main__":
    app.run(debug=True)