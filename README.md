# News-Summarization-and-Text-to-Speech-Application

This is a **Streamlit-based web application** that fetches news articles related to a given company name, performs sentiment analysis, and generates a text-to-speech (TTS) output in Hindi. The application is deployed on **Hugging Face Spaces** for easy access.

---

## **Features**
1. **News Extraction**: Fetches news articles from **NewsAPI**.
2. **Sentiment Analysis**: Analyzes the sentiment of each article (positive, negative, neutral).
3. **Text-to-Speech**: Converts the sentiment summary into Hindi speech using **gTTS**.
4. **Web Interface**: Built using **Streamlit** for a user-friendly interface.

---

## **How to Use**

### **1. Access the Application**
You can access the live application here:  
👉 [Hugging Face Space](https://huggingface.co/spaces/jangirdev82/News-app)

### **2. Input a Company Name**
1. Enter a company name (e.g., "Tesla").
2. Click **Fetch News**.

### **3. View Results**
- The application will display the **title**, **summary**, and **sentiment** of each news article.
- A **comparative sentiment analysis** will be shown, indicating the number of positive, negative, and neutral articles.
- A **Hindi text-to-speech (TTS)** summary will be generated and played automatically.

---

## **Technologies Used**
- **Streamlit**: For the web interface.
- **NewsAPI**: For fetching news articles.
- **Transformers**: For sentiment analysis.
- **gTTS**: For text-to-speech conversion.
- **Hugging Face Spaces**: For deployment.

---

## **Setup Instructions**

**1. Clone the Repository**
To run this application locally, clone the repository:

```bash
git clone https://github.com/Devendra-jangir/News-Summarization-and-Text-to-Speech-Application.git
cd News-Summarization-and-Text-to-Speech-Application
---
**2. Install Dependencies** 
Install the required Python packages:
pip install -r requirements.txt

**3. Set Up Environment Variables**
Create a .env file in the root directory and add your NewsAPI key:
# .env file
NEWSAPI_KEY=your_newsapi_key_here

4. Run the Application
Start the Streamlit application:
streamlit run app.py

Dependencies
Streamlit: For the web interface.
NewsAPI: For fetching news articles.
Transformers: For sentiment analysis.
gTTS: For text-to-speech conversion.
Python-dotenv: For managing environment variables.


Contact
For questions or feedback, feel free to reach out:
GitHub: Devendra-jangir
Email: jangirdev82@gmail.com

## **Live Demo**
👉 click on - https://huggingface.co/spaces/jangirdev82/News-app
