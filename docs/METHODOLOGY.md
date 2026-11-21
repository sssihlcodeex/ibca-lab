# Methodology

Research follows four stages: (1) mathematical formulation, (2) validation and benchmarking, (3) open-source release, (4) translational development.

## Leakage-resistant evaluation

- Group-held-out splits: plate-held-out (cellular imaging) and scaffold-held-out (molecular generalisation). `ibca_core.evaluation.group_holdout_split` keeps whole groups on one side.
- Independent train/validation/test partitions, with split construction documented.
- Check for duplicated or near-duplicated samples across partitions.

## Uncertainty and calibration

Confidence is not reliability. Report calibration (e.g. `expected_calibration_error`), and stress-test under distribution shift and changed experimental conditions.

## Reporting

State dataset provenance, preprocessing, model configuration, seeds, dependencies, training procedure, metrics and limitations. Distinguish in-dataset performance from evidence of generalisation.
