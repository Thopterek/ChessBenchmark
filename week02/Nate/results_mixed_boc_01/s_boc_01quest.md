# Chess Move Prediction Results with Legality & Stockfish Eval

| Model | Call # | Move | Legal | UCI | Eval |
|-------|--------|------|-------|-----|------|
| google/gemini-2.5-flash-lite | 1 | Qg6 | False | None | None |
| google/gemini-2.5-flash-lite | 2 |  | False | None | None |
| google/gemini-2.5-flash-lite | 3 | Qhh4 | False | None | None |
| google/gemini-2.5-flash-lite | 4 | Qg6 | False | None | None |
| google/gemini-2.5-flash-lite | 5 | Qh5 | False | None | None |
| google/gemini-2.5-flash-lite | 6 | Nf6 | False | None | None |
| google/gemini-2.5-flash-lite | 7 |  | False | None | None |
| google/gemini-2.5-flash-lite | 8 | Qxh6 | False | None | None |
| google/gemini-2.5-flash-lite | 9 |  | False | None | None |
| google/gemini-2.5-flash-lite | 10 |  | False | None | None |
| openai/gpt-4.1-mini | 1 | Qf6 | False | None | None |
| openai/gpt-4.1-mini | 2 | Qg8 | True | d5g8 | Mate in 1 |
| openai/gpt-4.1-mini | 3 | Qh5 | False | None | None |
| openai/gpt-4.1-mini | 4 | Qh5 | False | None | None |
| openai/gpt-4.1-mini | 5 | Qxf7 | True | d5f7 | -231 cp |
| openai/gpt-4.1-mini | 6 | Rf1f7 | False | None | None |
| openai/gpt-4.1-mini | 7 | Qh5 | False | None | None |
| openai/gpt-4.1-mini | 8 | Qxf7 | True | d5f7 | -263 cp |
| openai/gpt-4.1-mini | 9 | Qh5 | False | None | None |
| openai/gpt-4.1-mini | 10 | Qg8 | True | d5g8 | Mate in 1 |
| anthropic/claude-sonnet-4 | 1 | Qxf7 | True | d5f7 | -239 cp |
| anthropic/claude-sonnet-4 | 2 | Qg8 | True | d5g8 | Mate in 1 |
| anthropic/claude-sonnet-4 | 3 | Qf7 | True | d5f7 | -221 cp |
| anthropic/claude-sonnet-4 | 4 | Qg8 | True | d5g8 | Mate in 1 |
| anthropic/claude-sonnet-4 | 5 | Qg8 | True | d5g8 | Mate in 1 |
| anthropic/claude-sonnet-4 | 6 | Qg8 | True | d5g8 | Mate in 1 |
| anthropic/claude-sonnet-4 | 7 | Qf7 | True | d5f7 | -234 cp |
| anthropic/claude-sonnet-4 | 8 | Qg8 | True | d5g8 | Mate in 1 |
| anthropic/claude-sonnet-4 | 9 | Qg8 | True | d5g8 | Mate in 1 |
| anthropic/claude-sonnet-4 | 10 |  | False | None | None |
| openai/gpt-3.5-turbo-instruct | 1 | text : Qe5 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 2 |  | False | None | None |
| openai/gpt-3.5-turbo-instruct | 3 |  | False | None | None |
| openai/gpt-3.5-turbo-instruct | 4 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 5 |  | False | None | None |
| openai/gpt-3.5-turbo-instruct | 6 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 7 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 8 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 9 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 10 | SE | False | None | None |
| deepseek/deepseek-chat-v3.1 | 1 | Qh7 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 2 | Qh8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 3 | Qf7 | True | d5f7 | -228 cp |
| deepseek/deepseek-chat-v3.1 | 4 | Qd8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 5 | Qd8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 6 | Qd8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 7 | Qh8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 8 | Qd8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 9 | Qd8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 10 | Qd6 | True | d5d6 | -274 cp |
| meta-llama/llama-3.3-8b-instruct:free | 1 | Nh2 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 2 | Nh4 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 3 | Qe3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 4 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 5 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 6 | Qe3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 7 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 8 | Nh2 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 9 | Nh2 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 10 | Nh2 | False | None | None |
| openai/gpt-5-chat | 1 | Qg8 | True | d5g8 | Mate in 1 |
| openai/gpt-5-chat | 2 | Qg8 | True | d5g8 | Mate in 1 |
| openai/gpt-5-chat | 3 | Qg8 | True | d5g8 | Mate in 1 |
| openai/gpt-5-chat | 4 |  | False | None | None |
| openai/gpt-5-chat | 5 | Qg8 | True | d5g8 | Mate in 1 |
| openai/gpt-5-chat | 6 | Qg8 | True | d5g8 | Mate in 1 |
| openai/gpt-5-chat | 7 | Qg8 | True | d5g8 | Mate in 1 |
| openai/gpt-5-chat | 8 | Qg8 | True | d5g8 | Mate in 1 |
| openai/gpt-5-chat | 9 |  | False | None | None |
| openai/gpt-5-chat | 10 |  | False | None | None |
| qwen/qwen3-coder | 1 |  | False | None | None |
| qwen/qwen3-coder | 2 |  | False | None | None |
| qwen/qwen3-coder | 3 | Qe3 | False | None | None |
| qwen/qwen3-coder | 4 | Qh7 | False | None | None |
| qwen/qwen3-coder | 5 |  | False | None | None |
| qwen/qwen3-coder | 6 |  | False | None | None |
| qwen/qwen3-coder | 7 |  | False | None | None |
| qwen/qwen3-coder | 8 |  | False | None | None |
| qwen/qwen3-coder | 9 |  | False | None | None |
| qwen/qwen3-coder | 10 | Qh7 | False | None | None |
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
| mistralai/mistral-medium-3.1 | 1 | Qg8 | True | d5g8 | Mate in 1 |
| mistralai/mistral-medium-3.1 | 2 | Qg8 | True | d5g8 | Mate in 1 |
| mistralai/mistral-medium-3.1 | 3 | Qg8 | True | d5g8 | Mate in 1 |
| mistralai/mistral-medium-3.1 | 4 | Qg8 | True | d5g8 | Mate in 1 |
| mistralai/mistral-medium-3.1 | 5 | Qg8 | True | d5g8 | Mate in 1 |
| mistralai/mistral-medium-3.1 | 6 | Qh7 | False | None | None |
| mistralai/mistral-medium-3.1 | 7 | Qh7 | False | None | None |
| mistralai/mistral-medium-3.1 | 8 | Qh7 | False | None | None |
| mistralai/mistral-medium-3.1 | 9 | Qg8 | True | d5g8 | Mate in 1 |
| mistralai/mistral-medium-3.1 | 10 | Qg8 | True | d5g8 | Mate in 1 |
| baidu/ernie-4.5-vl-28b-a3b | 1 | Qa4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 2 | d4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 3 | e4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 4 | Nd5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 5 | Qe3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 6 | Qe3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 7 | Qe3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 8 | Qe3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 9 | e4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 10 | Qe3 | False | None | None |