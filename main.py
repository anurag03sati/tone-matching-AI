import os
import openai
from crewai import Agent, Task, Crew, Process
from crewai_tools import BaseTool
import docx

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = "your_openai_api_key"

# Define the tool to read DOCX files
class DocxReadTool(BaseTool):
    name: str = "DocxReadTool"
    description: str = "Reads DOCX files and extracts the text."

    def _run(self, file_path: str) -> str:
        doc = docx.Document(file_path)
        full_text = []
        for paragraph in doc.paragraphs:
            full_text.append(paragraph.text)
        return '\n'.join(full_text)

# Define the tool to use OpenAI GPT-4 for summarization
class GPT4SummarizeTool(BaseTool):
    name: str = "GPT4SummarizeTool"
    description: str = "Uses OpenAI GPT-4 to summarize text."

    def _run(self, text: str) -> str:
        openai.api_key = os.environ["OPENAI_API_KEY"]
        response = openai.chat.completion.create(
            engine="text-davinci-003",
            prompt=f"Summarize the following text in 2 paragraphs:\n\n{text}",
            max_tokens=150
        )
        return response.choices[0].text.strip()

# Create an agent for summarizing documents and text input
summarizer_agent = Agent(
    role='Document Summarizer',
    goal='Summarize content from DOCX files or direct text input.',
    verbose=True,
    memory=True,
    backstory=(
        "You are an expert at distilling complex information into concise, easy-to-understand summaries."
    ),
    tools=[DocxReadTool(), GPT4SummarizeTool()],
    allow_delegation=False
)

# Create a task to summarize the content from a DOCX file or text input
summarize_task = Task(
    description=(
        "Summarize the provided content. The content can be in the form of a DOCX file or direct text input."
        "Focus on the main points and provide a concise summary."
        "Your final answer must be a 2-paragraph summary of the content."
    ),
    expected_output='A 2-paragraph summary of the provided content.',
    tools=[DocxReadTool(), GPT4SummarizeTool()],
    agent=summarizer_agent,
)

# Combine the agent and task into a crew and execute the process
crew = Crew(
    agents=[summarizer_agent],
    tasks=[summarize_task],
    process=Process.sequential  # Sequential task execution
)

# Function to kick off the crew with either a file path or direct text
def kickoff_crew(input_type: str, content: str):
    if input_type == 'file':
        inputs = {'file_path': content}
    elif input_type == 'text':
        inputs = {'text_input': content}
    else:
        raise ValueError("Invalid input type. Use 'file' or 'text'.")
    result = crew.kickoff(inputs=inputs)
    return result

# Example usage
# For DOCX file:
# docx_file_path = 'path/to/your/document.docx'
# print(kickoff_crew('file', docx_file_path))

# For direct text input:
text_input = "This is a sample text input that needs to be summarized."
print(kickoff_crew('text', text_input))
