import json

class News():
    def __init__(self, identifier:int, category:str, title:str, content:str) -> None:
        self.identifier = identifier
        self.category = category
        self.title = title
        self.content = content
        self.content_markup = ""

        self.resume = self.content[0:150]+"[...]" if len(self.content) != 0 else ""
        self.resume_markup = ""
        
    def properties(self):
        print(f"id: {self.identifier}")
        print(f"category: {self.category}")
        print(f"title: {self.title}")
        print(f"\ncontent: {self.content}\n")
        print(f"resume: {self.resume}")

    def create_dict_object(self):
        self.dict_object = {
            "identifier": f"{self.identifier}",
            "category": f"{self.category}",
            "title": f"{self.title}",
            "content": f"{self.content}",
            "content_markup": f"{self.identifier}",
            "resume": f"{self.resume}",
            "resume_markup": f"{self.resume_markup}",
        }

        return self.dict_object
    
    def convert_to_json(self, dict_object:dict):
        self.json_string = json.dumps(dict_object)

        return self.json_string