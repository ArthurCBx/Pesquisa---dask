"""
Gera 10 arquivos CSV sintéticos em data/ para o Exemplo 3 do benchmark.
Total: 10 M de linhas (~500 MB no disco).
"""
import pandas as pd
import numpy as np
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
N_ARQUIVOS = 10
LINHAS_POR_ARQUIVO = 1_000_000

os.makedirs(DATA_DIR, exist_ok=True)

rng = np.random.default_rng(42)
for i in range(N_ARQUIVOS):
    path = os.path.join(DATA_DIR, f"dados_{i:02d}.csv")
    pd.DataFrame({
        "id":         np.arange(i * LINHAS_POR_ARQUIVO, (i + 1) * LINHAS_POR_ARQUIVO),
        "categoria":  rng.choice(["A", "B", "C", "D"], LINHAS_POR_ARQUIVO),
        "valor":      rng.normal(0, 100, LINHAS_POR_ARQUIVO),
        "quantidade": rng.integers(1, 500, LINHAS_POR_ARQUIVO),
    }).to_csv(path, index=False)
    print(f"  [{i+1:02d}/{N_ARQUIVOS}] {path}  ({os.path.getsize(path)/1e6:.0f} MB)")

total = sum(os.path.getsize(os.path.join(DATA_DIR, f"dados_{i:02d}.csv")) for i in range(N_ARQUIVOS))
print(f"\nPronto! {N_ARQUIVOS} arquivos | Total: {total/1e6:.0f} MB em {DATA_DIR}/")
