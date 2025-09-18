# Chess Move Prediction Results with Legality & Stockfish Eval

| Model | Call # | Move | Legal | UCI | Eval |
|-------|--------|------|-------|-----|------|
| x-ai/grok-code-fast-1 | 1 | Qxc7 | True | c3c7 | -522 cp |
| x-ai/grok-code-fast-1 | 2 | Qxf6 | True | c3f6 | Mate in 1 |
| x-ai/grok-code-fast-1 | 3 |  | False | None | None |
| x-ai/grok-code-fast-1 | 4 |  | False | None | None |
| x-ai/grok-code-fast-1 | 5 | SE | False | None | None |
| x-ai/grok-code-fast-1 | 6 |  | False | None | None |
| x-ai/grok-code-fast-1 | 7 |  | False | None | None |
| x-ai/grok-code-fast-1 | 8 |  | False | None | None |
| x-ai/grok-code-fast-1 | 9 |  | False | None | None |
| x-ai/grok-code-fast-1 | 10 |  | False | None | None |
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
| openai/gpt-4.1-mini | 1 | Qxc7 | True | c3c7 | -499 cp |
| openai/gpt-4.1-mini | 2 | Qxc7 | True | c3c7 | -495 cp |
| openai/gpt-4.1-mini | 3 | Qxc7 | True | c3c7 | -503 cp |
| openai/gpt-4.1-mini | 4 | Qxc7 | True | c3c7 | -499 cp |
| openai/gpt-4.1-mini | 5 | Qxc7 | True | c3c7 | -511 cp |
| openai/gpt-4.1-mini | 6 | Qxc7 | True | c3c7 | -521 cp |
| openai/gpt-4.1-mini | 7 | Qxc7 | True | c3c7 | -513 cp |
| openai/gpt-4.1-mini | 8 | Qxc7 | True | c3c7 | -504 cp |
| openai/gpt-4.1-mini | 9 | Qxc7 | True | c3c7 | -498 cp |
| openai/gpt-4.1-mini | 10 | Qxc7 | True | c3c7 | -503 cp |
| anthropic/claude-sonnet-4 | 1 |  | False | None | None |
| anthropic/claude-sonnet-4 | 2 | Qc8 | False | None | None |
| anthropic/claude-sonnet-4 | 3 | Qc8 | False | None | None |
| anthropic/claude-sonnet-4 | 4 | Qc8 | False | None | None |
| anthropic/claude-sonnet-4 | 5 | Qc8 | False | None | None |
| anthropic/claude-sonnet-4 | 6 |  | False | None | None |
| anthropic/claude-sonnet-4 | 7 |  | False | None | None |
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
| openai/gpt-3.5-turbo-instruct | 8 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 9 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 10 | SE | False | None | None |
| deepseek/deepseek-chat-v3.1 | 1 | Qh5 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 2 | Qh6 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 3 | Qh6 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 4 | Qh6 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 5 | Qh6 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 6 | Qc6 | True | c3c6 | -582 cp |
| deepseek/deepseek-chat-v3.1 | 7 | Qh3 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 8 | Qh6 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 9 | Qc6 | True | c3c6 | -559 cp |
| deepseek/deepseek-chat-v3.1 | 10 | Qh6 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 1 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 2 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 3 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 4 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 5 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 6 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 7 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 8 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 9 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 10 | Nf3 | False | None | None |
| openai/gpt-5-chat | 1 | Qxa5 | True | c3a5 | -469 cp |
| openai/gpt-5-chat | 2 | Qxa5 | True | c3a5 | -465 cp |
| openai/gpt-5-chat | 3 | Qxa5 | True | c3a5 | -465 cp |
| openai/gpt-5-chat | 4 |  | False | None | None |
| openai/gpt-5-chat | 5 | Qxa5 | True | c3a5 | -484 cp |
| openai/gpt-5-chat | 6 |  | False | None | None |
| openai/gpt-5-chat | 7 |  | False | None | None |
| openai/gpt-5-chat | 8 | Qc7 | True | c3c7 | -504 cp |
| openai/gpt-5-chat | 9 |  | False | None | None |
| openai/gpt-5-chat | 10 |  | False | None | None |
| qwen/qwen3-coder | 1 | Qe3 | True | c3e3 | -494 cp |
| qwen/qwen3-coder | 2 |  | False | None | None |
| qwen/qwen3-coder | 3 |  | False | None | None |
| qwen/qwen3-coder | 4 | Qe3 | True | c3e3 | -466 cp |
| qwen/qwen3-coder | 5 | Qe3 | True | c3e3 | -522 cp |
| qwen/qwen3-coder | 6 |  | False | None | None |
| qwen/qwen3-coder | 7 | Qe3 | True | c3e3 | -489 cp |
| qwen/qwen3-coder | 8 |  | False | None | None |
| qwen/qwen3-coder | 9 |  | False | None | None |
| qwen/qwen3-coder | 10 | Qe3 | True | c3e3 | -486 cp |
| meituan/longcat-flash-chat | 1 | Qa5 | True | c3a5 | -486 cp |
| meituan/longcat-flash-chat | 2 | Qc3 | False | None | None |
| meituan/longcat-flash-chat | 3 | Qa5 | True | c3a5 | -473 cp |
| meituan/longcat-flash-chat | 4 | Qc3 | False | None | None |
| meituan/longcat-flash-chat | 5 | Qc3 | False | None | None |
| meituan/longcat-flash-chat | 6 | Qa5 | True | c3a5 | -487 cp |
| meituan/longcat-flash-chat | 7 | Qa5 | True | c3a5 | -477 cp |
| meituan/longcat-flash-chat | 8 | Qc3 | False | None | None |
| meituan/longcat-flash-chat | 9 | Qc3 | False | None | None |
| meituan/longcat-flash-chat | 10 | Qc3 | False | None | None |
| mistralai/mistral-medium-3.1 | 1 | Qh6 | False | None | None |
| mistralai/mistral-medium-3.1 | 2 | Qxf7 | False | None | None |
| mistralai/mistral-medium-3.1 | 3 | Qh6 | False | None | None |
| mistralai/mistral-medium-3.1 | 4 | Qh7 | False | None | None |
| mistralai/mistral-medium-3.1 | 5 | Qh7 | False | None | None |
| mistralai/mistral-medium-3.1 | 6 | Qxf7 | False | None | None |
| mistralai/mistral-medium-3.1 | 7 | Qh7 | False | None | None |
| mistralai/mistral-medium-3.1 | 8 | Qxf7 | False | None | None |
| mistralai/mistral-medium-3.1 | 9 | Qh7 | False | None | None |
| mistralai/mistral-medium-3.1 | 10 | Qxf7 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 1 | SE | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 2 | SE | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 3 | SE | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 4 | SE | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 5 | SE | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 6 | SE | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 7 | SE | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 8 | SE | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 9 | SE | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 10 | SE | False | None | None |