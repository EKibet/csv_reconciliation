# Reconciliation Toolkit GUI - User Documentation

Welcome to the Reconciliation Toolkit GUI, a graphical user interface for reconciling CSV files. This tool allows you to easily select source and target CSV files, initiate the reconciliation process, and visualize the results.

## Prerequisites

1. **Clone the Repository and Checkout `gui-tool` Branch:**
   ```bash
   git clone https://github.com/EKibet/csv_reconciliation.git
   cd csv_reconciliation
   git checkout gui-tool
   ```

2. **Create a Virtual Environment (Optional but Recommended):**
   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment:**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On Unix or MacOS:
     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies:**
   ```bash
   make install
   ```
   or 
   ```bash
   pip install -r requirements.txt
   ```

5. **Launch the GUI Tool:**
   ```bash
   make gui
   ```
   or  
   ```bash
   python3 reconciliation_gui/reconciliation_gui.py
   ```

## GUI Interface

Upon launching the GUI, you'll encounter the following options:

- **Choose Source CSV**: Use the "Browse" button to select your source CSV file. Choose from the project's media folder.
- **Choose Target CSV**: Utilize the "Browse" button to select your target CSV file. Choose from the project's media folder.
- **Run Reconciliation**: Initiate the reconciliation process by clicking the "Run Reconciliation" button.

Once the reconciliation completes, a CSV report containing discrepancies will be generated and saved in the `media` directory.

## Viewing Results

After the reconciliation, access the report in the `media` directory:

### Option 1: Manual Viewing

1. Navigate to the media directory within the project folder.
2. Locate the CSV file with a unique timestamp (e.g., 20230101235959.csv).
3. Open the CSV file using a spreadsheet application like Microsoft Excel or Google Sheets to inspect detailed reconciliation results.

### Option 2: In-GUI Viewing

Click on the "View Results" button within the GUI after the reconciliation process is complete. The reconciliation report will be displayed directly in the GUI, enabling you to inspect discrepancies without using an external spreadsheet application.

## Exit the GUI

Close the GUI window when you have completed the reconciliation process.

## Additional Notes

- Ensure that your source and target CSV files have the required columns and format as specified in the documentation.
- In the future, the tool will support large datasets through the use of Dask for parallel processing.

## GUI Demo

![Reconciliation GUI Tool Demo](/media/reconciliation-gui-inaction.gif)
