# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class ActivityRunsOperations:
    """ActivityRunsOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.synapse.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    async def query_by_pipeline_run(
        self,
        workspace_name: str,
        pipeline_name: str,
        run_id: str,
        filter_parameters: "models.RunFilterParameters",
        **kwargs
    ) -> "models.ActivityRunsQueryResponse":
        """Query activity runs based on input filter conditions.

        :param workspace_name: The name of the workspace to execute operations on.
        :type workspace_name: str
        :param pipeline_name: The pipeline name.
        :type pipeline_name: str
        :param run_id: The pipeline run identifier.
        :type run_id: str
        :param filter_parameters: Parameters to filter the activity runs.
        :type filter_parameters: ~azure.synapse.models.RunFilterParameters
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ActivityRunsQueryResponse or the result of cls(response)
        :rtype: ~azure.synapse.models.ActivityRunsQueryResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ActivityRunsQueryResponse"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2019-11-01-preview"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.query_by_pipeline_run.metadata['url']
        path_format_arguments = {
            'SynapseDnsSuffix': self._serialize.url("self._config.synapse_dns_suffix", self._config.synapse_dns_suffix, 'str', skip_quote=True),
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str', skip_quote=True),
            'pipelineName': self._serialize.url("pipeline_name", pipeline_name, 'str', max_length=260, min_length=1, pattern=r'^[A-Za-z0-9_][^<>*#.%&:\\+?/]*$'),
            'runId': self._serialize.url("run_id", run_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(filter_parameters, 'RunFilterParameters')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.CloudError, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('ActivityRunsQueryResponse', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    query_by_pipeline_run.metadata = {'url': '/pipelines/{pipelineName}/pipelineruns/{runId}/queryActivityruns'}
