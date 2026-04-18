import scanpy as sc

print("Loading 10X-like dataset...")

# built-in demo dataset (used for assignments)
adata = sc.datasets.pbmc3k()

print("Dataset loaded")

# save raw data
adata.write("pbmc3k_ra01_loaw.h5ad")

print("Saved raw AnnData object as pbmc3k_raw.h5ad")
print("DONE")