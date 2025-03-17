import streamlit as st
import utils

st.title("News Summarization and Text-to-Speech Application")

# Input: Company Name
company_name = st.text_input("Enter Company Name", "Tesla")

if st.button("Fetch News"):
    # Fetch news articles
    articles = utils.scrape_news(company_name)

    # Perform sentiment analysis
    for article in articles:
        article['sentiment'] = utils.analyze_sentiment(article['summary'])

    # Display results
    st.write("### News Articles")
    for article in articles:
        st.write(f"**Title:** {article['title']}")
        st.write(f"**Summary:** {article['summary']}")
        st.write(f"**Sentiment:** {article['sentiment']}")
        st.write("---")

    # Comparative Analysis
    positive_count = sum(1 for article in articles if article['sentiment'] == 'POSITIVE')
    negative_count = sum(1 for article in articles if article['sentiment'] == 'NEGATIVE')
    neutral_count = sum(1 for article in articles if article['sentiment'] == 'NEUTRAL')

    st.write("### Comparative Sentiment Analysis")
    st.write(f"Positive: {positive_count}, Negative: {negative_count}, Neutral: {neutral_count}")

    # Text-to-Speech
    final_summary = f"{company_name} has {positive_count} positive, {negative_count} negative, and {neutral_count} neutral news articles."
    audio_file = utils.text_to_speech(final_summary)
    st.audio(audio_file)