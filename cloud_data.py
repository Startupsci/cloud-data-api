"""Cloud Data API using Python and Google Cloud Endpoints."""
import endpoints
from protorpc import message_types
from protorpc import remote

from models import AboutMessage

@endpoints.api(name='cloudData', version='v1')
class CloudDataApi(remote.Service):
    """Cloud Data API v1."""

    @endpoints.method(message_types.VoidMessage, AboutMessage,
                      path = "about", http_method='GET', name = "about")
    def about(self, request):
      return AboutMessage(about="Cloud Data API v1")

api = endpoints.api_server([CloudDataApi])
