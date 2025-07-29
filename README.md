📄 PubMed Papers CLI



A Python CLI tool to fetch research papers from PubMed API, filter those with non-academic (pharma/biotech) author affiliations, and export results as CSV.

🚀 Features
✅ Fetch research papers using PubMed API.
✅ Identify non-academic authors using affiliation-based heuristics.
✅ Export results as CSV with columns:

PubmedID

Title

Publication Date

Non-academic Author(s)

Company Affiliation(s)

Corresponding Author Email

✅ Command-line options for help, debug mode, and saving to file.
✅ Clean modular code (api.py, filters.py, cli.py).
✅ Dependency management using Poetry.

📂 Folder Structure

pubmed-papers-cli/
│── pubmed_papers/
│   ├── api.py          # Handles PubMed API calls
│   ├── filters.py      # Extracts non-academic authors & affiliations
│   ├── cli.py          # CLI tool using Typer
│   └── __init__.py
│
├── pyproject.toml      # Poetry configuration
├── README.md
└── poetry.lock
🛠️ Installation
1️⃣ Clone the Repository

git clone https://github.com/ShubhangiRaghuvanshi/pubmed-papers-cli.git
cd pubmed-papers-cli
2️⃣ Install Dependencies

poetry install
▶️ Usage
🔹 Basic Command

poetry run get-papers-list "breast cancer"
🔹 Save Output to CSV

poetry run get-papers-list "breast cancer" -f results.csv
🔹 Debug Mode

poetry run get-papers-list "breast cancer" -d
📊 Example CSV Output
PubmedID	Title	Publication Date	Non-academic Author(s)	Company Affiliation(s)	Corresponding Author Email
40727739	Evaluation of the Antitumor Effectiveness...	2025	Pierre Sicard, Sylvain R	PhyMedExp, IPAM/Biocampus, INSERM/CNRS	pierre@example.com

🔧 Tech Stack
Python 3.10+

Typer – CLI framework

Requests – API calls

Pandas – CSV export

Poetry – Dependency management

📌 How It Works
1️⃣ api.py → Fetches PubMed IDs and XML details.
2️⃣ filters.py → Parses XML, finds non-academic authors & company affiliations.
3️⃣ cli.py → CLI interface to run the tool and export results.

👩‍💻 Author
Shubhangi Raghuvanshi

🔗 GitHub Profile
