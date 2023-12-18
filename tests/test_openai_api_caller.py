import pytest
from app.services.openai_api_caller import Caller

from unittest.mock import patch, MagicMock

def test_caller_initialization():
    caller = Caller("test_prompt", {"name": "test_function"})

    assert caller.prompt == "test_prompt"
    assert caller.function == {"name": "test_function"}
    assert caller.messages == [{"role": "user", "content": "test_prompt"}]
    assert caller.function_call == {"name": "test_function"}

@patch('openai.ChatCompletion.create')
def test_create_completion_call(mock_create):
    caller = Caller("test_prompt", {"name": "test_function"})

    caller.create_completion_call()

    mock_create.assert_called_once_with(
        model="gpt-3.5-turbo-0613",
        messages=[{"role": "user", "content": "test_prompt"}],
        functions=[{"name": "test_function"}],
        function_call={"name": "test_function"}
    )

@patch('app.services.openai_api_caller.Caller.create_completion_call')
def test_get_structured_completion(mock_completion_call):
    mock_message = MagicMock()
    mock_message.message.to_dict.return_value = {
        'function_call': {'arguments': '{"test": "value"}'}
    }
    mock_completion_call.return_value = MagicMock(choices=[mock_message])

    caller = Caller("test_prompt", {"name": "test_function"})
    result = caller.get_structured_completion()

    assert result == {"test": "value"}
