from flask import Flask, request, jsonify
import pandas as pd
from flask import jsonify
app=Flask(__name__)

def grant(hours):
    amount = 0
    print("covid grant calculator called")
    if hours <= 20:  #2 Lakh 50 thousand
        amount = amount + 500
        print("hours lost is less than 20")

    else:
        amount = amount + 750
        print("hours lost is equal or more than 20")

    print( amount, "AUD is paid!")

    return hours



@app.route("/calc", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        data = request.get_json()
        
        df= pd.DataFrame(data["data"])
        print(df)
        l = list(df["CREDIT"].values)


        hours = sum(l)

        hour1 = grant(hours)
        print("Grant amount is :" ,hour1, "AUD")
        d = {
        "hours lost" : float(hours),
        "Amount" : float(hour1)
        }
        return jsonify(d)



if __name__ == "__main__":
    app.run()
