# -*- coding: utf-8 -*- #
# Copyright 2014 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Commands for reading and manipulating project-level data."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.calliope import base


class ProjectInfo(base.Group):
  """Read and manipulate project-level data like quotas and metadata."""


ProjectInfo.category = 'Tools'

ProjectInfo.detailed_help = {
    'DESCRIPTION': """
        Read and manipulate project-level data like quotas and metadata.


        `Note`: project-level metadata is a distinct concept from instance-level
        metadata; for details on instance metadata see:
        https://cloud.google.com/compute/docs/storing-retrieving-metadata
        """,
}
