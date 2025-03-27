# -------------------------------------------------------------------------
# Project: dogdog-ui
# Author: songjianfeng
# Date: 2025/3/25 14:34
# Description:
# -------------------------------------------------------------------------
import os

from airtest.core.api import Template

from common.config import config
from common.ui import current_device_type


class DogTemplate(Template):
    def __init__(self, filename, **kwargs):
        base_dir = current_device_type.value
        self.filename = os.path.join(config.get_images_dir(), base_dir, filename)
        super().__init__(self.filename, **kwargs)
