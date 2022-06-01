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

import braket.ir.neutral_atom.problem_v1 as ir


def test_creation():
    problem = ir.Problem(
        setup=ir.Setup(
            atom_array=ir.AtomArray(
                sites=[
                    [0.0, 0.0],
                    [0.0, 3.0e-6],
                    [0.0, 6.0e-6],
                    [3.0e-6, 0.0],
                    [3.0e-6, 3.0e-6],
                    [3.0e-6, 6.0e-6],
                ],
                filling=[1, 1, 1, 1, 0, 0],
            )
        ),
        hamiltonian=ir.Hamiltonian(
            driving_fields=[
                ir.DrivingField(
                    amplitude=ir.AhsField(
                        sequence=ir.Sequence(
                            values=[0.0, 2.51327e7, 2.51327e7, 0.0],
                            times=[0.0, 3.0e-7, 2.7e-6, 3.0e-6],
                        ),
                        pattern="uniform",
                    ),
                    phase=ir.AhsField(
                        sequence=ir.Sequence(values=[0, 0], times=[0.0, 3.0e-6]), pattern="uniform"
                    ),
                    detuning=ir.AhsField(
                        sequence=ir.Sequence(
                            values=[-1.25664e8, -1.25664e8, 1.25664e8, 1.25664e8],
                            times=[0.0, 3.0e-7, 2.7e-6, 3.0e-6],
                        ),
                        pattern="uniform",
                    ),
                )
            ],
            shifting_fields=[
                ir.ShiftingField(
                    magnitude=ir.AhsField(
                        sequence=ir.Sequence(values=[-1.25664e8, 1.25664e8], times=[0.0, 3.0e-6]),
                        pattern=[0.5, 1.0, 0.5, 0.5, 0.5, 0.5],
                    )
                )
            ],
        ),
    )
    assert ir.Problem.parse_raw(problem.json()) == problem
    assert problem == ir.Problem.parse_raw_schema(problem.json())
