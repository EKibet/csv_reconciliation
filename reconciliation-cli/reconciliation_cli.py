import argparse
import pandas as pd
from datetime import datetime


def reconcile_csv(source_path, target_path, output_path):
    # Read CSV files into pandas DataFrames
    source_df = pd.read_csv(source_path)
    target_df = pd.read_csv(target_path)

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

    # Create a DataFrame for discrepancies
    discrepancies_df = pd.DataFrame(
        columns=["Type", "Record Identifier", "Field", "Source Value", "Target Value"]
    )

    # Records missing in target
    discrepancies_df = pd.concat(
        [discrepancies_df, missing_in_target.assign(Type="Missing in Target")]
    )

    # Records missing in source
    discrepancies_df = pd.concat(
        [discrepancies_df, missing_in_source.assign(Type="Missing in Source")]
    )

    # Records with field discrepancies
    field_discrepancy_columns = []
    for column in source_df.columns[1:]:  # Skip the unique identifier column
        column_discrepancies = field_discrepancies[
            field_discrepancies[f"{column}_source"]
            != field_discrepancies[f"{column}_target"]
        ]
        field_discrepancy_columns.append(
            column_discrepancies.rename(
                columns={
                    unique_identifier: "Record Identifier",
                    f"{column}_source": "Source Value",
                    f"{column}_target": "Target Value",
                }
            ).assign(Type="Field Discrepancy", Field=column)
        )

    # Count the number of columns with discrepancies
    num_discrepancy_columns = sum(
        1
        for column_discrepancy in field_discrepancy_columns
        if not column_discrepancy.empty
    )

    # Concatenate the field discrepancies
    discrepancies_df = pd.concat([discrepancies_df] + field_discrepancy_columns)

    # Save the reconciliation report to CSV
    discrepancies_df.to_csv(output_path, index=False)

    # Return a summary message
    return f"Reconciliation completed:\n- Records missing in target: {len(missing_in_target)}\n- Records missing in source: {len(missing_in_source)}\n- Columns with field discrepancies: {num_discrepancy_columns}\nReport saved to: {output_path}"


def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(description="CSV Reconciler CLI")

    # Add command-line arguments
    parser.add_argument(
        "-s", "--source", help="Path to the source CSV file", required=True
    )
    parser.add_argument(
        "-t", "--target", help="Path to the target CSV file", required=True
    )
    parser.add_argument(
        "-o",
        "--output",
        help="Path to save the output reconciliation report",
        required=True,
    )

    # Parse the command-line arguments
    args = parser.parse_args()

    # Perform the reconciliation
    try:
        result_message = reconcile_csv(args.source, args.target, args.output)
        print(result_message)
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
