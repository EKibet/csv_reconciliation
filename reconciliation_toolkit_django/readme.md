
# Reconciliation Toolkit Django App

Welcome to the Reconciliation Toolkit Django App! This app provides a graphical user interface (GUI) for reconciling records between two CSV files.

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/EKibet/csv_reconciliation.git
   ```

2. Navigate to the project directory:

   ```bash
   cd reconciliation-toolkit-django
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### 1. Run the Django Server

Run the Django development server to launch the app:

```bash
python manage.py runserver
```

The app will be accessible at `http://127.0.0.1:8000/` in your web browser.

### 2. Access the GUI

Visit the GUI by navigating to `http://127.0.0.1:8000/` in your web browser.

### 3. GUI Options

- **Choose Source CSV**: Click the "Browse" button to select the source CSV file.
- **Choose Target CSV**: Click the "Browse" button to select the target CSV file.
- **Run Reconciliation**: Click the "Run Reconciliation" button to initiate the reconciliation process.
- **View Results**: After reconciliation, click on this button to view the results directly within the GUI.

### 4. Viewing Results

You can view the reconciliation report either manually or within the GUI:

- **Manually View Results**: Navigate to the `media` directory within the project folder, and open the CSV file with a unique timestamp (e.g., `20230101235959.csv`) using a spreadsheet application.

- **View Results Within the GUI**: Click on the "View Results" button within the GUI after the reconciliation process is complete.

### 5. Exit the GUI

Close the GUI window when you have completed the reconciliation process.

## Contributing

If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

Happy reconciling!
