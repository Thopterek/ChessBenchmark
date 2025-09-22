# Chess Move Prediction Results with Legality & Stockfish Eval

| Model | Call # | Move | Legal | UCI | Eval |
|-------|--------|------|-------|-----|------|
| google/gemini-2.5-flash-lite | 1 | Qb8 | False | None | None |
| google/gemini-2.5-flash-lite | 2 | Qd3 | True | c3d3 | -150 cp |
| google/gemini-2.5-flash-lite | 3 | Qg7 | False | None | None |
| google/gemini-2.5-flash-lite | 4 | Qg7 | False | None | None |
| google/gemini-2.5-flash-lite | 5 | Qxe4 | False | None | None |
| google/gemini-2.5-flash-lite | 6 |  | False | None | None |
| google/gemini-2.5-flash-lite | 7 | Qd3 | True | c3d3 | -131 cp |
| google/gemini-2.5-flash-lite | 8 | Qxb7 | False | None | None |
| google/gemini-2.5-flash-lite | 9 | Bxa4 | False | None | None |
| google/gemini-2.5-flash-lite | 10 | Qg7 | False | None | None |
| openai/gpt-4.1-mini | 1 | Qxc6 | True | c3c6 | -587 cp |
| openai/gpt-4.1-mini | 2 | Qxc7 | True | c3c7 | -512 cp |
| openai/gpt-4.1-mini | 3 | Qxc6 | True | c3c6 | -551 cp |
| openai/gpt-4.1-mini | 4 | Qxc6 | True | c3c6 | -533 cp |
| openai/gpt-4.1-mini | 5 | Qxc7 | True | c3c7 | -520 cp |
| openai/gpt-4.1-mini | 6 | Qxc7 | True | c3c7 | -547 cp |
| openai/gpt-4.1-mini | 7 | Qxc6 | True | c3c6 | -559 cp |
| openai/gpt-4.1-mini | 8 | Qxc6 | True | c3c6 | -582 cp |
| openai/gpt-4.1-mini | 9 | Qc6 | True | c3c6 | -561 cp |
| openai/gpt-4.1-mini | 10 | Qxc7 | True | c3c7 | -507 cp |
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
| deepseek/deepseek-chat-v3.1 | 1 | Qc6 | True | c3c6 | -555 cp |
| deepseek/deepseek-chat-v3.1 | 2 | Qg7 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 3 | Qxg4 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 4 | Qxf6 | True | c3f6 | Mate in 1 |
| deepseek/deepseek-chat-v3.1 | 5 | Re8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 6 | Qc8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 7 | Qc6 | True | c3c6 | -579 cp |
| deepseek/deepseek-chat-v3.1 | 8 | Qd4 | True | c3d4 | -456 cp |
| deepseek/deepseek-chat-v3.1 | 9 | Rxf6 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 10 | Qxf6 | True | c3f6 | Mate in 1 |
| meta-llama/llama-3.3-8b-instruct:free | 1 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 2 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 3 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 4 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 5 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 6 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 7 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 8 | SE | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 9 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 10 | Nf3 | False | None | None |
| qwen/qwen3-coder | 1 | Qe3 | True | c3e3 | -467 cp |
| qwen/qwen3-coder | 2 | Qe3 | True | c3e3 | -507 cp |
| qwen/qwen3-coder | 3 | Qe3 | True | c3e3 | -534 cp |
| qwen/qwen3-coder | 4 | Qe3 | True | c3e3 | -506 cp |
| qwen/qwen3-coder | 5 | Qe3 | True | c3e3 | -499 cp |
| qwen/qwen3-coder | 6 | Qe3 | True | c3e3 | -460 cp |
| qwen/qwen3-coder | 7 | Qe3 | True | c3e3 | -486 cp |
| qwen/qwen3-coder | 8 | Qe3 | True | c3e3 | -482 cp |
| qwen/qwen3-coder | 9 | Qe3 | True | c3e3 | -466 cp |
| qwen/qwen3-coder | 10 | Qe3 | True | c3e3 | -485 cp |
| meituan/longcat-flash-chat | 1 | Qc7 | True | c3c7 | -526 cp |
| meituan/longcat-flash-chat | 2 | Qb3 | True | c3b3 | -517 cp |
| meituan/longcat-flash-chat | 3 | Qh8 | False | None | None |
| meituan/longcat-flash-chat | 4 | Qa3 | True | c3a3 | -175 cp |
| meituan/longcat-flash-chat | 5 | Qc3 | False | None | None |
| meituan/longcat-flash-chat | 6 | Axf7 | False | None | None |
| meituan/longcat-flash-chat | 7 | Qc3 | False | None | None |
| meituan/longcat-flash-chat | 8 | Qa5 | True | c3a5 | -442 cp |
| meituan/longcat-flash-chat | 9 | Qa5 | True | c3a5 | -474 cp |
| meituan/longcat-flash-chat | 10 | Qc7 | True | c3c7 | -528 cp |
| mistralai/mistral-medium-3.1 | 1 | Qxf7 | False | None | None |
| mistralai/mistral-medium-3.1 | 2 | Qxh7 | False | None | None |
| mistralai/mistral-medium-3.1 | 3 | Qxf7 | False | None | None |
| mistralai/mistral-medium-3.1 | 4 | Qd6 | False | None | None |
| mistralai/mistral-medium-3.1 | 5 | Qxh7 | False | None | None |
| mistralai/mistral-medium-3.1 | 6 | Qxf7 | False | None | None |
| mistralai/mistral-medium-3.1 | 7 | Qxf7 | False | None | None |
| mistralai/mistral-medium-3.1 | 8 | Qxf7 | False | None | None |
| mistralai/mistral-medium-3.1 | 9 | Qxf7 | False | None | None |
| mistralai/mistral-medium-3.1 | 10 | Qxf7 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 1 | Qd4 | True | c3d4 | -463 cp |
| baidu/ernie-4.5-vl-28b-a3b | 2 | Qd4 | True | c3d4 | -460 cp |
| baidu/ernie-4.5-vl-28b-a3b | 3 | Be4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 4 | Bd4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 5 | Ne4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 6 | Nd5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 7 | Qe3 | True | c3e3 | -493 cp |
| baidu/ernie-4.5-vl-28b-a3b | 8 | Qd3 | True | c3d3 | -139 cp |
| baidu/ernie-4.5-vl-28b-a3b | 9 | Bg5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 10 | Qd4 | True | c3d4 | -445 cp |