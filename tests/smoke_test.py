import numpy as np
from coastline import segment_coastline

def test_segment_coastline_produces_edges():
	# synthetic image: a black/white half split simulates a coastline-like edge
	img = np.zeros((100, 100), dtype=np.uint8)
	img[:, 50:] = 255
	edges = segment_coastline(img, 50, 150)
	# Expect some edges along the boundary column
	assert edges.sum() > 0
