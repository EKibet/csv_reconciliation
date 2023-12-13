# Reconciliation Toolkit GUI - User Documentation

Welcome to the Reconciliation Toolkit GUI, a graphical user interface for reconciling CSV files. This tool allows you to easily select source and target CSV files, initiate the reconciliation process, and visualize the results.

## Prerequisites

Before running the GUI tool, ensure that you have the following prerequisites installed on your system:

1. Python 3.x (Download and installation instructions: [Python Downloads](https://www.python.org/downloads/))
2. Required Python packages. Install them using the following command:

   ```bash
   pip install pandas 
   ```

## Running the GUI Tool

Follow these step-by-step instructions to run the Reconciliation Toolkit GUI:

### 1. Clone the Repository

Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/EKibet/csv_reconciliation
```

### 2. Navigate to the Project Directory

Change into the project directory:

```bash
cd reconciliation-toolkit
```

### 3. Launch the GUI Tool

Run the following command to launch the GUI tool:

```bash
python gui_tool.py
```

### 4. GUI Interface

Once the GUI is launched, you will see a window with the following options:

- **Choose Source CSV**: Click the "Browse" button to select the source CSV file.
- **Choose Target CSV**: Click the "Browse" button to select the target CSV file.
- **Run Reconciliation**: Click the "Run Reconciliation" button to initiate the reconciliation process.
- After running the reconciliation, the tool will generate a CSV report with discrepancies. 
- The report will be saved in the media directory.

### 5. View Results

After running the reconciliation, the tool will generate a CSV report with discrepancies. The report will be saved in the `media` directory.
To view the reconciliation report:

Option 1: Manually View Results

Navigate to the media directory within the project folder.
Look for the CSV file with a unique timestamp (e.g., 20230101235959.csv).
Open the CSV file using a spreadsheet application like Microsoft Excel or Google Sheets to view the detailed reconciliation results.
Option 2: View Results Within the GUI

Click on the "View Results" button within the GUI after the reconciliation process is complete.
The reconciliation report will be displayed directly within the GUI, allowing you to inspect the discrepancies without opening an external spreadsheet application.

### 6. Exit the GUI

Close the GUI window when you have completed the reconciliation process.

## Additional Notes

- Ensure that your source and target CSV files have the required columns and format as specified in the documentation.
- The tool supports large datasets through the use of Dask for parallel processing.
