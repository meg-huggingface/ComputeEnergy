# Compute Energy

This provides basic code to extract the electricity usage for different CPUs and GPUs that Hugging Face offers in [Inference Endpoints](https://api.endpoints.huggingface.cloud). 

The values given are in Watts, and are extracted from the various Datasheets the manufacturers have made available.
Sometimes they are referred to as 'Power', othertimes as 'Max Thermal Design Power (TDP)'. 

(TODO: Are these always the same thing?)

All data is included in `compute_datasheet_info.json`.
The datasheets are linked in the `'sources'` key.

## Example Usage:

import get_electricity

get_electricity.get_electricity('nvidia-h100')

## Supported Instance Types:

'intel-icl', 'intel-spr', 'intel-xeon', 'nvidia-a10g', 'nvidia-t4', 'nvidia-l4', 'nvidia-a100', 'nvidia-l40s', 'nvidia-h100'
