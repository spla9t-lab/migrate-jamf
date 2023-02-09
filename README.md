# Epic Jamf Migration Script

Have you ever wanted to move all your data from one Jamf server to another? 
Do you want to do it in the coolest way possible? 
Well, look no further! 
This script is the one for you!

## Usage

- Replace the values for `source_server_url`, `destination_server_url`, `source_username`, `source_password`, `destination_username`, and `destination_password` in the script with the appropriate values for your environment.
- Run the script and watch as your data is effortlessly migrated from one server to the other! 

## What does this script do?

This script migrates your data from one Jamf server to another using the power of the Jamf API. By defualt it migrates all the objects of the following types: 

- policies
- mobile_device_applications
- mobile_device_configuration_profiles

It's that simple! You don't even have to lift a finger! 
Well, you do have to run the script and modify it to fit your use case, but you get the point! 

Here's a full list of all object types that can be used with this script but YMMV. Check out Jamf's API Documentation for a list not lazily grabbed from a chatGPT question that pulled from data from 2021:

 - computers
 - mobile_devices
 - users
 - user_groups
 - policies
 - smart_computer_groups
 - static_computer_groups
 - mobile_device_groups
 - mobile_device_configuration_profiles
 - mobile_device_applications
 - directory_bindings
 - os_x_configuration_profiles
 - advanced_computer_searches
 - advanced_mobile_device_searches
 - packages
 - scripts
 - netboot_servers
 - netboot_images
 - ebooks
 - printers
 - directories
 - network_segments
 - extension_attributes
 - computer_extension_attributes
 - mobile_device_extension_attributes
 - patch_policies

## How does it all work?

The script just gets all the objects of each type from the source server and then creates the same objects on the destination server. 

It's magic! 

## But wait, there's more!

This script is written in Python and uses the requests library to interact with the Jamf API. 
It's easy to understand and modify if needed, so feel free to add your own personal touch! 

## Conclusion

This script is the answer to all your Jamf migration needs. 
Don't waste any more time migrating your data the manually. 
Use this script and be the coolest IT pro around!

