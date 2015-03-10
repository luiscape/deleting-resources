# Deleting Galley Items on HDX
Script to delete gallery items from HDX. It takes a JSON file as input (together with your HDX API key). The JSON file should be formatted as follows:

```json
[
  {
    "view_count": 2,
    "description": "A web-application that loads a datafile from the HDX Repository and display the content of it. \r\n\r\nThe application was developed by [Dominik Kalisch](http://www.kalisch.biz/) and will soon be made open-source through his [GitHub account](https://github.com/dkalisch/).",
    "title": "Data Explorer",
    "url": "http://hdx.iao.fraunhofer.de/?file=CH070_baseline.xlsx",
    "created": "2014-05-13T14:02:27.065598",
    "image_url": "https://docs.hdx.rwlabs.org/wp-content/uploads/generic_app_image.png",
    "type": "application",
    "id": "2b005a80-6de2-48b4-b8d6-20f8cf8c18f5",
    "owner_id": "154de241-38d6-47d3-a77f-0a9848a61df3"
  },
  ...
 ]
```

## Usage
Make sure to install the dependencies on `requirements.txt` and run the following: 

```bash
$ python code/delete-gallery-items.py
```

Remember to add your API key inside the `delete-gallery-item.py` script.

Given you have the right permissions, you will see all the gallery items being deleted one at a time.

## License
This is licensed under [MIT](LICENSE.md).