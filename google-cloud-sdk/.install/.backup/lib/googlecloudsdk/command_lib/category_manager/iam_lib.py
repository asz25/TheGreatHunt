# -*- coding: utf-8 -*- #
# Copyright 2017 Google Inc. All Rights Reserved.
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
"""Commands for IAM related operations in Cloud Category Manager."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.api_lib.category_manager import store
from googlecloudsdk.api_lib.category_manager import utils
from googlecloudsdk.command_lib.category_manager import util
from googlecloudsdk.command_lib.iam import iam_util


def AddIamPolicyBinding(resource_resource, role, member, module):
  """Add a member to an iam role binding on resource."""
  policy = module.GetIamPolicy(resource_resource)
  iam_util.AddBindingToIamPolicy(utils.GetMessagesModule().Binding, policy,
                                 member, role)
  return module.SetIamPolicy(resource_resource, policy)


def RemoveIamPolicyBinding(resource_resource, role, member, module):
  """Remove a member to a resource."""
  policy = module.GetIamPolicy(resource_resource)
  iam_util.RemoveBindingFromIamPolicy(policy, member, role)
  return module.SetIamPolicy(resource_resource, policy)


def GetOrgIamPolicy(org_resource):
  """Get Iam policy with an organization reference."""
  return store.GetIamPolicy(util.GetTaxonomyStoreFromOrgResource(org_resource))
