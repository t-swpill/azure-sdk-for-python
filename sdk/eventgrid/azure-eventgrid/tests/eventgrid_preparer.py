import hashlib
from collections import namedtuple

from azure.mgmt.eventgrid import EventGridManagementClient
from azure.mgmt.eventgrid.models import Topic, DomainTopic, SystemTopic, PartnerTopic, Resource
#, WebHookEventSubscriptionDestination,
#    EventHubEventSubscriptionDestination,
#    StorageQueueEventSubscriptionDestination,
#    HybridConnectionEventSubscriptionDestination,
#    ServiceBusQueueEventSubscriptionDestination,
#    ServiceBusTopicEventSubscriptionDestination,
#    AzureFunctionEventSubscriptionDestination


from azure_devtools.scenario_tests.exceptions import AzureTestError

from devtools_testutils import (
    ResourceGroupPreparer, AzureMgmtPreparer, FakeResource
)

from devtools_testutils.resource_testcase import RESOURCE_GROUP_PARAM

#EVENTGRID_DEFAULT_AUTH_RULE_NAME = 'RootManageSharedAccessKey'
#EVENTGRID_NAMESPACE_PARAM = 'eventgrid_namespace'
EVENTGRID_TOPIC_PARAM = 'eventgrid_topic'
EVENTGRID_SUBSCRIPTION_PARAM = 'eventgrid_subscription'


class EventGridTopicPreparer(_EventGridChildResourcePreparer):
    def __init__(self,
                 name_prefix='',
                 parameter_name=EVENTGRID_TOPIC_PARAM,
                 parameter_location=TOPIC_LOCATION,
                 resource_group_parameter_name=RESOURCE_GROUP_PARAM,
                 disable_recording=True, playback_fake_resource=None,
                 client_kwargs=None):
        super(EventGridTopicPreparer, self).__init__(name_prefix,
                                                     resource_group_parameter_name=resource_group_parameter_name,
                                                     disable_recording=disable_recording,
                                                     playback_fake_resource=playback_fake_resource,
                                                     client_kwargs=client_kwargs)
        self.parameter_name = parameter_name
        self.parameter_location = parameter_location

    def create_resource(self, name, location, **kwargs):
        if self.is_live:
            self.client = self.create_mgmt_client(EventGridManagementClient)
            group = self._get_resource_group(**kwargs)
            topic = Topic(location=location)
            self.resource = self.client.topics.create_or_update(
                group.name,
                name,
                topic,
                {}
            )
        else:
            self.resource = FakeResource(name=name, id=name)
        return {
            self.parameter_name: self.resource,
        }

    def remove_resource(self, name, **kwargs):
        if self.is_live:
            group = self._get_resource_group(**kwargs)
            self.client.topics.delete(group.name, name, polling=False)



class EventGridSubscriptionPreparer(_EventGridChildResourcePreparer):
    def __init__(self,
                 name_prefix='',
                 parameter_name=SERVICEBUS_SUBSCRIPTION_PARAM,
                 resource_group_parameter_name=RESOURCE_GROUP_PARAM,
                 servicebus_namespace_parameter_name=SERVICEBUS_NAMESPACE_PARAM,
                 servicebus_topic_parameter_name=SERVICEBUS_TOPIC_PARAM,
                 disable_recording=True, playback_fake_resource=None,
                 client_kwargs=None):
        super(EventGridSubscriptionPreparer, self).__init__(name_prefix,
                                                     resource_group_parameter_name=resource_group_parameter_name,
                                                     servicebus_namespace_parameter_name=servicebus_namespace_parameter_name,
                                                     disable_recording=disable_recording,
                                                     playback_fake_resource=playback_fake_resource,
                                                     client_kwargs=client_kwargs)
        self.servicebus_topic_parameter_name = servicebus_topic_parameter_name
        self.parameter_name = parameter_name

    def create_resource(self, name, **kwargs):
        if self.is_live:
            self.client = self.create_mgmt_client(EventGridManagementClient)
            group = self._get_resource_group(**kwargs)
            namespace = self._get_namespace(**kwargs)
            topic = self._get_topic(**kwargs)
            self.resource = self.client.subscriptions.create_or_update(
                group.name,
                topic.name,
                name,
                {}
            )
        else:
            self.resource = FakeResource(name=name, id=name)
        return {
            self.parameter_name: self.resource,
        }

    def remove_resource(self, name, **kwargs):
        if self.is_live:
            group = self._get_resource_group(**kwargs)
            namespace = self._get_namespace(**kwargs)
            topic = self._get_topic(**kwargs)
            self.client.subscriptions.delete(group.name, namespace.name, topic.name, name, polling=False)

    def _get_topic(self, **kwargs):
        try:
            return kwargs.get(self.servicebus_topic_parameter_name)
        except KeyError:
            template = 'To create this service bus subscription a service bus topic is required. Please add ' \
                       'decorator @{} in front of this service bus preparer.'
            raise AzureTestError(template.format(EventGridTopicPreparer.__name__))



