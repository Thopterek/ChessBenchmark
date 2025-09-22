# Chess Move Prediction Results with Legality & Stockfish Eval

| Model | Call # | Move | Legal | UCI | Eval |
|-------|--------|------|-------|-----|------|
| google/gemini-2.5-flash-lite | 1 | Qh6 | True | h5h6 | 175 cp |
| google/gemini-2.5-flash-lite | 2 | Qg6 | True | h5g6 | -648 cp |
| google/gemini-2.5-flash-lite | 3 | Qh7 | True | h5h7 | -503 cp |
| google/gemini-2.5-flash-lite | 4 | Qh7 | True | h5h7 | -539 cp |
| google/gemini-2.5-flash-lite | 5 | Qh6 | True | h5h6 | 201 cp |
| google/gemini-2.5-flash-lite | 6 | Qh7 | True | h5h7 | -535 cp |
| google/gemini-2.5-flash-lite | 7 | Qh7 | True | h5h7 | -515 cp |
| google/gemini-2.5-flash-lite | 8 | Qg7 | False | None | None |
| google/gemini-2.5-flash-lite | 9 | Qh7 | True | h5h7 | -526 cp |
| google/gemini-2.5-flash-lite | 10 | Qh7 | True | h5h7 | -475 cp |
| openai/gpt-4.1-mini | 1 | Qxg7 | False | None | None |
| openai/gpt-4.1-mini | 2 | Qh6 | True | h5h6 | 169 cp |
| openai/gpt-4.1-mini | 3 | Qg7 | False | None | None |
| openai/gpt-4.1-mini | 4 |  | False | None | None |
| openai/gpt-4.1-mini | 5 | Qh6 | True | h5h6 | 159 cp |
| openai/gpt-4.1-mini | 6 | Qh6 | True | h5h6 | 176 cp |
| openai/gpt-4.1-mini | 7 | Qh6 | True | h5h6 | 195 cp |
| openai/gpt-4.1-mini | 8 | Qxh7 | True | h5h7 | -530 cp |
| openai/gpt-4.1-mini | 9 | Qg7 | False | None | None |
| openai/gpt-4.1-mini | 10 | Qg7 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 1 | d5 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 2 | e5 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 3 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 4 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 5 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 6 | Qe3 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 7 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 8 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 9 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 10 | SE | False | None | None |
| deepseek/deepseek-chat-v3.1 | 1 | Qxh7 | True | h5h7 | -539 cp |
| deepseek/deepseek-chat-v3.1 | 2 | Qh6 | True | h5h6 | 164 cp |
| deepseek/deepseek-chat-v3.1 | 3 | Qh6 | True | h5h6 | 173 cp |
| deepseek/deepseek-chat-v3.1 | 4 | Rxe8 | True | e1e8 | -404 cp |
| deepseek/deepseek-chat-v3.1 | 5 | Qxf7 | True | h5f7 | Mate in 1 |
| deepseek/deepseek-chat-v3.1 | 6 | Qxf7 | True | h5f7 | Mate in 1 |
| deepseek/deepseek-chat-v3.1 | 7 | Qf7 | True | h5f7 | Mate in 1 |
| deepseek/deepseek-chat-v3.1 | 8 | Qh6 | True | h5h6 | 190 cp |
| deepseek/deepseek-chat-v3.1 | 9 | Bd5 | True | c4d5 | -531 cp |
| deepseek/deepseek-chat-v3.1 | 10 | Qg6 | True | h5g6 | -646 cp |
| meta-llama/llama-3.3-8b-instruct:free | 1 | Qg4 | True | h5g4 | -565 cp |
| meta-llama/llama-3.3-8b-instruct:free | 2 | Qxd5 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 3 | Qg4 | True | h5g4 | -609 cp |
| meta-llama/llama-3.3-8b-instruct:free | 4 | Qc3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 5 | Nh3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 6 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 7 | Qxf5 | True | h5f5 | 19 cp |
| meta-llama/llama-3.3-8b-instruct:free | 8 | Qc8 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 9 | Qg4 | True | h5g4 | -586 cp |
| meta-llama/llama-3.3-8b-instruct:free | 10 | Qc3 | False | None | None |
| qwen/qwen3-coder | 1 | Qh7 | True | h5h7 | -549 cp |
| qwen/qwen3-coder | 2 | Qh7 | True | h5h7 | -555 cp |
| qwen/qwen3-coder | 3 | Qh7 | True | h5h7 | -562 cp |
| qwen/qwen3-coder | 4 | Qxh7 | True | h5h7 | -564 cp |
| qwen/qwen3-coder | 5 | Qh7 | True | h5h7 | -559 cp |
| qwen/qwen3-coder | 6 | Qh7 | True | h5h7 | -550 cp |
| qwen/qwen3-coder | 7 | Qxh7 | True | h5h7 | -526 cp |
| qwen/qwen3-coder | 8 | Qg6 | True | h5g6 | -648 cp |
| qwen/qwen3-coder | 9 | Qxh7 | True | h5h7 | -566 cp |
| qwen/qwen3-coder | 10 | Qxh7 | True | h5h7 | -561 cp |
| meituan/longcat-flash-chat | 1 | Qh5 | False | None | None |
| meituan/longcat-flash-chat | 2 | Qh7 | True | h5h7 | -568 cp |
| meituan/longcat-flash-chat | 3 | Qh5 | False | None | None |
| meituan/longcat-flash-chat | 4 | Qh5 | False | None | None |
| meituan/longcat-flash-chat | 5 | Qh5 | False | None | None |
| meituan/longcat-flash-chat | 6 | Qh5 | False | None | None |
| meituan/longcat-flash-chat | 7 | Qh7 | True | h5h7 | -572 cp |
| meituan/longcat-flash-chat | 8 | Qh6 | True | h5h6 | 177 cp |
| meituan/longcat-flash-chat | 9 | Qh5 | False | None | None |
| meituan/longcat-flash-chat | 10 | Qh5 | False | None | None |
| mistralai/mistral-medium-3.1 | 1 | Qxh7 | True | h5h7 | -545 cp |
| mistralai/mistral-medium-3.1 | 2 | Qxg6 | True | h5g6 | -674 cp |
| mistralai/mistral-medium-3.1 | 3 | Qxg7 | False | None | None |
| mistralai/mistral-medium-3.1 | 4 | Qxg7 | False | None | None |
| mistralai/mistral-medium-3.1 | 5 | Qxg7 | False | None | None |
| mistralai/mistral-medium-3.1 | 6 | Qxh7 | True | h5h7 | -525 cp |
| mistralai/mistral-medium-3.1 | 7 | Qxh7 | True | h5h7 | -568 cp |
| mistralai/mistral-medium-3.1 | 8 | Qxg7 | False | None | None |
| mistralai/mistral-medium-3.1 | 9 | Qxg7 | False | None | None |
| mistralai/mistral-medium-3.1 | 10 | Qxg7 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 1 | Qd4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 2 | Qd4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 3 | Qd4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 4 | Qd4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 5 | Qd4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 6 | Qd4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 7 | Qd4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 8 | Qe4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 9 | Qd3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 10 | Qd4 | False | None | None |