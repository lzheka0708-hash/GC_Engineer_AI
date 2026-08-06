import json
from pathlib import Path
class DiagnosticsService:

    def __init__(self):
        self.knowledge_path = Path("knowledge")
    
    def load_json(self, file_path):    

        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def get_steps(self, device, module, problem):

        file_path = self.knowledge_path / "chromatek" / "crystal5000.json"

        data = self.load_json(file_path)

        return (
            data
            .get(module, {})
            .get(problem, {})
        )
