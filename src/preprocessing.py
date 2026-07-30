import pandas as pd


def clean_text_data(df, text_column="text"):
    """
    Remove missing, empty, and duplicate text samples.
    """
    df = df.copy()

    df = df.dropna(subset=[text_column])
    df[text_column] = df[text_column].astype(str).str.strip()
    df = df[df[text_column] != ""]
    df = df.drop_duplicates(subset=[text_column])

    return df


def balance_classes(df, label_column="label", random_state=42):
    """
    Balance Stress and Depression classes using random downsampling.
    """
    minimum_size = df[label_column].value_counts().min()

    balanced_df = (
        df.groupby(label_column, group_keys=False)
        .sample(n=minimum_size, random_state=random_state)
        .sample(frac=1, random_state=random_state)
        .reset_index(drop=True)
    )

    return balanced_df
