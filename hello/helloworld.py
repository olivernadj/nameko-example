from nameko.rpc import rpc


class GreetingService:
    name = "greeting_service"

    @rpc
    def hello(self, name):
        return "Hello, {}!".format(name)

    @rpc
    def version(self):
        return "0.0.2"
