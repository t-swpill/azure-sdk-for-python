# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import msrest.serialization


class CloudEvent(msrest.serialization.Model):
    """Properties of an event published to an Event Grid topic using the CloudEvent 1.0 Schema.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. An identifier for the event. The combination of id and source must be
     unique for each distinct event.
    :type id: str
    :param source: Required. Identifies the context in which an event happened. The combination of
     id and source must be unique for each distinct event.
    :type source: str
    :param data: Event data specific to the event type.
    :type data: object
    :param type: Required. Type of event related to the originating occurrence.
    :type type: str
    :param time: The time (in UTC) the event was generated, in RFC3339 format.
    :type time: ~datetime.datetime
    :param specversion: Required. The version of the CloudEvents specification which the event
     uses.
    :type specversion: str
    :param dataschema: Identifies the schema that data adheres to.
    :type dataschema: str
    :param datacontenttype: Content type of data value.
    :type datacontenttype: str
    :param subject: This describes the subject of the event in the context of the event producer
     (identified by source).
    :type subject: str
    """

    _validation = {
        'id': {'required': True},
        'source': {'required': True},
        'type': {'required': True},
        'specversion': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'source': {'key': 'source', 'type': 'str'},
        'data': {'key': 'data', 'type': 'object'},
        'type': {'key': 'type', 'type': 'str'},
        'time': {'key': 'time', 'type': 'iso-8601'},
        'specversion': {'key': 'specversion', 'type': 'str'},
        'dataschema': {'key': 'dataschema', 'type': 'str'},
        'datacontenttype': {'key': 'datacontenttype', 'type': 'str'},
        'subject': {'key': 'subject', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(CloudEvent, self).__init__(**kwargs)
        self.id = kwargs['id']
        self.source = kwargs['source']
        self.data = kwargs.get('data', None)
        self.type = kwargs['type']
        self.time = kwargs.get('time', None)
        self.specversion = kwargs['specversion']
        self.dataschema = kwargs.get('dataschema', None)
        self.datacontenttype = kwargs.get('datacontenttype', None)
        self.subject = kwargs.get('subject', None)

    @classmethod
    def from_dict(self, source):
        """
        Returns an array of CloudEvent objects given a dict of events following the CloudEvent schema.

        :param source: Required. The dict object following the CloudEvent schema.
        :type source: dict

        :rtype: List[~azure.eventgrid.CloudEvent]
        """
        pass


class EventGridEvent(msrest.serialization.Model):
    """Properties of an event published to an Event Grid topic using the EventGrid Schema.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. An unique identifier for the event.
    :type id: str
    :param topic: The resource path of the event source.
    :type topic: str
    :param subject: Required. A resource path relative to the topic path.
    :type subject: str
    :param data: Required. Event data specific to the event type.
    :type data: object
    :param event_type: Required. The type of the event that occurred.
    :type event_type: str
    :param event_time: Required. The time (in UTC) the event was generated.
    :type event_time: ~datetime.datetime
    :ivar metadata_version: The schema version of the event metadata.
    :vartype metadata_version: str
    :param data_version: Required. The schema version of the data object.
    :type data_version: str
    """

    _validation = {
        'id': {'required': True},
        'subject': {'required': True},
        'data': {'required': True},
        'event_type': {'required': True},
        'event_time': {'required': True},
        'metadata_version': {'readonly': True},
        'data_version': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'topic': {'key': 'topic', 'type': 'str'},
        'subject': {'key': 'subject', 'type': 'str'},
        'data': {'key': 'data', 'type': 'object'},
        'event_type': {'key': 'eventType', 'type': 'str'},
        'event_time': {'key': 'eventTime', 'type': 'iso-8601'},
        'metadata_version': {'key': 'metadataVersion', 'type': 'str'},
        'data_version': {'key': 'dataVersion', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(EventGridEvent, self).__init__(**kwargs)
        self.id = kwargs['id']
        self.topic = kwargs.get('topic', None)
        self.subject = kwargs['subject']
        self.data = kwargs['data']
        self.event_type = kwargs['event_type']
        self.event_time = kwargs['event_time']
        self.metadata_version = None
        self.data_version = kwargs['data_version']

    @classmethod
    def from_dict(self, source):
        """
        Returns an array of EventGridEvent objects given a dict of events following the EventGridEvent schema.

        :param source: Required. The dict object following the EventGridEvent schema.
        :type source: dict

        :rtype: List[~azure.eventgrid.EventGridEvent]
        """
        pass

class SubscriptionDeletedEventData(msrest.serialization.Model):
    """Schema of the Data property of an EventGridEvent for a Microsoft.EventGrid.SubscriptionDeletedEvent.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar event_subscription_id: The Azure resource ID of the deleted event subscription.
    :vartype event_subscription_id: str
    """

    _validation = {
        'event_subscription_id': {'readonly': True},
    }

    _attribute_map = {
        'event_subscription_id': {'key': 'eventSubscriptionId', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(SubscriptionDeletedEventData, self).__init__(**kwargs)
        self.event_subscription_id = None


class SubscriptionValidationEventData(msrest.serialization.Model):
    """Schema of the Data property of an EventGridEvent for a Microsoft.EventGrid.SubscriptionValidationEvent.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar validation_code: The validation code sent by Azure Event Grid to validate an event
     subscription. To complete the validation handshake, the subscriber must either respond with
     this validation code as part of the validation response, or perform a GET request on the
     validationUrl (available starting version 2018-05-01-preview).
    :vartype validation_code: str
    :ivar validation_url: The validation URL sent by Azure Event Grid (available starting version
     2018-05-01-preview). To complete the validation handshake, the subscriber must either respond
     with the validationCode as part of the validation response, or perform a GET request on the
     validationUrl (available starting version 2018-05-01-preview).
    :vartype validation_url: str
    """

    _validation = {
        'validation_code': {'readonly': True},
        'validation_url': {'readonly': True},
    }

    _attribute_map = {
        'validation_code': {'key': 'validationCode', 'type': 'str'},
        'validation_url': {'key': 'validationUrl', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(SubscriptionValidationEventData, self).__init__(**kwargs)
        self.validation_code = None
        self.validation_url = None


class SubscriptionValidationResponse(msrest.serialization.Model):
    """To complete an event subscription validation handshake, a subscriber can use either the validationCode or the validationUrl received in a SubscriptionValidationEvent. When the validationCode is used, the SubscriptionValidationResponse can be used to build the response.

    :param validation_response: The validation response sent by the subscriber to Azure Event Grid
     to complete the validation of an event subscription.
    :type validation_response: str
    """

    _attribute_map = {
        'validation_response': {'key': 'validationResponse', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(SubscriptionValidationResponse, self).__init__(**kwargs)
        self.validation_response = kwargs.get('validation_response', None)

class EventBatch(object):
    """A batch of events.

    Sending events in a batch is more performant than sending individual events.
    EventBatch helps you create the maximum allowed size batch of either `EventGridEvent` or `CloudEvent` to improve sending performance.

    Use the `add` method to add events until the maximum batch size limit in bytes has been reached -
    at which point a `ValueError` will be raised.
    Use the `publish_events` method of :class:`EventGridPublisherClient<azure.eventgrid.EventGridPublisherClient>`
    for sending.

    **Please use the create_batch method of EventGridPublisherClient
    to create an EventBatch object instead of instantiating an EventBatch object directly.**

    :param int max_size_in_bytes: The maximum size of bytes data that an EventDataBatch object can hold.
    """

    def __init__(self, max_size_in_bytes=None):
        # type: (Optional[int], Optional[str], Optional[Union[str, bytes]]) -> None
        return
        self.max_size_in_bytes = max_size_in_bytes #or constants.MAX_MESSAGE_LENGTH_BYTES
        self.schema = None
        self.event_list = []#BatchMessage(data=[], multi_messages=False, properties=None)

        self._size = 0#self.message.gather()[0].get_message_encoded_size()
        self._count = 0

    def __repr__(self):
        # type: () -> str
        batch_repr = "max_size_in_bytes={}, event_count={}".format(
            self.max_size_in_bytes, self._count
        )
        return "EventBatch({})".format(batch_repr)

    def __len__(self):
        return self._count

    def _load_events(self, events):
        for event_data in events:
            try:
                self.add(event_data)
            except ValueError:
                raise ValueError("The combined size of EventData collection exceeds the Event Hub frame size limit. "
                                 "Please send a smaller collection of EventData, or use EventDataBatch, "
                                 "which is guaranteed to be under the frame size limit")

    @property
    def size_in_bytes(self):
        # type: () -> int
        """The combined size of the events in the batch, in bytes.

        :rtype: int
        """
        return self._size

    def add(self, event):
        # type: (EventGridEvent, CloudEvent) -> None
        """Try to add an EventGridEvent/CloudEvent to the batch.

        The total size of an added event is the sum of its body, properties, etc.
        If this added size results in the batch exceeding the maximum batch size, a `ValueError` will
        be raised.

        :param event: The EventData to add to the batch.
        :type event: ~azure.eventgrid.EventGridEvent or ~azure.eventgrid.EventGridEvent 
        :rtype: None
        :raise: :class:`ValueError`, when exceeding the size limit.
        """
        pass
        #if self._partition_key:
        #    if (
        #        event_data.partition_key
        #        and event_data.partition_key != self._partition_key
        #    ):
        #        raise ValueError(
        #            "The partition key of event_data does not match the partition key of this batch."
        #        )
        #    if not event_data.partition_key:
        #        set_message_partition_key(event_data.message, self._partition_key)

        #trace_message(event_data)
        #event_data_size = event_data.message.get_message_encoded_size()

        ## For a BatchMessage, if the encoded_message_size of event_data is < 256, then the overhead cost to encode that
        ## message into the BatchMessage would be 5 bytes, if >= 256, it would be 8 bytes.
        #size_after_add = (
        #    self._size
        #    + event_data_size
        #    + _BATCH_MESSAGE_OVERHEAD_COST[0 if (event_data_size < 256) else 1]
        #)

        #if size_after_add > self.max_size_in_bytes:
        #    raise ValueError(
        #        "EventDataBatch has reached its size limit: {}".format(
        #            self.max_size_in_bytes
        #        )
        #    )

        #self.message._body_gen.append(event_data)  # pylint: disable=protected-access
        #self._size = size_after_add
        #self._count += 1
    
    @property
    def event_schema(self):
        """The event schema for all events in the batch.

        :rtype: str
        """
        return self.schema

class BaseEventType(object):
    """The base type for different event type objects.

    """
    # class variable
    #event_type_mappings = _initialize_mapping()

    def __init__(self, **kwargs):
        # type: (Optional[int], Optional[str], Optional[Union[str, bytes]]) -> None
        return
        self.event_type = None   # type: str
        self.event_data = None  # type: dict
        # list other envelope properties
    
    def create_event_type_object(self):
        """A specific event type object is returned based on the event type specified in the event.
        The BaseEventType.event_type_mappings dict will be used to initialize the event type object
        corresponding to `self.event_type`

        :rtype: List[Any]
        """

        pass
    
    def _populate(self):
        pass