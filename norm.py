import scanpy as sc

print("Loading QC data...")

adata = sc.read(r"C:\Users\hp\Desktop\scRNA_assignment\01_loading\pbmc3k_ra01_loaw.h5ad")

print("Normalizing data...")

sc.pp.normalize_total(adata)
sc.pp.log1p(adata)

print("Saving normalized data...")

adata.write("pbmc3k_normalized.h5ad")

print("DONE")