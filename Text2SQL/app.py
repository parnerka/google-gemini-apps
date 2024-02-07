from dotenv import load_dotenv
load_dotenv() # load env variables from .env file

import streamlit as st
import os
import sqlite3
import google.generativeai as genai 

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Loading Gemini and provide SQL query as response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text

# Retrieving query from the db
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    conn.commit()
    conn.close()
    for row in result:
        print(row)
    return result

# Defining your prompt
prompt = [
    '''
    You are an expert in converting english questions to SQL queries!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS,
    SECTION, MARKS \n\n For example, \nExample 1 - How many entries of records are present?,
    the SQL query would be SELECT COUNT(*) FROM STUDENT; 
    \nExample 2 - Tell me all the students studying in CS101 class,
    the SQL query would be SELECT NAME FROM STUDENT WHERE CLASS = "CS101";
    also the sql code should not have ``` in the beginning and end and sql word in the output.
    '''
]

# Streamlit app
st.set_page_config(page_title="Text2SQL")
st.header("Gemini does Text2SQL!")

question = st.text_input('Input: ',key='input')

submit = st.button('Ask Gemini!')

# If the user clicks the submit button
if submit:
    response = get_gemini_response(question, prompt)
    print(response)
    data = read_sql_query(response, 'student.db')
    st.subheader('Gemini Response: ')
    for row in data:
        print(row)
        st.write(row)