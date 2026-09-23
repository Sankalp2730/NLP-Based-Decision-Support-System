# 📊 NLP Financial Decision System

An AI-powered **Natural Language Processing (NLP) Financial Decision Support System** that analyzes financial news and generates data-driven **BUY, HOLD, SELL, STRONG BUY, or STRONG SELL** signals.

The system combines **financial sentiment analysis, Named Entity Recognition (NER), topic modeling, financial keyword analysis, and a decision-scoring engine** to transform unstructured financial news into structured decision-support information.

> **Note:** This project is an academic decision-support system. Its generated BUY/SELL signals are not financial advice and should not be used as a substitute for professional investment advice.

---

# 1. 📌 Project Overview

Financial markets generate enormous amounts of textual information every day through:

* Financial news
* Company announcements
* Earnings reports
* Economic reports
* Market updates
* Analyst commentary
* Business and technology news

Manually analyzing all this information is time-consuming.

This project addresses the problem by using NLP and transformer-based models to automatically analyze financial text and generate an interpretable decision signal.

The system follows this pipeline:

```text
Financial News
      ↓
Data Collection
      ↓
Text Preprocessing
      ↓
FinBERT Sentiment Analysis
      ↓
Named Entity Recognition
      ↓
Financial Keyword Analysis
      ↓
Topic Modeling
      ↓
Decision Scoring Engine
      ↓
BUY / HOLD / SELL Signal
      ↓
Streamlit Dashboard
```

---

# 2. 🎯 Problem Statement

Financial decision-making requires processing large volumes of unstructured textual information.

Traditional approaches require investors or analysts to manually read and interpret financial news, which can be:

* Time-consuming
* Subjective
* Difficult to scale
* Prone to information overload

The objective of this project is to develop an NLP-based system that automatically extracts useful information from financial news and provides an interpretable decision-support signal.

---

# 3. 🎯 Objectives

The major objectives of this project are:

1. Collect financial news automatically.
2. Clean and preprocess the collected text.
3. Analyze financial sentiment using FinBERT.
4. Identify important entities using Named Entity Recognition.
5. Discover major themes using topic modeling.
6. Identify positive and negative financial indicators.
7. Combine NLP signals into a decision score.
8. Generate BUY, HOLD, and SELL signals.
9. Provide explanations for generated decisions.
10. Evaluate the sentiment-analysis component.
11. Present results through an interactive Streamlit dashboard.

---

# 4. 🧠 Technologies Used

| Technology                    | Purpose                      |
| ----------------------------- | ---------------------------- |
| Python                        | Core programming language    |
| Pandas                        | Data processing              |
| NumPy                         | Numerical operations         |
| Scikit-learn                  | TF-IDF, NMF and evaluation   |
| Transformers                  | Transformer-based NLP models |
| PyTorch                       | Deep-learning backend        |
| FinBERT                       | Financial sentiment analysis |
| BERT NER                      | Named Entity Recognition     |
| Streamlit                     | Interactive dashboard        |
| Hugging Face                  | Pre-trained NLP models       |
| Matplotlib / Streamlit charts | Visualization                |
| CSV                           | Data storage                 |

---

# 5. 🤖 NLP Models

## 5.1 FinBERT

The project uses:

```text
ProsusAI/finbert
```

FinBERT is designed specifically for financial language and classifies financial text into:

```text
Positive
Negative
Neutral
```

Example:

```text
"The company reported record profits and strong revenue growth."
```

Possible output:

```text
Sentiment: Positive
Confidence: 0.95
```

---

# 6. 🔍 Named Entity Recognition

The project uses:

```text
dslim/bert-base-NER
```

NER identifies important entities in text.

Examples include:

```text
Microsoft → ORG
India → LOC
Person names → PER
```

The identified entities provide additional context about the financial news.

---

# 7. 📚 Topic Modeling

Topic modeling is performed using:

```text
TF-IDF
+
NMF (Non-negative Matrix Factorization)
```

