# CM0526 - Silhouette-based space carving

This repo contains a solution for the final project of the G3DCV (2022/2023) course at Venice University.
The implemented features are:

- [x] Camera calibration
- [x] Pose estimation
- [x] Silhouette extraction
- [x] Voxel Carving
- [x] Voxel coloring

## Prerequisites

In order to install the required dependencies and run the source code you must have installed anaconda (or miniconda) on your system

If you want to avoid anaconda, be sure to have installed
- OpenCV == 4.6
- Numpy  == 1.21
- Progress == 1.6
- Jupyter notebook

## How to run

### 1. Activate the environment

    ```bash
    conda env activate --from-file environment.yml
    ```

### 1. Download data

    ```bash
    chmod +x init.sh
    ./init.sh
    ```
### 2. Start the jupyter notebooks
    ```bash
    jupyter notebook
    ```

