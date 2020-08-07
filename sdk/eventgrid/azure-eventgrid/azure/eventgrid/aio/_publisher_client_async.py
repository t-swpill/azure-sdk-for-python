# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any

from azure.core import AsyncPipelineClient
from msrest import Deserializer, Serializer

from .._models import CloudEvent, EventGridEvent
from .._helpers import _get_topic_hostname_only_fqdn, _get_authentication_policy
from azure.core.pipeline.policies import AzureKeyCredentialPolicy
from azure.core.credentials import AzureKeyCredential
from .._generated.aio import EventGridPublisherClient as EventGridPublisherClientAsync
from .. import _constants as constants


class EventGridPublisherClient(object):
    """Asynchronous EventGrid Python Publisher Client.

    :param str topic_hostname: The topic endpoint to send the events to.
    :param credential: The credential object used for authentication which implements SAS key authentication or SAS token authentication.
    :type credential: Union[~azure.core.credentials.AzureKeyCredential, azure.eventgrid.EventGridSharedAccessSignatureCredential]
    """

    def __init__(self, topic_hostname, credential, **kwargs):
        # type: (str, Union[AzureKeyCredential, EventGridSharedAccessSignatureCredential], Any) -> None
        auth_policy = _get_authentication_policy(credential)
        self._client = EventGridPublisherClientAsync(authentication_policy=auth_policy)
        self._topic_hostname = topic_hostname


    async def send(self, events, **kwargs):
        # type: (Union[List[CloudEvent], List[EventGridEvent], List[CustomEvent]], Any) -> None
        """Sends event data to topic hostname specified during client initialization.

        :param  events: A list of CloudEvent/EventGridEvent/CustomEvent to be sent.
        :type events: Union[List[models.CloudEvent], List[models.EventGridEvent], List[models.CustomEvent]]
        :rtype: None
         """

        if all(isinstance(e, CloudEvent) for e in events):
            await self._client.publish_cloud_event_events(self._topic_hostname, events, **kwargs)
        elif all(isinstance(e, EventGridEvent) for e in events):
            await self._client.publish_events(self._topic_hostname, events, **kwargs)
        elif all(isinstance(e, CustomEvent) for e in events):
            serialized_events = [dict(e) for e in events]
            await self._client.publish_custom_event_events(self._topic_hostname, serialized_events, **kwargs)
        else:
            raise Exception("Event schema is not correct. Please send as list of all CloudEvents, list of all EventGridEvents, or list of all CustomEvents.")
    