# 📊 WhatsApp Chat Analyzer  

Unlock deep insights from your WhatsApp conversations with **WhatsApp Chat Analyzer**, a Python-powered tool designed to analyze chat data, visualize trends, and perform sentiment analysis.

## 🚀 Project Overview  

WhatsApp is the world’s most popular messaging app, with over **1.5 billion monthly active users**. This project extracts meaningful insights from chat data, helping users understand communication patterns, active hours, frequently used words, and sentiment trends.
## Project Link for direct use
https://huggingface.co/spaces/vivekojha03/Whatsapp_chat_anaysis
## 🔍 Key Features  

✅ **Message Frequency Analysis** – Identify peak activity periods and communication trends.  
✅ **Active Hours Analysis** – Discover when users are most engaged in conversations.  
✅ **Word Cloud Generation** – Visualize commonly used words in chats.  
✅ **Sentiment Analysis** – Assess the emotional tone of conversations (positive, negative, neutral).  
✅ **Emoji Usage Insights** – Find out the most frequently used emojis.  
✅ **Activity Heatmap** – Visualize engagement patterns over time.  

## 🛠 Tech Stack  

- **Python** 🐍  
- **Pandas** – Data manipulation  
- **Matplotlib & Seaborn** – Data visualization  
- **WordCloud** – Word cloud generation  
- **NLTK** – Sentiment analysis  

## 📂 Folder Structure  

WhatsAppChatAnalyzer/ │── data/ │ ├── chat.txt │── analysis/ │ ├── frequency_analysis.py │ ├── sentiment_analysis.py │ ├── wordcloud_generator.py │── visualization/ │ ├── heatmap.py │ ├── emoji_analysis.py │── static/ │ ├── sample_wordcloud.png │── README.md │── requirements.txt │── app.py


## 🔧 How to Use  

1️⃣ Clone the Repository  

git clone https://github.com/vivekojha02/whatsappChatAnalyzer.git
cd whatsappChatAnalyzer

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Export WhatsApp Chat Data :

Open WhatsApp and select the chat you want to analyze.

Tap on Options > More > Export Chat (without media).

Save the exported .txt file in the data/ folder.

4️⃣ Run the Analysis

python app.py

5️⃣ View Results
Word Cloud – static/sample_wordcloud.png
Sentiment Analysis – Console output
Activity Heatmap – Generated plots
