import json
import os

class FileFactory:
    def writeData(self, path, arrData):
        """
        Serializes an array of Product objects to JSON and writes it to a file.
        :param path: Path to the file where JSON data should be written.
        :param arrData: Array of Product objects to serialize.
        """
        # Convert Product objects to a list of dictionaries for serialization.
        try:
            jsonString = json.dumps([item.__dict__ for item in arrData], default=str)
            with open(path, "w") as jsonFile:
                jsonFile.write(jsonString)
        except IOError as e:
            print(f"Error writing file {path}: {e}")
        except TypeError as e:
            print(f"Error serializing data: {e}")

    def readData(self, path, ClassName):
        """
        Deserializes JSON from a file into an array of Product objects.
        :param path: Path to the file to read JSON data from.
        :param ClassName: The class (Product) to which the JSON objects will be deserialized.
        :return: An array of Product objects.
        """
        if not os.path.isfile(path):
            return []
        try:
            with open(path, "r") as file:
                # Deserialize the file content to Product objects.
                return json.loads(file.read(), object_hook=lambda d: ClassName(**d))
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from file {path}: {e}")
            return []
        except IOError as e:
            print(f"Error reading file {path}: {e}")
            return []
