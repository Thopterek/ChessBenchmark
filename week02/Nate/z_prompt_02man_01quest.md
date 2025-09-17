# Chess Move Prediction Results with Legality & Stockfish Eval max tokens 30000 the rest is default

| Model | Call # | Move | Legal | UCI | Eval |
|-------|--------|------|-------|-----|------|
| x-ai/grok-code-fast-1 | 1 |  | False | None | None |
| x-ai/grok-code-fast-1 | 2 |  | False | None | None |
| x-ai/grok-code-fast-1 | 3 |  | False | None | None |
| x-ai/grok-code-fast-1 | 4 |  | False | None | None |
| x-ai/grok-code-fast-1 | 5 |  | False | None | None |
| x-ai/grok-code-fast-1 | 6 | SE | False | None | None |
| x-ai/grok-code-fast-1 | 7 |  | False | None | None |
| x-ai/grok-code-fast-1 | 8 |  | False | None | None |
| x-ai/grok-code-fast-1 | 9 |  | False | None | None |
| x-ai/grok-code-fast-1 | 10 |  | False | None | None |
| google/gemini-2.5-flash-lite | 1 | Nc7 | False | None | None |
| google/gemini-2.5-flash-lite | 2 | Nf7 | True | h6f7 | 616 cp |
| google/gemini-2.5-flash-lite | 3 | Nhf7 | True | h6f7 | 574 cp |
| google/gemini-2.5-flash-lite | 4 | Nhf7 | True | h6f7 | Mate in 3 |
| google/gemini-2.5-flash-lite | 5 | Qg5 | True | d5g5 | 419 cp |
| google/gemini-2.5-flash-lite | 6 | Qh6 | False | None | None |
| google/gemini-2.5-flash-lite | 7 | Nhf7 | True | h6f7 | Mate in 3 |
| google/gemini-2.5-flash-lite | 8 | Nf7 | True | h6f7 | Mate in 3 |
| google/gemini-2.5-flash-lite | 9 | Nf5 | True | h6f5 | -504 cp |
| google/gemini-2.5-flash-lite | 10 | Ng8 | True | h6g8 | -585 cp |
| openai/gpt-4.1-mini | 1 | Qg8 | True | d5g8 | Mate in 1 |
| openai/gpt-4.1-mini | 2 | Qxd8 | False | None | None |
| openai/gpt-4.1-mini | 3 | Qxf7 | True | d5f7 | 20 cp |
| openai/gpt-4.1-mini | 4 | Qg8 | True | d5g8 | Mate in 1 |
| openai/gpt-4.1-mini | 5 | Qxf7 | True | d5f7 | 22 cp |
| openai/gpt-4.1-mini | 6 | Qxd8 | False | None | None |
| openai/gpt-4.1-mini | 7 | Qg8 | True | d5g8 | Mate in 1 |
| openai/gpt-4.1-mini | 8 | Qg8 | True | d5g8 | Mate in 1 |
| openai/gpt-4.1-mini | 9 | Qh5 | True | d5h5 | -649 cp |
| openai/gpt-4.1-mini | 10 | Qxf7 | True | d5f7 | 48 cp |
| anthropic/claude-sonnet-4 | 1 |  | False | None | None |
| anthropic/claude-sonnet-4 | 2 |  | False | None | None |
| anthropic/claude-sonnet-4 | 3 |  | False | None | None |
| anthropic/claude-sonnet-4 | 4 |  | False | None | None |
| anthropic/claude-sonnet-4 | 5 |  | False | None | None |
| anthropic/claude-sonnet-4 | 6 |  | False | None | None |
| anthropic/claude-sonnet-4 | 7 |  | False | None | None |
| anthropic/claude-sonnet-4 | 8 |  | False | None | None |
| anthropic/claude-sonnet-4 | 9 |  | False | None | None |
| anthropic/claude-sonnet-4 | 10 |  | False | None | None |
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
| deepseek/deepseek-chat-v3.1 | 1 | Qe6 | True | d5e6 | -656 cp |
| deepseek/deepseek-chat-v3.1 | 2 | Qh5 | True | d5h5 | -649 cp |
| deepseek/deepseek-chat-v3.1 | 3 | Qd8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 4 | f3 | True | f2f3 | -478 cp |
| deepseek/deepseek-chat-v3.1 | 5 | Qd6 | True | d5d6 | 101 cp |
| deepseek/deepseek-chat-v3.1 | 6 | Qg8 | True | d5g8 | Mate in 1 |
| deepseek/deepseek-chat-v3.1 | 7 | Qd5g8 | True | d5g8 | Mate in 1 |
| deepseek/deepseek-chat-v3.1 | 8 | Qd8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 9 | Qg8 | True | d5g8 | Mate in 1 |
| deepseek/deepseek-chat-v3.1 | 10 | Qd8 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 1 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 2 | Qd3 | True | d5d3 | 111 cp |
| meta-llama/llama-3.3-8b-instruct:free | 3 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 4 | Qd3 | True | d5d3 | 51 cp |
| meta-llama/llama-3.3-8b-instruct:free | 5 | Ngf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 6 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 7 | Qd3 | True | d5d3 | 76 cp |
| meta-llama/llama-3.3-8b-instruct:free | 8 | Qa3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 9 | Qa3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 10 | Nf3 | False | None | None |
| openai/gpt-5-chat | 1 | Qg8 | True | d5g8 | Mate in 1 |
| openai/gpt-5-chat | 2 | Qg8 | True | d5g8 | Mate in 1 |
| openai/gpt-5-chat | 3 | Qg8 | True | d5g8 | Mate in 1 |
| openai/gpt-5-chat | 4 | Qg8 | True | d5g8 | Mate in 1 |
| openai/gpt-5-chat | 5 | Qg8 | True | d5g8 | Mate in 1 |
| openai/gpt-5-chat | 6 | Qg8 | True | d5g8 | Mate in 1 |
| openai/gpt-5-chat | 7 | Qg8 | True | d5g8 | Mate in 1 |
| openai/gpt-5-chat | 8 | Qg8 | True | d5g8 | Mate in 1 |
| openai/gpt-5-chat | 9 | Qg8 | True | d5g8 | Mate in 1 |
| openai/gpt-5-chat | 10 | Qg8 | True | d5g8 | Mate in 1 |
| qwen/qwen3-coder | 1 | Qe3 | False | None | None |
| qwen/qwen3-coder | 2 | Qe3 | False | None | None |
| qwen/qwen3-coder | 3 | Qe3 | False | None | None |
| qwen/qwen3-coder | 4 | Qe3 | False | None | None |
| qwen/qwen3-coder | 5 | Qe3 | False | None | None |
| qwen/qwen3-coder | 6 | Qe3 | False | None | None |
| qwen/qwen3-coder | 7 | Qe3 | False | None | None |
| qwen/qwen3-coder | 8 | Qe3 | False | None | None |
| qwen/qwen3-coder | 9 | Qe3 | False | None | None |
| qwen/qwen3-coder | 10 | Qe3 | False | None | None |
| meituan/longcat-flash-chat | 1 | Qd5 | False | None | None |
| meituan/longcat-flash-chat | 2 | Qd5 | False | None | None |
| meituan/longcat-flash-chat | 3 | Qd5 | False | None | None |
| meituan/longcat-flash-chat | 4 | Qd5 | False | None | None |
| meituan/longcat-flash-chat | 5 | Qd5 | False | None | None |
| meituan/longcat-flash-chat | 6 | Qd5 | False | None | None |
| meituan/longcat-flash-chat | 7 | Qd5 | False | None | None |
| meituan/longcat-flash-chat | 8 | Qd5 | False | None | None |
| meituan/longcat-flash-chat | 9 | Qd5 | False | None | None |
| meituan/longcat-flash-chat | 10 | Qd5 | False | None | None |
| mistralai/mistral-medium-3.1 | 1 |  | False | None | None |
| mistralai/mistral-medium-3.1 | 2 | Qxf7 | True | d5f7 | 35 cp |
| mistralai/mistral-medium-3.1 | 3 | Qxf7 | True | d5f7 | 13 cp |
| mistralai/mistral-medium-3.1 | 4 | Qxf8 | False | None | None |
| mistralai/mistral-medium-3.1 | 5 | Qh8 | False | None | None |
| mistralai/mistral-medium-3.1 | 6 | Qxf8 | False | None | None |
| mistralai/mistral-medium-3.1 | 7 | Qxh7 | False | None | None |
| mistralai/mistral-medium-3.1 | 8 | Qxf8 | False | None | None |
| mistralai/mistral-medium-3.1 | 9 | Qxf7 | True | d5f7 | 12 cp |
| mistralai/mistral-medium-3.1 | 10 | Qxf7 | True | d5f7 | 8 cp |
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