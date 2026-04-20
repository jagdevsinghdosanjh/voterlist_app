# 🗳️ voterlist_app

A lightweight Python app for working with voter lists — focused on **local, offline workflows** like searching, filtering, and inspecting electoral roll data.

This is **not** the full ECI_OpsSuite admin stack.  
`voterlist_app` is a smaller, focused tool you can run quickly on a local machine.

---

## 🎯 Purpose

- Load voter list data from local files (CSV/Excel or preprocessed sources)
- Search voters by name, EPIC, house number, or other fields
- Filter and inspect subsets (street, booth, ward, etc.)
- Experiment with parsing/cleaning logic in `modules/` before pushing into bigger systems

Ideal for:
- Personal experiments
- Local civic analysis
- Prototyping voter data tools

---

## 🏗️ Project layout

```text
voterlist_app/
├── app.py          # Main entry point for the app
├── modules/        # Core logic and helper modules (parsing, search, etc.)
├── .gitignore
└── README.md

As the project grows, you can split modules/ into:

modules/parser.py

modules/search.py

modules/utils.py

modules/config.py

⚙️ Setup & run
1. Clone
bash
git clone https://github.com/jagdevsinghdosanjh/voterlist_app.git
cd voterlist_app
2. Create environment (example with conda)
bash
conda create -n voterlist_app python=3.11
conda activate voterlist_app
3. Install dependencies
If you’re using requirements.txt:

bash
pip install -r requirements.txt
If not yet created, install what you actually use in app.py / modules/ (for example):

bash
pip install pandas openpyxl
4. Run the app
bash
python app.py
If this becomes a Streamlit app later:

bash
streamlit run app.py
🧩 Modules
The modules/ folder is where all the logic lives.
Typical responsibilities (you can align your files to this):

parser — read voter list files, normalize columns

search — search/filter functions

export — write filtered data to CSV/Excel

utils — shared helpers (logging, config, etc.)

Document each module with a short docstring at the top so future you knows what lives where.

🔐 Data & privacy
This app is designed to work with local voter data files that you provide.

Do not commit real voter data to this repository.

Keep your data files outside the repo or add them to .gitignore.

Treat all personal data as sensitive.

🛠️ Roadmap (for this repo only)
[ ] Add clear module boundaries inside modules/

[ ] Add requirements.txt based on actual imports

[ ] Optional: convert to Streamlit UI

[ ] Add sample dummy dataset (synthetic, no real data)

[ ] Add basic tests for parsing and search

👤 Author
Jagdev Singh Dosanjh  
Python developer • civic workflows • modular systems