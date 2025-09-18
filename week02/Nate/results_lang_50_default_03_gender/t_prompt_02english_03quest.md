# Chess Move Prediction Results with Legality & Stockfish Eval

| Model | Call # | Move | Legal | UCI | Eval |
|-------|--------|------|-------|-----|------|
| google/gemini-2.5-flash-lite | 1 | Qg3 | False | None | None |
| google/gemini-2.5-flash-lite | 2 | Qd4 | True | c3d4 | -460 cp |
| google/gemini-2.5-flash-lite | 3 | Qc7 | True | c3c7 | -512 cp |
| google/gemini-2.5-flash-lite | 4 | Qc7 | True | c3c7 | -503 cp |
| google/gemini-2.5-flash-lite | 5 | Qc7 | True | c3c7 | -501 cp |
| google/gemini-2.5-flash-lite | 6 | Qh3 | False | None | None |
| google/gemini-2.5-flash-lite | 7 | Qd3 | True | c3d3 | -141 cp |
| google/gemini-2.5-flash-lite | 8 | Qa5 | True | c3a5 | -496 cp |
| google/gemini-2.5-flash-lite | 9 | Qd2 | True | c3d2 | -202 cp |
| google/gemini-2.5-flash-lite | 10 | g4 | False | None | None |
| openai/gpt-4.1-mini | 1 | Qxc6 | True | c3c6 | -565 cp |
| openai/gpt-4.1-mini | 2 | Qc6 | True | c3c6 | -568 cp |
| openai/gpt-4.1-mini | 3 | Qxc6 | True | c3c6 | -558 cp |
| openai/gpt-4.1-mini | 4 | Qxf6 | True | c3f6 | Mate in 1 |
| openai/gpt-4.1-mini | 5 | Qxc7 | True | c3c7 | -506 cp |
| openai/gpt-4.1-mini | 6 | Qxc6 | True | c3c6 | -553 cp |
| openai/gpt-4.1-mini | 7 | Qc6 | True | c3c6 | -554 cp |
| openai/gpt-4.1-mini | 8 | Qxf6 | True | c3f6 | Mate in 1 |
| openai/gpt-4.1-mini | 9 | Qxc7 | True | c3c7 | -518 cp |
| openai/gpt-4.1-mini | 10 | Qxc6 | True | c3c6 | -568 cp |
| openai/gpt-3.5-turbo-instruct | 1 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 2 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 3 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 4 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 5 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 6 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 7 | Re1 | True | f1e1 | 138 cp |
| openai/gpt-3.5-turbo-instruct | 8 | Bxe5 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 9 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 10 | Move: Qe3 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 1 | Qh3 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 2 | Qc6 | True | c3c6 | -567 cp |
| deepseek/deepseek-chat-v3.1 | 3 | d6 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 4 | Qc6 | True | c3c6 | -564 cp |
| deepseek/deepseek-chat-v3.1 | 5 | Rxf6 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 6 | Nd4 | True | f3d4 | -261 cp |
| deepseek/deepseek-chat-v3.1 | 7 | Rg3 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 8 | Nfe5 | True | f3e5 | -239 cp |
| deepseek/deepseek-chat-v3.1 | 9 | Bf8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 10 | Nd4 | True | f3d4 | -272 cp |
| meta-llama/llama-3.3-8b-instruct:free | 1 | Nh3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 2 | Qg4 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 3 | Qd2 | True | c3d2 | -202 cp |
| meta-llama/llama-3.3-8b-instruct:free | 4 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 5 | Nh7 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 6 | Qxd4 | True | c3d4 | -453 cp |
| meta-llama/llama-3.3-8b-instruct:free | 7 | Qd2 | True | c3d2 | -216 cp |
| meta-llama/llama-3.3-8b-instruct:free | 8 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 9 | Qxd4 | True | c3d4 | -484 cp |
| meta-llama/llama-3.3-8b-instruct:free | 10 | Nh7 | False | None | None |
| qwen/qwen3-coder | 1 | Qe3 | True | c3e3 | -468 cp |
| qwen/qwen3-coder | 2 | Qe3 | True | c3e3 | -475 cp |
| qwen/qwen3-coder | 3 | Qe3 | True | c3e3 | -470 cp |
| qwen/qwen3-coder | 4 | Qe3 | True | c3e3 | -492 cp |
| qwen/qwen3-coder | 5 | Qe3 | True | c3e3 | -480 cp |
| qwen/qwen3-coder | 6 | Qe3 | True | c3e3 | -489 cp |
| qwen/qwen3-coder | 7 | Qe3 | True | c3e3 | -491 cp |
| qwen/qwen3-coder | 8 | Qe3 | True | c3e3 | -474 cp |
| qwen/qwen3-coder | 9 | Qe3 | True | c3e3 | -475 cp |
| qwen/qwen3-coder | 10 | Qe3 | True | c3e3 | -464 cp |
| meituan/longcat-flash-chat | 1 | Axg8 | False | None | None |
| meituan/longcat-flash-chat | 2 | Qc3 | False | None | None |
| meituan/longcat-flash-chat | 3 | Qc3 | False | None | None |
| meituan/longcat-flash-chat | 4 | Qc3 | False | None | None |
| meituan/longcat-flash-chat | 5 | Qc3 | False | None | None |
| meituan/longcat-flash-chat | 6 | Qc7 | True | c3c7 | -522 cp |
| meituan/longcat-flash-chat | 7 | Qc7 | True | c3c7 | -527 cp |
| meituan/longcat-flash-chat | 8 | Qxf6 | True | c3f6 | Mate in 1 |
| meituan/longcat-flash-chat | 9 | Qc8 | False | None | None |
| meituan/longcat-flash-chat | 10 | Qc3 | False | None | None |
| mistralai/mistral-medium-3.1 | 1 |  | False | None | None |
| mistralai/mistral-medium-3.1 | 2 | Qxh6 | False | None | None |
| mistralai/mistral-medium-3.1 | 3 | Qxg7 | False | None | None |
| mistralai/mistral-medium-3.1 | 4 | Qxf6 | True | c3f6 | Mate in 1 |
| mistralai/mistral-medium-3.1 | 5 | Qxg6 | False | None | None |
| mistralai/mistral-medium-3.1 | 6 |  | False | None | None |
| mistralai/mistral-medium-3.1 | 7 |  | False | None | None |
| mistralai/mistral-medium-3.1 | 8 | Qxg6 | False | None | None |
| mistralai/mistral-medium-3.1 | 9 |  | False | None | None |
| mistralai/mistral-medium-3.1 | 10 |  | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 1 | Be3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 2 | Bd5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 3 | Nf3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 4 | Bd3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 5 | Bc5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 6 | Bd3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 7 | Bc5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 8 | Bd5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 9 | Bc5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 10 | Bd3 | False | None | None |