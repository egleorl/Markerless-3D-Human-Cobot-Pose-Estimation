# This file is part of Markerless-3D-Human-Cobot-Pose-Estimation
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Portions derived from Ultralytics YOLO, Copyright © Ultralytics Inc., AGPL-3.0.

import pyrealsense2 as rs
import numpy as np
import cv2
import os
import pandas as pd

bag_file = r"C:\path\to\your\file\data\example.bag"  # .bag file name
output_dir = r"C:\path\to\your\output\folder"  # Unique output folder
os.makedirs(output_dir, exist_ok=True)

# Pipeline configuration
pipeline = rs.pipeline()
config = rs.config()
config.enable_device_from_file(bag_file, repeat_playback=False)

# Start the pipeline
pipeline.start(config)

# Align depth frames with RGB frames ->  This is an essential step in obtaining reliable depth information!!
align_to = rs.stream.color
align = rs.align(align_to)

frame_count = 0
timestamps = []

try:
    while True:
        frames = pipeline.wait_for_frames()
        aligned_frames = align.process(frames)

        color_frame = aligned_frames.get_color_frame()
        depth_frame = aligned_frames.get_depth_frame()

        if not color_frame or not depth_frame:
            continue

        color_image = np.asanyarray(color_frame.get_data())
        depth_array = np.asanyarray(depth_frame.get_data())

        rgb_filename = os.path.join(output_dir, f"rgb_frame_{frame_count:05d}.png")
        cv2.imwrite(rgb_filename, cv2.cvtColor(color_image, cv2.COLOR_RGB2BGR))

        # Save depth frame as .npy -> -> In the next script, each RGB frame is associated with its corresponding numpy file to add depth
        depth_filename = os.path.join(output_dir, f"depth_frame_{frame_count:05d}.npy")
        np.save(depth_filename, depth_array)

        # extract timestamps as metadata from the bag file, useful for subsequent synchronization needs
        timestamp_ms = color_frame.get_timestamp()
        time_of_arrival = None
        if color_frame.supports_frame_metadata(rs.frame_metadata_value.time_of_arrival):
            time_of_arrival = color_frame.get_frame_metadata(rs.frame_metadata_value.time_of_arrival)

        timestamps.append({
            'frame_index': frame_count,
            'timestamp_ms': timestamp_ms,
            'time_of_arrival_ms': time_of_arrival
        })

        print(f"Frame {frame_count} saved")
        frame_count += 1

except RuntimeError:
    print("End of .bag video")

finally:
    pipeline.stop()
    df_timestamps = pd.DataFrame(timestamps)
    df_timestamps.to_csv(os.path.join(output_dir, 'frame_timestamps.csv'), index=False)
    print(f"Conversion completed: {frame_count} frames saved in {output_dir}.")

# === USEFUL REFERENCES ===
# useful references links: https://github.com/IntelRealSense/librealsense/issues/13755#issuecomment-2659343709 

# https://github.com/IntelRealSense/librealsense/issues/13867#issuecomment-2736919072
