'''
Author: EasonZhang
Date: 2024-07-26 16:06:23
LastEditors: EasonZhang
LastEditTime: 2024-07-26 16:12:01
FilePath: /A2PM-MESA/point_matchers/ASpanFormer/configs/data/megadepth_test_1500.py
Description: path update

Copyright (c) 2024 by EasonZhang, All Rights Reserved. 
'''
from point_matchers.ASpanFormer.src.config.default import _CN as cfg

TEST_BASE_PATH = "assets/megadepth_test_1500_scene_info"

cfg.DATASET.TEST_DATA_SOURCE = "MegaDepth"
cfg.DATASET.TEST_DATA_ROOT = "data/megadepth/test"
cfg.DATASET.TEST_NPZ_ROOT = f"{TEST_BASE_PATH}"
cfg.DATASET.TEST_LIST_PATH = f"{TEST_BASE_PATH}/megadepth_test_1500.txt"

cfg.DATASET.MGDPT_IMG_RESIZE = 1152
cfg.DATASET.MGDPT_IMG_PAD=True
cfg.DATASET.MGDPT_DF =8
cfg.DATASET.MIN_OVERLAP_SCORE_TEST = 0.0