The system identifies major themes from the collected financial articles.

Possible topics include:

* Stock markets
* Banking
* Technology
* Economy
* Investments
* Corporate earnings

The exact topics are automatically discovered from the collected dataset.

---

# 8. 🧹 Data Preprocessing

The preprocessing pipeline performs:

1. HTML removal
2. URL removal
3. Lowercase conversion
4. Special-character removal
5. Whitespace normalization
6. Empty-text removal
7. Duplicate removal

The cleaned dataset is stored in:

```text
data/processed/finance_news_clean.csv
```

---

# 9. 📥 Data Collection

The data collection component collects financial news based on multiple search topics, including:

```text
Stock Market
Indian Economy
Technology Stocks
Banking Finance
Global Economy
```

The raw data is stored in:

```text
data/raw/
```

The collected information is then passed to the preprocessing stage.

---

# 10. ⚙️ System Architecture

The overall architecture is:

```text
                 ┌──────────────────────┐
                 │   Financial News     │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │  Data Collection    │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │ Text Preprocessing   │
                 └──────────┬───────────┘
                            │
              ┌─────────────┼─────────────┐
              │             │             │
              ▼             ▼             ▼
        ┌──────────┐  ┌──────────┐  ┌──────────────┐
        │ FinBERT  │  │   NER    │  │ Topic Model  │
        │Sentiment │  │ Entities │  │    NMF       │
        └────┬─────┘  └────┬─────┘  └──────┬───────┘
             │             │               │
             └─────────────┼───────────────┘
                           │
                           ▼
                 ┌──────────────────────┐
                 │ Financial Keywords   │
                 │     Analysis         │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │ Decision Engine      │
                 └──────────┬───────────┘
                            │
                            ▼
               ┌─────────────────────────┐
               │ Decision Score          │
               │                         │
               │ STRONG BUY              │
               │ BUY                     │
               │ HOLD                    │
               │ SELL                    │
               │ STRONG SELL             │
               └───────────┬─────────────┘
                           │
                           ▼
                 ┌──────────────────────┐
                 │ Streamlit Dashboard  │
                 └──────────────────────┘
```

---

# 11. 📊 Decision Engine

The decision engine combines several NLP signals.

## Sentiment Component

Positive sentiment contributes a positive score.

Negative sentiment contributes a negative score.

Neutral sentiment contributes approximately zero.

## Entity Component

The number of detected entities provides additional context about how specific the financial article is.

## Financial Keyword Component

The system checks for positive and negative financial indicators.

### Positive indicators

Examples:

```text
growth
profit
revenue increase
strong earnings
investment
expansion
surge
rally
gain
bullish
strong performance
```

### Negative indicators

Examples:

```text
loss
decline
fall
drop
weak demand
debt
risk
crisis
recession
downgrade
bearish
higher costs
```

---

# 12. 🧮 Decision Score

The enhanced decision engine uses a weighted combination of NLP signals.

Conceptually:

```text
Decision Score =
    70% Sentiment
  + 20% Financial Keyword Signal
  + 10% Entity Signal
```

The final score is constrained between:

```text
-1 and +1
```

Decision thresholds:

```text
Score >= 0.60
        ↓
   STRONG BUY

Score >= 0.20
        ↓
      BUY

-0.20 < Score < 0.20
        ↓
      HOLD

Score <= -0.20
        ↓
      SELL

Score <= -0.60
        ↓
  STRONG SELL
```

---

# 13. 💡 Decision Explanation

The system also generates an explanation for every decision.

Example:

```text
The NLP system detected positive sentiment with
92% confidence. It identified 5 financial entities,
4 positive financial indicators and 0 negative
financial indicators. Based on the combined NLP
signals, the system generated a STRONG BUY decision.
```

This makes the system more interpretable than a simple black-box classification model.

---

# 14. 📁 Project Structure

