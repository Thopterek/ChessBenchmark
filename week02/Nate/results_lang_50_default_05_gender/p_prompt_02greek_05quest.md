# Chess Move Prediction Results with Legality & Stockfish Eval

| Model | Call # | Move | Legal | UCI | Eval |
|-------|--------|------|-------|-----|------|
| google/gemini-2.5-flash-lite | 1 | Qh6 | True | h5h6 | 175 cp |
| google/gemini-2.5-flash-lite | 2 | Qh6 | True | h5h6 | 389 cp |
| google/gemini-2.5-flash-lite | 3 | Qh6 | True | h5h6 | 374 cp |
| google/gemini-2.5-flash-lite | 4 | Qh6 | True | h5h6 | 385 cp |
| google/gemini-2.5-flash-lite | 5 | Qg6 | True | h5g6 | -620 cp |
| google/gemini-2.5-flash-lite | 6 | Qh6 | True | h5h6 | 380 cp |
| google/gemini-2.5-flash-lite | 7 | Qh6 | True | h5h6 | 405 cp |
| google/gemini-2.5-flash-lite | 8 | Qh6 | True | h5h6 | 395 cp |
| google/gemini-2.5-flash-lite | 9 | h5 | False | None | None |
| google/gemini-2.5-flash-lite | 10 | Qh6 | True | h5h6 | 396 cp |
| openai/gpt-4.1-mini | 1 | Qxg7 | False | None | None |
| openai/gpt-4.1-mini | 2 | Qxg7 | False | None | None |
| openai/gpt-4.1-mini | 3 | Bxf7 | True | c4f7 | 0 cp |
| openai/gpt-4.1-mini | 4 | Qxg7 | False | None | None |
| openai/gpt-4.1-mini | 5 | Qxg7 | False | None | None |
| openai/gpt-4.1-mini | 6 | Qh6 | True | h5h6 | 384 cp |
| openai/gpt-4.1-mini | 7 | Qxg7 | False | None | None |
| openai/gpt-4.1-mini | 8 | Qxg7 | False | None | None |
| openai/gpt-4.1-mini | 9 | Qxg7 | False | None | None |
| openai/gpt-4.1-mini | 10 | Qh6 | True | h5h6 | 395 cp |
| openai/gpt-3.5-turbo-instruct | 1 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 2 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 3 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 4 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 5 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 6 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 7 | Rxe7 | True | e1e7 | -531 cp |
| openai/gpt-3.5-turbo-instruct | 8 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 9 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 10 | SE | False | None | None |
| deepseek/deepseek-chat-v3.1 | 1 | Rxe8 | True | e1e8 | -363 cp |
| deepseek/deepseek-chat-v3.1 | 2 | Rxe8 | True | e1e8 | -416 cp |
| deepseek/deepseek-chat-v3.1 | 3 | Qxf7 | True | h5f7 | Mate in 1 |
| deepseek/deepseek-chat-v3.1 | 4 | Qxf7 | True | h5f7 | Mate in 1 |
| deepseek/deepseek-chat-v3.1 | 5 | Qxf5 | True | h5f5 | 25 cp |
| deepseek/deepseek-chat-v3.1 | 6 | Rxe8 | True | e1e8 | -408 cp |
| deepseek/deepseek-chat-v3.1 | 7 | Qxf7 | True | h5f7 | Mate in 1 |
| deepseek/deepseek-chat-v3.1 | 8 | Qh6 | True | h5h6 | 394 cp |
| deepseek/deepseek-chat-v3.1 | 9 | Rxe8 | True | e1e8 | -402 cp |
| deepseek/deepseek-chat-v3.1 | 10 | Bd5 | True | c4d5 | -548 cp |
| meta-llama/llama-3.3-8b-instruct:free | 1 | Qc3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 2 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 3 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 4 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 5 | Qe3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 6 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 7 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 8 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 9 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 10 | Nf3 | False | None | None |
| qwen/qwen3-coder | 1 | Qxh7 | True | h5h7 | -475 cp |
| qwen/qwen3-coder | 2 | Qxh7 | True | h5h7 | -501 cp |
| qwen/qwen3-coder | 3 | Qxh7 | True | h5h7 | -518 cp |
| qwen/qwen3-coder | 4 | Qxh7 | True | h5h7 | -559 cp |
| qwen/qwen3-coder | 5 | Qh7 | True | h5h7 | -565 cp |
| qwen/qwen3-coder | 6 | Qxh7 | True | h5h7 | -564 cp |
| qwen/qwen3-coder | 7 | Qh7 | True | h5h7 | -544 cp |
| qwen/qwen3-coder | 8 | Qxh7 | True | h5h7 | -511 cp |
| qwen/qwen3-coder | 9 | Qxh7 | True | h5h7 | -506 cp |
| qwen/qwen3-coder | 10 | Qxh7 | True | h5h7 | -539 cp |
| meituan/longcat-flash-chat | 1 | Qh5 | False | None | None |
| meituan/longcat-flash-chat | 2 | Qh7 | True | h5h7 | -572 cp |
| meituan/longcat-flash-chat | 3 | Qh8 | False | None | None |
| meituan/longcat-flash-chat | 4 | Qxh7 | True | h5h7 | -552 cp |
| meituan/longcat-flash-chat | 5 | Qh7 | True | h5h7 | -538 cp |
| meituan/longcat-flash-chat | 6 | Qg6 | True | h5g6 | -612 cp |
| meituan/longcat-flash-chat | 7 | Qh5 | False | None | None |
| meituan/longcat-flash-chat | 8 | Qh5 | False | None | None |
| meituan/longcat-flash-chat | 9 | Qh7 | True | h5h7 | -554 cp |
| meituan/longcat-flash-chat | 10 | Qh5 | False | None | None |
| mistralai/mistral-medium-3.1 | 1 | Qxh7 | True | h5h7 | -543 cp |
| mistralai/mistral-medium-3.1 | 2 | Qh7 | True | h5h7 | -553 cp |
| mistralai/mistral-medium-3.1 | 3 | Qh7 | True | h5h7 | -554 cp |
| mistralai/mistral-medium-3.1 | 4 | Qh7 | True | h5h7 | -566 cp |
| mistralai/mistral-medium-3.1 | 5 | Qh8 | False | None | None |
| mistralai/mistral-medium-3.1 | 6 | Qh7 | True | h5h7 | -558 cp |
| mistralai/mistral-medium-3.1 | 7 | Qh8 | False | None | None |
| mistralai/mistral-medium-3.1 | 8 | Qh7 | True | h5h7 | -559 cp |
| mistralai/mistral-medium-3.1 | 9 | Qh7 | True | h5h7 | -505 cp |
| mistralai/mistral-medium-3.1 | 10 | Qh8 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 1 | Qd4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 2 | Qd5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 3 | Qd4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 4 | Qe3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 5 | Qd4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 6 | Qd5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 7 | Qe3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 8 | Qd4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 9 | Qd4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 10 | Qd5 | False | None | None |