from crewai_tools import BaseTool

class DocxReadTool(BaseTool):
    name: str = "DocxReadTool"
    description: str = "Reads DOCX files, preprocesses the text, and converts it into a JSON format."

    def _run(self, file_path: str) -> dict:
        doc = docx.Document(file_path)
        full_text = []
        for paragraph in doc.paragraphs:
            full_text.append(paragraph.text)
        text = '\n'.join(full_text)

        # Apply preprocessing steps
        text = remove_timestamps(text)
        text = remove_extra_spaces(text)
        conversation_json = convert_to_json(text)

        return conversation_json