#class EventGridNamespaceAuthorizationRulePreparer(_EventGridChildResourcePreparer):
#    def __init__(self,
#                 name_prefix='',
#                 access_rights=[AccessRights.manage, AccessRights.send, AccessRights.listen],
#                 parameter_name=SERVICEBUS_AUTHORIZATION_RULE_PARAM,
#                 resource_group_parameter_name=RESOURCE_GROUP_PARAM,
#                 servicebus_namespace_parameter_name=SERVICEBUS_NAMESPACE_PARAM,
#                 disable_recording=True, playback_fake_resource=None,
#                 client_kwargs=None):
#        super(EventGridNamespaceAuthorizationRulePreparer, self).__init__(name_prefix,
#                                                     resource_group_parameter_name=resource_group_parameter_name,
#                                                     servicebus_namespace_parameter_name=servicebus_namespace_parameter_name,
#                                                     disable_recording=disable_recording,
#                                                     playback_fake_resource=playback_fake_resource,
#                                                     client_kwargs=client_kwargs)
#        self.parameter_name = parameter_name
#        self.access_rights = access_rights
#
#    def create_resource(self, name, **kwargs):
#        if self.is_live:
#            self.client = self.create_mgmt_client(EventGridManagementClient)
#            group = self._get_resource_group(**kwargs)
#            namespace = self._get_namespace(**kwargs)
#            self.resource = self.client.namespaces.create_or_update_authorization_rule(
#                group.name,
#                namespace.name,
#                name,
#                self.access_rights
#            )
#
#            key = self.client.namespaces.list_keys(group.name, namespace.name, name)
#            connection_string = key.primary_connection_string
#        else:
#            self.resource = FakeResource(name=name, id=name)
#            connection_string = 'https://microsoft.com'
#        return {
#            self.parameter_name: self.resource,
#            '{}_connection_string'.format(self.parameter_name): connection_string,
#        }
#
#    def remove_resource(self, name, **kwargs):
#        if self.is_live:
#            group = self._get_resource_group(**kwargs)
#            namespace = self._get_namespace(**kwargs)
#            self.client.namespaces.delete_authorization_rule(group.name, namespace.name, name, polling=False)
#
#
#class EventGridQueueAuthorizationRulePreparer(_EventGridChildResourcePreparer):
#    def __init__(self,
#                 name_prefix='',
#                 access_rights=[AccessRights.manage, AccessRights.send, AccessRights.listen],
#                 parameter_name=SERVICEBUS_QUEUE_AUTHORIZATION_RULE_PARAM,
#                 resource_group_parameter_name=RESOURCE_GROUP_PARAM,
#                 servicebus_namespace_parameter_name=SERVICEBUS_NAMESPACE_PARAM,
#                 servicebus_queue_parameter_name=SERVICEBUS_QUEUE_PARAM,
#                 disable_recording=True, playback_fake_resource=None,
#                 client_kwargs=None):
#        super(EventGridQueueAuthorizationRulePreparer, self).__init__(name_prefix,
#                                                     resource_group_parameter_name=resource_group_parameter_name,
#                                                     servicebus_namespace_parameter_name=servicebus_namespace_parameter_name,
#                                                     disable_recording=disable_recording,
#                                                     playback_fake_resource=playback_fake_resource,
#                                                     client_kwargs=client_kwargs)
#        self.parameter_name = parameter_name
#        self.access_rights = access_rights
#        self.servicebus_queue_parameter_name = servicebus_queue_parameter_name
#
#    def create_resource(self, name, **kwargs):
#        if self.is_live:
#            self.client = self.create_mgmt_client(EventGridManagementClient)
#            group = self._get_resource_group(**kwargs)
#            namespace = self._get_namespace(**kwargs)
#            queue = self._get_queue(**kwargs)
#            self.resource = self.client.queues.create_or_update_authorization_rule(
#                group.name,
#                namespace.name,
#                queue.name,
#                name,
#                self.access_rights
#            )
#
#            key = self.client.queues.list_keys(group.name, namespace.name, queue.name, name)
#            connection_string = key.primary_connection_string
#        else:
#            self.resource = FakeResource(name=name, id=name)
#            connection_string = 'https://microsoft.com'
#        return {
#            self.parameter_name: self.resource,
#            '{}_connection_string'.format(self.parameter_name): connection_string,
#        }
#
#    def remove_resource(self, name, **kwargs):
#        if self.is_live:
#            group = self._get_resource_group(**kwargs)
#            namespace = self._get_namespace(**kwargs)
#            queue = self._get_queue(**kwargs)
#            self.client.queues.delete_authorization_rule(group.name, namespace.name, queue.name, name, polling=False)
#
#    def _get_queue(self, **kwargs):
#        try:
#            return kwargs.get(self.servicebus_queue_parameter_name)
#        except KeyError:
#            template = 'To create this service bus queue authorization rule a service bus queue is required. Please add ' \
#                       'decorator @{} in front of this service bus preparer.'
#            raise AzureTestError(template.format(EventGridQueuePreparer.__name__))



