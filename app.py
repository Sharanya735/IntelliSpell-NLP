import streamlit as st
from spellchecker import SpellChecker
import re
import pandas as pd

# --- CUSTOM LEVENSHTEIN DISTANCE FOR DEMONSTRATION ---
def levenshtein_distance(s1, s2):
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]

# --- UI CONFIGURATION ---
st.set_page_config(
    page_title="IntelliSpell NLP",
    page_icon="✨",
    layout="wide"
)

# Premium CSS for high-end look
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600&display=swap');

    /* Global Typography */
    html, body, [class*="css"] {
        font-family: 'Outfit', sans-serif;
    }

    /* Vibrant Gradient Background */
    .stApp {
        background: radial-gradient(circle at 50% 50%, #1a1c2c 0%, #0d0e14 100%);
        color: #ffffff;
    }

    /* Glassmorphism Logic */
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 25px;
        margin-bottom: 25px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        animation: fadeIn 0.8s ease-in-out;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Input area styling */
    .stTextArea textarea {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        color: white !important;
        border-radius: 12px !important;
        font-size: 1.1rem !important;
    }

    /* Highlights */
    .highlight {
        background-color: rgba(255, 75, 75, 0.15);
        color: #ff6e6e;
        padding: 3px 8px;
        border-radius: 8px;
        font-weight: 600;
        border-bottom: 2px solid #ff4b4b;
        margin: 0 2px;
    }
    
    .corrected {
        background-color: rgba(46, 204, 113, 0.15);
        color: #2ecc71;
        padding: 3px 8px;
        border-radius: 8px;
        font-weight: 600;
        border-bottom: 2px solid #2ecc71;
        margin: 0 2px;
    }

    /* Header Styling */
    h1 {
        font-weight: 600 !important;
        background: linear-gradient(90deg, #6a11cb 0%, #2575fc 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3.5rem !important;
        letter-spacing: -1px;
    }

    /* Metric Cards */
    div[data-testid="stMetricValue"] {
        font-family: 'Outfit', sans-serif !important;
        font-weight: 600 !important;
        color: #2575fc !important;
    }
    
    .footer {
        text-align: center;
        margin-top: 50px;
        color: rgba(255, 255, 255, 0.4);
        font-size: 0.9rem;
    }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: rgba(255, 255, 255, 0.02);
        border-right: 1px solid rgba(255, 255, 255, 0.05);
    }
    .sidebar-title {
        color: #2575fc;
        font-weight: 600;
        font-size: 1.5rem;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: METHODOLOGY ---
st.sidebar.markdown('<div class="sidebar-title">📚 Project Docs</div>', unsafe_allow_html=True)
st.sidebar.markdown("""
### NLP Concepts Used:
1. **Tokenization**: Breaking text into individual words.
2. **Levenshtein Distance**: Measuring how many edits (insert, delete, replace) are needed to change one word to another.
3. **Probabilistic Correction**: Using word frequency to suggest the most likely correction.
4. **Dictionary-based Lookup**: Comparing words against a known vocabulary.

### How it works:
- **Detection**: Words not in the English dictionary are flagged.
- **Suggestion**: The system finds words with small edit distances.
- **Ranking**: Suggestions are ranked based on their popularity/frequency in language.
""")

# --- MAIN PAGE ---
st.markdown('<h1 style="text-align: center; margin-bottom: 0;">✨ IntelliSpell NLP</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: rgba(255,255,255,0.6); margin-bottom: 40px;">Professional Grade Spell Rectifier & Language Tool</p>', unsafe_allow_html=True)

st.markdown('<h3 style="margin-top: 0;">✍️ Text Input</h3>', unsafe_allow_html=True)
user_input = st.text_area("", 
                         placeholder="Type your sentence here (e.g., I luv NLP but mine speling is bad...)",
                         height=150)

if user_input:
    # Initialize SpellChecker and add common abbreviations
    spell = SpellChecker()
    spell.word_frequency.load_words(['nlp', 'ai', 'ml'])
    # Boost the frequency of 'love' to ensure 'luv' -> 'love' (not 'lug')
    spell.word_frequency.add('love') 
    
    # Pre-processing
    words = re.findall(r"\w+|[^\w\s]", user_input, re.UNICODE)
    alnum_words = [w.lower() for w in words if w.isalnum()]
    misspelled_set = spell.unknown(alnum_words)
    
    # Process the words
    final_tokens = []
    corrections_log = []
    
    # Custom mapping for common slang/chat-speak (NLP best practice)
    slang_map = {
        "luv": "love",
        "u": "you",
        "r": "are",
        "n": "and",
        "wanna": "want to",
        "gonna": "going to"
    }
    
    for word in words:
        clean_word = word.lower()
        if clean_word in slang_map:
            best = slang_map[clean_word]
            # Handle capitalization
            if word[0].isupper():
                best = best.capitalize()
            final_tokens.append(f'<span class="corrected">{best}</span>')
            corrections_log.append({"Original": word, "Corrected": best, "Type": "Slang Mapping"})
        elif clean_word in misspelled_set:
            best = spell.correction(clean_word) or word
            # Handle capitalization
            if word[0].isupper():
                best = best.capitalize()
            
            final_tokens.append(f'<span class="corrected">{best}</span>')
            corrections_log.append({"Original": word, "Corrected": best, "Type": "Algorithmic"})
        else:
            final_tokens.append(word)

    # UI Layout for Comparison
    col_in, col_out = st.columns(2)
    
    with col_in:
        st.info("🔍 **Original Text (Flags Errors)**")
        highlighted_original = ""
        for word in words:
            if word.lower() in misspelled_set or word.lower() in slang_map:
                highlighted_original += f'<span class="highlight">{word}</span> '
            else:
                highlighted_original += f"{word} "
        st.markdown(f'<div class="glass-card">{highlighted_original}</div>', unsafe_allow_html=True)

    with col_out:
        st.success("✅ **Rectified Output**")
        rectified_text = " ".join(final_tokens)
        st.markdown(f'<div class="glass-card">{rectified_text}</div>', unsafe_allow_html=True)
    
    # Clean text version for copying
    plain_rectified = " ".join([re.sub(r'<[^>]+>', '', t) for t in final_tokens])
    st.code(plain_rectified, language="text")
    st.caption("☝️ You can copy the rectified sentence from above code block.")

    # Details table
    if corrections_log:
        with st.expander("📊 View Detailed Substitutions & Math (Edit Distance)"):
            df = pd.DataFrame(corrections_log)
            # Add Levenshtein distance to the table using our custom function!
            df['Edit Distance'] = df.apply(lambda row: levenshtein_distance(row['Original'].lower(), row['Corrected'].lower()), axis=1)
            # Add top 3 suggestions to the table for algorithmic ones
            df['Alt Suggestions'] = df['Original'].apply(lambda x: ", ".join(list(spell.candidates(x.lower()))[:3]) if x.lower() not in slang_map else "N/A")
            
            st.dataframe(df, use_container_width=True)
    else:
        st.balloons()
        st.success("Perfect! No errors detected.")

    # --- ADVANCED FEATURES SECTION ---
    st.markdown('<h3 style="margin-top: 40px;">🔬 Advanced NLP Insights</h3>', unsafe_allow_html=True)
    
    total_words_count = len(alnum_words)
    errors_count = len(misspelled_set)
    error_rate = (errors_count / total_words_count * 100) if total_words_count > 0 else 0
    
    feat_col1, feat_col2, feat_col3 = st.columns(3)
    feat_col1.metric("Total Words", total_words_count)
    feat_col2.metric("Errors Detected", errors_count)
    feat_col3.metric("Metric: Error Rate", f"{error_rate:.1f}%")

with st.expander("📝 Why these corrections? (Probabilistic Model)"):
    st.write("""
    The `pyspellchecker` uses a **Word Frequency Dictionary**. 
    When you misspell a word, it calculates all words within an **Edit Distance** of 1 or 2. 
    It then ranks these candidates by their frequency in common English text. 
    The word appearing most often is chosen as the primary correction.
    """)

with st.expander("🖥️ Evaluation & Limitations"):
    st.markdown("""
    - **Accuracy**: Highly accurate for non-word errors (e.g., 'teh' vs 'the').
    - **Context Awareness**: This tool is dictionary-based. It might not catch **homophones** (e.g., using 'their' instead of 'there' if both are spelled correctly).
    - **Speed**: Optimized for small to medium texts.
    - **Challenge**: Proper nouns (names) might be flagged as errors if not in the dictionary.
    """)
