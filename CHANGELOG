## [XX-XX-XX] Initial public release

- **Data processing scripts:**
  - Added `3d_POSE/bag_to_frame_original.py` for extraction and alignment of RGB and depth frames from Intel RealSense `.bag` files, including timestamp synchronization.
  - Added `3D_POSE/coord_extract_original.py` for running YOLOv8-based pose estimation (human and UR10e cobot) on extracted frames, and for reconstructing/exporting 3D keypoints with confidence scores.

- **Training pipeline:**
  - Added `COBOT_MODEL/train.py` and `config.yaml` for custom training of the cobot pose estimation model with YOLOv8.
  - Integrated dataset handling for images and YOLO-format keypoint annotations.
  - Added `COBOT_MODEL/config.yaml` support for custom UR10e keypoint configuration (12 keypoints, including main joints, additional structural points, and gripper).

- **Validation and results:**
  - Included folders for storing validation metrics, training logs, and custom-trained weights in `COBOT_MODEL/runs/`.
  - Provided example data and annotation structure in `cOBOT_MODEL/data/` with subfolders for `images` and `labels` (train/val split).

- **Documentation and compliance:**
  - Added comprehensive `README.md` with project overview, citation instructions, authors, acknowledgments, license/compliance notes, and project structure.
  - Included `NOTICE` file for Ultralytics YOLO attribution.
  - Added full AGPL-3.0 `LICENSE` for code, weights, and derived materials.
  - Included this `CHANGELOG.md` to record major changes and state modifications from the original Ultralytics codebase.
