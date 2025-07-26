# -------------------------------------------------------------------------
# Project: dogdog-ui
# Author: songjianfeng
# Date: 2025/1/22 15:00
# Description: 特征配置文件，用于加载feature.toml中的特征定义
# -------------------------------------------------------------------------
import os.path

import toml

feature_config_path = os.path.abspath(__file__).replace('.py', '.toml')
feature_config = toml.load(feature_config_path)
print(feature_config)
# 获取特征配置
features = feature_config.get('feature') 