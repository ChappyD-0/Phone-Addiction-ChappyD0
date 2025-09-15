import requests, json

URL = "http://127.0.0.1:8000/score"

payload = {
  "Age": 18,
  "Gender": "Female",
  "Location": "West Anthony",
  "School_Grade": "12th",
  "Daily_Usage_Hours": 3.1,
  "Sleep_Hours": 3.9,
  "Academic_Performance": 78,
  "Social_Interactions": 8,
  "Exercise_Hours": 1.6,
  "Anxiety_Level": 9,
  "Depression_Level": 10,
  "Self_Esteem": 3,
  "Parental_Control": 0,
  "Screen_Time_Before_Bed": 1.4,
  "Phone_Checks_Per_Day": 128,
  "Apps_Used_Daily": 7,
  "Time_on_Social_Media": 3.1,
  "Time_on_Gaming": 1.6,
  "Time_on_Education": 0.8,
  "Phone_Usage_Purpose": "Social Media",
  "Family_Communication": 8,
  "Weekend_Usage_Hours": 3.0
}

if __name__ == "__main__":
  r = requests.post(URL, json=payload, timeout=10)
  r.raise_for_status()
  print(json.dumps(r.json(), indent=2))
