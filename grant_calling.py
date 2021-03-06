import requests

{
    "data": [
  {
    "INDEX": 0,
    "DATE": "2021-07-11",
    "SOURCE NAME": "CENTRELINK",  
    "CREDIT": 750,
    "HOURS": 25,  
    "DEBIT": 0
  },
  {
    "INDEX": 1,
    "DATE": "2021-07-18",
    "SOURCE NAME": "CENTRELINK",
    "CREDIT": 750,
    "HOURS": 25,
    "DEBIT": 0
  },
  {
    "INDEX": 2,
    "DATE": "2021-07-25",
    "SOURCE NAME": "CENTRELINK",
    "CREDIT": 750,
    "HOURS": 25,
    "DEBIT": 0
  },
  {
    "INDEX": 3,
    "DATE": "2021-08-01",
    "SOURCE NAME": "CENTRELINK",
    "CREDIT": 750,
    "HOURS": 25,
    "DEBIT": 0
  },
  {
    "INDEX": 4,
    "DATE": "2021-08-08",
    "SOURCE NAME": "CENTRELINK",
    "CREDIT": 750,
    "HOURS": 25,
    "DEBIT": 0
  },
  {
    "INDEX": 5,
    "DATE": "2021-08-15",
    "SOURCE NAME": "CENTRELINK",
    "CREDIT": 750,
    "HOURS": 25,
    "DEBIT": 0
  },
  {
    "INDEX": 6,
    "DATE": "2021-08-22",
    "SOURCE NAME": "CENTRELINK",
    "CREDIT": 750,
    "HOURS": 25,
    "DEBIT": 0
  },
  {
    "INDEX": 7,
    "DATE": "2021-08-29",
    "SOURCE NAME": "CENTRELINK",
    "CREDIT": 750,
    "HOURS": 25,
    "DEBIT": 0
  },
  {
    "INDEX": 8,
    "DATE": "2021-09-05",
    "SOURCE NAME": "CENTRELINK",
    "CREDIT": 750,
    "HOURS": 25,
    "DEBIT": 0
  },
  {
    "INDEX": 9,
    "DATE": "2021-09-12",
    "SOURCE NAME": "CENTRELINK",
    "CREDIT": 750,
    "HOURS": 25,
    "DEBIT": 0
  },
  {
    "INDEX": 10,
    "DATE": "2021-09-19",
    "SOURCE NAME": "CENTRELINK",
    "CREDIT": 750,
    "HOURS": 25,
    "DEBIT": 0
  },
  {
    "INDEX": 11,
    "DATE": "2021-09-26",
    "SOURCE NAME": "CENTRELINK",
    "CREDIT": 750,
    "HOURS": 25,
    "DEBIT": 0
  },
  {
    "INDEX": 12,
    "DATE": "2021-10-03",
    "SOURCE NAME": "CENTRELINK",
    "CREDIT": 750,
    "HOURS": 25,
    "DEBIT": 0
  }
]
}
print(data)
print()
import pandas as pd
df = pd.DataFrame(data["data"])


print(df)

print()

res = requests.post(url = "https://grant2.herokuapp.com/calc", json = data)


print(res.json())
