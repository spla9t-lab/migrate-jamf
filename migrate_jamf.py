import requests
import json

# Replace these with the appropriate values for your environment
source_server_url = "https://source.jamfcloud.com"
destination_server_url = "https://destination.jamfcloud.com"
source_username = "source_username"
source_password = "source_password"
destination_username = "destination_username"
destination_password = "destination_password"

# Build the header for the API call
header = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Basic " + str(
        (source_username + ":" + source_password).encode("utf-8").hex()
    )
}

# API endpoint to get all objects of a specific type
get_objects_endpoint = "/uapi/v1/objects"

# API endpoint to create a new object of a specific type
create_object_endpoint = "/uapi/v1/objects"

# Define the types of objects we want to migrate
object_types = ["policies", "mobile_device_applications", "mobile_device_configuration_profiles"]

# Function to get all objects of a specific type from the source server
def get_objects(type):
    endpoint = source_server_url + get_objects_endpoint + "/" + type
    response = requests.get(endpoint, headers=header)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to get objects of type: " + type)
        print("Status code: " + str(response.status_code))
        return None

# Function to create a new object of a specific type on the destination server
def create_object(type, object):
    endpoint = destination_server_url + create_object_endpoint + "/" + type
    header = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Basic " + str(
            (destination_username + ":" + destination_password).encode("utf-8").hex()
        )
    }
    response = requests.post(endpoint, headers=header, data=json.dumps(object))
    if response.status_code == 201:
        return response.json()
    else:
        print("Failed to create object of type: " + type)
        print("Status code: " + str(response.status_code))
        return None

# Loop through each object type and migrate the objects
for object_type in object_types:
    objects = get_objects(object_type)
    if objects is not None:
        for object in objects:
            create_object(object_type, object)
