# Unoffical Streamtape API Wrapper

![Screenshot from 2024-04-27 03-24-10](https://github.com/swadhinbiswas/Streamtape/assets/107450069/a0b2566a-45d8-47d8-bb77-9f5d0bcbba76)

## Streamtape tries to give the user the best experience you can get on a video-sharing website

![Screenshot from 2024-04-27 03-24-24](https://github.com/swadhinbiswas/Streamtape/assets/107450069/f186fb0f-3f95-437e-a165-bd5e826d6f7b)

## Video sharing has never been easier

*It is a simple API wrapper for the streaming service streamtape.com. The API documentation can be found on the [docs page](link:). The whole structure of the API has been split into different classes for easy overview and usage.*

## Installation

Install With

```python3
pip3 install pystreamtape
```

## Usage

**General usage**
*Class start with follwing initialization :*

```python3
   var=Streamtape('api_key','api_secret')

```

## General response

### For the general purpose of any response, the ApiResponse class has been created to return a dict with this structure:

```json
{
    "status": <status-code>,
    "msg": "<informational message. might vary, use the status code in your code!>",
    "result": <result of the request. varies depending on the request>
}
```

```python3
from streamtape import Streamtape
var=Streamtape('api_key','api_secret')

var.account_info()

var.download_ticket()

var.download_link()

var.file_info()

var.upload_file()

var.add_remote_upload()

var.remove_upload_upload()

var.cheak_upload_status()

var.list_of_files()

var.create_folder()

var.rename_folder()

var.delete_folder()

var.move_folder()

var.delete_file()

var.list_running_conversions()

var.list_of_confails()

var.list_of_finished_conversions()

var.list_of_conversion_formats()

var.convert_file()

var.cancel_conversion()

var.get_conversion_status()

var.get_conversion_formats()

var. get_thumbnail()

var.get_splash()

```