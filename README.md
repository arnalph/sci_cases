# sci_cases

`sci_cases` is a Python package for fetching and parsing Supreme Court of India case data.

## Installation

You can install the package from PyPI using pip:

```sh
pip install sci_cases
```

## Usage

Here's how you can use the `sci_cases` package to fetch and parse Supreme Court of India case data.

### Importing the Package

First, import the necessary functions from the package:

```python
from sci_cases import cases_query, get_judgement
```

### Fetching Case Data

Use the `cases_query` function to fetch case data from the Supreme Court of India's website. You can specify various parameters to filter the results.

#### Example Usage:

```python
# Fetch case data for the given parameters
case_data = cases_query(cause_title="union of india", page="23")

# Print the fetched case data
print(case_data)
```

### Fetching Judgment Details

Use the `get_judgement` function to fetch detailed judgment information using the judgment ID.

#### Example Usage:

```python
# Fetch judgment details for the first case in the fetched case data
if case_data["cases"]:
    judgment_id = case_data["cases"][0]["judgment_id"]
    judgement_details = get_judgement(judgment_id)

    # Print the fetched judgment details
    print(judgement_details)
```

### Example Workflow

```python
from sci_cases import cases_query, get_judgement

# Fetch case data for the given parameters
case_data = cases_query(cause_title="union of india", page="23")

# Fetch judgment details for the first case in the fetched case data
if case_data["cases"]:
    judgment_id = case_data["cases"][0]["judgment_id"]
    judgement_details = get_judgement(judgment_id)

    # Print the fetched judgment details
    print(judgement_details)
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
