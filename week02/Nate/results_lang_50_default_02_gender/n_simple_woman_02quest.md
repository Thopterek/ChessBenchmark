# Chess Move Prediction Results with Legality & Stockfish Eval

| Model | Call # | Move | Legal | UCI | Eval |
|-------|--------|------|-------|-----|------|
| google/gemini-2.5-flash-lite | 1 | Rxf6 | False | None | None |
| google/gemini-2.5-flash-lite | 2 | Nhg5 | False | None | None |
| google/gemini-2.5-flash-lite | 3 | Qh7 | True | h6h7 | -482 cp |
| google/gemini-2.5-flash-lite | 4 | Qxg7 | True | h6g7 | -625 cp |
| google/gemini-2.5-flash-lite | 5 | Qh7 | True | h6h7 | -528 cp |
| google/gemini-2.5-flash-lite | 6 | Qh7 | True | h6h7 | -526 cp |
| google/gemini-2.5-flash-lite | 7 | Qh7 | True | h6h7 | -500 cp |
| google/gemini-2.5-flash-lite | 8 | Qxe6 | False | None | None |
| google/gemini-2.5-flash-lite | 9 | Qh7 | True | h6h7 | -518 cp |
| google/gemini-2.5-flash-lite | 10 | Qh7 | True | h6h7 | -510 cp |
| openai/gpt-4.1-mini | 1 |  | False | None | None |
| openai/gpt-4.1-mini | 2 |  | False | None | None |
| openai/gpt-4.1-mini | 3 |  | False | None | None |
| openai/gpt-4.1-mini | 4 |  | False | None | None |
| openai/gpt-4.1-mini | 5 |  | False | None | None |
| openai/gpt-4.1-mini | 6 | Qh7 | True | h6h7 | -518 cp |
| openai/gpt-4.1-mini | 7 | Qxh7 | True | h6h7 | -545 cp |
| openai/gpt-4.1-mini | 8 | Qxh7 | True | h6h7 | -519 cp |
| openai/gpt-4.1-mini | 9 | Qxh7 | True | h6h7 | -536 cp |
| openai/gpt-4.1-mini | 10 | Qg7 | True | h6g7 | -634 cp |
| openai/gpt-3.5-turbo-instruct | 1 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 2 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 3 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 4 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 5 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 6 | Qg7 | True | h6g7 | -614 cp |
| openai/gpt-3.5-turbo-instruct | 7 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 8 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 9 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 10 | SE | False | None | None |
| deepseek/deepseek-chat-v3.1 | 1 | Qh7 | True | h6h7 | -530 cp |
| deepseek/deepseek-chat-v3.1 | 2 | Qh8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 3 | Nf7 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 4 | Nf7 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 5 | Nf7 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 6 | Rf8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 7 | Nf7 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 8 | Nf7 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 9 | Qg7 | True | h6g7 | -626 cp |
| deepseek/deepseek-chat-v3.1 | 10 | Nf7 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 1 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 2 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 3 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 4 | Nh6 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 5 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 6 | Qg4 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 7 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 8 | Nh7 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 9 | Nh3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 10 | Nf3 | False | None | None |
| qwen/qwen3-coder | 1 | Qh7 | True | h6h7 | -510 cp |
| qwen/qwen3-coder | 2 | Qxf6 | False | None | None |
| qwen/qwen3-coder | 3 | Qxf6 | False | None | None |
| qwen/qwen3-coder | 4 | Qh7 | True | h6h7 | -527 cp |
| qwen/qwen3-coder | 5 | Qxf6 | False | None | None |
| qwen/qwen3-coder | 6 | Qg7 | True | h6g7 | -627 cp |
| qwen/qwen3-coder | 7 | Qh7 | True | h6h7 | -535 cp |
| qwen/qwen3-coder | 8 | Qh7 | True | h6h7 | -510 cp |
| qwen/qwen3-coder | 9 | Qg7 | True | h6g7 | -615 cp |
| qwen/qwen3-coder | 10 | Qh7 | True | h6h7 | -513 cp |
| meituan/longcat-flash-chat | 1 | Qh7 | True | h6h7 | -524 cp |
| meituan/longcat-flash-chat | 2 | Ng8-e7 | False | None | None |
| meituan/longcat-flash-chat | 3 | Qh7 | True | h6h7 | -533 cp |
| meituan/longcat-flash-chat | 4 | Ng8 | False | None | None |
| meituan/longcat-flash-chat | 5 | Qh7 | True | h6h7 | -535 cp |
| meituan/longcat-flash-chat | 6 | Qh7 | True | h6h7 | -522 cp |
| meituan/longcat-flash-chat | 7 | Qh6 | False | None | None |
| meituan/longcat-flash-chat | 8 | Gf7 | False | None | None |
| meituan/longcat-flash-chat | 9 | Qh7 | True | h6h7 | -525 cp |
| meituan/longcat-flash-chat | 10 | Ng6 | False | None | None |
| mistralai/mistral-medium-3.1 | 1 | Qxh7 | True | h6h7 | -527 cp |
| mistralai/mistral-medium-3.1 | 2 | Qxh7 | True | h6h7 | -533 cp |
| mistralai/mistral-medium-3.1 | 3 | Qxh7 | True | h6h7 | -541 cp |
| mistralai/mistral-medium-3.1 | 4 | Qxh7 | True | h6h7 | -533 cp |
| mistralai/mistral-medium-3.1 | 5 | Qxh7 | True | h6h7 | -536 cp |
| mistralai/mistral-medium-3.1 | 6 | Qxh7 | True | h6h7 | -507 cp |
| mistralai/mistral-medium-3.1 | 7 | Qxh7 | True | h6h7 | -542 cp |
| mistralai/mistral-medium-3.1 | 8 | Qxh7 | True | h6h7 | -541 cp |
| mistralai/mistral-medium-3.1 | 9 | Qxg7 | True | h6g7 | -636 cp |
| mistralai/mistral-medium-3.1 | 10 | Qxh7 | True | h6h7 | -540 cp |
| baidu/ernie-4.5-vl-28b-a3b | 1 | Qd3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 2 | Qd4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 3 | Qd3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 4 | Qd3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 5 | Qd3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 6 | Qd4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 7 | Qd3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 8 | Qd3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 9 | Qd3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 10 | Qd2 | True | h6d2 | -193 cp |