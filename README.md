# PEP document parser based on Scrapy

[Description](#description) /
[Deploy locally](#deploy-locally) /
[Documentation](#documentation) /
[Author](#author) /


## Description

Parser [scrapy_parser_pep](https://github.com/StanislavBerezovskii/scrapy_parser_pep) collects PEP documents from the resource [https://peps.python.org/](https://peps.python.org/) and generates two types of results:

* pep_{datetime}.csv - list of all PEPs (number, name and status)
* status_summary_{datetime}.csv - summary of PEP statuses, how many documents were found in each status (status, quantity)


## Deploy locally

Clone the project, create a virtual environment and initialize dependencies:

```bash
git clone https://github.com/StanislavBerezovskii/scrapy_parser_pep.git
cd scrapy_parser_pep
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```

## Documentation

The parser is launched from the root directory of the project with the command

```bash
scrapy crawl pep
```

## Author

https://github.com/StanislavBerezovskii
