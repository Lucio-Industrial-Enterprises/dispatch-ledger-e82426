# Warehouse tools

Small Python utilities for warehouse order and shipping workflows.

Run the tests with `python3 -m unittest discover -s tests -v`.

## Shipping

`shipping_quote(weight_kg, zone, service="standard")` returns a delivery quote
in dollars. Zones are `local` and `regional`; weights must be positive.

| Service    | Surcharge | Local base | Regional base |
|------------|-----------|------------|---------------|
| `standard` | –         | $5.00      | $8.00         |
| `express`  | +$7.00    | $12.00     | $15.00        |

Rate formula: `base + 1.5 × weight_kg (+ $7 for express)`

### Command-line usage

```
python -m warehouse.cli <weight_kg> <zone> [--service {standard,express}]
```

Examples:

```bash
# Standard quote – 3 kg to a local address
python -m warehouse.cli 3 local
# $9.50

# Express quote – 3 kg to a regional address
python -m warehouse.cli 3 regional --service express
# $19.50
```
