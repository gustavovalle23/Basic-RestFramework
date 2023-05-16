import newrelic.agent
import newrelic.console


class TenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        tenant = "646186b8e9cd687e613c9014"
        newrelic.agent.add_custom_attribute("tenant", tenant)

        response = self.get_response(request)
        return response
