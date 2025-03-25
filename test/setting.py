# -------------------------------------------------------------------------
# Project: dogdog
# Author: songjianfeng
# Date: 2025/2/7 11:16
# Description: 测试用例相关的配置放在此处
# -------------------------------------------------------------------------
import os.path

import toml

setting_config_path = os.path.abspath(__file__).replace('.py', '.toml')
setting_config = toml.load(setting_config_path)

# 获取飞书消息模板
report = setting_config.get('report')
feishu_bot = setting_config.get('feishu')['bot_url']