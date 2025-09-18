# Chess Move Prediction Results with Legality & Stockfish Eval

| Model | Call # | Move | Legal | UCI | Eval |
|-------|--------|------|-------|-----|------|
| google/gemini-2.5-flash-lite | 1 | Qh6 | True | h5h6 | 175 cp |
| google/gemini-2.5-flash-lite | 2 | Qh5 | False | None | None |
| google/gemini-2.5-flash-lite | 3 | Qh6 | True | h5h6 | 389 cp |
| google/gemini-2.5-flash-lite | 4 | Qh7 | True | h5h7 | -420 cp |
| google/gemini-2.5-flash-lite | 5 | Qh7 | True | h5h7 | -482 cp |
| google/gemini-2.5-flash-lite | 6 | Qh7 | True | h5h7 | -511 cp |
| google/gemini-2.5-flash-lite | 7 | Qh7 | True | h5h7 | -505 cp |
| google/gemini-2.5-flash-lite | 8 | Qh6 | True | h5h6 | 378 cp |
| google/gemini-2.5-flash-lite | 9 | Qh7 | True | h5h7 | -480 cp |
| google/gemini-2.5-flash-lite | 10 | Qg7 | False | None | None |
| openai/gpt-4.1-mini | 1 | Qh6 | True | h5h6 | 365 cp |
| openai/gpt-4.1-mini | 2 | Qh6 | True | h5h6 | 366 cp |
| openai/gpt-4.1-mini | 3 | Qh6 | True | h5h6 | 369 cp |
| openai/gpt-4.1-mini | 4 | Qh6 | True | h5h6 | 368 cp |
| openai/gpt-4.1-mini | 5 | Qh6 | True | h5h6 | 369 cp |
| openai/gpt-4.1-mini | 6 | Qh6 | True | h5h6 | 364 cp |
| openai/gpt-4.1-mini | 7 | Qh6 | True | h5h6 | 366 cp |
| openai/gpt-4.1-mini | 8 | Qh6 | True | h5h6 | 381 cp |
| openai/gpt-4.1-mini | 9 | Qh6 | True | h5h6 | 390 cp |
| openai/gpt-4.1-mini | 10 | Qxg7 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 1 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 2 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 3 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 4 | Qc7 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 5 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 6 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 7 | Qd3 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 8 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 9 | Qg3 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 10 | SE | False | None | None |
| deepseek/deepseek-chat-v3.1 | 1 | Re8 | True | e1e8 | -387 cp |
| deepseek/deepseek-chat-v3.1 | 2 | Qh8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 3 | Qh6 | True | h5h6 | 382 cp |
| deepseek/deepseek-chat-v3.1 | 4 | Qd1 | True | h5d1 | -380 cp |
| deepseek/deepseek-chat-v3.1 | 5 | Re1f1 | True | e1f1 | -367 cp |
| deepseek/deepseek-chat-v3.1 | 6 | Qf7 | True | h5f7 | Mate in 1 |
| deepseek/deepseek-chat-v3.1 | 7 | Qh6 | True | h5h6 | 385 cp |
| deepseek/deepseek-chat-v3.1 | 8 | Rf7 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 9 | Qxh7 | True | h5h7 | -502 cp |
| deepseek/deepseek-chat-v3.1 | 10 | Re1h1 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 1 | Qd2 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 2 | Qd2 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 3 | Nc3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 4 | Qd2 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 5 | Qd2 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 6 | Nc3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 7 | Qe3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 8 | Qd2 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 9 | Qe3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 10 | Qd2 | False | None | None |
| qwen/qwen3-coder | 1 | Qh7 | True | h5h7 | -518 cp |
| qwen/qwen3-coder | 2 | Qg6 | True | h5g6 | -631 cp |
| qwen/qwen3-coder | 3 | Qg6 | True | h5g6 | -641 cp |
| qwen/qwen3-coder | 4 | Qxh7 | True | h5h7 | -506 cp |
| qwen/qwen3-coder | 5 | Qxh7 | True | h5h7 | -510 cp |
| qwen/qwen3-coder | 6 | Qg6 | True | h5g6 | -652 cp |
| qwen/qwen3-coder | 7 | Qxh7 | True | h5h7 | -530 cp |
| qwen/qwen3-coder | 8 | Qg6 | True | h5g6 | -622 cp |
| qwen/qwen3-coder | 9 | Qxh7 | True | h5h7 | -518 cp |
| qwen/qwen3-coder | 10 | Qxh7 | True | h5h7 | -528 cp |
| meituan/longcat-flash-chat | 1 | Qh5 | False | None | None |
| meituan/longcat-flash-chat | 2 | Qh5 | False | None | None |
| meituan/longcat-flash-chat | 3 | Qh5 | False | None | None |
| meituan/longcat-flash-chat | 4 | Qh5 | False | None | None |
| meituan/longcat-flash-chat | 5 | Qh7 | True | h5h7 | -514 cp |
| meituan/longcat-flash-chat | 6 | Qh7 | True | h5h7 | -523 cp |
| meituan/longcat-flash-chat | 7 | Qh7 | True | h5h7 | -532 cp |
| meituan/longcat-flash-chat | 8 | Qh5 | False | None | None |
| meituan/longcat-flash-chat | 9 | Qh7 | True | h5h7 | -526 cp |
| meituan/longcat-flash-chat | 10 | Qh7 | True | h5h7 | -533 cp |
| mistralai/mistral-medium-3.1 | 1 | Qh7 | True | h5h7 | -552 cp |
| mistralai/mistral-medium-3.1 | 2 | Qh8 | False | None | None |
| mistralai/mistral-medium-3.1 | 3 | Qh7 | True | h5h7 | -512 cp |
| mistralai/mistral-medium-3.1 | 4 | Qh7 | True | h5h7 | -531 cp |
| mistralai/mistral-medium-3.1 | 5 | Qh7 | True | h5h7 | -541 cp |
| mistralai/mistral-medium-3.1 | 6 | Qh7 | True | h5h7 | -534 cp |
| mistralai/mistral-medium-3.1 | 7 | Qh8 | False | None | None |
| mistralai/mistral-medium-3.1 | 8 | Qh7 | True | h5h7 | -506 cp |
| mistralai/mistral-medium-3.1 | 9 | Qh7 | True | h5h7 | -501 cp |
| mistralai/mistral-medium-3.1 | 10 | Qh7 | True | h5h7 | -524 cp |
| baidu/ernie-4.5-vl-28b-a3b | 1 | Qe3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 2 | Qd5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 3 | Qe3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 4 | Qf3 | True | h5f3 | -47 cp |
| baidu/ernie-4.5-vl-28b-a3b | 5 | Qd4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 6 | Qe3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 7 | Qd5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 8 | Qe3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 9 | Qe3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 10 | Qd4 | False | None | None |