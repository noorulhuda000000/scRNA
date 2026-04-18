# Pre-processing of 10X Single-Cell RNA-seq Data

## 1. Overview of 10X scRNA-seq Pipeline

Single-cell RNA sequencing (scRNA-seq) using 10X Genomics allows gene expression profiling at the level of individual cells. The general workflow includes:

- Library preparation and barcoding of individual cells
- Sequencing to generate FASTQ files
- Processing using tools like Cell Ranger
- Generation of a gene-cell count matrix

The count matrix is then used for downstream analysis such as quality control, normalization, and clustering.

---

## 2. AnnData Overview

AnnData is a data structure used for storing and analyzing single-cell data.

- Rows represent cells (observations)
- Columns represent genes (features)
- `.X` stores the expression matrix
- `.obs` contains cell metadata
- `.var` contains gene metadata

AnnData efficiently handles sparse matrices and large datasets, making it suitable for scRNA-seq analysis.

---

## 3. Preprocessing Pipeline Implementation

In this project, a basic preprocessing pipeline was implemented using Scanpy:

### Step 1: Data Loading
- Dataset: PBMC 3k (built-in Scanpy dataset)
- Stored as: `pbmc3k_raw.h5ad`

### Step 2: Quality Control
- Removed low-quality cells and genes
- Output: `pbmc3k_qc.h5ad`

### Step 3: Normalization
- Performed total count normalization
- Applied log transformation
- Output: `pbmc3k_normalized.h5ad`

---

## 4. Project Structure
01_loading/ # Raw data loading
02_qc/ # Quality control step
03_normalization/ # Normalization step

---

## 5. Conclusion

This project demonstrates a basic preprocessing workflow for single-cell RNA-seq data using Scanpy and AnnData. The pipeline includes loading, quality control, and normalization, which are essential steps before downstream analysis.
