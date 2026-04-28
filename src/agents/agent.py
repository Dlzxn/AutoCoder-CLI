from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
import torch, json


class Agent:
    def __init__(self, config: BitsAndBytesConfig, tools: list, model_name: str = 'Qwen/Qwen2.5-Coder-14B-Instruct', device='cuda'):
        self.model = AutoModelForCausalLM.from_pretrained(
                    model_name,
                    quantization_config=config,
                    device = device
                    )
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.tools = tools
        self.model.eval()


    def generate(self, text: str):
        message = [{'role': 'user',
                    'content': text
                    }
                   ]
        message_with_template = self.tokenizer.apply_chat_template(
            message,
            add_generation_prompt=True,
            tools=self.tools,
            tokenize=False
        )
        tokens = self.tokenizer(message_with_template, return_tensors='pt').to(self.model.device)
        input_len = tokens.input_ids.shape[1]
        result = self.model.generate(
            **tokens,
            max_new_tokens=4096
        )
        generated_tokens = result[0][input_len:]
        answer = self.tokenizer.decode(generated_tokens, skip_special_tokens=True)
        return answer


