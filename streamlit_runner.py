import sys
from streamlit.web import cli as stcli

sys.argv = ["streamlit", "run", "Book_List.py"]
sys.exit(stcli.main())