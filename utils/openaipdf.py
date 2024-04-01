from openai import OpenAI
import os, sys,  time
from typing import List, Optional

class PDFChat:
    """
    A class to interact with the OpenAI API to create an assistant for answering questions based on a PDF file.

    Attributes:
        client (OpenAI): Client for interacting with OpenAI API.
        assistant_id (Optional[str]): ID of the created assistant. None until an assistant is created.
    """
    def __init__(self) -> None:
        """
        Initializes the PDFAssistant with the API key from environment variables.
        """
        api_key: Optional[str] = os.getenv("OPENAI_API_KEY")
        if api_key is None:
            raise ValueError("API Key not found in environment variables")
        self.client = OpenAI(api_key=api_key)
        self.assistant_id: Optional[str] = None

    def upload_file(self, filename: str) -> None:
        """
        Uploads a file to the OpenAI API and creates an assistant related to that file.

        Args:
            filename (str): The path to the file to be uploaded.
        """
        file = self.client.files.create(
            file=open(filename, 'rb'),
            purpose="assistants"
        )

        assistant = self.client.beta.assistants.create(
            name="PDF Helper",
            instructions="You are my assistant who can answer questions from the given pdf",
            tools=[{"type": "retrieval"}],
            model="gpt-3.5-turbo-0125",
            file_ids=[file.id]
        )
        self.assistant_id = assistant.id

    def get_answers(self, question: str) -> List[str]:
        """
        Asks a question to the assistant and retrieves the answers.

        Args:
            question (str): The question to be asked to the assistant.

        Returns:
            List[str]: A list of answers from the assistant.

        Raises:
            ValueError: If the assistant has not been created yet.
        """
        if self.assistant_id is None:
            raise ValueError("Assistant not created. Please upload a file first.")

        thread = self.client.beta.threads.create()

        self.client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=question
        )

        run = self.client.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=self.assistant_id
        )

        while True:
            run_status = self.client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
            time.sleep(10)
            if run_status.status == 'completed':
                messages = self.client.beta.threads.messages.list(thread_id=thread.id)
                break
            else:
                time.sleep(2)

        return [message.content[0].text.value for message in messages.data if message.role == "assistant"]
            
            
if __name__ == "__main__":
    client = PDFChat()
    filename = sys.argv[1]
    client.upload_file(filename)

    while True:
          question = input("Enter your question (or type 'exit' to quit): ")
          if question.lower() in ['exit', 'quit']:
            break

          answers = client.get_answers(question)
          for answer in answers:
              print(answer)