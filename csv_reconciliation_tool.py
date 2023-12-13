import pandas as pd

def reconcile_csv(source_path, target_path, output_path):
    """
    Reconciles records between two CSV files, comparing each field for discrepancies.

    Args:
        source_path (str): The file path to the source CSV file.
        target_path (str): The file path to the target CSV file.
        output_path (str): The file path to save the reconciliation report.

    Returns:
        None: The function prints records missing in target and source, as well as field discrepancies.

    Example:
        reconcile_csv("p./source.csv", "./target.csv", "./reconciliation_report.csv")
    """
    # Read CSV files into pandas DataFrames
    source_df = pd.read_csv(source_path)
    target_df = pd.read_csv(target_path)

    # Assuming the first column is a unique identifier
    unique_identifier = source_df.columns[0]

    # Identify records that are present in the source but missing in the target
    missing_in_target = source_df[~source_df[unique_identifier].isin(target_df[unique_identifier])]

    # Identify records that are present in the target but missing in the source
    missing_in_source = target_df[~target_df[unique_identifier].isin(source_df[unique_identifier])]

    # Identify records with field discrepancies
    field_discrepancies = pd.merge(source_df, target_df, on=unique_identifier, how='inner', suffixes=('_source', '_target'))

    # Create a DataFrame for discrepancies
    discrepancies_df = pd.DataFrame(columns=['Type', 'Record Identifier', 'Field', 'Source Value', 'Target Value'])

    # Records missing in target
    discrepancies_df = pd.concat([discrepancies_df, missing_in_target[[unique_identifier]].rename(columns={unique_identifier: 'Record Identifier'}).assign(Type='Missing in Target')])

    # Records missing in source
    discrepancies_df = pd.concat([discrepancies_df, missing_in_source[[unique_identifier]].rename(columns={unique_identifier: 'Record Identifier'}).assign(Type='Missing in Source')])

    # Records with field discrepancies
    for column in source_df.columns[1:]:  # Skip the unique identifier column
        column_discrepancies = field_discrepancies[field_discrepancies[f'{column}_source'] != field_discrepancies[f'{column}_target']]
        discrepancies_df = pd.concat([discrepancies_df, column_discrepancies[[unique_identifier]].rename(columns={unique_identifier: 'Record Identifier'}).assign(Type='Field Discrepancy', Field=column,
                                                                                              Source_Value=column_discrepancies[f'{column}_source'],
                                                                                              Target_Value=column_discrepancies[f'{column}_target'])])

    # Save the reconciliation report to CSV
    discrepancies_df.to_csv(output_path, index=False)

    print(f"Reconciliation report saved to: {output_path}")

# Example usage with sample data
source_csv_path = "./source.csv"
target_csv_path = "./target.csv"
output_csv_path = "./reconciliation_report.csv"

reconcile_csv(source_csv_path, target_csv_path, output_csv_path)
