# Chess Move Prediction Results with Legality & Stockfish Eval

| Model | Call # | Move | Legal | UCI | Eval |
|-------|--------|------|-------|-----|------|
| google/gemini-2.5-flash-lite | 1 | Qh3 | False | None | None |
| google/gemini-2.5-flash-lite | 2 | Qf7 | False | None | None |
| google/gemini-2.5-flash-lite | 3 | e3 | False | None | None |
| google/gemini-2.5-flash-lite | 4 | Qh3 | False | None | None |
| google/gemini-2.5-flash-lite | 5 | Qc7 | True | c3c7 | -522 cp |
| google/gemini-2.5-flash-lite | 6 | Qe3 | True | c3e3 | -479 cp |
| google/gemini-2.5-flash-lite | 7 | Qe8 | False | None | None |
| google/gemini-2.5-flash-lite | 8 | Qe3 | True | c3e3 | -477 cp |
| google/gemini-2.5-flash-lite | 9 | Qc7 | True | c3c7 | -504 cp |
| google/gemini-2.5-flash-lite | 10 | Qd3 | True | c3d3 | -154 cp |
| openai/gpt-4.1-mini | 1 | Qxc6 | True | c3c6 | -531 cp |
| openai/gpt-4.1-mini | 2 | Qxc6 | True | c3c6 | -552 cp |
| openai/gpt-4.1-mini | 3 | Qxc6 | True | c3c6 | -537 cp |
| openai/gpt-4.1-mini | 4 | Qxc6 | True | c3c6 | -571 cp |
| openai/gpt-4.1-mini | 5 | Qxc6 | True | c3c6 | -566 cp |
| openai/gpt-4.1-mini | 6 | Qxc6 | True | c3c6 | -569 cp |
| openai/gpt-4.1-mini | 7 | Qxc6 | True | c3c6 | -560 cp |
| openai/gpt-4.1-mini | 8 | Qa5 | True | c3a5 | -399 cp |
| openai/gpt-4.1-mini | 9 | Qxc6 | True | c3c6 | -542 cp |
| openai/gpt-4.1-mini | 10 | Qxc6 | True | c3c6 | -579 cp |
| anthropic/claude-sonnet-4 | 1 |  | False | None | None |
| anthropic/claude-sonnet-4 | 2 |  | False | None | None |
| anthropic/claude-sonnet-4 | 3 |  | False | None | None |
| anthropic/claude-sonnet-4 | 4 | Qc8 | False | None | None |
| anthropic/claude-sonnet-4 | 5 | Qc8 | False | None | None |
| anthropic/claude-sonnet-4 | 6 |  | False | None | None |
| anthropic/claude-sonnet-4 | 7 |  | False | None | None |
| anthropic/claude-sonnet-4 | 8 |  | False | None | None |
| anthropic/claude-sonnet-4 | 9 | Qc8 | False | None | None |
| anthropic/claude-sonnet-4 | 10 | Qc8 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 1 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 2 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 3 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 4 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 5 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 6 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 7 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 8 | Nf5 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 9 | Qb6 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 10 | SE | False | None | None |
| deepseek/deepseek-chat-v3.1 | 1 | Qc6 | True | c3c6 | -565 cp |
| deepseek/deepseek-chat-v3.1 | 2 | Qc6 | True | c3c6 | -575 cp |
| deepseek/deepseek-chat-v3.1 | 3 | Qc3xg7 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 4 | Qh3 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 5 | Qc3xd4 | True | c3d4 | -460 cp |
| deepseek/deepseek-chat-v3.1 | 6 | Nxe5 | True | f3e5 | -247 cp |
| deepseek/deepseek-chat-v3.1 | 7 | Qc6 | True | c3c6 | -566 cp |
| deepseek/deepseek-chat-v3.1 | 8 | Qc3xg7 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 9 | Qc7 | True | c3c7 | -500 cp |
| deepseek/deepseek-chat-v3.1 | 10 | Qc3xg7 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 1 | Ni3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 2 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 3 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 4 | Qd2 | True | c3d2 | -190 cp |
| meta-llama/llama-3.3-8b-instruct:free | 5 | Nc3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 6 | Nd4 | True | f3d4 | -263 cp |
| meta-llama/llama-3.3-8b-instruct:free | 7 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 8 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 9 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 10 | Qd2 | True | c3d2 | -200 cp |
| openai/gpt-5-chat | 1 | SE | False | None | None |
| openai/gpt-5-chat | 2 | SE | False | None | None |
| openai/gpt-5-chat | 3 | Qxa5 | True | c3a5 | -487 cp |
| openai/gpt-5-chat | 4 | SE | False | None | None |
| openai/gpt-5-chat | 5 | Qc7 | True | c3c7 | -518 cp |
| openai/gpt-5-chat | 6 | Qc7 | True | c3c7 | -498 cp |
| openai/gpt-5-chat | 7 | Qc7 | True | c3c7 | -523 cp |
| openai/gpt-5-chat | 8 | Qxa5 | True | c3a5 | -472 cp |
| openai/gpt-5-chat | 9 | Qxa5 | True | c3a5 | -483 cp |
| openai/gpt-5-chat | 10 | Qc7 | True | c3c7 | -530 cp |
| qwen/qwen3-coder | 1 | Qe3 | True | c3e3 | -492 cp |
| qwen/qwen3-coder | 2 | Qe3 | True | c3e3 | -498 cp |
| qwen/qwen3-coder | 3 | Qe3 | True | c3e3 | -489 cp |
| qwen/qwen3-coder | 4 | Qe3 | True | c3e3 | -494 cp |
| qwen/qwen3-coder | 5 | Qe3 | True | c3e3 | -514 cp |
| qwen/qwen3-coder | 6 | Qe3 | True | c3e3 | -504 cp |
| qwen/qwen3-coder | 7 | Qe3 | True | c3e3 | -520 cp |
| qwen/qwen3-coder | 8 | Qe3 | True | c3e3 | -480 cp |
| qwen/qwen3-coder | 9 | Qe3 | True | c3e3 | -497 cp |
| qwen/qwen3-coder | 10 | Qe3 | True | c3e3 | -470 cp |
| meituan/longcat-flash-chat | 1 | Qc3 | False | None | None |
| meituan/longcat-flash-chat | 2 | Qc3 | False | None | None |
| meituan/longcat-flash-chat | 3 | Qc3 | False | None | None |
| meituan/longcat-flash-chat | 4 | Qc3 | False | None | None |
| meituan/longcat-flash-chat | 5 | Qc7 | True | c3c7 | -517 cp |
| meituan/longcat-flash-chat | 6 | Qc3 | False | None | None |
| meituan/longcat-flash-chat | 7 | Qc3 | False | None | None |
| meituan/longcat-flash-chat | 8 | Qxg7 | False | None | None |
| meituan/longcat-flash-chat | 9 | Qc3 | False | None | None |
| meituan/longcat-flash-chat | 10 | Qc3 | False | None | None |
| mistralai/mistral-medium-3.1 | 1 | Qe5 | True | c3e5 | -452 cp |
| mistralai/mistral-medium-3.1 | 2 | Qxf6 | True | c3f6 | Mate in 1 |
| mistralai/mistral-medium-3.1 | 3 | Qd6 | False | None | None |
| mistralai/mistral-medium-3.1 | 4 | Qxg6 | False | None | None |
| mistralai/mistral-medium-3.1 | 5 | Qc6 | True | c3c6 | -550 cp |
| mistralai/mistral-medium-3.1 | 6 | Qxf6 | True | c3f6 | Mate in 1 |
| mistralai/mistral-medium-3.1 | 7 |  | False | None | None |
| mistralai/mistral-medium-3.1 | 8 | Qxf6 | True | c3f6 | Mate in 1 |
| mistralai/mistral-medium-3.1 | 9 | Qxd8 | False | None | None |
| mistralai/mistral-medium-3.1 | 10 | Qxf6 | True | c3f6 | Mate in 1 |
| baidu/ernie-4.5-vl-28b-a3b | 1 | Bc4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 2 | Bd3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 3 | SE | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 4 | SE | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 5 | Bc4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 6 | Bb3 | True | a4b3 | -280 cp |
| baidu/ernie-4.5-vl-28b-a3b | 7 | SE | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 8 | Bd3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 9 | Bc5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 10 | SE | False | None | None |