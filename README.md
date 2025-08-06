# DeepEval RAG Evaluation

This project demonstrates how to evaluate the performance of a Retrieval-Augmented Generation (RAG) system using [DeepEval](https://github.com/confident-ai/deepeval), a powerful evaluation framework for LLM applications.

---

## 📌 What is DeepEval?

[DeepEval](https://github.com/confident-ai/deepeval) is an open-source Python library designed for evaluating generative AI systems. It supports:
- Relevancy metrics
- Hallucination detection
- Precision-based contextual analysis
- RAG evaluations and custom test cases

🔗 Official website: [https://www.confident-ai.com](https://www.confident-ai.com)

---

## 🧪 Evaluation Metrics Used

The following metrics from DeepEval are used to assess the quality of your RAG pipeline:

| Metric | Description |
|--------|-------------|
| `AnswerRelevancyMetric` | Measures how relevant the model's answer is to the input query. |
| `ContextualRelevancyMetric` | Checks if the output uses context appropriately. |
| `ContextualPrecisionMetric` | Measures precision of context usage (less irrelevant context used). |
| `HallucinationMetric` | Detects if the model has hallucinated information not supported by context. |

---

## 📁 File Breakdown

| File | Description |
|------|-------------|
| `test_example.py` | Python script that loads the Excel file, evaluates rows using DeepEval, and writes the scores back. |
| `deepeval_rag_test.xlsx` | Input Excel containing: `input`, `actual_output`, `expected_output`, `retrieval_context`, and `context`. |
| `requirements.txt` | Python dependencies required to run the project. |
| `README.md` | Documentation for the project (you’re reading it!). |

---

## 🛠️ How to Use

### 1. Clone the Repo

```bash
git clone (https://github.com/Data-Science-Wallah/deepeva)
cd deepeval_ragas_eval
