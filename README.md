# Markerless 3D Human–Cobot Pose Estimation (UR10e) with YOLOv8

This repository provides a markerless pipeline for the concurrent 3D pose estimation of a human operator and a UR10e cobot using a single RGB-D camera. The approach integrates a 2D pose estimation architecture (YOLOv8) and a 3D coordinate reconstruction stage, enabling the analysis of shared actions and kinematics in human–robot collaboration (HRC) scenarios.

> **This project builds upon [Ultralytics YOLO](https://github.com/ultralytics/ultralytics), licensed under [AGPL-3.0](https://www.ultralytics.com/legal/agpl-3-0-software-license). Copyright © Ultralytics Inc.**

---

## Overview

- **Scripts for Data Extraction and Processing (`3D_POSE/`):**
  - `bag_to_frame_original.py`: Extracts synchronized RGB and depth frames from Intel RealSense `.bag` recordings.
  - `coord_extract_original.py`: Runs YOLOv8-based pose estimation on the extracted frames and reconstructs 3D keypoints for both the human and the UR10e cobot in a temporally synchronized manner. The output is a single CSV file containing the timestamped 3D coordinates and confidence scores for all keypoints and other details.

- **Training Materials (`COBOT_MODEL/`):**
  - `train.py`: Script used to train the custom YOLOv8 model for the cobot.
  - `config.yaml`: Configuration file for keypoint layout and training parameters.

- **Results (`COBOT_MODEL/`):**
  - `runs/`: Contains validation metrics, training logs, and custom-trained model weights.

---

## Dataset Access

The dataset used for training and validation is not included in this repository due to size constraints.

**To request access to the data:**
- Please contact: **eglemaria.orlando@phd.unipd.it**
- When available, you will receive a download link.

To use the data:
1. Download and unzip the archive you receive.
2. The extracted `data/` folder will already be organized with the conventional structure (`images/train`, `images/val`, `labels/train`, `labels/val`).
3. Simply place the entire `data/` folder in the same directory as the training script (`train.py`) and configuration file (`config.yaml`).

---

## License

- The entire codebase, trained weights, and validation metrics are released under the AGPL-3.0 license.
- Portions of the code and weights are derived from Ultralytics YOLO (see LICENSE and NOTICE for details).
- If this software is provided as a service (e.g., web app, API), users must be offered the complete corresponding source code as required by AGPL‑3.0.

---

## Citation

If you use this project, please cite both this repository and Ultralytics as follows:

> This project builds upon Ultralytics YOLO ([GitHub](https://github.com/ultralytics/ultralytics)), licensed under AGPL-3.0. For details, see the upstream repository.

### **Related Paper**

If you use this codebase or datasets for your research, please also cite:

```
@article{orlando2026capturing,
  title={Capturing Shared Actions and Coordination in Collaborative Workspaces: A Markerless Pipeline for Synchronized Human-Robot 3D Pose Estimation},
  author={Orlando, Egle Maria and Nenna, Federica and Lorusso, Federico Maria and Mingardi, Michele and Buodo, Giulia and Gamberini, Luciano},
  journal={IEEE Access},
  year={2026},
  publisher={IEEE}
}
```

---

## Authors

- **Egle Maria Orlando** (University of Padova, eglemaria.orlando@phd.unipd.it)
- **Federica Nenna** (University of Padova)
- **Federico Maria Lorusso** (University of Padova)
- **Michele Mingardi** (University of Padova)
- **Giulia Buodo** (University of Padova)
- **Luciano Gamberini** (University of Padova)

---

## Acknowledgments

- [Ultralytics](https://ultralytics.com) for the YOLOv8 base code and all dataset contributors.
- [Intel RealSense SDK 2.0](https://github.com/IntelRealSense/librealsense) (2024), Intel Corporation, for the hardware and SDK used for RGB-D data acquisition.
- Lambrecht et al. (2019) for part of the dataset used for cobot training.

This study was carried out within the PNRR research activities of the consortium iNEST (Interconnected North-Est Innovation Ecosystem) funded by the European Union Next-GenerationEU (Piano Nazionale di Ripresa e Resilienza (PNRR) – Missione 4 Componente 2, Investimento 1.5 – D.D. 1058 23/06/2022, ECS_00000043).

---

## State Changes

See `CHANGELOG.md` for details of changes and custom modules added to the original Ultralytics YOLO codebase.
