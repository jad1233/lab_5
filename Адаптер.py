class Target:
    def request(self):
        return "Target: Default behavior."

class Adaptee:
    def specific_request(self):
        return "Adaptee: Specific behavior (incompatible)."

class Adapter(Target):
    def __init__(self, adaptee: Adaptee):
        self._adaptee = adaptee

    def request(self):
        return f"Adapter: Adapted behavior -> {self._adaptee.specific_request()}"

# Пример использования
if __name__ == "__main__":
    adaptee = Adaptee()
    print("Adaptee:", adaptee.specific_request())

    adapter = Adapter(adaptee)
    print("Adapter:", adapter.request())
