#!/usr/bin/env python3

import argparse
from pathlib import Path
import sys

from yaml import dump as dump_yaml

from ingest_validation_tools.schema_loader import (
    list_types, get_table_schema, get_directory_schemas)
from ingest_validation_tools.docs_utils import (
    get_tsv_name, generate_template_tsv, generate_readme_md)
from ingest_validation_tools.argparse_types import dir_path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'type',
        choices=list_types(),
        help='What type to generate')
    parser.add_argument(
        'target',
        type=dir_path,
        help='Directory to write output to')
    args = parser.parse_args()

    table_schema = get_table_schema(args.type)
    directory_schemas = get_directory_schemas(args.type)

    with open(Path(args.target) / get_tsv_name(args.type), 'w') as f:
        f.write(generate_template_tsv(table_schema))
    with open(Path(args.target) / 'README.md', 'w') as f:
        f.write(generate_readme_md(table_schema, directory_schemas, args.type))
    with open(Path(args.target) / 'unified.yaml', 'w') as f:
        f.write(
            f'# NOTE: Do not edit this; It is generated by {__file__}.\n\n'
            + dump_yaml(table_schema))


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
