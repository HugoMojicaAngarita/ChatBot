# Recipe Chatbot

This project develops a chatbot that can process and parse information from a recipe dataset into ingredients and instructions. It utilizes various natural language processing (NLP) tools and libraries to analyze and divide the text.

## Table of Contents

1. [Project Description](#project-description)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Code Structure](#code-structure)
5. [Datasets](#datasets)
6. [Results](#results)
7. [License](#license)

## Project Description

This project focuses on creating a chatbot that can take a recipe dataset, process the text to parse it into ingredients and instructions, and provide responses to questions about the recipes.

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/your-repository.git
    ```
2. Navigate to the project directory:
    ```bash
    cd your-repository
    ```
3. Install the necessary dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the main script to start the chatbot:
    ```bash
    python gui.py
    ```
2. Once the GUI is open, you can load PDF documents and ask questions about the recipes.

## Code Structure

- `gui.py`: Contains the code for the graphical user interface.
- `text_processing.py`: Contains functions for loading, processing, and parsing recipe texts.
- `requirements.txt`: List of dependencies required for the project.
- `images/`: Folder containing images used in the GUI.
- `source_documents/`: Folder where recipe PDFs are stored.

## Datasets

We utilize the following datasets for this project:
- [Nutrition details for most common foods](https://www.kaggle.com/datasets/niharika41298/nutrition-details-for-most-common-foods)
- [Food ingredients and recipe dataset with images](https://www.kaggle.com/datasets/pes12017000148/food-ingredients-and-recipe-dataset-with-images)

## Results

- **Recipe Distribution:** The dataset contains various categories such as breakfasts, lunches, and dinners.
- **Ingredient Frequency:** Common ingredients include X, Y, and Z.
- **Accuracy Evaluation:** We employ metrics such as accuracy and precision to evaluate the model's performance.
- **Error Analysis:** The model succeeded in most cases but failed in instances where instructions were poorly structured or incomplete.

## License

This project is licensed under the terms of the MIT license. See the `LICENSE` file for more details.
