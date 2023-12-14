# CSV Reconciler

## Overview

CSV Reconciler is a tool designed to facilitate the reconciliation of data between two CSV files. This tool is available both as a Command Line Interface (CLI) and as a Graphical User Interface (GUI).

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [CLI Usage](#cli-usage)
  - [GUI Usage](#gui-usage)
- [Common Issues and Solutions](#common-issues-and-solutions)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/csv-reconciler.git
   ```

2. **Navigate to the Project Directory:**
   ```bash
   cd csv-reconciler
   ```

3. **Create a Virtual Environment (Optional but Recommended):**
   ```bash
   python -m venv venv
   ```

4. **Activate the Virtual Environment:**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On Unix or MacOS:
     ```bash
     source venv/bin/activate
     ```

5. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

6. **Make the CLI Executable (Unix/MacOS):**
   ```bash
   chmod +x csv_reconciler.py
   ```

## Usage

### CLI Usage

**Run CSV Reconciler:**
```bash
python csv_reconciler.py -s source.csv -t target.csv -o reconciliation_report.csv
```

#### CLI Options:

- `-s` or `--source`: Path to the source CSV file.
- `-t` or `--target`: Path to the target CSV file.
- `-o` or `--output`: Path to save the output reconciliation report.

#### Example:
```bash
python csv_reconciler.py -s path/to/source.csv -t path/to/target.csv -o path/to/reconciliation_report.csv
```

### GUI Usage

To launch the GUI, execute the following command:
```bash
python gui.py
```

1. **Choose Source CSV:**
   Click the "Browse" button to select the source CSV file.

2. **Choose Target CSV:**
   Click the "Browse" button to select the target CSV file.

3. **Run Reconciliation:**
   Click the "Run Reconciliation" button to initiate the reconciliation process.

4. **View Results:**
   After reconciliation, click the "View Results" button to see the reconciliation report.

## Common Issues and Solutions

1. **File Not Found:**
   - Ensure that the provided file paths are correct.
   - Check file names for typos.

2. **Invalid CSV Format:**
   - Verify that the CSV files are well-formatted with headers.

3. **Permission Denied:**
   - Ensure that you have the necessary permissions to read/write files in the specified directories.

4. **No Python Interpreter Found:**
   - Add the shebang line (`#!/usr/bin/env python`) at the beginning of the script.
   - Ensure the script is executable (`chmod +x csv_reconciler.py`).

## Contributing

Feel free to contribute by opening issues or submitting pull requests. Your feedback is highly appreciated!

## License

This project is licensed under the [MIT License](LICENSE).