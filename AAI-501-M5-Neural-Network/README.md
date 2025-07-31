# Module 5 NLP Coding Assignment - Worked Solutions

This repository contains the Jupyter Notebook for the "Module 5 NLP Coding Assignment". In this assignment, you'll utilize Natural Language Processing (NLP) techniques to perform a supervised text regression task aimed at predicting scores for student essays. This exercise is based on a dataset provided by The William and Flora Hewlett Foundation.

## Overview

The notebook guides you through several key tasks:

- **Data Preprocessing**: Loading and filtering of essay data, focusing on specific essay sets.
- **Vectorization Techniques**: Implementing both conventional text representations and neural network embeddings.
- **Model Training**: Developing regression models including Ridge regression using traditional and deep learning approaches.
- **Evaluation**: Assessing model performance using distribution plots and error analyses.

## Assignment Tasks

1. **Setup**: Set random seeds for reproducibility.
2. **Data Loading**: Use Pandas to load and clean the dataset from a TSV file.
3. **Feature Engineering**:
   - Implement Count Vectorizer for bag-of-words representation.
   - Use Universal Sentence Encoder for semantic embeddings.
4. **Model Implementation**:
   - Train Ridge regression models using both feature sets.
5. **Model Evaluation**:
   - Visualize score distributions and errors.
   - Compare performance across models.
6. **Conclusion**:
   - Identify the best-performing model.
   - Discuss automatic essay scoring feasibility.
   - Recommend improvements.

## How to Use

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Set up the environment**:
   Install Python, Jupyter Notebook, and the necessary libraries (NumPy, Pandas, Matplotlib, Seaborn, TensorFlow, scikit-learn, etc.). You can use Conda for setting up the environment:

- conda create -n aai-501-m5 python=3.9
- conda install numpy=1.20 pandas matplotlib xlrd scikit-learn tensorflow
- conda activate aai-501-m5
- conda install jupyter

3. **Run the Jupyter Notebook**:
   ```bash
   jupyter notebook 
   ```

4. Follow the instructions within the notebook to explore the text regression task.

## Dataset

The dataset used is a subset from the [Kaggle ASAP-AES competition](https://www.kaggle.com/c/asap-aes). The focus is on analyzing essays and predicting scores.

## Observations

- The Universal Sentence Encoder performed significantly better than CountVectorizer.
- USE captures semantic nuances of the essays beyond mere word counts.
- The Ridge model trained with USE embeddings showed a higher R^2 score, indicating better predictive capacity.

## Improvements

- Address model bias on extreme scores.
- Enhance features with grammar, coherence, and style metrics.
- Explore post-processing for finer alignment with human scoring.

## License

This project is licensed under the MIT License. More details can be found in the [LICENSE](LICENSE) file.

## Contact

For questions or feedback, please contact [Your Name] at [your.email@example.com].
