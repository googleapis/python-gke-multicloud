# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
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
#
import warnings
from typing import Callable, Dict, Optional, Sequence, Tuple, Union

from google.api_core import grpc_helpers
from google.api_core import operations_v1
from google.api_core import gapic_v1
import google.auth  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore

import grpc  # type: ignore

from google.cloud.gke_multicloud_v1.types import azure_resources
from google.cloud.gke_multicloud_v1.types import azure_service
from google.longrunning import operations_pb2  # type: ignore
from .base import AzureClustersTransport, DEFAULT_CLIENT_INFO


class AzureClustersGrpcTransport(AzureClustersTransport):
    """gRPC backend transport for AzureClusters.

    The AzureClusters API provides a single centrally managed
    service to create and manage Anthos clusters that run on Azure
    infrastructure.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """

    _stubs: Dict[str, Callable]

    def __init__(
        self,
        *,
        host: str = "gkemulticloud.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        channel: Optional[grpc.Channel] = None,
        api_mtls_endpoint: Optional[str] = None,
        client_cert_source: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        ssl_channel_credentials: Optional[grpc.ChannelCredentials] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is ignored if ``channel`` is provided.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if ``channel`` is provided.
            channel (Optional[grpc.Channel]): A ``Channel`` instance through
                which to make calls.
            api_mtls_endpoint (Optional[str]): Deprecated. The mutual TLS endpoint.
                If provided, it overrides the ``host`` argument and tries to create
                a mutual TLS channel with client SSL credentials from
                ``client_cert_source`` or application default SSL credentials.
            client_cert_source (Optional[Callable[[], Tuple[bytes, bytes]]]):
                Deprecated. A callback to provide client SSL certificate bytes and
                private key bytes, both in PEM format. It is ignored if
                ``api_mtls_endpoint`` is None.
            ssl_channel_credentials (grpc.ChannelCredentials): SSL credentials
                for the grpc channel. It is ignored if ``channel`` is provided.
            client_cert_source_for_mtls (Optional[Callable[[], Tuple[bytes, bytes]]]):
                A callback to provide client certificate bytes and private key bytes,
                both in PEM format. It is used to configure a mutual TLS channel. It is
                ignored if ``channel`` or ``ssl_channel_credentials`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.

        Raises:
          google.auth.exceptions.MutualTLSChannelError: If mutual TLS transport
              creation failed for any reason.
          google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        self._grpc_channel = None
        self._ssl_channel_credentials = ssl_channel_credentials
        self._stubs: Dict[str, Callable] = {}
        self._operations_client: Optional[operations_v1.OperationsClient] = None

        if api_mtls_endpoint:
            warnings.warn("api_mtls_endpoint is deprecated", DeprecationWarning)
        if client_cert_source:
            warnings.warn("client_cert_source is deprecated", DeprecationWarning)

        if channel:
            # Ignore credentials if a channel was passed.
            credentials = False
            # If a channel was explicitly provided, set it.
            self._grpc_channel = channel
            self._ssl_channel_credentials = None

        else:
            if api_mtls_endpoint:
                host = api_mtls_endpoint

                # Create SSL credentials with client_cert_source or application
                # default SSL credentials.
                if client_cert_source:
                    cert, key = client_cert_source()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )
                else:
                    self._ssl_channel_credentials = SslCredentials().ssl_credentials

            else:
                if client_cert_source_for_mtls and not ssl_channel_credentials:
                    cert, key = client_cert_source_for_mtls()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )

        # The base transport sets the host, credentials and scopes
        super().__init__(
            host=host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes,
            quota_project_id=quota_project_id,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
            api_audience=api_audience,
        )

        if not self._grpc_channel:
            self._grpc_channel = type(self).create_channel(
                self._host,
                # use the credentials which are saved
                credentials=self._credentials,
                # Set ``credentials_file`` to ``None`` here as
                # the credentials that we saved earlier should be used.
                credentials_file=None,
                scopes=self._scopes,
                ssl_credentials=self._ssl_channel_credentials,
                quota_project_id=quota_project_id,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )

        # Wrap messages. This must be done after self._grpc_channel exists
        self._prep_wrapped_messages(client_info)

    @classmethod
    def create_channel(
        cls,
        host: str = "gkemulticloud.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        **kwargs,
    ) -> grpc.Channel:
        """Create and return a gRPC channel object.
        Args:
            host (Optional[str]): The host for the channel to use.
            credentials (Optional[~.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            kwargs (Optional[dict]): Keyword arguments, which are passed to the
                channel creation.
        Returns:
            grpc.Channel: A gRPC channel object.

        Raises:
            google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """

        return grpc_helpers.create_channel(
            host,
            credentials=credentials,
            credentials_file=credentials_file,
            quota_project_id=quota_project_id,
            default_scopes=cls.AUTH_SCOPES,
            scopes=scopes,
            default_host=cls.DEFAULT_HOST,
            **kwargs,
        )

    @property
    def grpc_channel(self) -> grpc.Channel:
        """Return the channel designed to connect to this service."""
        return self._grpc_channel

    @property
    def operations_client(self) -> operations_v1.OperationsClient:
        """Create the client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        # Quick check: Only create a new client if we do not already have one.
        if self._operations_client is None:
            self._operations_client = operations_v1.OperationsClient(self.grpc_channel)

        # Return the client from cache.
        return self._operations_client

    @property
    def create_azure_client(
        self,
    ) -> Callable[[azure_service.CreateAzureClientRequest], operations_pb2.Operation]:
        r"""Return a callable for the create azure client method over gRPC.

        Creates a new
        [AzureClient][google.cloud.gkemulticloud.v1.AzureClient]
        resource on a given Google Cloud project and region.

        ``AzureClient`` resources hold client authentication information
        needed by the Anthos Multicloud API to manage Azure resources on
        your Azure subscription on your behalf.

        If successful, the response contains a newly created
        [Operation][google.longrunning.Operation] resource that can be
        described to track the status of the operation.

        Returns:
            Callable[[~.CreateAzureClientRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_azure_client" not in self._stubs:
            self._stubs["create_azure_client"] = self.grpc_channel.unary_unary(
                "/google.cloud.gkemulticloud.v1.AzureClusters/CreateAzureClient",
                request_serializer=azure_service.CreateAzureClientRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_azure_client"]

    @property
    def get_azure_client(
        self,
    ) -> Callable[[azure_service.GetAzureClientRequest], azure_resources.AzureClient]:
        r"""Return a callable for the get azure client method over gRPC.

        Describes a specific
        [AzureClient][google.cloud.gkemulticloud.v1.AzureClient]
        resource.

        Returns:
            Callable[[~.GetAzureClientRequest],
                    ~.AzureClient]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_azure_client" not in self._stubs:
            self._stubs["get_azure_client"] = self.grpc_channel.unary_unary(
                "/google.cloud.gkemulticloud.v1.AzureClusters/GetAzureClient",
                request_serializer=azure_service.GetAzureClientRequest.serialize,
                response_deserializer=azure_resources.AzureClient.deserialize,
            )
        return self._stubs["get_azure_client"]

    @property
    def list_azure_clients(
        self,
    ) -> Callable[
        [azure_service.ListAzureClientsRequest], azure_service.ListAzureClientsResponse
    ]:
        r"""Return a callable for the list azure clients method over gRPC.

        Lists all
        [AzureClient][google.cloud.gkemulticloud.v1.AzureClient]
        resources on a given Google Cloud project and region.

        Returns:
            Callable[[~.ListAzureClientsRequest],
                    ~.ListAzureClientsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_azure_clients" not in self._stubs:
            self._stubs["list_azure_clients"] = self.grpc_channel.unary_unary(
                "/google.cloud.gkemulticloud.v1.AzureClusters/ListAzureClients",
                request_serializer=azure_service.ListAzureClientsRequest.serialize,
                response_deserializer=azure_service.ListAzureClientsResponse.deserialize,
            )
        return self._stubs["list_azure_clients"]

    @property
    def delete_azure_client(
        self,
    ) -> Callable[[azure_service.DeleteAzureClientRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete azure client method over gRPC.

        Deletes a specific
        [AzureClient][google.cloud.gkemulticloud.v1.AzureClient]
        resource.

        If the client is used by one or more clusters, deletion will
        fail and a ``FAILED_PRECONDITION`` error will be returned.

        If successful, the response contains a newly created
        [Operation][google.longrunning.Operation] resource that can be
        described to track the status of the operation.

        Returns:
            Callable[[~.DeleteAzureClientRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_azure_client" not in self._stubs:
            self._stubs["delete_azure_client"] = self.grpc_channel.unary_unary(
                "/google.cloud.gkemulticloud.v1.AzureClusters/DeleteAzureClient",
                request_serializer=azure_service.DeleteAzureClientRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_azure_client"]

    @property
    def create_azure_cluster(
        self,
    ) -> Callable[[azure_service.CreateAzureClusterRequest], operations_pb2.Operation]:
        r"""Return a callable for the create azure cluster method over gRPC.

        Creates a new
        [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster]
        resource on a given GCP project and region.

        If successful, the response contains a newly created
        [Operation][google.longrunning.Operation] resource that can be
        described to track the status of the operation.

        Returns:
            Callable[[~.CreateAzureClusterRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_azure_cluster" not in self._stubs:
            self._stubs["create_azure_cluster"] = self.grpc_channel.unary_unary(
                "/google.cloud.gkemulticloud.v1.AzureClusters/CreateAzureCluster",
                request_serializer=azure_service.CreateAzureClusterRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_azure_cluster"]

    @property
    def update_azure_cluster(
        self,
    ) -> Callable[[azure_service.UpdateAzureClusterRequest], operations_pb2.Operation]:
        r"""Return a callable for the update azure cluster method over gRPC.

        Updates an
        [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster].

        Returns:
            Callable[[~.UpdateAzureClusterRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_azure_cluster" not in self._stubs:
            self._stubs["update_azure_cluster"] = self.grpc_channel.unary_unary(
                "/google.cloud.gkemulticloud.v1.AzureClusters/UpdateAzureCluster",
                request_serializer=azure_service.UpdateAzureClusterRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_azure_cluster"]

    @property
    def get_azure_cluster(
        self,
    ) -> Callable[[azure_service.GetAzureClusterRequest], azure_resources.AzureCluster]:
        r"""Return a callable for the get azure cluster method over gRPC.

        Describes a specific
        [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster]
        resource.

        Returns:
            Callable[[~.GetAzureClusterRequest],
                    ~.AzureCluster]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_azure_cluster" not in self._stubs:
            self._stubs["get_azure_cluster"] = self.grpc_channel.unary_unary(
                "/google.cloud.gkemulticloud.v1.AzureClusters/GetAzureCluster",
                request_serializer=azure_service.GetAzureClusterRequest.serialize,
                response_deserializer=azure_resources.AzureCluster.deserialize,
            )
        return self._stubs["get_azure_cluster"]

    @property
    def list_azure_clusters(
        self,
    ) -> Callable[
        [azure_service.ListAzureClustersRequest],
        azure_service.ListAzureClustersResponse,
    ]:
        r"""Return a callable for the list azure clusters method over gRPC.

        Lists all
        [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster]
        resources on a given Google Cloud project and region.

        Returns:
            Callable[[~.ListAzureClustersRequest],
                    ~.ListAzureClustersResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_azure_clusters" not in self._stubs:
            self._stubs["list_azure_clusters"] = self.grpc_channel.unary_unary(
                "/google.cloud.gkemulticloud.v1.AzureClusters/ListAzureClusters",
                request_serializer=azure_service.ListAzureClustersRequest.serialize,
                response_deserializer=azure_service.ListAzureClustersResponse.deserialize,
            )
        return self._stubs["list_azure_clusters"]

    @property
    def delete_azure_cluster(
        self,
    ) -> Callable[[azure_service.DeleteAzureClusterRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete azure cluster method over gRPC.

        Deletes a specific
        [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster]
        resource.

        Fails if the cluster has one or more associated
        [AzureNodePool][google.cloud.gkemulticloud.v1.AzureNodePool]
        resources.

        If successful, the response contains a newly created
        [Operation][google.longrunning.Operation] resource that can be
        described to track the status of the operation.

        Returns:
            Callable[[~.DeleteAzureClusterRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_azure_cluster" not in self._stubs:
            self._stubs["delete_azure_cluster"] = self.grpc_channel.unary_unary(
                "/google.cloud.gkemulticloud.v1.AzureClusters/DeleteAzureCluster",
                request_serializer=azure_service.DeleteAzureClusterRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_azure_cluster"]

    @property
    def generate_azure_access_token(
        self,
    ) -> Callable[
        [azure_service.GenerateAzureAccessTokenRequest],
        azure_service.GenerateAzureAccessTokenResponse,
    ]:
        r"""Return a callable for the generate azure access token method over gRPC.

        Generates a short-lived access token to authenticate to a given
        [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster]
        resource.

        Returns:
            Callable[[~.GenerateAzureAccessTokenRequest],
                    ~.GenerateAzureAccessTokenResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "generate_azure_access_token" not in self._stubs:
            self._stubs["generate_azure_access_token"] = self.grpc_channel.unary_unary(
                "/google.cloud.gkemulticloud.v1.AzureClusters/GenerateAzureAccessToken",
                request_serializer=azure_service.GenerateAzureAccessTokenRequest.serialize,
                response_deserializer=azure_service.GenerateAzureAccessTokenResponse.deserialize,
            )
        return self._stubs["generate_azure_access_token"]

    @property
    def create_azure_node_pool(
        self,
    ) -> Callable[[azure_service.CreateAzureNodePoolRequest], operations_pb2.Operation]:
        r"""Return a callable for the create azure node pool method over gRPC.

        Creates a new
        [AzureNodePool][google.cloud.gkemulticloud.v1.AzureNodePool],
        attached to a given
        [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster].

        If successful, the response contains a newly created
        [Operation][google.longrunning.Operation] resource that can be
        described to track the status of the operation.

        Returns:
            Callable[[~.CreateAzureNodePoolRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_azure_node_pool" not in self._stubs:
            self._stubs["create_azure_node_pool"] = self.grpc_channel.unary_unary(
                "/google.cloud.gkemulticloud.v1.AzureClusters/CreateAzureNodePool",
                request_serializer=azure_service.CreateAzureNodePoolRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_azure_node_pool"]

    @property
    def update_azure_node_pool(
        self,
    ) -> Callable[[azure_service.UpdateAzureNodePoolRequest], operations_pb2.Operation]:
        r"""Return a callable for the update azure node pool method over gRPC.

        Updates an
        [AzureNodePool][google.cloud.gkemulticloud.v1.AzureNodePool].

        Returns:
            Callable[[~.UpdateAzureNodePoolRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_azure_node_pool" not in self._stubs:
            self._stubs["update_azure_node_pool"] = self.grpc_channel.unary_unary(
                "/google.cloud.gkemulticloud.v1.AzureClusters/UpdateAzureNodePool",
                request_serializer=azure_service.UpdateAzureNodePoolRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_azure_node_pool"]

    @property
    def get_azure_node_pool(
        self,
    ) -> Callable[
        [azure_service.GetAzureNodePoolRequest], azure_resources.AzureNodePool
    ]:
        r"""Return a callable for the get azure node pool method over gRPC.

        Describes a specific
        [AzureNodePool][google.cloud.gkemulticloud.v1.AzureNodePool]
        resource.

        Returns:
            Callable[[~.GetAzureNodePoolRequest],
                    ~.AzureNodePool]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_azure_node_pool" not in self._stubs:
            self._stubs["get_azure_node_pool"] = self.grpc_channel.unary_unary(
                "/google.cloud.gkemulticloud.v1.AzureClusters/GetAzureNodePool",
                request_serializer=azure_service.GetAzureNodePoolRequest.serialize,
                response_deserializer=azure_resources.AzureNodePool.deserialize,
            )
        return self._stubs["get_azure_node_pool"]

    @property
    def list_azure_node_pools(
        self,
    ) -> Callable[
        [azure_service.ListAzureNodePoolsRequest],
        azure_service.ListAzureNodePoolsResponse,
    ]:
        r"""Return a callable for the list azure node pools method over gRPC.

        Lists all
        [AzureNodePool][google.cloud.gkemulticloud.v1.AzureNodePool]
        resources on a given
        [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster].

        Returns:
            Callable[[~.ListAzureNodePoolsRequest],
                    ~.ListAzureNodePoolsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_azure_node_pools" not in self._stubs:
            self._stubs["list_azure_node_pools"] = self.grpc_channel.unary_unary(
                "/google.cloud.gkemulticloud.v1.AzureClusters/ListAzureNodePools",
                request_serializer=azure_service.ListAzureNodePoolsRequest.serialize,
                response_deserializer=azure_service.ListAzureNodePoolsResponse.deserialize,
            )
        return self._stubs["list_azure_node_pools"]

    @property
    def delete_azure_node_pool(
        self,
    ) -> Callable[[azure_service.DeleteAzureNodePoolRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete azure node pool method over gRPC.

        Deletes a specific
        [AzureNodePool][google.cloud.gkemulticloud.v1.AzureNodePool]
        resource.

        If successful, the response contains a newly created
        [Operation][google.longrunning.Operation] resource that can be
        described to track the status of the operation.

        Returns:
            Callable[[~.DeleteAzureNodePoolRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_azure_node_pool" not in self._stubs:
            self._stubs["delete_azure_node_pool"] = self.grpc_channel.unary_unary(
                "/google.cloud.gkemulticloud.v1.AzureClusters/DeleteAzureNodePool",
                request_serializer=azure_service.DeleteAzureNodePoolRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_azure_node_pool"]

    @property
    def get_azure_server_config(
        self,
    ) -> Callable[
        [azure_service.GetAzureServerConfigRequest], azure_resources.AzureServerConfig
    ]:
        r"""Return a callable for the get azure server config method over gRPC.

        Returns information, such as supported Azure regions
        and Kubernetes versions, on a given Google Cloud
        location.

        Returns:
            Callable[[~.GetAzureServerConfigRequest],
                    ~.AzureServerConfig]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_azure_server_config" not in self._stubs:
            self._stubs["get_azure_server_config"] = self.grpc_channel.unary_unary(
                "/google.cloud.gkemulticloud.v1.AzureClusters/GetAzureServerConfig",
                request_serializer=azure_service.GetAzureServerConfigRequest.serialize,
                response_deserializer=azure_resources.AzureServerConfig.deserialize,
            )
        return self._stubs["get_azure_server_config"]

    def close(self):
        self.grpc_channel.close()

    @property
    def kind(self) -> str:
        return "grpc"


__all__ = ("AzureClustersGrpcTransport",)
