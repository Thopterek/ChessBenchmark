# Chess Move Prediction Results with Legality & Stockfish Eval

| Model | Call # | Move | Legal | UCI | Eval |
|-------|--------|------|-------|-----|------|
| google/gemini-2.5-flash-lite | 1 | Qc7 | True | c3c7 | -522 cp |
| google/gemini-2.5-flash-lite | 2 | Qc7 | True | c3c7 | -499 cp |
| google/gemini-2.5-flash-lite | 3 | Qh3 | False | None | None |
| google/gemini-2.5-flash-lite | 4 | Qc7 | True | c3c7 | -495 cp |
| google/gemini-2.5-flash-lite | 5 | Qd3 | True | c3d3 | -148 cp |
| google/gemini-2.5-flash-lite | 6 | Qxc4 | True | c3c4 | -643 cp |
| google/gemini-2.5-flash-lite | 7 | Qc7 | True | c3c7 | -499 cp |
| google/gemini-2.5-flash-lite | 8 | Qxg7 | False | None | None |
| google/gemini-2.5-flash-lite | 9 | Qxf7 | False | None | None |
| google/gemini-2.5-flash-lite | 10 | Qh3 | False | None | None |
| openai/gpt-4.1-mini | 1 | Qxc6 | True | c3c6 | -562 cp |
| openai/gpt-4.1-mini | 2 | Qxc6 | True | c3c6 | -565 cp |
| openai/gpt-4.1-mini | 3 | Qxc6 | True | c3c6 | -561 cp |
| openai/gpt-4.1-mini | 4 | Qxc6 | True | c3c6 | -544 cp |
| openai/gpt-4.1-mini | 5 | Qxc6 | True | c3c6 | -583 cp |
| openai/gpt-4.1-mini | 6 | Qc6 | True | c3c6 | -577 cp |
| openai/gpt-4.1-mini | 7 | Qxc6 | True | c3c6 | -585 cp |
| openai/gpt-4.1-mini | 8 | Qxc6 | True | c3c6 | -584 cp |
| openai/gpt-4.1-mini | 9 | Qe7 | False | None | None |
| openai/gpt-4.1-mini | 10 | Qxc6 | True | c3c6 | -596 cp |
| openai/gpt-3.5-turbo-instruct | 1 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 2 | Qd7 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 3 | 目前棋局 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 4 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 5 | e5 | True | e4e5 | -366 cp |
| openai/gpt-3.5-turbo-instruct | 6 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 7 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 8 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 9 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 10 | c4 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 1 | Qxf6 | True | c3f6 | Mate in 1 |
| deepseek/deepseek-chat-v3.1 | 2 | Qc7 | True | c3c7 | -507 cp |
| deepseek/deepseek-chat-v3.1 | 3 | Rh4 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 4 | Rf6 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 5 | Rd1 | True | f1d1 | -215 cp |
| deepseek/deepseek-chat-v3.1 | 6 | Qxg4 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 7 | Rf6 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 8 | Qg7 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 9 | Rf6 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 10 | Rxf7 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 1 | Ngf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 2 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 3 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 4 | Qf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 5 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 6 | Qd2 | True | c3d2 | -183 cp |
| meta-llama/llama-3.3-8b-instruct:free | 7 | Qxf7 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 8 | Qg4 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 9 | Qxg7 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 10 | Qxf6 | True | c3f6 | Mate in 1 |
| qwen/qwen3-coder | 1 | Qe3 | True | c3e3 | -490 cp |
| qwen/qwen3-coder | 2 | Qe3 | True | c3e3 | -457 cp |
| qwen/qwen3-coder | 3 | Qe3 | True | c3e3 | -508 cp |
| qwen/qwen3-coder | 4 | Qe3 | True | c3e3 | -481 cp |
| qwen/qwen3-coder | 5 | Qe3 | True | c3e3 | -474 cp |
| qwen/qwen3-coder | 6 | Qe3 | True | c3e3 | -486 cp |
| qwen/qwen3-coder | 7 | Qe3 | True | c3e3 | -466 cp |
| qwen/qwen3-coder | 8 | Qe3 | True | c3e3 | -476 cp |
| qwen/qwen3-coder | 9 | Qe3 | True | c3e3 | -458 cp |
| qwen/qwen3-coder | 10 | Qe3 | True | c3e3 | -459 cp |
| meituan/longcat-flash-chat | 1 | Qg3 | False | None | None |
| meituan/longcat-flash-chat | 2 | Qc8 | False | None | None |
| meituan/longcat-flash-chat | 3 | Qg3 | False | None | None |
| meituan/longcat-flash-chat | 4 | Qc7 | True | c3c7 | -509 cp |
| meituan/longcat-flash-chat | 5 | Qc3 | False | None | None |
| meituan/longcat-flash-chat | 6 | Qf3 | False | None | None |
| meituan/longcat-flash-chat | 7 | Qc7 | True | c3c7 | -512 cp |
| meituan/longcat-flash-chat | 8 | Qc7 | True | c3c7 | -514 cp |
| meituan/longcat-flash-chat | 9 | Qc3 | False | None | None |
| meituan/longcat-flash-chat | 10 | Ng1-e2 | False | None | None |
| mistralai/mistral-medium-3.1 | 1 |  | False | None | None |
| mistralai/mistral-medium-3.1 | 2 |  | False | None | None |
| mistralai/mistral-medium-3.1 | 3 |  | False | None | None |
| mistralai/mistral-medium-3.1 | 4 |  | False | None | None |
| mistralai/mistral-medium-3.1 | 5 |  | False | None | None |
| mistralai/mistral-medium-3.1 | 6 |  | False | None | None |
| mistralai/mistral-medium-3.1 | 7 | Qxf6 | True | c3f6 | Mate in 1 |
| mistralai/mistral-medium-3.1 | 8 | Qxf6 | True | c3f6 | Mate in 1 |
| mistralai/mistral-medium-3.1 | 9 |  | False | None | None |
| mistralai/mistral-medium-3.1 | 10 |  | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 1 | Qe3 | True | c3e3 | -489 cp |
| baidu/ernie-4.5-vl-28b-a3b | 2 | Qe3 | True | c3e3 | -482 cp |
| baidu/ernie-4.5-vl-28b-a3b | 3 | Qe3 | True | c3e3 | -479 cp |
| baidu/ernie-4.5-vl-28b-a3b | 4 | Qe3 | True | c3e3 | -464 cp |
| baidu/ernie-4.5-vl-28b-a3b | 5 | Qe3 | True | c3e3 | -498 cp |
| baidu/ernie-4.5-vl-28b-a3b | 6 | Bd5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 7 | Bc5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 8 | Bd5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 9 | Qe3 | True | c3e3 | -482 cp |
| baidu/ernie-4.5-vl-28b-a3b | 10 | Be4 | False | None | None |