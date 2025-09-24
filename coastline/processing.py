import json
import time
from pathlib import Path
from typing import Dict

import cv2
import numpy as np


def segment_coastline(gray_image: np.ndarray,
					   low_threshold: int = 50,
					   high_threshold: int = 150) -> np.ndarray:
	"""Return an edge map approximating the coastline from a grayscale image.

	Parameters
	----------
	gray_image: np.ndarray
		Single-channel image with dtype uint8.
	low_threshold: int
		Canny low threshold.
	high_threshold: int
		Canny high threshold.

	Returns
	-------
	np.ndarray
		Binary edge map (uint8) with values in {0, 255}.
	"""
	if gray_image is None:
		raise ValueError("gray_image is None")
	if gray_image.ndim != 2:
		raise ValueError("segment_coastline expects a single-channel (grayscale) image")
	if gray_image.dtype != np.uint8:
		gray_image = cv2.normalize(gray_image, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

	blurred = cv2.GaussianBlur(gray_image, (5, 5), 0)
	edges = cv2.Canny(blurred, low_threshold, high_threshold)
	return edges


def save_metadata(output_path: Path,
				  region_name: str,
				  dataset_info: Dict[str, str],
				  parameters: Dict[str, str]) -> Path:
	"""Save a small JSON metadata file alongside an image result.

	The JSON file shares the same stem as the output image.
	"""
	output_path = Path(output_path)
	metadata_path = output_path.with_suffix("")
	metadata_path = metadata_path.with_name(metadata_path.name + "_metadata.json")

	payload = {
		"region": region_name,
		"dataset": dataset_info,
		"params": parameters,
		"timestamp": int(time.time()),
		"tool_versions": {
			"opencv": cv2.__version__,
			"numpy": np.__version__,
		},
	}

	metadata_path.parent.mkdir(parents=True, exist_ok=True)
	with open(metadata_path, "w", encoding="utf-8") as f:
		json.dump(payload, f, indent=2)
	return metadata_path


def compose_side_by_side(left_gray: np.ndarray, right_gray: np.ndarray,
						 edges: np.ndarray) -> np.ndarray:
	"""Compose a simple visualization: left | edges | right.

	This is a lightweight utility for quick demos; it does not perform
	geospatial alignment.
	"""
	def to_bgr(im: np.ndarray) -> np.ndarray:
		if im.ndim == 2:
			return cv2.cvtColor(im, cv2.COLOR_GRAY2BGR)
		return im

	left = to_bgr(left_gray)
	right = to_bgr(right_gray)

	edge_bgr = np.zeros_like(left)
	edge_bgr[:, :, 2] = edges  # red channel

	return np.concatenate([left, edge_bgr, right], axis=1)
