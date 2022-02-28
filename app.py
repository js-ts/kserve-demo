import kserve
from typing import Dict

class AlexNetModel(kserve.Model):
    def __init__(self, name: str):
       super().__init__(name)
       self.name = name
       self.load()

    def load(self):
        pass

    def predict(self, request: Dict) -> Dict:
        pass

if __name__ == "__main__":
    model = AlexNetModel("custom-model")
    kserve.ModelServer().start([model])
