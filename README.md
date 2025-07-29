PubMed Papers CLI Tool
A Python command-line tool to fetch research papers from PubMed, filter those with non-academic (pharmaceutical/biotech) author affiliations, and export the results to CSV.

✨ Features
✅ Fetch research papers using the PubMed API.
✅ Identify non-academic authors using affiliation keywords.
✅ Output results as a CSV file with the following columns:

PubmedID

Title

Publication Date

Non-academic Author(s)

Company Affiliation(s)

Corresponding Author Email

✅ Supports command-line options:

-h / --help → Show help message

-d / --debug → Print debug info

-f / --file → Save results to a CSV file

✅ Modular structure (api.py, filters.py, cli.py)
✅ Uses Poetry for dependency management

📂 Project Structure
graphql

pubmed_papers/
│── pubmed_papers/
│   ├── __init__.py
│   ├── api.py        # Handles PubMed API requests
│   ├── filters.py    # Extracts non-academic authors and affiliations
│   └── cli.py        # Command-line interface using Typer
│
├── README.md
├── pyproject.toml     # Poetry configuration
└── poetry.lock
🔧 Installation1️⃣ Clone the repository

git clone https://github.com/ShubhangiRaghuvanshi/pubmed-papers-cli.git
cd pubmed-papers-cli
2️⃣ Install dependencies using Poetry
poetry install
▶️ Usage
📌 Run the CLI
poetry run get-papers-list "breast cancer"
📌 Save results to a CSV file
poetry run get-papers-list "breast cancer" -f results.csv
📌 Debug mode (prints fetched IDs)
poetry run get-papers-list "breast cancer" -d
🛠 Tech Stack
Python 3.10+

Typer – CLI framework

Requests – API requests

Pandas – CSV export

Poetry – Dependency management

📜 How It Works
api.py → Fetches PubMed IDs and XML details.

filters.py → Parses XML, identifies non-academic authors and company affiliations.

cli.py → Provides a simple CLI to run the tool and export results.

📌 Example Output (CSV)
PubmedID	Title	Publication Date	Non-academic Author(s)	Company Affiliation(s)	Corresponding Author Email
40727739	Evaluation of the Antitumor Effectiveness...	2025	Pierre Sicard, Sylvain Richard	PhyMedExp, IPAM/Biocampus	pierre@example.com

👨‍💻 Author
Shubhangi Raghuvanshi
