#streamlit
import streamlit as st

st.set_page_config(page_title="growth mindset project", page_icon="★")
st.title("Growth Mindset Chellange: Web App with Streamlit")

st.header("Welcome to your Growth Mindset Journey!")
st.write("This is a simple web app that will help you to develop a growth mindset. The app will provide you with a new chellange every day. You can also track your progress and see how you are doing.")

# qoute section
st.subheader("Today's growth mindset qoute:")
st.write("Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill")

st.header("What's Your Challenge Today?")
user_input = st.text_input("Describe a challenge you're facing:")
  #condition
if user_input:
        st.success(f" You're facing: (user_input). Keep pushing forward towords your goal!")
else:
    st.warning("Tell as about your Challenge to get started!")

 #reflexing
    st.header(" Reflect on Your Learning")
    reflection = st.text_area("Write your reflections here:")

    if reflection:
     st.success(f"Great Insight! Your reflection: {reflection}")
    else:
     st.info("Reflecting on past experience help you grow! Share your difficulties")  

 #acheivements
st.header("Celebrate Your Wins!")
acheivment = st.text_input("Share something you've recently accomplished:")
if acheivment:
  st.success(f" Amazing! You achieved: {acheivment}")
else:
      st.info("Big or small, every acheivment counts! Share on now")

#  footer
st.write("- - -")
st.write(" Keep believing in yourself. Growth is a journey, not a destination! ")
st.write("** Created by Abdul Qadir**")
