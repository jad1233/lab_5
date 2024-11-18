class Implementor:
    def operation_implementation(self):
        raise NotImplementedError("This method should be overridden.")

class ConcreteImplementorA(Implementor):
    def operation_implementation(self):
        return "ConcreteImplementorA: Performing operation."

class ConcreteImplementorB(Implementor):
    def operation_implementation(self):
        return "ConcreteImplementorB: Performing operation."

class Abstraction:
    def __init__(self, implementor: Implementor):
        self._implementor = implementor

    def operation(self):
        return f"Abstraction: {self._implementor.operation_implementation()}"

# Пример использования
if __name__ == "__main__":
    implementor_a = ConcreteImplementorA()
    abstraction = Abstraction(implementor_a)
    print(abstraction.operation())

    implementor_b = ConcreteImplementorB()
    abstraction = Abstraction(implementor_b)
    print(abstraction.operation())
