# mxif

Related files:
- [🔬 Background doc](https://docs.google.com/document/d/1ParihsMo5fqhJEhTTBfwqHuaBpr-ZeveZJKLgrZiQCo/edit): More details about this type.
- [📝 TSV template](https://raw.githubusercontent.com/hubmapconsortium/ingest-validation-tools/master/docs/mxif/mxif-metadata.tsv): Use this to submit metadata.
- [💻 Source code](https://github.com/hubmapconsortium/ingest-validation-tools/edit/master/src/ingest_validation_tools/table-schemas/level-2/mxif.yaml): Make a PR if this doc should be updated.

## Table of contents
<details><summary>Provenance</summary>

[`donor_id`](#donor_id)<br>
[`tissue_id`](#tissue_id)<br>
</details>

<details><summary>Level 1</summary>

[`execution_datetime`](#execution_datetime)<br>
[`protocols_io_doi`](#protocols_io_doi)<br>
[`operator`](#operator)<br>
[`operator_email`](#operator_email)<br>
[`pi`](#pi)<br>
[`pi_email`](#pi_email)<br>
[`assay_category`](#assay_category)<br>
[`assay_type`](#assay_type)<br>
[`analyte_class`](#analyte_class)<br>
[`is_targeted`](#is_targeted)<br>
</details>

<details><summary>Level 2</summary>

[`acquisition_instrument_vendor`](#acquisition_instrument_vendor)<br>
[`acquisition_instrument_model`](#acquisition_instrument_model)<br>
[`resolution_x_value`](#resolution_x_value)<br>
[`resolution_x_unit`](#resolution_x_unit)<br>
[`resolution_y_value`](#resolution_y_value)<br>
[`resolution_y_unit`](#resolution_y_unit)<br>
[`number_of_channels`](#number_of_channels)<br>
[`number_of_cycles`](#number_of_cycles)<br>
[`section_prep_protocols_io_doi`](#section_prep_protocols_io_doi)<br>
[`reagent_prep_protocols_io_doi`](#reagent_prep_protocols_io_doi)<br>
[`overall_protocols_io_doi`](#overall_protocols_io_doi)<br>
</details>

<details><summary>Paths</summary>

[`metadata_path`](#metadata_path)<br>
[`data_path`](#data_path)<br></details>

## Provenance

### `donor_id`
HuBMAP Display ID of the donor of the assayed tissue.

| constraint | value |
| --- | --- |
| pattern (regular expression) | `[A-Z]+[0-9]+` |
| required | `True` |

### `tissue_id`
HuBMAP Display ID of the assayed tissue.

| constraint | value |
| --- | --- |
| pattern (regular expression) | `([A-Z]+[0-9]+)-(BL\|BR\|LB\|RB\|HT\|LK\|RK\|LI\|LV\|LL\|RL\|LY\d\d\|SI\|SP\|TH\|TR\|UR\|OT)(-\d+)+(_\d+)?` |
| required | `True` |

## Level 1

### `execution_datetime`
Start date and time of assay, typically a date-time stamped folder generated by the acquisition instrument. YYYY-MM-DD hh:mm, where YYYY is the year, MM is the month with leading 0s, and DD is the day with leading 0s, hh is the hour with leading zeros, mm are the minutes with leading zeros.

| constraint | value |
| --- | --- |
| type | `datetime` |
| format | `%Y-%m-%d %H:%M` |
| required | `True` |

### `protocols_io_doi`
DOI for protocols.io referring to the protocol for this assay.

| constraint | value |
| --- | --- |
| required | `True` |
| pattern (regular expression) | `10\.17504/.*` |

### `operator`
Name of the person responsible for executing the assay.

| constraint | value |
| --- | --- |
| required | `True` |

### `operator_email`
Email address for the operator.

| constraint | value |
| --- | --- |
| format | `email` |
| required | `True` |

### `pi`
Name of the principal investigator responsible for the data.

| constraint | value |
| --- | --- |
| required | `True` |

### `pi_email`
Email address for the principal investigator.

| constraint | value |
| --- | --- |
| format | `email` |
| required | `True` |

### `assay_category`
Each assay is placed into one of the following 3 general categories: generation of images of microscopic entities, identification & quantitation of molecules by mass spectrometry, and determination of nucleotide sequence.

| constraint | value |
| --- | --- |
| enum | `imaging` |
| required | `True` |

### `assay_type`
The specific type of assay being executed.

| constraint | value |
| --- | --- |
| enum | `MxIF` |
| required | `True` |

### `analyte_class`
Analytes are the target molecules being measured with the assay.

| constraint | value |
| --- | --- |
| enum | `protein` |
| required | `True` |

### `is_targeted`
Specifies whether or not a specific molecule(s) is/are targeted for detection/measurement by the assay. The CODEX analyte is protein.

| constraint | value |
| --- | --- |
| type | `boolean` |
| required | `True` |

## Level 2

### `acquisition_instrument_vendor`
An acquisition_instrument is the device that contains the signal detection hardware and signal processing software. Assays generate signals such as light of various intensities or color or signals representing molecular mass.

| constraint | value |
| --- | --- |
| required | `True` |

### `acquisition_instrument_model`
Manufacturers of an acquisition instrument may offer various versions (models) of that instrument with different features or sensitivities. Differences in features or sensitivities may be relevant to processing or interpretation of the data.

| constraint | value |
| --- | --- |
| required | `True` |

### `resolution_x_value`
The width of a pixel.

| constraint | value |
| --- | --- |
| type | `number` |
| required | `True` |

### `resolution_x_unit`
The unit of measurement of width of a pixel.(nm)

| constraint | value |
| --- | --- |
| enum | `nm` or `um` |
| required | `True` |

### `resolution_y_value`
The height of a pixel.

| constraint | value |
| --- | --- |
| type | `number` |
| required | `True` |

### `resolution_y_unit`
The unit of measurement of height of a pixel.(nm)

| constraint | value |
| --- | --- |
| enum | `nm` or `um` |
| required | `True` |

### `number_of_channels`
Number of fluorescent channels imaged during each cycle.

| constraint | value |
| --- | --- |
| type | `integer` |
| required | `True` |

### `number_of_cycles`
Number of cycles of 1. antibody application, 2. image capture, 3. antibody stripping.

| constraint | value |
| --- | --- |
| type | `integer` |
| required | `True` |

### `section_prep_protocols_io_doi`
DOI for protocols.io referring to the protocol for preparing tissue sections for the assay.

| constraint | value |
| --- | --- |
| required | `True` |
| pattern (regular expression) | `10\.17504/.*` |

### `reagent_prep_protocols_io_doi`
DOI for protocols.io referring to the protocol for preparing reagents for the assay.

| constraint | value |
| --- | --- |
| required | `True` |
| pattern (regular expression) | `10\.17504/.*` |

### `overall_protocols_io_doi`
DOI for protocols.io for the overall process.

| constraint | value |
| --- | --- |
| required | `True` |
| pattern (regular expression) | `10\.17504/.*` |

## Paths

### `metadata_path`
Relative path to file or directory with free-form or instrument/lab specific metadata. Optional. Leave blank if not applicable.

| constraint | value |
| --- | --- |
| required | `False` |

### `data_path`
Relative path to file or directory with instrument data. Downstream processing will depend on filename extension conventions.

| constraint | value |
| --- | --- |
| required | `True` |
