import streamlit as st
import pandas as pd
import os
import sys


# --------------------------------------------------
# PROJECT PATH
# --------------------------------------------------

BASE_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

SRC_DIR = os.path.join(
    BASE_DIR,
    "src"
)

sys.path.append(SRC_DIR)


# --------------------------------------------------
# IMPORT NLP COMPONENTS
# --------------------------------------------------

from sentiment_model import analyze_sentiment
from decision_engine import make_decision


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="NLP Financial Decision System",
    page_icon="📊",
    layout="wide"
)


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("📊 NLP Financial Decision System")

st.markdown(
    """
    **AI-powered financial text analysis and decision support system**

    Analyze financial news using Natural Language Processing,
    sentiment analysis and decision intelligence.
    """
)

st.divider()


# ==================================================
# LIVE TEXT ANALYSIS
# ==================================================

st.header("🔍 Analyze Financial Text")

text = st.text_area(
    "Enter financial news, company announcement or market statement:",
    height=180,
    placeholder=(
        "Example: The company reported strong quarterly earnings "
        "and expects revenue to increase significantly next year."
    )
)


if st.button(
    "Analyze Text",
    type="primary",
    use_container_width=True
):

    if not text.strip():

        st.warning(
            "Please enter some financial text first."
        )

    else:

        with st.spinner(
            "Running NLP analysis..."
        ):

            # Sentiment
            sentiment = analyze_sentiment(text)

            # Decision
            decision = make_decision(
                sentiment["label"],
                sentiment["score"]
            )

        st.success(
            "Analysis completed successfully."
        )

        st.divider()

        # ------------------------------------------
        # RESULTS
        # ------------------------------------------

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Sentiment",
                sentiment["label"].upper()
            )

        with col2:

            st.metric(
                "Confidence",
                f"{sentiment['score']:.2%}"
            )

        with col3:

            st.metric(
                "Decision",
                decision["decision"]
            )

        st.divider()

        # ------------------------------------------
        # DECISION SCORE
        # ------------------------------------------

        st.subheader("Decision Score")

        st.progress(
            min(
                max(
                    (decision["decision_score"] + 1) / 2,
                    0.0
                ),
                1.0
            )
        )

        st.write(
            f"Decision Score: "
            f"**{decision['decision_score']:.4f}**"
        )

        # ------------------------------------------
        # SIGNAL
        # ------------------------------------------

        if decision["decision"] in [
            "STRONG BUY",
            "BUY"
        ]:

            st.success(
                f"📈 Signal: **{decision['decision']}**"
            )

        elif decision["decision"] in [
            "STRONG SELL",
            "SELL"
        ]:

            st.error(
                f"📉 Signal: **{decision['decision']}**"
            )

        else:

            st.warning(
                "⏸️ Signal: **HOLD**"
            )

        st.divider()

        # ------------------------------------------
        # ORIGINAL TEXT
        # ------------------------------------------

        st.subheader("Analyzed Text")

        st.write(text)


# ==================================================
# HISTORICAL DATA
# ==================================================

st.divider()

st.header("📈 Historical Financial News Analysis")


RESULTS_FILE = os.path.join(
    BASE_DIR,
    "outputs",
    "results.csv"
)


if os.path.exists(RESULTS_FILE):

    df = pd.read_csv(
        RESULTS_FILE
    )

    # ------------------------------------------
    # SUMMARY METRICS
    # ------------------------------------------

    total_articles = len(df)

    positive_articles = len(
        df[df["sentiment"] == "positive"]
    )

    negative_articles = len(
        df[df["sentiment"] == "negative"]
    )

    neutral_articles = len(
        df[df["sentiment"] == "neutral"]
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "Total Articles",
            total_articles
        )

    with col2:

        st.metric(
            "Positive",
            positive_articles
        )

    with col3:

        st.metric(
            "Negative",
            negative_articles
        )

    with col4:

        st.metric(
            "Neutral",
            neutral_articles
        )

    st.divider()

    # ------------------------------------------
    # SENTIMENT CHART
    # ------------------------------------------

    st.subheader(
        "Sentiment Distribution"
    )

    sentiment_counts = (
        df["sentiment"]
        .value_counts()
    )

    st.bar_chart(
        sentiment_counts
    )

    # ------------------------------------------
    # DECISION CHART
    # ------------------------------------------

    st.subheader(
        "Decision Distribution"
    )

    decision_counts = (
        df["decision"]
        .value_counts()
    )

    st.bar_chart(
        decision_counts
    )

    # ------------------------------------------
    # RESULTS TABLE
    # ------------------------------------------

    st.subheader(
        "Analyzed Financial News"
    )

    display_columns = [
        "title",
        "sentiment",
        "sentiment_score",
        "decision",
        "decision_score",
        "entities"
    ]

    available_columns = [
        column
        for column in display_columns
        if column in df.columns
    ]

    st.dataframe(
        df[available_columns],
        use_container_width=True,
        height=500
    )

else:

    st.info(
        "No results found. "
        "Run `python src/main.py` first."
    )


# ==================================================
# FOOTER
# ==================================================

st.divider()

st.caption(
    "NLP Financial Decision System | "
    "Academic Project | "
    "Decision signals are for educational purposes only."
)