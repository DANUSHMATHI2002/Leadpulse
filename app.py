import os

if __name__ == "__main__":
    # This launches your dashboard correctly on the Hugging Face server
    os.system("streamlit run src/dashboard.py --server.port 7860 --server.address 0.0.0.0")