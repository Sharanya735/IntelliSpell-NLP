# NLP Mini Project: Intelligent Spell Checker & Auto-Corrector

## 1. Title
**Design and Implementation of an NLP-based Intelligent Spell Checker using Levenshtein Distance and Probabilistic Models.**

---

## 2. Abstract
Spelling errors are common in digital communication, ranging from simple typos to complex phonetic misspellings. This project implements an intelligent spell checker that leverages Natural Language Processing (NLP) techniques to detect and correct misspelled words. The system uses a combination of Dictionary-based lookup, Levenshtein Distance (Edit Distance), and Word Frequency Probabilities to provide the most accurate suggestions. It features an interactive web interface built with Streamlit, allowing users to visualize errors in real-time and see the mathematical logic behind corrections.

---

## 3. Project Overview & Methodology

### What is a Spell Checker in NLP?
A spell checker is a software tool or algorithm designed to identify and suggest corrections for misspelled words in a text. In NLP, it is a fundamental task that serves as a preprocessing step for more complex tasks like machine translation, sentiment analysis, and search engine indexing.

### Types of Spell Checking
1.  **Dictionary-Based**: Compares words against a pre-defined vocabulary. If a word isn't found, it's flagged as an error.
2.  **Edit Distance (Levenshtein)**: Calculates the minimum number of single-character edits (insertions, deletions, substitutions) required to change one word into another.
3.  **Probabilistic (N-grams/Frequency)**: Uses the probability of a word occurring in a corpus to decide which suggestion is most likely. (e.g., "the" is more likely than "thw").
4.  **Context-Aware**: Uses neighboring words (bigrams/trigrams) to correct errors even if the word itself is in the dictionary (e.g., "piece of cake" vs "peace of cake").

### Methodology Applied in This Project
-   **Tokenization**: Segments input into words and punctuation using advanced Regex.
-   **Heuristic Slang Mapping**: Uses a custom dictionary (Slang Map) to handle domain-specific or informal language that standard dictionaries might fail to rectify (e.g., "luv" to "love").
-   **Detection**: Cross-references words with a 2.5 million+ word English corpus.
-   **Rectification**: Employs Levenshtein Distance and Frequency Probabilities to select the mathematically most likely correction.
-   **Interactive Visualization**: Real-time rendering of results using Streamlit.

---

## 4. Implementation Details
The project is built using:
-   **Python**: Fast and efficient for NLP tasks.
-   **Streamlit**: For the interactive "Real-time" interface.
-   **PySpellChecker**: Based on Peter Norvig’s famous spell-checking algorithm.
-   **Pandas**: For structured data visualization.

### Key Logic: Levenshtein Distance
We implemented a custom Levenshtein function to demonstrate the core theory. It calculates the minimum edits (Insertion, Deletion, Substitution) needed to correct a word.

---

## 5. Evaluation & Challenges

### Accuracy
The system rectifies typos with high precision. By using word frequency, it ensures that "nural" becomes "neural" rather than a less common word.

### Limitations & Challenges
1.  **Context Errors (Homophones)**: It cannot currently detect "Their are here" vs "They are here".
2.  **Proper Nouns**: Names might be flagged as errors.

---

## 6. Demonstration Script (For Presentation)

**Step 1: Introduction**
"Good morning. I am presenting my NLP Spell Rectifier. It's designed to take any natural language input and automatically fix spelling errors."

**Step 2: Real-time Rectification**
"I will type: 'NLP is a grat field of reserch'. The system immediately identifies the errors."

**Step 3: Side-by-Side View**
"On the left, we see the original text with errors highlighted. On the right, we have the 'Rectified Output' where everything is fixed. I can also copy the final sentence directly."

**Step 4: The Logic**
"If you open the 'Detailed Substitutions' tab, you can see the top 3 candidates and the mathematical edit distance for each word."

---

## 7. Viva Questions & Answers (Top 10)

1.  **Q: What is Levenshtein Distance?**
    *   **A**: It is a string metric used to measure the difference between two sequences. It counts the minimum number of insertions, deletions, or substitutions required to change one string into another.
2.  **Q: What is the difference between a non-word error and a real-word error?**
    *   **A**: A non-word error is a typo that isn't in the dictionary (e.g., 'teh'). A real-word error is a correctly spelled word used in the wrong context (e.g., 'peace' instead of 'piece').
3.  **Q: Why use word frequency in suggestion ranking?**
    *   **A**: If multiple words have the same edit distance (e.g., 'thew' could be 'the' or 'thew'), we choose the one that occurs more frequently in general language usage to increase accuracy.
4.  **Q: What is Tokenization?**
    *   **A**: It is the process of splitting a string of text into smaller units called tokens (usually words or characters).
5.  **Q: How can we improve this project for "Real-word" errors?**
    *   **A**: By using N-gram models (like Bigrams or Trigrams) or Transformers (like BERT) to understand the context of the sentence.
6.  **Q: Which libraries are the backbone of this project?**
    *   **A**: Streamlit for UI and PySpellChecker for the algorithm and dictionary.
7.  **Q: Does the algorithm handle punctuation?**
    *   **A**: Yes, the implementation uses Regex-based tokenization to separate punctuation from the actual words.
8.  **Q: What is the complexity of the Levenshtein algorithm?**
    *   **A**: The basic dynamic programming approach is $O(m \times n)$, where $m$ and $n$ are the lengths of the two strings.
9.  **Q: How does the system handle names of people?**
    *   **A**: Standard dictionaries usually don't have all names. We can add a "custom dictionary" feature to allow the system to ignore specific names.
10. **Q: Why is NLP important in spell checking?**
    *   **A**: NLP provides the linguistic framework needed to understand word structure, context, and probability, which simple string matching cannot do.

---

## 8. Conclusion
This project successfully demonstrates the core principles of NLP in text processing. By combining mathematical models like Edit Distance with linguistic data like Word Frequency, we have built a reliable tool that mirrors the functionality of modern professional editors.