# Service Bus Namespace Preparer and its shorthand decorator
#class EventGridNamespacePreparer(AzureMgmtPreparer):
#    def __init__(self,
#                 name_prefix='',
#                 sku='Standard', location='westus',
#                 parameter_name=SERVICEBUS_NAMESPACE_PARAM,
#                 resource_group_parameter_name=RESOURCE_GROUP_PARAM,
#                 disable_recording=True, playback_fake_resource=None,
#                 client_kwargs=None):
#        super(EventGridNamespacePreparer, self).__init__(name_prefix, 24,
#                                                          disable_recording=disable_recording,
#                                                          playback_fake_resource=playback_fake_resource,
#                                                          client_kwargs=client_kwargs)
#        self.location = location
#        self.sku = sku
#        self.resource_group_parameter_name = resource_group_parameter_name
#        self.parameter_name = parameter_name
#        self.connection_string = ''
#
#    def create_resource(self, name, **kwargs):
#        if self.is_live:
#            self.client = self.create_mgmt_client(EventGridManagementClient)
#            group = self._get_resource_group(**kwargs)
#            namespace_async_operation = self.client.namespaces.create_or_update(
#                group.name,
#                name,
#                {
#                    'sku': {'name': self.sku},
#                    'location': self.location,
#                }
#            )
#            self.resource = namespace_async_operation.result()
#
#            key = self.client.namespaces.list_keys(group.name, name, SERVICEBUS_DEFAULT_AUTH_RULE_NAME)
#            self.connection_string = key.primary_connection_string
#            self.key_name = key.key_name
#            self.primary_key = key.primary_key
#        else:
#            self.resource = FakeResource(name=name, id=name)
#            self.connection_string = 'Endpoint=sb://test-azure-sdk-test.servicebus.windows.net/;SharedAccessKeyName=test;SharedAccessKey=THISISATESTKEYXXXXXXXXXXXXXXXXXXXXXXXXXXXX='
#            self.key_name = SERVICEBUS_DEFAULT_AUTH_RULE_NAME
#            self.primary_key = 'ZmFrZV9hY29jdW50X2tleQ=='
#        return {
#            self.parameter_name: self.resource,
#            '{}_connection_string'.format(self.parameter_name): self.connection_string,
#            '{}_key_name'.format(self.parameter_name): self.key_name,
#            '{}_primary_key'.format(self.parameter_name): self.primary_key,
#        }
#
#    def remove_resource(self, name, **kwargs):
#        if self.is_live:
#            group = self._get_resource_group(**kwargs)
#            self.client.namespaces.delete(group.name, name, polling=False)
#
#    def _get_resource_group(self, **kwargs):
#        try:
#            return kwargs.get(self.resource_group_parameter_name)
#        except KeyError:
#            template = 'To create a service bus a resource group is required. Please add ' \
#                       'decorator @{} in front of this service bus preparer.'
#            raise AzureTestError(template.format(ResourceGroupPreparer.__name__))
#

# Shared base class for service bus sub-resources that require a namespace and RG to exist.
#class _EventGridChildResourcePreparer(AzureMgmtPreparer):
#    def __init__(self,
#                 name_prefix='',
#                 resource_group_parameter_name=RESOURCE_GROUP_PARAM,
#                 servicebus_namespace_parameter_name=SERVICEBUS_NAMESPACE_PARAM,
#                 disable_recording=True, playback_fake_resource=None,
#                 client_kwargs=None):
#        super(_EventGridChildResourcePreparer, self).__init__(name_prefix, 24,
#                                                               disable_recording=disable_recording,
#                                                               playback_fake_resource=playback_fake_resource,
#                                                               client_kwargs=client_kwargs)
#        self.resource_group_parameter_name = resource_group_parameter_name
#        self.servicebus_namespace_parameter_name = servicebus_namespace_parameter_name
#
#    def _get_resource_group(self, **kwargs):
#        try:
#            return kwargs.get(self.resource_group_parameter_name)
#        except KeyError:
#            template = 'To create this service bus child resource service bus a resource group is required. Please add ' \
#                       'decorator @{} in front of this service bus preparer.'
#            raise AzureTestError(template.format(ResourceGroupPreparer.__name__))
#
#    def _get_namespace(self, **kwargs):
#        try:
#            return kwargs.get(self.servicebus_namespace_parameter_name)
#        except KeyError:
#            template = 'To create this service bus child resource a service bus namespace is required. Please add ' \
#                       'decorator @{} in front of this service bus preparer.'
#            raise AzureTestError(template.format(EventGridNamespacePreparer.__name__))