```text
NLP Decision System/
│
├── dashboard/
│   └── app.py
│
├── data/
│   ├── raw/
│   │   └── finance_news.csv
│   │
│   ├── processed/
│   │   └── finance_news_clean.csv
│   │
│   └── evaluation/
│       └── sentiment_test.csv
│
├── notebooks/
│   └── experiments.ipynb
│
├── outputs/
│   ├── results.csv
│   └── evaluation_results.csv
│
├── src/
│   ├── data_collection.py
│   ├── preprocessing.py
│   ├── sentiment_model.py
│   ├── ner_model.py
│   ├── topic_model.py
│   ├── decision_engine.py
│   ├── evaluate_model.py
│   └── main.py
│
└── README.md
```

---

# 15. 🧩 Description of Source Files

## `data_collection.py`

Collects financial news and saves raw data.

Run:

```bash
python src/data_collection.py
```

---

## `preprocessing.py`

Cleans the collected financial news.

Run:

```bash
python src/preprocessing.py
```

---

## `sentiment_model.py`

Loads FinBERT and performs financial sentiment analysis.

Run:

```bash
python src/sentiment_model.py
```

---

## `ner_model.py`

Performs Named Entity Recognition.

Run:

```bash
python src/ner_model.py
```

---

## `topic_model.py`

Discovers major topics using TF-IDF and NMF.

Run:

```bash
python src/topic_model.py
```

---

## `decision_engine.py`

Combines sentiment, entity information and financial keywords to generate decision scores.

Run:

```bash
python src/decision_engine.py
```

---

## `main.py`

Runs the complete NLP processing pipeline.

Run:

```bash
python src/main.py
```

---

## `evaluate_model.py`

Evaluates FinBERT using a labeled financial-text evaluation dataset.

Run:

```bash
python src/evaluate_model.py
```

---

## `dashboard/app.py`

Runs the Streamlit interface.

Run:

```bash
python -m streamlit run dashboard/app.py
```

---

# 16. 🚀 Installation

## Step 1 — Clone or download the project

Open a terminal inside the project directory.

Example:

```text
D:\NLP Decision System
```

---

## Step 2 — Install dependencies

Run:

```bash
python -m pip install pandas numpy scikit-learn transformers torch streamlit
```

If additional packages are used by the data collection component, install those as required.

---

# 17. ▶️ Running the Project

Run the components in this order.

### Step 1 — Collect data

```bash
python src/data_collection.py
```

---

### Step 2 — Preprocess data

```bash
python src/preprocessing.py
```

---

### Step 3 — Test FinBERT

```bash
python src/sentiment_model.py
```

The first run downloads the FinBERT model.

---

### Step 4 — Test NER

```bash
python src/ner_model.py
```

The first run downloads the NER model.

---

### Step 5 — Test topic modeling

```bash
python src/topic_model.py
```

---

### Step 6 — Test decision engine

```bash
python src/decision_engine.py
```

---

### Step 7 — Run complete pipeline

```bash
python src/main.py
```

This generates:

```text
outputs/results.csv
```

---

### Step 8 — Evaluate FinBERT

```bash
python src/evaluate_model.py
```

This generates:

```text
outputs/evaluation_results.csv
```

---

### Step 9 — Launch dashboard

```bash
python -m streamlit run dashboard/app.py
```

The application will normally be available locally at:

```text
http://localhost:8501
```

---

# 18. 📊 Output Dataset

The main output file is:

```text
outputs/results.csv
```

Important columns include:

| Column                | Description                 |
| --------------------- | --------------------------- |
| `title`               | Financial news title        |
| `published`           | Publication date/time       |
| `source_query`        | Search category             |
| `sentiment`           | Positive/Negative/Neutral   |
| `sentiment_score`     | FinBERT confidence          |
| `entities_count`      | Number of detected entities |
| `entities`            | Detected entities           |
| `positive_indicators` | Positive financial keywords |
| `negative_indicators` | Negative financial keywords |
| `decision`            | BUY/HOLD/SELL signal        |
| `decision_score`      | Combined NLP score          |
| `explanation`         | Decision explanation        |

