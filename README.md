# Teen Phone Addiction – ML + API (FastAPI)

A simple machine learning project that predicts the **probability of phone addiction** in teenagers. It follows a training approach (RandomForest) and exposes a **FastAPI** endpoint to score new records.

---

## Project Structure

```
my-ml/
├─ data/
│  └─ teen_phone_addiction_dataset.csv
├─ model/
│  ├─ train.py
│  ├─ teen-addiction-v1.joblib
│  └─ teen-addiction-features.json
├─ app.py
├─ client.py
├─ requirements.txt
└─ Dockerfile
```

---

## Setup

```bash
python -m venv ml-env
source ml-env/bin/activate
pip install -r requirements.txt
```

---

## Train the Model

```bash
python model/train.py
```

Expected output:

- Validation metrics in the console
    
- Saved model at `model/teen-addiction-v1.joblib`
    
- Saved feature columns at `model/teen-addiction-features.json`
    

---

## Run the API

```bash
uvicorn app:app --reload --port 8000
```

### Endpoint

```
POST /score
```

**Response**

```json
{ "score": 0.73 }
```

Where `score` is the predicted probability of addiction.

---

## Example Request

### CURL

```bash
curl -X POST "http://127.0.0.1:8000/score" \
  -H "Content-Type: application/json" \
  -d '{
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
  }'
```

### Python Client

```bash
python client.py
```

---

## Requirements

See `requirements.txt`.  
Recommended Python: **3.8**.

---

## Dataset

**Citation (APA):**
Sumedh1507. (n.d.). *Teen Phone Addiction* \[Data set]. Kaggle. Retrieved September 15, 2025, from [https://www.kaggle.com/datasets/sumedh1507/teen-phone-addiction](https://www.kaggle.com/datasets/sumedh1507/teen-phone-addiction)

**Methodology (as reported by the author):**

* **Survey-based collection:** data gathered via structured questionnaires from high-school and early-college students (ages 13–21).
* **Voluntary & anonymous:** participation was voluntary; all identifying details were excluded to protect privacy.
* **Time window:** collected over a 3-month period across several urban and semi-urban schools.
* **Consent:** all participants (or their guardians) provided consent for anonymous research use.
