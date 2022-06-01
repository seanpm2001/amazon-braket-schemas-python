# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

from decimal import Decimal
from typing import List, Tuple, Union

from pydantic import BaseModel, Field

from braket.schema_common import BraketSchemaBase, BraketSchemaHeader


class AtomArray(BaseModel):
    sites: List[Tuple[Decimal, ...]]
    filling: List[Decimal]


class Setup(BaseModel):
    atom_array: AtomArray


class Sequence(BaseModel):
    times: List[Decimal]
    values: List[Decimal]


class AhsField(BaseModel):
    sequence: Sequence
    pattern: Union[str, List[Decimal]]


class DrivingField(BaseModel):
    amplitude: AhsField
    phase: AhsField
    detuning: AhsField


class ShiftingField(BaseModel):
    magnitude: AhsField


class Hamiltonian(BaseModel):
    driving_fields: List[DrivingField]
    shifting_fields: List[ShiftingField]


class Problem(BraketSchemaBase):
    _PROBLEM_HEADER = BraketSchemaHeader(name="braket.ir.neutral_atom.problem", version="1")
    braketSchemaHeader: BraketSchemaHeader = Field(default=_PROBLEM_HEADER, const=_PROBLEM_HEADER)
    setup: Setup
    hamiltonian: Hamiltonian
