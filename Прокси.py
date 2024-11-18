class Subject:
    def request(self):
        raise NotImplementedError("This method should be overridden.")

class RealSubject(Subject):
    def request(self):
        print("RealSubject: Handling the request.")

class Proxy(Subject):
    def __init__(self, real_subject: RealSubject):
        self._real_subject = real_subject

    def request(self):
        print("Proxy: Performing some checks before forwarding the request.")
        # Here you can add additional logic, e.g., authentication, logging, etc.
        self._real_subject.request()

# Пример использования
if __name__ == "__main__":
    real_subject = RealSubject()
    proxy = Proxy(real_subject)
    proxy.request()
