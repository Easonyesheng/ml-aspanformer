'''
Author: EasonZhang
Date: 2024-06-06 16:10:41
LastEditors: EasonZhang
LastEditTime: 2024-06-06 22:30:46
FilePath: /SGAM/Matchers/ASpanFormer/configs/aspan/indoor/aspan_test.py
Description: modified

Copyright (c) 2024 by EasonZhang, All Rights Reserved. 
'''
from Matchers.ASpanFormer.src.config.default import _CN as cfg

cfg.ASPAN.MATCH_COARSE.MATCH_TYPE = 'dual_softmax'

cfg.ASPAN.MATCH_COARSE.BORDER_RM = 0
cfg.ASPAN.COARSE.COARSEST_LEVEL= [15,20]
cfg.ASPAN.COARSE.TRAIN_RES = [480,640]