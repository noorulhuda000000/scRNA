import scanpy as sc

adata = sc.read(r"C:\Users\hp\Desktop\scRNA_assignment\01_loading\pbmc3k_ra01_loaw.h5ad")

sc.pp.filter_cells(adata, min_genes=200)
sc.pp.filter_genes(adata, min_cells=3)

adata.write("pbmc3k_qc.h5ad")

print("QC done")