---

# 19. 📈 Evaluation

The sentiment component is evaluated using a manually labeled financial-text test dataset.

The evaluation includes:

* Accuracy
* Precision
* Recall
* F1-score
* Classification report
* Confusion matrix

The evaluation results are stored in:

```text
outputs/evaluation_results.csv
```

### Important Evaluation Note

The sentiment model evaluation and the investment decision signal are two different things.

FinBERT can be evaluated against labeled sentiment:

```text
Actual Sentiment
       ↓
FinBERT
       ↓
Predicted Sentiment
```

However, the BUY/SELL decision engine is a **rule-based decision-support component**, and its signals should not be described as proven stock-price predictions unless they are evaluated against an appropriate market outcome dataset.

---

# 20. 🖥️ Streamlit Dashboard

The dashboard provides an interactive interface for the system.

The dashboard is designed to provide:

### Live Text Analysis

Users can enter financial news manually.

The system returns:

```text
Sentiment
Confidence
Decision
Decision Score
Explanation
```

### Historical Analysis

The dashboard can display:

* Total articles
* Positive articles
* Negative articles
* Neutral articles
* Sentiment distribution
* Decision distribution
* Article-level analysis

---

# 21. 🧪 Example Input

Example positive financial statement:

```text
The company reported record quarterly revenue,
strong profit growth and expects demand to remain
robust over the next year.
```

Possible output:

```text
Sentiment: POSITIVE

Confidence: High

Decision: BUY / STRONG BUY
```

Example negative statement:

```text
The company reported a significant decline in revenue
and expects continued weakness due to falling demand
and higher operating costs.
```

Possible output:

```text
Sentiment: NEGATIVE

Confidence: High

Decision: SELL / STRONG SELL
```

The exact result depends on the NLP model output and decision-engine signals.

---

# 22. 🔐 Model Downloads

The first execution of the transformer models may download several hundred megabytes of model files.

The project uses:

```text
ProsusAI/finbert
```

and:

```text
dslim/bert-base-NER
```

Once downloaded, the models are cached locally by Hugging Face.

Internet access may therefore be required during the first model execution.

---

# 23. ⚠️ Limitations

The project has several important limitations.

### 1. Sentiment is not the same as price prediction

Positive financial news does not guarantee that a stock price will rise.

Similarly, negative sentiment does not guarantee a price decline.

---

### 2. Decision engine is rule-based

The current decision engine uses predefined weights and thresholds.

It is a decision-support mechanism rather than a trained stock-price prediction model.

---

### 3. Limited evaluation dataset

The sentiment evaluation dataset is relatively small.

A larger expert-labeled dataset would provide a more reliable evaluation.

---

### 4. No historical price integration

The current system primarily analyzes textual financial information.

It does not yet incorporate:

* Stock prices
* Trading volume
* Technical indicators
* Moving averages
* Market volatility
* Historical returns

---

### 5. Entity count is only a supporting signal

The number of detected entities does not inherently indicate whether an investment is good or bad.

It is included as a contextual feature in the current decision framework.

---

### 6. News source limitations

The quality and diversity of the decision depend on the financial news collected by the data-collection component.

---

# 24. 🔮 Future Scope

The project can be significantly extended.

## 1. Stock Price Integration

Integrate historical stock-market data.

Potential features:

```text
Open
High
Low
Close
Volume
Returns
Moving Average
RSI
MACD
Volatility
```

---

## 2. Machine Learning Decision Model

Instead of fixed rules, train a supervised model using:

```text
Sentiment
Entity information
Topic
Stock indicators
Historical returns
Volume
Market conditions
```

Possible algorithms:

* Logistic Regression
* Random Forest
* XGBoost
* LightGBM
* Neural Networks

---

## 3. Multimodal Financial Intelligence

Combine:

```text
News
+
Stock Prices
+
Financial Reports
+
Social Media
+
Economic Indicators
```

