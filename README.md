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

# Clone the repository to your local machine
git clone https://github.com/EKibet/csv_reconciliation.git

# 2. Navigate into the project directory
cd csv_reconciliation

# 2.1 Checkout into the gui-tool branch
git checkout gui-tool


### 3. Launch the GUI Tool

Run the following command to launch the GUI tool:

```bash
python3 reconciliation_gui/reconciliation_gui.py

```

## 4. GUI Interface

Upon launching the GUI, you'll encounter the following options:

- **Choose Source CSV**: Use the "Browse" button to select your source CSV file.
- **Choose Target CSV**: Utilize the "Browse" button to select your target CSV file.
- **Run Reconciliation**: Initiate the reconciliation process by clicking the "Run Reconciliation" button.

Once the reconciliation completes, a CSV report containing discrepancies will be generated and saved in the `media` directory.

## 5. Viewing Results

After the reconciliation, access the report in the `media` directory:

### Option 1: Manual Viewing

## 4. GUI Interface

Upon launching the GUI, you'll encounter the following options:

- **Choose Source CSV**: Use the "Browse" button to select your source CSV file.
- **Choose Target CSV**: Utilize the "Browse" button to select your target CSV file.
- **Run Reconciliation**: Initiate the reconciliation process by clicking the "Run Reconciliation" button.

Once the reconciliation completes, a CSV report containing discrepancies will be generated and saved in the `media` directory.

## 5. Viewing Results

After the reconciliation, access the report in the `media` directory:

### Option 1: Manual Viewing

1. Navigate to the media directory within the project folder.
2. Locate the CSV file with a unique timestamp (e.g., 20230101235959.csv).
3. Open the CSV file using a spreadsheet application like Microsoft Excel or Google Sheets to inspect detailed reconciliation results.

### Option 2: In-GUI Viewing

Click on the "View Results" button within the GUI after the reconciliation process is complete. The reconciliation report will be displayed directly in the GUI, enabling you to inspect discrepancies without using an external spreadsheet application.

### 6. Exit the GUI

Close the GUI window when you have completed the reconciliation process.

## Additional Notes

- Ensure that your source and target CSV files have the required columns and format as specified in the documentation.
- In future, the tool will support large datasets through the use of Dask for parallel processing.


### GUI Demo

![Screenshot 1](media/reconciliation-gui-inaction.gif)
