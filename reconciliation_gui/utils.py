import os
from datetime import datetime

import pandas as pd


def reconcile_csv_util(source_path, target_path, output_directory="./media"):
    """
    Reconciles records between two CSV files, comparing each field for discrepancies.

    Args:
        source_path (str): The file path to the source CSV file.
        target_path (str): The file path to the target CSV file.
        output_path (str): The file path to save the reconciliation report.

    Returns:
        str: A message indicating the successful saving of the reconciliation report.

    Example:
        reconcile_csv_util("./source.csv", "./target.csv", "./reconciliation_report.csv")
    """
    # Read CSV files into pandas DataFrames
    source_df = pd.read_csv(source_path, dtype=str)
    target_df = pd.read_csv(target_path, dtype=str)

    # Assuming the first column is a unique identifier
    unique_identifier = source_df.columns[0]

    # Identify records that are present in the source but missing in the target
    missing_in_target = source_df[
        ~source_df[unique_identifier].isin(target_df[unique_identifier])
    ]

    # Identify records that are present in the target but missing in the source
    missing_in_source = target_df[
        ~target_df[unique_identifier].isin(source_df[unique_identifier])
    ]

    # Identify records with field discrepancies
    field_discrepancies = pd.merge(
        source_df,
        target_df,
        on=unique_identifier,
        how="inner",
        suffixes=("_source", "_target"),
    )

    # Create a list to hold DataFrames for discrepancies
    discrepancies_dfs = []

    # Records missing in target
    discrepancies_dfs.append(
        missing_in_target[[unique_identifier]]
        .rename(columns={unique_identifier: "Record Identifier"})
        .assign(Type="Missing in Target")
    )

    # Records missing in source
    discrepancies_dfs.append(
        missing_in_source[[unique_identifier]]
        .rename(columns={unique_identifier: "Record Identifier"})
        .assign(Type="Missing in Source")
    )

    # Records with field discrepancies
    for column in source_df.columns[1:]:  # Skip the unique identifier column
        column_discrepancies = field_discrepancies[
            field_discrepancies[f"{column}_source"]
            != field_discrepancies[f"{column}_target"]
        ]
        discrepancies_dfs.append(
            column_discrepancies[[unique_identifier]]
            .rename(columns={unique_identifier: "Record Identifier"})
            .assign(
                Type="Field Discrepancy",
                Field=column,
                Source_Value=column_discrepancies[f"{column}_source"],
                Target_Value=column_discrepancies[f"{column}_target"],
            )
        )

    # Concatenate the DataFrames
    discrepancies_df = pd.concat(discrepancies_dfs, ignore_index=True)

    # Reorder columns
    columns_order = [
        "Type",
        "Record Identifier",
        "Field",
        "Source_Value",
        "Target_Value",
    ]
    discrepancies_df = discrepancies_df[columns_order]

    # Generate a timestamp for uniqueness
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    # Construct the unique output file name
    output_filename = f"{timestamp}.csv"

    # Construct the full output file path
    output_path = os.path.join(output_directory, output_filename)

    # Save the reconciliation report to CSV
    discrepancies_df.to_csv(output_path, index=False)

    return output_path
