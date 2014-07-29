# Copyright 2014 - Mirantis, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

from mistral.workbook import base
from mistral.workbook.v2 import namespaces as ns
from mistral.workbook.v2 import triggers as tr
from mistral.workbook.v2 import workflows as wf


class WorkbookSpec(base.BaseSpec):
    # See http://json-schema.org
    _schema = {
        "type": "object",
        "properties": {
            "Version": {"value": "2.0"},
            "Namespaces": {"type": "object"},
            "Workflows": {"type": "object"},
            "Triggers": {"type": "object"}
        },
        "additionalProperties": False
    }

    _version = '2.0'

    def __init__(self, data):
        super(WorkbookSpec, self).__init__(data)

        self._inject_version(['Namespaces', 'Workflows', 'Triggers'])

        self._namespaces = \
            self._spec_property('Namespaces', ns.NamespaceSpecList)
        self._workflows = \
            self._spec_property('Workflows', wf.WorkflowSpecList)
        self._triggers = self._spec_property('Triggers', tr.TriggerSpecList)

    def get_namespaces(self):
        return self._namespaces

    def get_workflows(self):
        return self._workflows

    def get_triggers(self):
        return self._triggers
