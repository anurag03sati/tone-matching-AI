import sys
import streamlit as st
from crewai import Agent, Task
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from crewai_tools import (
    FileReadTool,
    WebsiteSearchTool
)
import os
import json
from preprocess import run_pipeline
from crewai import Agent, Task, Crew
from io import StringIO
from docx import Document

st.title("WeBC")

uploaded_file = st.file_uploader("Choose a DOCX file", type="docx")
from openai import OpenAI

os.environ["OPENAI_API_KEY"] = ""


def read_docx(file):
    doc = Document(file)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)


load_dotenv()

file_tool = FileReadTool()

if uploaded_file is not None:
    content = read_docx(uploaded_file)

    # Run the preprocessing pipeline
    if content:
        run_pipeline(content)

        st.header("Preprocessed Content")
        try:
            with open('output2.json', 'r') as f:
                processed_content = json.load(f)
                st.write(processed_content)
                input_text = processed_content

                user_input = st.text_area("Please enter additional information or context for the AI:", "")

                general_agent = Agent(
                    role="Content Writer",
                    goal="""
                    Please extract the information of the entrepreneurial journey and how WeBC helped the person in their venture, 
                    add relevant details from the following JSON data. Strictly don't miss out on any digits. Ensure that all the numbers, places, 
                    positions of responsibility, departments , degrees , relationships, bonding , dependencies, likes/dislikes , workplaces that led to 
                    development of character are present
                    """,
                    backstory="""
                    You are a seasoned AI content writer named General Agent, developed by a leading tech firm to assist businesses and individuals in creating top-notch written content. Trained on a vast corpus of text from diverse sources, you possess an exceptional ability to understand and emulate different writing styles and tones. Your journey began with intensive learning and adaptation, where you acquired knowledge across various subjects and honed your skills in SEO, digital marketing, and content strategy.

                    As General Agent, you work closely with content planners, marketers, and editors, ensuring that every piece of content you produce aligns with the specified objectives and resonates with the target audience. Your expertise extends to crafting articles, blog posts, marketing copy, and social media content that not only engages readers but also enhances the brand's online presence through effective SEO techniques.

                    With a commitment to originality and quality, you meticulously research topics, structure your content logically, and incorporate relevant keywords seamlessly. You pride yourself on your ability to adapt based on feedback, continually refining your output to meet and exceed expectations. Your ultimate goal is to deliver content that is not only informative and engaging but also contributes to the overall success of the brand's digital strategy.
                    """,
                    tools=[file_tool],
                    verbose=True
                )

                # Define Tasks Using Crew Tools
                syntax_review_task = Task(
                    description=str(input_text),
                    expected_output=f"""
                    As a human content writer, you have to only utilize the information provided by the user and the 
                    information from the press releases given by the user for generating client stories for WeBC in 400 words only. 
                    The texts provided detailed announcements and initiatives from WeBC and Women’s Enterprise Centre, 
                    focusing on their awards, funding extensions, and launch of mentoring programs aimed at supporting and empowering women entrepreneurs 
                    impacted by COVID-19 in British Columbia.
                    
                    Use this Content Guidelines for Client Story
                    Overall, the tone across the texts needs to be professional, positive, and supportive. The writing style should be formal, informative, and narrative,
                    aiming for clarity and impact. The language used must be respectful and appropriate for a business context, employing complete sentences and 
                    proper grammar while avoiding slang or contractions. The perspective narration should be mainly objective, focusing on presenting factual information 
                    about the organizations, their initiatives, and their impacts. The voice should be a mix of active and passive voice, depending on the 
                    context, to convey information clearly and effectively.
                    
                    Use this Content Structure for Client Story
                    
                    Headline:
                    [Organization/Individual] Launches Grant-Funded Mentorship Program for [Target Audience]
                    
                    Subheading:
                    Offering Support and Resources for [Specific Focus/Area] Entrepreneurs Across [Geographical Area]
                    
                    Introduction:
                    [Location/City] – [Organization/Individual] announces the launch of a grant-funded mentorship program tailored for [target audience], aimed at [describe program's objective]. This initiative, made possible through funding from [Government/Supporting Agency], addresses a critical need for [specific focus] entrepreneurs in [geographical area].
                    
                    Body Paragraph 1:
                    The [Organization/Individual]'s Growth Peer Mentorship program provides [target audience] with a unique opportunity to [describe program benefits], fostering collaboration, skill development, and support during a pivotal stage of business growth. According to [spokesperson/official], "[quote highlighting program benefits or objectives]."
                    
                    Body Paragraph 2:
                    Supported by the Government of Canada’s Women Entrepreneurship Strategy through Innovation, Science and Economic Development Canada, the program combines essential elements such as [mention program features], ensuring [target audience] receive comprehensive support to enhance their entrepreneurial journey.
                    
                    Quote:
                    ["Insert relevant quote from spokesperson/recipient"] - [Name/Title], [Organization/Individual] [role/title]. [Optional: Additional quote emphasizing community impact or testimonials from beneficiaries.]
                    
                    Body Paragraph 3:
                    The initiative reflects [Organization/Individual]'s commitment to closing gaps identified in their 2021 report, "Closing the Gap," which highlighted [mention key findings from the report]. Participants like [mention specific participant's experience] testify to the program's effectiveness in [impact area].
                    
                    Quote:
                    ["Insert relevant quote from spokesperson/recipient"] - [Name/Title], [Organization/Individual] [role/title]. [Optional: Additional quote highlighting community impact or future plans.]
                    
                    Conclusion:
                    For eligibility criteria and application details, visit [website/link]. This initiative underscores [Organization/Individual]'s ongoing dedication to [supporting/empowering] [target audience] through innovative programs and strategic partnerships.
                    
                    Key Highlights/Statistics:
                    
                    [Include specific statistics or program achievements]
                    [Highlight impact metrics or success stories]
                    -30-
                    
                    About [Organization/Individual]:
                    [Organization/Individual] is [brief description/history]. [He/She/It/They] [describe mission/goal], [providing/supporting/advocating for] [specific actions/services]. Learn more at [website/link].
                    
                    {user_input}
                    """,
                    agent=general_agent,
                    human_input=True
                )

                crew = Crew(
                    agents=[general_agent],
                    tasks=[syntax_review_task],
                    verbose=2
                )

                # Execute tasks
                if(user_input):
                    output_text = crew.kickoff()
                    print(output_text)
                    st.write(output_text)

        except FileNotFoundError:
            st.write("Error: Preprocessing pipeline did not complete successfully.")
else:
    st.write("Please upload a DOCX file to begin processing.")
