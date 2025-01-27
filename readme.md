# BART-Based Abstractive Text Summarization for News Articles

## Business Objective

Text summarization is a critical aspect of data science and natural language processing, enabling the condensation of document size while retaining its meaning. This project focuses on abstractive summarization, leveraging the **BART model** to generate concise summaries that may introduce new phrases not present in the original text. The applications of this technology span diverse domains, including:

- Scientific research
- Literature
- Financial reporting
- Legal analysis
- Meeting and video conferencing summaries
- Programming documentation

---

## Data Description

The dataset comprises **40,000 professionally crafted summaries** of news articles, accompanied by links to the original articles. Sourced data is in CSV format and includes the following features:

- **Article Titles**: Headline of the news article.
- **Summaries**: Professionally written summaries.
- **URLs**: Links to the original articles.
- **Dates**: Publication dates of the articles.
- **Article Content**: Full content of the articles.

---

## Aim

To perform **abstractive text summarization** on the given dataset using the **BART (Bidirectional and Auto-Regressive Transformer)** model.

---

## Tech Stack

- **Programming Language**: [Python](https://www.python.org/)
- **Libraries**:
  - [`pandas`](https://pandas.pydata.org/) for data manipulation.
  - [`scikit-learn`](https://scikit-learn.org/) for data preprocessing.
  - [`PyTorch`](https://pytorch.org/) for deep learning model implementation.
  - [`Transformers`](https://huggingface.co/transformers/) by Hugging Face for NLP models and tokenizers.
- **Environment**: [Google Colab](https://colab.research.google.com/) for GPU-enabled training.

---

## Approach

### 1. Data Exploration and Preparation
- Import the dataset using the dataset library and load a subset for initial exploration.
- Clone the repository housing the data and download article details (titles, summaries, URLs, and dates) into a CSV file.
- Scrape and preprocess the data as needed for model training.

### 2. Environment Setup
- Set up a new environment and install required dependencies from `requirements.txt`.
- Configure the runtime to utilize GPU for faster processing.

### 3. BART Model Development
- Import necessary packages and libraries.
- Develop the following class functions:
  - **Dataset Class**: Handles loading and preprocessing of the dataset.
  - **Data Loader Class**: Prepares data for BART model input.
  - **BART Summarization Model**: Implements `BARTForConditionalGeneration` for abstractive summarization.
- Define the tokenizer and data loader for BART.

### 4. Model Training
- Preprocess the data and split it into training and testing sets.
- Construct a main class for executing the `BARTForConditionalGeneration` model and tokenizer.
- Define a trainer class to fine-tune the model on the dataset.

### 5. Summarization and Evaluation
- Generate summaries using the pre-trained and fine-tuned BART model.
- Evaluate the performance of the model using **Rouge** scores:
  - **Rouge-1**: Unigram overlap.
  - **Rouge-2**: Bigram overlap.
  - **Rouge-L**: Longest common subsequence.

### 6. Web Application Deployment
- Set up a web interface for users to input news articles and obtain summaries.
  - Install necessary packages from `requirements.txt`.
  - Navigate to the output folder and run `app.py`.
  - Access the web application locally on port 5000.
  - Input a news article link and display the generated summary.

---

## Project Structure

```plaintext
.
├── data/                                  # Contains raw and processed data.
│   ├── news_articles.csv                  # Dataset with article titles, summaries, and content.
├── src/                                   # Source code folder.
│   ├── bart_summarization.py              # Main script for model implementation.
│   ├── dataset_loader.py                  # Data preprocessing and loading utilities.
│   ├── trainer.py                         # Model training script.
├── app/                                   # Web application files.
│   ├── app.py                             # Flask app for deployment.
├── output/                                # Stores generated summaries and evaluation metrics.
├── requirements.txt                       # Dependency file for the project.
└── README.md                              # Project documentation.
```

---

## Getting Started

### 1. Clone the Repository

```bash
git clone <repository_url>
cd <repository_folder>
```

### 2. Install Dependencies

Install the required libraries with:

```bash
pip install -r requirements.txt
```

### 3. Run the Summarization Model

Execute the BART summarization model:

```bash
python src/bart_summarization.py
```

### 4. Deploy the Web Application

- Navigate to the `app` folder and run the Flask application:

```bash
python app.py
```

- Access the application at `http://127.0.0.1:5000`.

### 5. Evaluate the Results

- Check the `output/` folder for Rouge evaluation scores and generated summaries.

---

## Results

- **High-Quality Summaries**:
  - Generated abstractive summaries that capture the essence of news articles.
- **Evaluation Metrics**:
  - Achieved competitive Rouge scores.
- **Web Application**:
  - User-friendly interface for summarizing news articles on-demand.

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch:

```bash
git checkout -b feature-name
```

3. Commit your changes:

```bash
git commit -m "Add feature"
```

4. Push your branch:

```bash
git push origin feature-name
```

5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contact

For any questions or suggestions, please reach out to:

- **Name**: Abhinav Navneet
- **Email**: mailme.AbhinavN@gmail.com
- **GitHub**: [AjNavneet](https://github.com/AjNavneet)

---

## Acknowledgments

Special thanks to:

- [Hugging Face](https://huggingface.co/) for providing pre-trained models and tools.
- [Google Colab](https://colab.research.google.com/) for enabling GPU-based training.
- [PyTorch](https://pytorch.org/) for its deep learning framework.
- The Python open-source community for exceptional libraries and resources.

---
