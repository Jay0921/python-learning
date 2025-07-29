class LoggingMixin:
    @classmethod
    def info(cls):
        print(f"[LoggingMixin]: info")

    def log(self):
        print(f"[LoggingMixin]: log")

    def debug(self):
        print(f"[LoggingMixin]: debug")

class DebugMixin:
    def debug(self):
        print(f"[DebugMixin]: debug")

    def error(self):
        print(f"[DebugMixin]: error")

class Service(LoggingMixin, DebugMixin):
    def __init__(self):
        pass


service = Service()
Service.info()
# [LoggingMixin]: info
service.log()
# [LoggingMixin]: log
service.debug()
# [LoggingMixin]: debug
service.error()
# [DebugMixin]: error

print(Service.mro())
# (<class '__main__.Service'>, <class '__main__.LoggingMixin'>, <class '__main__.DebugMixin'>, <class 'object'>)
