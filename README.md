# Ownership Scrapper

## Description
This project is a Python-based application that allows you to scrape ownership data from a public US company's DEF 14A (Proxy statement) filing and determine the majority ownership. Currently, the project is a work in progress and can only extract Apple Inc.'s 2023 DEF-14A filing.

It utilizes virtualenv and virtualenv wrapper for easy installation and management of the project's dependencies.

## Installation

Please follow the instructions below to set up the Ownership Scrapper project on your local machine.

### Prerequisites
- Python 3.x
- Git

### Step 1: Clone the Repository
1. Open your terminal or command prompt.
2. Change the current working directory to the location where you want to clone the repository.
3. Execute the following command to clone the repository:
```shell
git clone https://github.com/your-username/ownership-scrapper.git
```
4. Once the cloning process is complete, navigate to the project's directory:
```shell
cd ownership-scrapper
```

### Step 2: Install virtualenv and virtualenv wrapper
1. Ensure that you have Python 3.x installed on your machine. If not, please download and install it from the official Python website (https://www.python.org).
2. Install `virtualenv` globally using the following command:
```shell
pip install virtualenv
```
3. Install `virtualenvwrapper` globally using the following command:
```shell
pip install virtualenvwrapper
```
   Note: If you encounter any issues during the installation, refer to the official `virtualenv` and `virtualenvwrapper` documentation for troubleshooting.

### Step 3: Create a virtual environment
1. Open your terminal or command prompt.
2. Create a virtual environment using `virtualenvwrapper` by executing the following command:
```shell
mkvirtualenv --python python3 -r requirements.txt ownership-scrapper
```
   Note: The `--python` flag specifies the path to your Python 3 executable. Adjust it if necessary. This command will also install all the required packages and libraries specified in the `requirements.txt` file.

3. The virtual environment will be created and activated automatically.

### Step 4: Install project dependencies (if step3 failed)
1. Ensure that your virtual environment is activated.
2. Install the project dependencies by running the following command:
```shell
pip install -r requirements.txt
```
   This command will install all the required packages and libraries specified in the `requirements.txt` file.

## Usage
To use the Ownership Scrapper project, follow these steps:

1. Ensure that your virtual environment is activated.
2. Run the main Python file to initiate the ownership scraping process:
```shell
python ownership.py
```
   Note: The project is currently a work in progress and can only extract Apple Inc.'s 2023 DEF-14A filing. You may need to modify the code to extract ownership data from other companies' filings or different years.

## License
This project is licensed under the [MIT License](LICENSE).

## Contributing
Contributions to the Ownership Scrapper project are welcome. If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## Authors
- [Arpita Choudhury](https://github.com/Arpita-ch95)
