import traceback
from django.shortcuts import HttpResponse
import logging
_logger = logging.getLogger("trololo")


def get_internal_server_id():
    import socket
    HOSTNAME = socket.gethostname()
    return socket.gethostbyname(HOSTNAME)


def health_check(request):
    from models import ClusterInfo
    #host_ip = request.META.get("HTTP_HOST")
    host_ip = get_internal_server_id()

    try:
        obj = ClusterInfo.objects.get(internal_ip=host_ip)
        if obj:
            flag = obj.enabled
            if flag:
                _logger.debug("Host '{}' IN CLUSTER".format(host_ip))
                return HttpResponse(status=200, content_type="text/html")
            else:
                _logger.info("Host '{}' NOT IN CLUSTER".format(host_ip))
                return HttpResponse(status=502, content_type="text/html")
        else:
            _logger.info("Cannot find host '{}' from DB - getting it as 'IN CLUSTER'".format(host_ip))
            return HttpResponse(status=200, content_type="text/html")
    except Exception, ex:
        _logger.info(u"Exception. Cannot define is '{}' in Cluster. Reason: {}; {}".format(host_ip, ex, traceback))
        return HttpResponse(status=200, content_type="text/html")
