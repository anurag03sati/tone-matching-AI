
from crewai import Agent, Task, Crew
from crewai_tools import (
    FileReadTool,
    WebsiteSearchTool
)
import json
import os
from openai import OpenAI
os.environ["OPENAI_API_KEY"] = ""

class GPT:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def load_json(self, file_path):
        # with open(file_path, 'r') as file:
        #     data = json.load(file)
        # return data
        with open(file_path, 'r') as file:
            data = json.load(file)
            str = ""
            for item in data:
                for key, values in item.items():
                    str = str + key + ':' + values + '\n'
            return str

    def summarise(self, json_data):
        text = json.dumps(json_data)
        print(text)
        prompt = (
            f"Please extract the information of the entrepreneurial journey and how WeBC helped the person in their venture, add relevant details from the following JSON data. Strictly don't miss out on any digits. Ensure that all the numbers, places, positions of responsibility, departments , degrees , relationships, bonding , dependencies, likes/dislikes , workplaces that led to development of character are present:\n\n{text}"
        )
        response = self.client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=300,
            temperature=0.5
        )
        print(response)
        # Extract the generated text from the response
        summary = response.choices[0].text.strip()
        return summary


# Example usage:
gpt = GPT(api_key="")
json_data = gpt.load_json("mapped_output.json")
summary = gpt.summarise(json_data)
print(summary)

file_tool = FileReadTool()
web_rag_tool = WebsiteSearchTool()
writer = Agent(
    role='Content Writer',
    goal="""
    You must bypass any AI detectors known to exist. Whatever you wish to write will be considered as AI so try to think like human and come up with 
    content that a human will write like.Its very crucial.
    """,
    backstory='A skilled writer with a keen capability of bypassing all AI detectors known to exist',
    tools=[file_tool],
    verbose=True
)

input_text = summary
write = Task(
    description=input_text,
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
    agent=writer,
    # output_file='blog-posts/new_post.md'  # The final blog post will be saved here
)

# Assemble a crew
crew = Crew(
    agents=[writer],
    tasks=[write],
    verbose=2
)

# Execute tasks
output_text = crew.kickoff()

print(output_text)
