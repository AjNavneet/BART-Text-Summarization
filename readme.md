# Abstractive Text Summarization Using BART for News Articles

### Business Objective

Text summarization is a critical research area in the field of data science and natural language processing (NLP). It involves reducing the size of a document while preserving its meaning. Summarization techniques fall into two categories: extractive and abstractive summarization. This project focuses on abstractive summarization, which aims to generate concise summaries that may include new phrases not present in the original text.

Abstractive summarization has applications in various domains, including science, literature, financial research, legal documents analysis, meetings, video conferencing, and programming languages. The objective of this project is to build a BART model for abstractive text summarization.

---

### Data Description

The dataset used in this project consists of 40,000 professionally written summaries of news articles, along with links to the original articles. The data is obtained from a GitHub repository and is available in CSV format. It includes features such as article titles, summaries, URLs, dates, and article content.

---

### Aim

To perform abstractive text summarization on the provided text data using the BART model.

---

### Tech Stack

- Language: `Python`
- Libraries: `pandas`, `scikit-learn`, `PyTorch`, `Transformers`
- Environment: `Google Colab`

---

## Approach

1. Import the dataset from the dataset library and load a subset for data overview.
2. Clone the repository containing the data.
3. Download the article titles, summaries, URLs, and dates into a CSV file.
4. Create a new environment, install the necessary requirements, and scrape the data.
5. Configure the runtime to use GPU for accelerated processing.
6. Import required packages and libraries.
7. Create a class function for the dataset.
8. Create a class function for the BART data loader.
9. Implement an abstractive summarization model class function.
10. Create a BART tokenizer.
11. Define the data loader.
12. Read and preprocess the data.
13. Split the data into training and testing sets.
14. Create the main class to run the 'BARTForConditionalGeneration' model and tokenizer.
15. Define the trainer class and fit the model.
16. Perform BART summarization using the pre-trained model.
17. Understand the concept of the BART evaluation metric - Rouge.
18. For running the web application:
   - Create a new environment.
   - Install the requirements from the requirements.txt file.
   - Navigate to the output folder.
   - Run app.py.
   - Access the web application locally on port 5000.
   - Provide an article link for summarization, and the summary will be generated.

---

## Key Concepts Explored

1. Understanding the business problem and the importance of text summarization.
2. In-depth knowledge of text summarization techniques, with a focus on abstractive summarization.
3. Understanding the BART model and encoder-decoder architecture.
4. Importing and working with the dataset.
5. Importing and using essential libraries.
6. Understanding pre-training and fine-tuning methodologies for NLP models.
7. Learning to clone data repositories using 'git clone.'
8. Fine-tuning the BART model using the Transformers library.
9. Creating class functions for dataset handling and data loading.
10. Implementing tokenization for NLP tasks.
11. Splitting the data, training, and fitting the model.
12. Performing abstractive summarization using the pre-trained model.
13. Understanding the evaluation metric Rouge.
14. Developing a web application for abstractive text summarization.

---