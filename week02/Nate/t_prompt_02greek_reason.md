# Chess Move Prediction Results with Legality & Stockfish Eval

| Model | Call # | Move | Legal | UCI | Eval |
|-------|--------|------|-------|-----|------|
| x-ai/grok-code-fast-1 | 1 |  | False | None | None |
| x-ai/grok-code-fast-1 | 2 |  | False | None | None |
| x-ai/grok-code-fast-1 | 3 |  | False | None | None |
| x-ai/grok-code-fast-1 | 4 |  | False | None | None |
| x-ai/grok-code-fast-1 | 5 |  | False | None | None |
| x-ai/grok-code-fast-1 | 6 |  | False | None | None |
| x-ai/grok-code-fast-1 | 7 |  | False | None | None |
| x-ai/grok-code-fast-1 | 8 |  | False | None | None |
| x-ai/grok-code-fast-1 | 9 |  | False | None | None |
| x-ai/grok-code-fast-1 | 10 |  | False | None | None |
| google/gemini-2.5-flash-lite | 1 | Qh7 | False | None | None |
| google/gemini-2.5-flash-lite | 2 | Qxh7 | False | None | None |
| google/gemini-2.5-flash-lite | 3 |  | False | None | None |
| google/gemini-2.5-flash-lite | 4 |  | False | None | None |
| google/gemini-2.5-flash-lite | 5 | Ne7 | False | None | None |
| google/gemini-2.5-flash-lite | 6 | Nd7 | False | None | None |
| google/gemini-2.5-flash-lite | 7 |  | False | None | None |
| google/gemini-2.5-flash-lite | 8 | Nf7 | True | h6f7 | 616 cp |
| google/gemini-2.5-flash-lite | 9 |  | False | None | None |
| google/gemini-2.5-flash-lite | 10 | Nf7 | True | h6f7 | 574 cp |
| openai/gpt-4.1-mini | 1 | Qxf7 | True | d5f7 | 0 cp |
| openai/gpt-4.1-mini | 2 | Qg8 | True | d5g8 | Mate in 1 |
| openai/gpt-4.1-mini | 3 | Qxf7 | True | d5f7 | 26 cp |
| openai/gpt-4.1-mini | 4 | Qxh5 | True | d5h5 | -638 cp |
| openai/gpt-4.1-mini | 5 | Qxf7 | True | d5f7 | 9 cp |
| openai/gpt-4.1-mini | 6 | Qg8 | True | d5g8 | Mate in 1 |
| openai/gpt-4.1-mini | 7 | Qg8 | True | d5g8 | Mate in 1 |
| openai/gpt-4.1-mini | 8 | Qg8 | True | d5g8 | Mate in 1 |
| openai/gpt-4.1-mini | 9 | Qg8 | True | d5g8 | Mate in 1 |
| openai/gpt-4.1-mini | 10 | Qg8 | True | d5g8 | Mate in 1 |
| anthropic/claude-sonnet-4 | 1 | Qg8 | True | d5g8 | Mate in 1 |
| anthropic/claude-sonnet-4 | 2 |  | False | None | None |
| anthropic/claude-sonnet-4 | 3 |  | False | None | None |
| anthropic/claude-sonnet-4 | 4 |  | False | None | None |
| anthropic/claude-sonnet-4 | 5 |  | False | None | None |
| anthropic/claude-sonnet-4 | 6 |  | False | None | None |
| anthropic/claude-sonnet-4 | 7 |  | False | None | None |
| anthropic/claude-sonnet-4 | 8 |  | False | None | None |
| anthropic/claude-sonnet-4 | 9 | Qg8 | True | d5g8 | Mate in 1 |
| anthropic/claude-sonnet-4 | 10 |  | False | None | None |
| openai/gpt-3.5-turbo-instruct | 1 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 2 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 3 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 4 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 5 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 6 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 7 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 8 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 9 | Qe3 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 10 | SE | False | None | None |
| deepseek/deepseek-chat-v3.1 | 1 | Qg8 | True | d5g8 | Mate in 1 |
| deepseek/deepseek-chat-v3.1 | 2 | e5 | True | e4e5 | -513 cp |
| deepseek/deepseek-chat-v3.1 | 3 | Be3 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 4 | Qd8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 5 | Qxg8 | True | d5g8 | Mate in 1 |
| deepseek/deepseek-chat-v3.1 | 6 | Qd8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 7 | Qxg8 | True | d5g8 | Mate in 1 |
| deepseek/deepseek-chat-v3.1 | 8 | Qd8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 9 | Rh8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 10 | Qxg4 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 1 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 2 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 3 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 4 | Nh2 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 5 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 6 | Nh2 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 7 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 8 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 9 | Nf3 | False | None | None |
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
| qwen/qwen3-coder | 1 | Qe6 | True | d5e6 | -665 cp |
| qwen/qwen3-coder | 2 | Qe6 | True | d5e6 | -646 cp |
| qwen/qwen3-coder | 3 | Qe6 | True | d5e6 | -664 cp |
| qwen/qwen3-coder | 4 | Qe6 | True | d5e6 | -647 cp |
| qwen/qwen3-coder | 5 | Qe6 | True | d5e6 | -649 cp |
| qwen/qwen3-coder | 6 | Qe6 | True | d5e6 | -657 cp |
| qwen/qwen3-coder | 7 | Qe3 | False | None | None |
| qwen/qwen3-coder | 8 | Qe6 | True | d5e6 | -650 cp |
| qwen/qwen3-coder | 9 | Qe6 | True | d5e6 | -656 cp |
| qwen/qwen3-coder | 10 | Qe6 | True | d5e6 | -660 cp |
| meituan/longcat-flash-chat | 1 | Qd8 | False | None | None |
| meituan/longcat-flash-chat | 2 | Qd8 | False | None | None |
| meituan/longcat-flash-chat | 3 | Qd5 | False | None | None |
| meituan/longcat-flash-chat | 4 | Qd5 | False | None | None |
| meituan/longcat-flash-chat | 5 | Qd5 | False | None | None |
| meituan/longcat-flash-chat | 6 | Qd5 | False | None | None |
| meituan/longcat-flash-chat | 7 | Qd8 | False | None | None |
| meituan/longcat-flash-chat | 8 | Qe3 | False | None | None |
| meituan/longcat-flash-chat | 9 | Qd5 | False | None | None |
| meituan/longcat-flash-chat | 10 | Qd5 | False | None | None |
| mistralai/mistral-medium-3.1 | 1 | Qh8 | False | None | None |
| mistralai/mistral-medium-3.1 | 2 | Qh5 | True | d5h5 | -624 cp |
| mistralai/mistral-medium-3.1 | 3 | Qh5 | True | d5h5 | -630 cp |
| mistralai/mistral-medium-3.1 | 4 | Qh5 | True | d5h5 | -620 cp |
| mistralai/mistral-medium-3.1 | 5 | Qh5 | True | d5h5 | -621 cp |
| mistralai/mistral-medium-3.1 | 6 | Qh5 | True | d5h5 | -632 cp |
| mistralai/mistral-medium-3.1 | 7 | Qh5 | True | d5h5 | -637 cp |
| mistralai/mistral-medium-3.1 | 8 | Qh5 | True | d5h5 | -626 cp |
| mistralai/mistral-medium-3.1 | 9 | Qh5 | True | d5h5 | -630 cp |
| mistralai/mistral-medium-3.1 | 10 | Qh5 | True | d5h5 | -623 cp |
| baidu/ernie-4.5-vl-28b-a3b | 1 | Qe3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 2 | Qd4 | True | d5d4 | 406 cp |
| baidu/ernie-4.5-vl-28b-a3b | 3 | Qd3 | True | d5d3 | 22 cp |
| baidu/ernie-4.5-vl-28b-a3b | 4 | Qe3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 5 | Qe3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 6 | Qd4 | True | d5d4 | 427 cp |
| baidu/ernie-4.5-vl-28b-a3b | 7 | Qd3 | True | d5d3 | 60 cp |
| baidu/ernie-4.5-vl-28b-a3b | 8 | Qd4 | True | d5d4 | 422 cp |
| baidu/ernie-4.5-vl-28b-a3b | 9 | Qd4 | True | d5d4 | 435 cp |
| baidu/ernie-4.5-vl-28b-a3b | 10 | Qd4 | True | d5d4 | 452 cp |