import json
from pathlib import Path

src = Path('notebooks/Hydro_mainly.ipynb')
nb = json.loads(src.read_text())

segments = [
    (Path('notebooks/Hydro_data_prep.ipynb'), range(0, 14)),
    (Path('notebooks/Hydro_analysis.ipynb'), range(14, 61)),
    (Path('notebooks/Hydro_ttf_eua.ipynb'), range(61, len(nb['cells'])))
]

for path, rng in segments:
    new_nb = {
        'cells': [nb['cells'][i] for i in rng],
        'metadata': nb.get('metadata', {}),
        'nbformat': nb.get('nbformat', 4),
        'nbformat_minor': nb.get('nbformat_minor', 0),
    }
    path.write_text(json.dumps(new_nb, indent=1))
    print(f'Wrote {path} with {len(rng)} cells')
