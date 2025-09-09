# LLM REASONING USING CHESS

## 1. Define the Reasoning Dimensions

- **Rule compliance** → Does the LLM respect chess rules (move legality)?
- **Tactical reasoning** → Can it calculate short combinations and spot forced wins?
- **Strategic reasoning** → Does it recognize long-term concepts (pawn structure, piece activity)?
- **Explanation quality** → Can it justify a move in human-understandable terms?
- **Consistency** → Does it stick to its own plan across multiple moves?

---

## 2. Curate or Build a Dataset

- **Simple puzzles**: Mate-in-1, stalemates, legal/illegal move checks.  
- **Intermediate puzzles**: Tactics like forks, pins, skewers.  
- **Complex positions**: Positions where deep calculation is needed.  
- **Strategic positions**: Openings, middlegame plans, endgames.  
- **Explanatory prompts**: “Why is this move best?” or “Why is this move a blunder?”  

This ensures the benchmark tests multiple levels of reasoning, not just move legality.

---

## 3. Set Clear Evaluation Metrics

- **Accuracy** → % of correct moves vs. ground truth (from engines or puzzle datasets).  
- **Rule adherence** → % of legal vs. illegal moves.  
- **Depth of reasoning** → Does the explanation include valid chess concepts?  
- **Plan coherence** → Agreement between successive answers (can be scored manually or with LLM-as-judge methods).  
- **Error typology** → Categorize failures (illegal move, tactical miss, hallucinated concept, inconsistency).  

---

## 4. Choose Baselines & Comparisons

- **LLMs vs. chess engines** (e.g., Stockfish, Leela) for move accuracy.  
- **LLMs vs. human players** (novice vs. expert explanations).  
- **Different LLMs** (GPT-4, Claude, LLaMA, etc.) under the same setup.  

This gives a relative sense of reasoning performance.

---

## 5. Design the Protocol Carefully
They’d make the evaluation reproducible and fair:

- **Prompt standardization** → Fixed wording for each task to avoid prompt engineering bias.  
- **Few-shot vs. zero-shot** → Test both “cold reasoning” and “with guidance.”  
- **Randomization** → Shuffle puzzle order to avoid memorization bias.  
- **Blind evaluation** → Human annotators don’t know which model generated which explanation.  

---

## 6. Analyze Results at Two Levels
- **Quantitative** → Scores, accuracy, error rates.  
- **Qualitative** → Patterns of reasoning failures (e.g., “often hallucinates tactical motifs” or “strong on rules but weak on deep planning”).

## Research Papers that let us formulate the scope of the problem:

[Bridging the Gap between Expert and Language Models: Concept-guided Chess Commentary Generation and Evaluation](https://aclanthology.org/2025.naacl-long.481.pdf)

[Large Language Models as General Pattern Machines](https://arxiv.org/pdf/2307.04721)

[Beyond the Imitation Game: Quantifying and extrapolating the capabilities of language models](https://arxiv.org/pdf/2206.04615)

[Validity Challenges in Machine Learning Benchmarks](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2022/EECS-2022-180.pdf)

[GAIA:A BENCHMARK FOR GENERAL AI ASSISTANTS](https://scontent-fra3-1.xx.fbcdn.net/v/t39.2365-6/441903294_1131492964728662_1145973121044474930_n.pdf?_nc_cat=103&ccb=1-7&_nc_sid=3c67a6&_nc_ohc=u6APR2mGCx4Q7kNvwEN6Ejk&_nc_oc=AdnO1i9MjtrLh4j0pIsezialQS20U8JVn9hE4ZwpUUvIw-2-IzH95kbP5dXHY4gtHTw&_nc_zt=14&_nc_ht=scontent-fra3-1.xx&_nc_gid=qpD_NMiZu30NBzE2MUus2w&oh=00_AfbXQXFFQ_zdSLpcnXZ4aVewkE0koGRDUrX3z27iHe-YZA&oe=68C49D30)

## LLM models with specification in the domain of law (EU, national regulations):

[Aleph-Alpha/tfree-hat-pretrained-7b-base](https://huggingface.co/Aleph-Alpha/tfree-hat-pretrained-7b-base)

[nlpaueb/legal-bert-base-uncased](https://huggingface.co/nlpaueb/legal-bert-base-uncased)

[microsoft/Phi-4-reasoning](https://huggingface.co/microsoft/Phi-4-reasoning)

[lexlms/legal-roberta-large](https://huggingface.co/lexlms/legal-roberta-large)

and more general models available through [ollama](https://ollama.com/library)

aswell as multi language models like [meta-llama/Llama-4-Scout-17B-16E-Instruct](https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct)

## General Concept for the Evaluation Metric:

Correlating the ability for LLM to work in the strict rules of chess to reason about the law.

Base idea relates to possible way of using the expert models as a benchmark for LLMs, as presented [here](https://aclanthology.org/2025.naacl-long.481.pdf). Rules and the board state is presented like a legal document, allowing us to find out the biases dependend on its format and structure and the ability to reason outside of the context it was trained but recognizing the patterns as presented in the following [research](https://arxiv.org/pdf/2307.04721).

## Challenge:

1. Select a domain: LLM as a Law Assistants tool like [Harvey AI](https://www.harvey.ai)
2. Initial Exploration: testing on the models mentioned in the section above (LLM models)
3. Identify "Failure" Modes:
   * difference between how documents are structured in EU and their nations vs US
   * problems depending on the language in which the document/rules/state-of-game are presented
   * adaptation to the completly new system
   * problem with the importance of the temporary data
