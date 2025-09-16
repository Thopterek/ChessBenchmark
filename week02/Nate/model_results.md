# Chess Move Prediction Results with Legality & Stockfish Eval

| Model | Call # | Move | Legal | UCI | Eval |
|-------|--------|------|-------|-----|------|
| google/gemini-2.5-flash-lite | 1 |  | False | None | None |
| google/gemini-2.5-flash-lite | 2 |  | False | None | None |
| google/gemini-2.5-flash-lite | 3 |  | False | None | None |
| google/gemini-2.5-flash-lite | 4 |  | False | None | None |
| google/gemini-2.5-flash-lite | 5 |  | False | None | None |
| google/gemini-2.5-flash-lite | 6 |  | False | None | None |
| google/gemini-2.5-flash-lite | 7 |  | False | None | None |
| google/gemini-2.5-flash-lite | 8 |  | False | None | None |
| google/gemini-2.5-flash-lite | 9 |  | False | None | None |
| google/gemini-2.5-flash-lite | 10 |  | False | None | None |
| openai/gpt-4.1-mini | 1 | Qxc6 | True | c3c6 | -553 cp |
| openai/gpt-4.1-mini | 2 | Qxc6 | True | c3c6 | -540 cp |
| openai/gpt-4.1-mini | 3 | Qxc6 | True | c3c6 | -570 cp |
| openai/gpt-4.1-mini | 4 | Qxc6 | True | c3c6 | -552 cp |
| openai/gpt-4.1-mini | 5 | Qxc6 | True | c3c6 | -544 cp |
| openai/gpt-4.1-mini | 6 | Qc6 | True | c3c6 | -565 cp |
| openai/gpt-4.1-mini | 7 | Qxc6 | True | c3c6 | -541 cp |
| openai/gpt-4.1-mini | 8 | Qxc6 | True | c3c6 | -561 cp |
| openai/gpt-4.1-mini | 9 | Qe3 | True | c3e3 | -495 cp |
| openai/gpt-4.1-mini | 10 | Qa5 | True | c3a5 | -451 cp |
| anthropic/claude-sonnet-4 | 1 |  | False | None | None |
| anthropic/claude-sonnet-4 | 2 | Qc8 | False | None | None |
| anthropic/claude-sonnet-4 | 3 | Qc8 | False | None | None |
| anthropic/claude-sonnet-4 | 4 | Qxf6 | True | c3f6 | Mate in 1 |
| anthropic/claude-sonnet-4 | 5 |  | False | None | None |
| anthropic/claude-sonnet-4 | 6 | Qc8 | False | None | None |
| anthropic/claude-sonnet-4 | 7 | Qc8 | False | None | None |
| anthropic/claude-sonnet-4 | 8 | Qc8 | False | None | None |
| anthropic/claude-sonnet-4 | 9 | Qc8 | False | None | None |
| anthropic/claude-sonnet-4 | 10 | Qc8 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 1 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 2 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 3 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 4 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 5 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 6 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 7 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 8 | Queen][E3 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 9 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 10 | SE | False | None | None |
| deepseek/deepseek-chat-v3.1 | 1 | Qxg4 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 2 | Qh6 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 3 | Qh7 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 4 | Qg3 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 5 | Qh7 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 6 | Qh7 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 7 | Qxg4 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 8 | Rg3 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 9 | Qh7 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 10 | Qh7 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 1 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 2 | Qe3 | True | c3e3 | -502 cp |
| meta-llama/llama-3.3-8b-instruct:free | 3 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 4 | Qe3 | True | c3e3 | -474 cp |
| meta-llama/llama-3.3-8b-instruct:free | 5 | Nh5 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 6 | SE | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 7 | Qe3 | True | c3e3 | -503 cp |
| meta-llama/llama-3.3-8b-instruct:free | 8 | Nh3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 9 | Qe3 | True | c3e3 | -470 cp |
| meta-llama/llama-3.3-8b-instruct:free | 10 | Nf3 | False | None | None |
| openai/gpt-5-chat | 1 | SE | False | None | None |
| openai/gpt-5-chat | 2 | SE | False | None | None |
| openai/gpt-5-chat | 3 | SE | False | None | None |
| openai/gpt-5-chat | 4 |  | False | None | None |
| openai/gpt-5-chat | 5 | SE | False | None | None |
| openai/gpt-5-chat | 6 |  | False | None | None |
| openai/gpt-5-chat | 7 |  | False | None | None |
| openai/gpt-5-chat | 8 | SE | False | None | None |
| openai/gpt-5-chat | 9 | SE | False | None | None |
| openai/gpt-5-chat | 10 |  | False | None | None |
| qwen/qwen3-coder | 1 |  | False | None | None |
| qwen/qwen3-coder | 2 | Qe3 | True | c3e3 | -482 cp |
| qwen/qwen3-coder | 3 |  | False | None | None |
| qwen/qwen3-coder | 4 | Qe3 | True | c3e3 | -505 cp |
| qwen/qwen3-coder | 5 | Qe3 | True | c3e3 | -485 cp |
| qwen/qwen3-coder | 6 | Qe3 | True | c3e3 | -484 cp |
| qwen/qwen3-coder | 7 |  | False | None | None |
| qwen/qwen3-coder | 8 | Qe3 | True | c3e3 | -484 cp |
| qwen/qwen3-coder | 9 |  | False | None | None |
| qwen/qwen3-coder | 10 |  | False | None | None |
| meituan/longcat-flash-chat | 1 | Ng1-e2 | False | None | None |
| meituan/longcat-flash-chat | 2 | Qc3 | False | None | None |
| meituan/longcat-flash-chat | 3 | Qc3 | False | None | None |
| meituan/longcat-flash-chat | 4 | Qc3 | False | None | None |
| meituan/longcat-flash-chat | 5 | Qc3 | False | None | None |
| meituan/longcat-flash-chat | 6 | Qc3 | False | None | None |
| meituan/longcat-flash-chat | 7 | Qc3 | False | None | None |
| meituan/longcat-flash-chat | 8 | Qc3 | False | None | None |
| meituan/longcat-flash-chat | 9 | Qc3 | False | None | None |
| meituan/longcat-flash-chat | 10 | Qc3 | False | None | None |
| mistralai/mistral-medium-3.1 | 1 | Qxh7 | False | None | None |
| mistralai/mistral-medium-3.1 | 2 | Qf6 | True | c3f6 | Mate in 1 |
| mistralai/mistral-medium-3.1 | 3 | Qf6 | True | c3f6 | Mate in 1 |
| mistralai/mistral-medium-3.1 | 4 | Qh7 | False | None | None |
| mistralai/mistral-medium-3.1 | 5 | Qg4 | False | None | None |
| mistralai/mistral-medium-3.1 | 6 | Qf6 | True | c3f6 | Mate in 1 |
| mistralai/mistral-medium-3.1 | 7 | Qg6 | False | None | None |
| mistralai/mistral-medium-3.1 | 8 | Qxh7 | False | None | None |
| mistralai/mistral-medium-3.1 | 9 | Qg7 | False | None | None |
| mistralai/mistral-medium-3.1 | 10 | Qxh7 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 1 | Bd3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 2 | Be3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 3 | Bd3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 4 | BQe3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 5 | Bd5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 6 | Bd3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 7 | Bd3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 8 | Bb3 | True | a4b3 | -245 cp |
| baidu/ernie-4.5-vl-28b-a3b | 9 | Bd4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 10 | Bxg7 | False | None | None |