# BART-Based Abstractive Text Summarization for News Articles

### Business Objective

Text summarization, a vital aspect of data science and natural language processing, involves condensing document size while retaining meaning. This project centers on abstractive summarization, specifically utilizing the BART model to generate concise summaries that may introduce new phrases not present in the original text. Applications span diverse domains, including science, literature, finance, legal analysis, meetings, video conferencing, and programming languages.

---

### Data Description

The dataset comprises 40,000 professionally crafted summaries of news articles, alongside links to the original articles. Sourced from a GitHub repository, the data is formatted in CSV, encompassing features such as article titles, summaries, URLs, dates, and article content.

---

### Aim

To execute abstractive text summarization on the given data using the BART model.

---

### Tech Stack

- Language: `Python`
- Libraries: `pandas`, `scikit-learn`, `PyTorch`, `Transformers`
- Environment: `Google Colab`

---

## Approach

1. Import the dataset using the dataset library and load a subset for initial data exploration.
2. Clone the repository housing the data.
3. Download article titles, summaries, URLs, and dates into a CSV file.
4. Set up a new environment, install required dependencies, and scrape the data.
5. Configure the runtime to utilize GPU for enhanced processing.
6. Import necessary packages and libraries.
7. Develop a class function for the dataset.
8. Create a class function for the BART data loader.
9. Implement a class function for the abstractive summarization model.
10. Establish a BART tokenizer.
11. Define the data loader.
12. Read and preprocess the data.
13. Split the data into training and testing sets.
14. Construct the main class for executing the 'BARTForConditionalGeneration' model and tokenizer.
15. Define the trainer class and train the model.
16. Execute BART summarization leveraging the pre-trained model.
17. Grasp the concept of the BART evaluation metric - Rouge.
18. For web application deployment:
      - Set up a new environment.
      - Install necessary packages from requirements.txt.
      - Navigate to the output folder.
      - Run app.py.
      - Access the web application locally on port 5000.
      - Input an article link for summarization, and the generated summary will be displayed.

---
