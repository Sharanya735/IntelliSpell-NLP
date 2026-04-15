@echo off
echo [1/3] Checking dependencies...
pip install -r requirements.txt
echo [2/3] Dependencies installed successfully!
echo [3/3] Launching Interactive Spell Checker...
streamlit run app.py
pause
