#  Customer Churn AI Agent

A multi-agent AI application that predicts customer churn using Machine Learning and LangGraph.

##  Project Overview

This project predicts whether a customer is likely to churn based on their profile and purchasing behavior.

The application uses:

- Machine Learning (Random Forest, Decision Tree, Logistic Regression)
- LangGraph Multi-Agent Architecture
- Python
- Pandas
- Scikit-learn

The AI system not only predicts churn but also explains the prediction, assigns a priority level, and recommends customer retention strategies.

---

##  Features

- Customer churn prediction
- Data preprocessing
- Machine Learning model training
- Random Forest feature importance
- Multi-agent workflow using LangGraph
- Risk Analysis Agent
- Explanation Agent
- Priority Agent
- Strategy Recommendation Agent

---

##  Project Structure

```text
customer_churn_agent/
│
├── agents/
│   ├── explanation_agent.py
│   ├── priority_agent.py
│   ├── risk_agent.py
│   └── strategy_agent.py
│
├── data/
│   └── customer_churn_data.csv
│
├── graphs/
│   ├── state.py
│   └── supervisor.py
│
├── ml/
│   ├── preprocess.py
│   ├── train_model.py
│   ├── predict.py
│   └── churn_model.pkl
│
├── prompts/
├── scripts/
├── utils/
│
├── app.py
├── requirements.txt
└── README.md
```

---

##  Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- LangGraph

---

##  Machine Learning Models

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier

The Random Forest model is used for customer churn prediction.

---

##  AI Agents

### Risk Agent

Predicts whether a customer will churn.

### Explanation Agent

Explains the possible reasons for the prediction.

### Priority Agent

Assigns a priority level based on churn risk.

### Strategy Agent

Suggests retention strategies for the customer.

---

## ▶ How to Run

### Clone the repository

```bash
git clone https://github.com/your-username/customer_churn_agent.git
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Train the model

```bash
python ml/train_model.py
```

### Run the application

```bash
python app.py
```

---

##  Sample Output

```text
Prediction : No Churn
Confidence : 99.0%

Priority : Low

Explanation
- Low customer satisfaction
- Customer has not purchased recently
- Customer rarely uses the application
- Customer has raised many support tickets

Recommended Strategy
- Continue regular engagement
- Send personalized offers occasionally
- Reward customer loyalty
```

---

##  Future Improvements

- Streamlit Web Application
- SHAP-based model explanations
- Database integration
- REST API using FastAPI
- Real customer dataset support

---

##  Author

**Niharika Savu**

GitHub: https://github.com/savuniharika