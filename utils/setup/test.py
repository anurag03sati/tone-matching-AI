import sys
import streamlit as st
from crewai import Agent, Task
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from crewai_tools import (
    FileReadTool,
    WebsiteSearchTool
)
import json
from preprocess import run_pipeline
from crewai import Agent, Task, Crew
from io import StringIO
from docx import Document


st.title("WeBC")

uploaded_file = st.file_uploader("Choose a DOCX file", type="docx")
def read_docx(file):
    doc = Document(file)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)

load_dotenv()

llm = ChatOpenAI(
    model="crewai-gemma:2b",
    # model='crewai-phi3',
    base_url="http://localhost:11434/v1"
)
file_tool = FileReadTool()


if uploaded_file is not None:
    content = read_docx(uploaded_file)
    # st.header("Original File Content")
    # st.write(content)

    # Run the preprocessing pipeline
    if content:
        run_pipeline(content)

        st.header("Preprocessed Content")
        try:
            with open('output2.json', 'r') as f:
                processed_content = json.load(f)
                st.write(processed_content)
                input_text=processed_content
                general_agent = Agent(
                    role="Content Writer",
                    goal="""
                    As a human content writer, you have to only utilize the information provided by the user and the information from the meeting transcripts given by the user for generating client stories for WeBC in 300 words only. This story is mainly about woman, their entreprenurial journey and their experience with WEBC. The writing highlights Client's dedication, passion, and the positive impact of her services. The value of WEBC's program is emphasized. There's a story element, following Client's journey and the company's development.

                    Use this Content Guidelines for Client Story

                    The overall tone of the story is professional, positive and supportive. The language is respectful and appropriate for a business context. The overall style of the story is Formal, Informative and Narrative. The writing uses complete sentences, proper grammar, and avoids slang or contractions. The focus is on providing clear and concise information about the client, company, and their services. The voice is in 3rd Person. The story is told from an objective perspective, focusing on client and its Services. The story will be in paragraph with a mix of active and passive voice. Ensure the writing is simple and clear for an 8th-grade level. Maintain a professional, positive tone throughout.

                    Use this Content Structure for Client Story

                    [Title] Name, Business, Location
                    If this information is not provided by the user then simply leave a blank place holder [] for that information. 
                    Who she is/what she does [100 words about the woman and her business]. If this information is not provided by the user then simply leave a blank place holder [] for that information. Use professional & informative tone for this paragraph. It must provide factual information about client’s background, her career transition, and the business she founded. The tone is serious and respectful, reflecting the gravity and importance of the work being discussed. It must convey admiration for client's expertise and dedication to her field. The style of this paragraph is concise and straightforward using specific details to convey the subject's expertise and the business's unique value. Use this structure for this paragraph: 
                    Introduction to client's career.
                    Transition to her founding.
                    Explanation of the business’s purpose and the innovative approach it takes.
                    Emphasis on the primary focus of the business, highlighting the specific contexts in which it operates.
                    How she got there [the catalyst that made her start her business or decide to grow her business if she’s a more advanced entrepreneur]. If this information is not provided by the user then simply leave a blank place holder [] for that information. The voice of this para is professional and authoritative. It provides detailed information about the client’s company. The tone is informative and matter-of-fact. The style of this paragraph is clear and precise, with a focus on providing specific details about client’s company and their applications.
                    Then, If provided by the user insert a short/impactful quote from her in invertted commas. If a quote is not provided by the user then do not insert it. 
                    Problem or opportunity In <year> she joined the WeBC <name of program> to [insert why she joined - paraphrase her reasoning from her questionnaire response]. If the problem is not provided by the user then simply leave a blank place holder [] for that information. If the year is not provided by the user then simply leave a blank place holder [] for that information. If the name of the program is not provided by the user then simply write “WEBC Program” for that information. Please take care if the quote is not provided by the user then simply leave a blank place holder [] for that information. If why she joined is not provided by the user then simply leave a blank place holder [] for that information.
                    What the program did for her [Again, paraphrase and/or include quote, depending how much information is provided by the user] Please take care if the quote is not provided by the user then simply leave a place holder [] for the quote. 
                    Add concluding lines in praise of the WEBC program of the client and statements like [client name] is keeping an eye on upcoming programs to further enhance their business skills. They are grateful for resources like WeBC that support new business owners and provide tools for success. Or [Client Name] is looking forward to maintaining the connections made during this program for years to come.
                    
                    """,
                    backstory="""
                    You have previously written content for a big content industry and here to accomplish. 
                    """,
                    tools=[file_tool],
                    verbose=True,
                    llm=llm
                )

                # Define Tasks Using Crew Tools
                syntax_review_task = Task(
                    description=str(input_text),
                    expected_output="""
                    As a human content writer, you have to only utilize the information provided by the user and the information from the meeting transcripts given by the user for generating client stories for WeBC in 300 words only. This story is mainly about woman, their entreprenurial journey and their experience with WEBC. The writing highlights Client's dedication, passion, and the positive impact of her services. The value of WEBC's program is emphasized. There's a story element, following Client's journey and the company's development.

                    Use this Content Guidelines for Client Story

                    The overall tone of the story is professional, positive and supportive. The language is respectful and appropriate for a business context. The overall style of the story is Formal, Informative and Narrative. The writing uses complete sentences, proper grammar, and avoids slang or contractions. The focus is on providing clear and concise information about the client, company, and their services. The voice is in 3rd Person. The story is told from an objective perspective, focusing on client and its Services. The story will be in paragraph with a mix of active and passive voice. Ensure the writing is simple and clear for an 8th-grade level. Maintain a professional, positive tone throughout.

                    Use this Content Structure for Client Story

                    [Title] Name, Business, Location
                    If this information is not provided by the user then simply leave a blank place holder [] for that information. 
                    Who she is/what she does [100 words about the woman and her business]. If this information is not provided by the user then simply leave a blank place holder [] for that information. Use professional & informative tone for this paragraph. It must provide factual information about client’s background, her career transition, and the business she founded. The tone is serious and respectful, reflecting the gravity and importance of the work being discussed. It must convey admiration for client's expertise and dedication to her field. The style of this paragraph is concise and straightforward using specific details to convey the subject's expertise and the business's unique value. Use this structure for this paragraph: 
                    Introduction to client's career.
                    Transition to her founding.
                    Explanation of the business’s purpose and the innovative approach it takes.
                    Emphasis on the primary focus of the business, highlighting the specific contexts in which it operates.
                    How she got there [the catalyst that made her start her business or decide to grow her business if she’s a more advanced entrepreneur]. If this information is not provided by the user then simply leave a blank place holder [] for that information. The voice of this para is professional and authoritative. It provides detailed information about the client’s company. The tone is informative and matter-of-fact. The style of this paragraph is clear and precise, with a focus on providing specific details about client’s company and their applications.
                    Then, If provided by the user insert a short/impactful quote from her in invertted commas. If a quote is not provided by the user then do not insert it. 
                    Problem or opportunity In <year> she joined the WeBC <name of program> to [insert why she joined - paraphrase her reasoning from her questionnaire response]. If the problem is not provided by the user then simply leave a blank place holder [] for that information. If the year is not provided by the user then simply leave a blank place holder [] for that information. If the name of the program is not provided by the user then simply write “WEBC Program” for that information. Please take care if the quote is not provided by the user then simply leave a blank place holder [] for that information. If why she joined is not provided by the user then simply leave a blank place holder [] for that information.
                    What the program did for her [Again, paraphrase and/or include quote, depending how much information is provided by the user] Please take care if the quote is not provided by the user then simply leave a place holder [] for the quote. 
                    Add concluding lines in praise of the WEBC program of the client and statements like [client name] is keeping an eye on upcoming programs to further enhance their business skills. They are grateful for resources like WeBC that support new business owners and provide tools for success. Or [Client Name] is looking forward to maintaining the connections made during this program for years to come.
                    """,
                    agent=general_agent,
                    human_input=True
                    # output_file='blog-posts/new_post.md'  # The final blog post will be saved here
                )
                crew = Crew(
                    agents=[general_agent],
                    tasks=[syntax_review_task],
                    verbose=2
                )

                # Execute tasks
                output_text = crew.kickoff()

                print(output_text)
                st.write(output_text)
        except FileNotFoundError:
            st.write("Error: Preprocessing pipeline did not complete successfully.")

    else:
        st.write("Please upload a DOCX file to begin processing.")


