# PDF Email Sender

This script sends bulk email with PDF file as attachment. It reads PDF files from a specified directory and its subdirectories, and then sends these files as attachments to a predefined email address.

## Requirements

- `smtplib`, `os`, `datetime`, `dotenv`, `email` modules

- Install the required dependencies using the following command:

    ```
    pip install -r requirements.txt
    ```

## Installation

1. Clone the repository or download the script.

2. Create a file named `credentials.env` and include the following environment variables:

    ```
    DISPLAY_NAME=Your_Display_Name
    EMAIL=Your_Email_Address
    PASSWORD=Your_Email_Password
    ```

3. Run the script by executing the following command:

    ```
    py main.py
    ```

4. Follow the prompts to enter the run batch ID and the folder path containing the PDF files.
