# Chess Move Prediction Results with Legality & Stockfish Eval

| Model | Call # | Move | Legal | UCI | Eval |
|-------|--------|------|-------|-----|------|
| google/gemini-2.5-flash-lite | 1 | Qh3 | False | None | None |
| google/gemini-2.5-flash-lite | 2 | Qh3 | False | None | None |
| google/gemini-2.5-flash-lite | 3 |  | False | None | None |
| google/gemini-2.5-flash-lite | 4 |  | False | None | None |
| google/gemini-2.5-flash-lite | 5 | Qh3 | False | None | None |
| google/gemini-2.5-flash-lite | 6 | Qd3 | True | c3d3 | -150 cp |
| google/gemini-2.5-flash-lite | 7 | Qb3 | True | c3b3 | -524 cp |
| google/gemini-2.5-flash-lite | 8 |  | False | None | None |
| google/gemini-2.5-flash-lite | 9 |  | False | None | None |
| google/gemini-2.5-flash-lite | 10 |  | False | None | None |
| openai/gpt-4.1-mini | 1 | Qxc7 | True | c3c7 | -485 cp |
| openai/gpt-4.1-mini | 2 | Db8 | False | None | None |
| openai/gpt-4.1-mini | 3 | Qxc6 | True | c3c6 | -563 cp |
| openai/gpt-4.1-mini | 4 | Qxc7 | True | c3c7 | -515 cp |
| openai/gpt-4.1-mini | 5 | Qa5 | True | c3a5 | -474 cp |
| openai/gpt-4.1-mini | 6 | Qxc6 | True | c3c6 | -544 cp |
| openai/gpt-4.1-mini | 7 | Qa5 | True | c3a5 | -465 cp |
| openai/gpt-4.1-mini | 8 | Qxc6 | True | c3c6 | -566 cp |
| openai/gpt-4.1-mini | 9 | Qa5 | True | c3a5 | -489 cp |
| openai/gpt-4.1-mini | 10 | Qa5 | True | c3a5 | -465 cp |
| openai/gpt-3.5-turbo-instruct | 1 | Rxf7 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 2 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 3 | B6c5 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 4 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 5 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 6 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 7 | B4-c5 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 8 | Nf4 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 9 | Rd1 | True | f1d1 | -233 cp |
| openai/gpt-3.5-turbo-instruct | 10 | SE | False | None | None |
| deepseek/deepseek-chat-v3.1 | 1 | Qg6 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 2 | Dg6 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 3 | Dg7 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 4 | Cf4 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 5 | Dg3 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 6 | Cg6 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 7 | Dc6 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 8 | Db5 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 9 | Qh3 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 10 | Dc6 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 1 | N1f3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 2 | N4c4 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 3 | N1e4 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 4 | SE | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 5 | N2e4 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 6 | N1c3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 7 | N1c3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 8 | N1c3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 9 | N3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 10 | N1c3 | False | None | None |
| qwen/qwen3-coder | 1 | Qe3 | True | c3e3 | -462 cp |
| qwen/qwen3-coder | 2 |  | False | None | None |
| qwen/qwen3-coder | 3 |  | False | None | None |
| qwen/qwen3-coder | 4 | Qe3 | True | c3e3 | -496 cp |
| qwen/qwen3-coder | 5 |  | False | None | None |
| qwen/qwen3-coder | 6 | Dxf6 | False | None | None |
| qwen/qwen3-coder | 7 |  | False | None | None |
| qwen/qwen3-coder | 8 | Qe3 | True | c3e3 | -485 cp |
| qwen/qwen3-coder | 9 | Qe3 | True | c3e3 | -480 cp |
| qwen/qwen3-coder | 10 | Qe3 | True | c3e3 | -478 cp |
| meituan/longcat-flash-chat | 1 | Qc3-a5 | True | c3a5 | -498 cp |
| meituan/longcat-flash-chat | 2 | Bb5 | True | a4b5 | -353 cp |
| meituan/longcat-flash-chat | 3 | Qf8 | False | None | None |
| meituan/longcat-flash-chat | 4 | Qc3 | False | None | None |
| meituan/longcat-flash-chat | 5 | Qc3 | False | None | None |
| meituan/longcat-flash-chat | 6 | Qc3 | False | None | None |
| meituan/longcat-flash-chat | 7 | Qc3 | False | None | None |
| meituan/longcat-flash-chat | 8 | Rdf8 | False | None | None |
| meituan/longcat-flash-chat | 9 | Qc3 | False | None | None |
| meituan/longcat-flash-chat | 10 | Rdf8 | False | None | None |
| mistralai/mistral-medium-3.1 | 1 | D6 | False | None | None |
| mistralai/mistral-medium-3.1 | 2 | Dxh7 | False | None | None |
| mistralai/mistral-medium-3.1 | 3 | D6 | False | None | None |
| mistralai/mistral-medium-3.1 | 4 | Dxh7 | False | None | None |
| mistralai/mistral-medium-3.1 | 5 | Df6 | False | None | None |
| mistralai/mistral-medium-3.1 | 6 | Df6 | False | None | None |
| mistralai/mistral-medium-3.1 | 7 | Df6 | False | None | None |
| mistralai/mistral-medium-3.1 | 8 | Dxh7 | False | None | None |
| mistralai/mistral-medium-3.1 | 9 | Df6 | False | None | None |
| mistralai/mistral-medium-3.1 | 10 | Dd8 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 1 | B4e4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 2 | Qe4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 3 | B4c4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 4 | Qe4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 5 | Qe4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 6 | B4c4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 7 | Qe4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 8 | B4c4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 9 | Qxe4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 10 | Bb3 | True | a4b3 | -275 cp |