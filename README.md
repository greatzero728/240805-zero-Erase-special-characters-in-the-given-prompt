# Text Processor Desktop App

![Erase special characters in the given prompt](https://github.com/greatzero728/240805-zero-Erase-special-characters-in-the-given-prompt/blob/main/Erase%20special%20characters%20in%20the%20given%20prompt.gif)

## Introduction

This desktop application allows users to process text by removing specific characters and content within square brackets, with the exception of the word "client". It's built using Python and Tkinter for the GUI, and regular expressions for text processing.

## Features

- Remove asterisks (`*`), parentheses (`(`, `)`), and content inside square brackets (`[ ]`), except the word "client".
- Simple and intuitive GUI for easy text input and processing.
- Ability to clear the text area for new input.

## How to Build and Run the App

### Prerequisites

- Python 3.x installed on your computer. You can download it from [python.org](https://www.python.org/).
- Tkinter installed (it usually comes pre-installed with Python).

### Installation Steps

1. Clone the repository or download the source code.

   ```sh
   git clone <repository_url>
   cd <repository_directory>
   ```

2. Ensure you have Tkinter installed. If not, install it using pip:

   ```sh
   pip install tk
   ```

3. Run the application:

   ```sh
   python zero.py
   ```

### Running the Application

- After running `zero.py`, a window will open with a text area and two buttons: "Process Text" and "Cut Text".
- Enter or paste the text you want to process in the text area.
- Click "Process Text" to clean the text according to the rules.
- Click "Cut Text" to cut the processed text to the clipboard.

## How the App Works

1. **Text Input:**
   - Users can enter or paste any text into the provided text area.

2. **Processing Rules:**
   - The app removes the following characters: `*`, `(`, `)`.
   - The app removes all content inside square brackets `[ ]`, except when the content is the word "client". In such cases, the word "client" is preserved.

3. **Output:**
   - The processed text is displayed in the same text area, replacing the original input.
   - The processed text can be copied to the clipboard by clicking the "Cut Text" button.