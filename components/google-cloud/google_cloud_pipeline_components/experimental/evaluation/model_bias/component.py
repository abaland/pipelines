# Copyright 2023 The Kubeflow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from google_cloud_pipeline_components.types.artifact_types import BQTable
from kfp.dsl import Artifact
from kfp.dsl import ConcatPlaceholder
from kfp.dsl import container_component
from kfp.dsl import ContainerSpec
from kfp.dsl import IfPresentPlaceholder
from kfp.dsl import Input
from kfp.dsl import Output
from kfp.dsl import OutputPath
from kfp.dsl import PIPELINE_JOB_ID_PLACEHOLDER
from kfp.dsl import PIPELINE_ROOT_PLACEHOLDER
from kfp.dsl import PIPELINE_TASK_ID_PLACEHOLDER


@container_component
def detect_model_bias(
    gcp_resources: OutputPath(str),
    bias_model_metrics: Output[Artifact],
    project: str,
    target_field_name: str,
    bias_configs: list,
    location: str = 'us-central1',
    predictions_format: str = 'jsonl',
    predictions_gcs_source: Input[Artifact] = None,
    predictions_bigquery_source: Input[BQTable] = None,
    thresholds: list = [],
    encryption_spec_key_name: str = '',
):
  """Detects bias metrics from a model's predictions.

  Args:
      project (str): Project to run data bias detection.
      location (Optional[str]): Location for running data bias detection. If not
        set, defaulted to `us-central1`.
      target_field_name (str): The full name path of the features target field
        in the predictions file. Formatted to be able to find nested columns,
        delimited by `.`. Alternatively referred to as the ground truth (or
        ground_truth_column) field.
      predictions_format (Optional[str]): The file format for the batch
        prediction results. `jsonl`, `csv`, and `bigquery` are the currently
        allowed formats. If not set, defaulted to `jsonl`.
      predictions_gcs_source (Optional[system.Artifact]): An artifact with its
        URI pointing toward a GCS directory with prediction or explanation files
        to be used for this evaluation. For prediction results, the files should
        be named "prediction.results-*". For explanation results, the files
        should be named "explanation.results-*".
      predictions_bigquery_source (Optional[google.BQTable]): BigQuery table
        with prediction or explanation data to be used for this evaluation. For
        prediction results, the table column should be named "predicted_*".
      bias_configs (Sequence[BiasConfig]): A list of
        google.cloud.aiplatform_v1.types.ModelEvaluation.BiasConfig. When
        provided, compute model bias metrics for each defined slice. Below is an
        example of how to format this input.
        1: First, create a BiasConfig. ```from
          google.cloud.aiplatform_v1.types.ModelEvaluation import BiasConfig
          from google.cloud.aiplatform_v1.types.ModelEvaluationSlice.Slice
          import SliceSpec from
          google.cloud.aiplatform_v1.types.ModelEvaluationSlice.Slice.SliceSpec
          import SliceConfig bias_config = BiasConfig(bias_slices=SliceSpec(
          configs={ 'feature_a': SliceConfig(SliceSpec.Value(string_value=
          'label_a') ) }))```
        2: Create a list to store the bias configs into. `bias_configs = []`.
        3: Format each BiasConfig into a JSON or Dict. `bias_config_json =
          json_format.MessageToJson(bias_config` or `bias_config_dict =
          json_format.MessageToDict(bias_config).
        4: Combine each bias_config JSON into a list.
          `bias_configs.append(bias_config_json)`.
        5: Finally, pass bias_configs as an parameter for this component.
          `DetectModelBiasOp(bias_configs=bias_configs)`
      thresholds (Optional[Sequence[float]]): A list of float values to be used
        as prediction decision thresholds. Defaulted to [0.5f] in the container.
      encryption_spec_key_name (Optional[str]): Customer-managed encryption key
        options for the CustomJob. If this is set, then all resources created by
        the CustomJob will be encrypted with the provided encryption key.

  Returns:
      bias_model_metrics (system.Artifact):
          Artifact tracking the model bias detection output.
      gcp_resources (str):
          Serialized gcp_resources proto tracking the batch prediction job.
          For more details, see
          https://github.com/kubeflow/pipelines/blob/master/components/google-cloud/google_cloud_pipeline_components/proto/README.md.
  """
  return ContainerSpec(
      image='gcr.io/ml-pipeline/model-evaluation:v0.9.1',
      command=[
          'python3',
          '/main.py',
      ],
      args=[
          '--task',
          'model_bias',
          '--bias_configs',
          bias_configs,
          '--target_field_name',
          target_field_name,
          '--batch_prediction_format',
          predictions_format,
          IfPresentPlaceholder(
              input_name='predictions_gcs_source',
              then=[
                  '--batch_prediction_gcs_source',
                  "{{$.inputs.artifacts['predictions_gcs_source'].uri}}",
              ],
          ),
          IfPresentPlaceholder(
              input_name='predictions_bigquery_source',
              then=[
                  '--batch_prediction_bigquery_source',
                  ConcatPlaceholder([
                      'bq://',
                      "{{$.inputs.artifacts['predictions_bigquery_source'].metadata['projectId']}}",
                      '.',
                      "{{$.inputs.artifacts['predictions_bigquery_source'].metadata['datasetId']}}",
                      '.',
                      "{{$.inputs.artifacts['predictions_bigquery_source'].metadata['tableId']}}",
                  ]),
              ],
          ),
          '--project',
          project,
          '--location',
          location,
          '--dataflow_job_prefix',
          f'evaluation-detect-model-bias-{PIPELINE_JOB_ID_PLACEHOLDER}-{PIPELINE_TASK_ID_PLACEHOLDER}',
          '--root_dir',
          f'{PIPELINE_ROOT_PLACEHOLDER}/{PIPELINE_JOB_ID_PLACEHOLDER}-{PIPELINE_TASK_ID_PLACEHOLDER}',
          '--output_metrics_gcs_path',
          bias_model_metrics.path,
          '--gcp_resources',
          gcp_resources,
          '--thresholds',
          thresholds,
          '--executor_input',
          '{{$}}',
      ],
  )
