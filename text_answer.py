from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate

class HindiBot:
    def __init__(self, model_name="llama3.2", stop_token="<|eot_id|>"):
        self.llm = OllamaLLM(model=model_name, stop=[stop_token])
        self.template = """
            <|begin_of_text|>
            <|start_header_id|>system<|end_header_id|>
            "You are a bot that can understand Hindi language very well and can respond to the user's queries in Hindi."
            <|eot_id|>
            <|start_header_id|>user<|end_header_id|>
            {user_prompt}
            <|eot_id|>
            <|start_header_id|>assistant<|end_header_id|>
        """
        self.prompt = PromptTemplate(
            input_variables=["user_prompt"],
            template=self.template
        )
    
    def get_response(self, user_prompt: str) -> str:
        formatted_prompt = self.prompt.format(user_prompt=user_prompt)
        response = self.llm(formatted_prompt)
        return response
    