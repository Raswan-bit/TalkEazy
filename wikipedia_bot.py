import wikipedia
import streamlit as st

# Set the title for the app
st.title("Wikipedia Q&A Bot")

# Take user input
question = st.text_input("Ask any question:")

if question:
    try:
        # Get the summary of the question
        answer = wikipedia.summary(question, sentences=2)
        st.write("**Answer:**", answer)

        # Provide a link to the full Wikipedia page
        page = wikipedia.page(question)
        st.write("Read more:", page.url)
    except wikipedia.exceptions.DisambiguationError as e:
        # Handle ambiguous queries
        st.write("Your query is ambiguous. Here are some options:")
        for option in e.options[:5]:  # Display top 5 options
            st.write(f"- {option}")
    except wikipedia.exceptions.PageError:
        # Handle missing pages
        st.write("No page found for your query. Try rephrasing.")
    except Exception as e:
        # Handle other unexpected errors
        st.write(f"An error occurred: {e}")