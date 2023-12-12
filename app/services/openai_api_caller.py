import instructor
from instructor.distil import OpenAI

class Caller():
    """
    A class to manage calls and completions with OpenAI's API.

    Attributes:
    - prompt (str): The user's input or prompt for which a completion is desired.
    - response_model (BaseModel): The Pydantic model that is used as the response model in the instructor client call.
    - client (instructor.patch): The instructor client that will handle the OpenAI API call.
    - messages (list[dict]): A list of message objects, initially containing the user's prompt.

    Methods:
    - create_completion_call(): Make a chat completion call to OpenAI's API.
    - get_structured_completion(): Retrieve and structure the completion response from OpenAI's API.
    """

    def __init__(self, prompt, response_model):
        """
        Initializes the Caller class.

        Args:
        - prompt (str): The user's input or prompt.
        """
        self.response_model = response_model
        self.prompt = prompt
        self.client = instructor.patch((OpenAI()))
        self.messages = [
        {
            "role": "user",
            "content": self.prompt
        }
        ]
        self.returned_model = None

    def make_request(self):
        """
        Make a chat completion call to OpenAI's API based on the provided prompt, using the 
        instructor client.

        Returns:
        Pydantic model: The response from instructor client.
        """
        self.returned_model = self.client.chat.completions.create(
            model="gpt-3.5-turbo-0613",
            response_model = self.response_model,
            messages=self.messages,
        )


    def json_model(self):
        """
        Retrieve the structured completion response from OpenAI's API, focusing on the function call's arguments.

        Returns:
        dict: The structured arguments from the completion response.
        """
        if self.returned_model:
            return self.returned_model.model_dump_json()
        
        raise ValueError("Caller does not have a returned model. Try running make_request method first")
