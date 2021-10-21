from flask import Flask, request, jsonify
import pandas as pd
from flask import jsonify
app=Flask(__name__)




@app.route("/calc", methods=['GET', 'POST'])
def calculator():

    if request.method == 'POST':

        data = request.get_json()

        df= pd.DataFrame(data["data"])

        print(df)

        l1= list(df["CREDIT"].values)

        l2 = list(df["HOURS"].values)

        l1  = sum(l1)
        l2 = sum(l2)


        print("Grant amount is :" ,l1, "AUD")

        d = {
        "hours lost" : float(l2),
        "Amount" : float(l1)
        }
        return jsonify(d)
    else :
        return None



if __name__ == "__main__":
    app.run()
