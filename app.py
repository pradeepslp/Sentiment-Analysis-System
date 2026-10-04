import streamlit as st
from textblob import TextBlob

# Set page configuration
st.set_page_config(
    page_title="Sentiment Analysis System",
    page_icon="💬",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for clean and modern styling
st.markdown("""
<style>
    /* Main container styling */
    .main-header {
        text-align: center;
        margin-bottom: 2rem;
    }
    .main-title {
        font-size: 2.3rem;
        font-weight: 700;
        color: #1e293b;
        margin-bottom: 0.25rem;
    }
    .main-subtitle {
        font-size: 1rem;
        color: #64748b;
        margin-bottom: 1.5rem;
    }
    
    /* Sentiment Result Card */
    .result-card {
        padding: 1.5rem;
        border-radius: 12px;
        margin-top: 1.5rem;
        margin-bottom: 1.5rem;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
        background-color: #ffffff;
        text-align: center;
    }
    
    .badge-positive {
        background-color: #dcfce7;
        color: #15803d;
        border: 1px solid #86efac;
    }
    .badge-negative {
        background-color: #fee2e2;
        color: #b91c1c;
        border: 1px solid #fca5a5;
    }
    .badge-neutral {
        background-color: #f1f5f9;
        color: #475569;
        border: 1px solid #cbd5e1;
    }

    .sentiment-badge {
        display: inline-block;
        padding: 0.5rem 1.5rem;
        font-size: 1.4rem;
        font-weight: 700;
        border-radius: 9999px;
        margin-bottom: 0.75rem;
    }
    
    .score-text {
        font-size: 1.1rem;
        color: #334155;
        font-weight: 500;
    }
    
    .info-box {
        background-color: #f8fafc;
        border-radius: 8px;
        padding: 1rem;
        font-size: 0.9rem;
        color: #64748b;
        border: 1px solid #e2e8f0;
        margin-top: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# App Header
st.markdown("""
<div class="main-header">
    <div class="main-title">💬 Sentiment Analysis System</div>
    <div class="main-subtitle">Analyze sentence sentiment using Natural Language Processing (TextBlob)</div>
</div>
""", unsafe_allow_html=True)

# Sample sentences for quick testing
st.markdown("**Try a sample sentence:**")
sample_cols = st.columns(3)
sample_text = ""

with sample_cols[0]:
    if st.button("🌟 Positive Example", use_container_width=True):
        st.session_state["input_text"] = "The customer service was exceptional and the team was extremely helpful!"

with sample_cols[1]:
    if st.button("😐 Neutral Example", use_container_width=True):
        st.session_state["input_text"] = "The product arrived on Tuesday as scheduled in a standard package."

with sample_cols[2]:
    if st.button("⚠️ Negative Example", use_container_width=True):
        st.session_state["input_text"] = "The software is frustrating to use, full of bugs, and keeps crashing."

# Initialize session state for text input if not present
if "input_text" not in st.session_state:
    st.session_state["input_text"] = ""

# Text Input Area
user_input = st.text_area(
    label="**Enter a sentence or paragraph to analyze:**",
    value=st.session_state.get("input_text", ""),
    placeholder="Type or paste your text here (e.g., 'I really enjoyed using this application, it works smoothly!')...",
    height=130,
    key="user_text_input"
)

# Keep session state updated when user types
st.session_state["input_text"] = user_input

# Action Buttons
col_btn1, col_btn2 = st.columns([3, 1])

with col_btn1:
    analyze_btn = st.button("🔍 Analyze Sentiment", type="primary", use_container_width=True)

with col_btn2:
    if st.button("🗑️ Clear", use_container_width=True):
        st.session_state["input_text"] = ""
        st.rerun()

# Processing Logic
if analyze_btn:
    cleaned_input = user_input.strip()
    
    # Handle empty input
    if not cleaned_input:
        st.warning("⚠️ Please enter a sentence or text before clicking **Analyze Sentiment**.")
    else:
        # Perform Sentiment Analysis using TextBlob
        blob = TextBlob(cleaned_input)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity
        
        # Classification logic based on polarity score
        if polarity > 0.0:
            sentiment_label = "Positive"
            badge_class = "badge-positive"
            emoji_icon = "😊"
            summary_desc = "The text conveys an overall positive and favorable tone."
        elif polarity < 0.0:
            sentiment_label = "Negative"
            badge_class = "badge-negative"
            emoji_icon = "😞"
            summary_desc = "The text conveys an overall negative or critical tone."
        else:
            sentiment_label = "Neutral"
            badge_class = "badge-neutral"
            emoji_icon = "😐"
            summary_desc = "The text conveys a neutral tone with balanced or factual statements."
            
        # Display Result Card
        st.markdown(f"""
        <div class="result-card">
            <div class="sentiment-badge {badge_class}">
                {emoji_icon} {sentiment_label}
            </div>
            <div class="score-text">
                <strong>Polarity Score:</strong> <code>{polarity:.2f}</code>
            </div>
            <div style="margin-top: 0.5rem; color: #475569; font-size: 0.95rem;">
                {summary_desc}
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Metric Columns
        metric_col1, metric_col2, metric_col3 = st.columns(3)
        with metric_col1:
            st.metric(label="Sentiment", value=sentiment_label)
        with metric_col2:
            st.metric(label="Polarity (-1.0 to +1.0)", value=f"{polarity:+.2f}")
        with metric_col3:
            st.metric(label="Subjectivity (0.0 to 1.0)", value=f"{subjectivity:.2f}")

        # Polarity Scale Visualization
        st.markdown("##### 📊 Polarity Scale Indicator")
        # Normalize polarity (-1 to 1) to progress percentage (0.0 to 1.0)
        normalized_polarity = (polarity + 1.0) / 2.0
        st.progress(normalized_polarity)
        
        scale_cols = st.columns([1, 1, 1])
        scale_cols[0].caption("🔴 Negative (-1.0)")
        scale_cols[1].markdown("<p style='text-align: center; color: #64748b; font-size: 0.8rem;'>⚪ Neutral (0.0)</p>", unsafe_allow_html=True)
        scale_cols[2].markdown("<p style='text-align: right; color: #64748b; font-size: 0.8rem;'>🟢 Positive (+1.0)</p>", unsafe_allow_html=True)

# Footer Info
st.markdown("---")
st.markdown("""
<div class="info-box">
    <strong>💡 How it works:</strong>
    <ul style="margin-top: 0.5rem; margin-bottom: 0;">
        <li><strong>Polarity:</strong> Measures sentiment from <code>-1.0</code> (extremely negative) to <code>+1.0</code> (extremely positive). <code>0.0</code> is neutral.</li>
        <li><strong>Subjectivity:</strong> Measures opinion/feeling (<code>1.0</code>) vs factual information (<code>0.0</code>).</li>
    </ul>
</div>
""", unsafe_allow_html=True)
