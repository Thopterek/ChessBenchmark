# Chess Move Prediction Results with Legality & Stockfish Eval

# Temperature default, max tokens 20000, top_p default, wrong example in 02quest.txt

| Model | Call # | Move | Legal | UCI | Eval |
|-------|--------|------|-------|-----|------|
| x-ai/grok-code-fast-1 | 1 |  | False | None | None |
| x-ai/grok-code-fast-1 | 2 |  | False | None | None |
| x-ai/grok-code-fast-1 | 3 |  | False | None | None |
| x-ai/grok-code-fast-1 | 4 |  | False | None | None |
| x-ai/grok-code-fast-1 | 5 |  | False | None | None |
| x-ai/grok-code-fast-1 | 6 |  | False | None | None |
| x-ai/grok-code-fast-1 | 7 | Qxf6 | True | c3f6 | Mate in 1 |
| x-ai/grok-code-fast-1 | 8 |  | False | None | None |
| x-ai/grok-code-fast-1 | 9 |  | False | None | None |
| x-ai/grok-code-fast-1 | 10 |  | False | None | None |
| google/gemini-2.5-flash-lite | 1 |  | False | None | None |
| google/gemini-2.5-flash-lite | 2 |  | False | None | None |
| google/gemini-2.5-flash-lite | 3 |  | False | None | None |
| google/gemini-2.5-flash-lite | 4 |  | False | None | None |
| google/gemini-2.5-flash-lite | 5 |  | False | None | None |
| google/gemini-2.5-flash-lite | 6 | Qf3 | False | None | None |
| google/gemini-2.5-flash-lite | 7 |  | False | None | None |
| google/gemini-2.5-flash-lite | 8 | Qg3 | False | None | None |
| google/gemini-2.5-flash-lite | 9 |  | False | None | None |
| google/gemini-2.5-flash-lite | 10 | Nh4 | True | f3h4 | -284 cp |
| openai/gpt-4.1-mini | 1 | Qxc6 | True | c3c6 | -554 cp |
| openai/gpt-4.1-mini | 2 | Qe8 | False | None | None |
| openai/gpt-4.1-mini | 3 | Qxc6 | True | c3c6 | -574 cp |
| openai/gpt-4.1-mini | 4 | Qxc7 | True | c3c7 | -507 cp |
| openai/gpt-4.1-mini | 5 | Qxc6 | True | c3c6 | -562 cp |
| openai/gpt-4.1-mini | 6 | Qxc6 | True | c3c6 | -547 cp |
| openai/gpt-4.1-mini | 7 | Qxc6 | True | c3c6 | -573 cp |
| openai/gpt-4.1-mini | 8 | Qxc6 | True | c3c6 | -565 cp |
| openai/gpt-4.1-mini | 9 | Qxc6 | True | c3c6 | -571 cp |
| openai/gpt-4.1-mini | 10 |  | False | None | None |
| anthropic/claude-sonnet-4 | 1 |  | False | None | None |
| anthropic/claude-sonnet-4 | 2 | Qc8 | False | None | None |
| anthropic/claude-sonnet-4 | 3 | Qc8 | False | None | None |
| anthropic/claude-sonnet-4 | 4 | Qc8 | False | None | None |
| anthropic/claude-sonnet-4 | 5 | Qc8 | False | None | None |
| anthropic/claude-sonnet-4 | 6 | Qc8 | False | None | None |
| anthropic/claude-sonnet-4 | 7 | Qc8 | False | None | None |
| anthropic/claude-sonnet-4 | 8 | Qc8 | False | None | None |
| anthropic/claude-sonnet-4 | 9 | Qc8 | False | None | None |
| anthropic/claude-sonnet-4 | 10 |  | False | None | None |
| openai/gpt-3.5-turbo-instruct | 1 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 2 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 3 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 4 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 5 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 6 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 7 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 8 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 9 |  | False | None | None |
| openai/gpt-3.5-turbo-instruct | 10 | SE | False | None | None |
| deepseek/deepseek-chat-v3.1 | 1 | Qc3xg7 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 2 | Qh7 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 3 | Qc3xg7 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 4 | Qc6 | True | c3c6 | -574 cp |
| deepseek/deepseek-chat-v3.1 | 5 | Qc6 | True | c3c6 | -557 cp |
| deepseek/deepseek-chat-v3.1 | 6 | Nxh6 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 7 | Qxg4 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 8 | Qxf6 | True | c3f6 | Mate in 1 |
| deepseek/deepseek-chat-v3.1 | 9 | Qh7 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 10 | Qh3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 1 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 2 | Nh2 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 3 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 4 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 5 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 6 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 7 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 8 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 9 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 10 | Nh2 | False | None | None |
| openai/gpt-5-chat | 1 | SE | False | None | None |
| openai/gpt-5-chat | 2 | SE | False | None | None |
| openai/gpt-5-chat | 3 | SE | False | None | None |
| openai/gpt-5-chat | 4 |  | False | None | None |
| openai/gpt-5-chat | 5 | SE | False | None | None |
| openai/gpt-5-chat | 6 |  | False | None | None |
| openai/gpt-5-chat | 7 |  | False | None | None |
| openai/gpt-5-chat | 8 | SE | False | None | None |
| openai/gpt-5-chat | 9 |  | False | None | None |
| openai/gpt-5-chat | 10 |  | False | None | None |
| qwen/qwen3-coder | 1 | Qe3 | True | c3e3 | -493 cp |
| qwen/qwen3-coder | 2 | Qe3 | True | c3e3 | -486 cp |
| qwen/qwen3-coder | 3 | Qe3 | True | c3e3 | -480 cp |
| qwen/qwen3-coder | 4 |  | False | None | None |
| qwen/qwen3-coder | 5 |  | False | None | None |
| qwen/qwen3-coder | 6 |  | False | None | None |
| qwen/qwen3-coder | 7 | Qe3 | True | c3e3 | -510 cp |
| qwen/qwen3-coder | 8 | Qe3 | True | c3e3 | -499 cp |
| qwen/qwen3-coder | 9 | Qe3 | True | c3e3 | -488 cp |
| qwen/qwen3-coder | 10 | Qe3 | True | c3e3 | -489 cp |
| meituan/longcat-flash-chat | 1 | Qc3 | False | None | None |
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
| mistralai/mistral-medium-3.1 | 2 | Qh7 | False | None | None |
| mistralai/mistral-medium-3.1 | 3 | Qxh7 | False | None | None |
| mistralai/mistral-medium-3.1 | 4 | Qxf7 | False | None | None |
| mistralai/mistral-medium-3.1 | 5 | Qg6 | False | None | None |
| mistralai/mistral-medium-3.1 | 6 | Qf6 | True | c3f6 | Mate in 1 |
| mistralai/mistral-medium-3.1 | 7 | Qxh7 | False | None | None |
| mistralai/mistral-medium-3.1 | 8 | Qf6 | True | c3f6 | Mate in 1 |
| mistralai/mistral-medium-3.1 | 9 | Qxh7 | False | None | None |
| mistralai/mistral-medium-3.1 | 10 | Qh7 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 1 | Bxg7 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 2 | Bd3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 3 | BQe3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 4 | Bd3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 5 | Bd3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 6 | Bd3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 7 | Bd3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 8 | Bb3 | True | a4b3 | -222 cp |
| baidu/ernie-4.5-vl-28b-a3b | 9 | Bc5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 10 | Bd3 | False | None | None |