to create a more comprehensive decision-support system.

---

## 4. Real-Time News Processing

The system could continuously monitor financial news and update decisions automatically.

---

## 5. Company-Specific Analysis

The system could allow users to select a company and view:

```text
Company
    ↓
Recent News
    ↓
Sentiment Trend
    ↓
Topics
    ↓
Entities
    ↓
Decision Trend
```

---

## 6. Historical Backtesting

Future versions can test whether generated signals historically correspond to subsequent market movements.

For example:

```text
News Date
    ↓
Generated BUY signal
    ↓
Observe next 1 / 5 / 10 trading days
    ↓
Calculate return
```

This would provide a much stronger evaluation of the decision engine.

---

# 25. 🎓 Academic Significance

This project demonstrates the practical application of multiple NLP techniques in a financial domain.

It combines:

```text
Natural Language Processing
        +
Transformer Models
        +
Information Extraction
        +
Topic Modeling
        +
Decision Intelligence
        +
Data Visualization
```

The project therefore demonstrates an end-to-end AI pipeline rather than implementing only a single NLP algorithm.

---

# 26. 📌 Key Contributions

The major contributions of this project are:

1. Automated financial-news collection.
2. Domain-specific sentiment analysis using FinBERT.
3. Financial information extraction using NER.
4. Automatic topic discovery.
5. Financial keyword analysis.
6. Multi-factor decision scoring.
7. Explainable decision generation.
8. Model evaluation framework.
9. Interactive Streamlit dashboard.
10. End-to-end NLP decision-support pipeline.

---

# 27. 🏁 Conclusion

The **NLP Financial Decision System** demonstrates how modern NLP techniques can transform unstructured financial news into structured, interpretable information.

The system combines financial sentiment analysis, Named Entity Recognition, topic modeling and financial keyword analysis to produce a decision-support score.

The resulting system can automatically process large amounts of financial text and provide users with:

```text
Sentiment
+
Confidence
+
Entities
+
Financial Indicators
+
Decision Score
+
Decision Explanation
```

The current system serves as a strong foundation for future development involving historical stock prices, machine-learning-based prediction, real-time data streams and financial backtesting.

---

# 28. 👨‍💻 Project Status

### Current implementation

```text
✅ Data Collection
✅ Data Preprocessing
✅ FinBERT Sentiment Analysis
✅ Named Entity Recognition
✅ Topic Modeling
✅ Financial Keyword Analysis
✅ Enhanced Decision Engine
✅ Decision Explanations
✅ End-to-End Pipeline
✅ Results CSV
✅ Sentiment Evaluation
✅ Evaluation Metrics
✅ Streamlit Dashboard
```

### Future enhancements

```text
⬜ Stock-price integration
⬜ Historical backtesting
⬜ Supervised BUY/SELL prediction
⬜ Real-time news monitoring
⬜ Company-specific dashboards
⬜ Advanced financial forecasting
```

---

# 29. ⚠️ Disclaimer

This project is developed for **academic and educational purposes**.

The BUY, HOLD, SELL, STRONG BUY and STRONG SELL outputs are generated by an NLP-based decision-support system and **should not be considered financial advice, investment recommendations, or guaranteed predictions of future stock prices**.

Investment decisions should be made using appropriate financial research and professional advice.

Execution Commands

cd "D:\NLP Decision System"

python src/data_collection.py

python src/preprocessing.py

python src/sentiment_model.py

python src/ner_model.py

python src/topic_model.py

python src/decision_engine.py

python src/main.py

python src/evaluate_model.py

python -m streamlit run dashboard/app.py


Testing 

Positive
The company reported record profits and strong revenue growth, while demand remained robust and management expects excellent performance next year.

Negative
The company reported a sharp decline in revenue and profits due to weak demand, rising costs and significant losses.

Neutral 
The company announced its quarterly financial results today, with revenue remaining broadly in line with market expectations.