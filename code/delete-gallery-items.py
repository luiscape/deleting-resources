
# Script to extract features from GeoJSON files
# making the resulting files a collection of features
# without the proper GeoJSON "wrapper".

## TODO:
# - Create function to delete all datasets from UNOSAT.

import sys
import yajl as json
import requests
from termcolor import colored as color

###################
## Configuration ##
###################
apikey = 'XXX'  # consider adding key via cli
gallery_path = 'data/gallery_items.json'
verbose = False

# Loading data from a local resource.
def loadData(p, verbose=verbose):
    if verbose is True:
        print "--------------------------------------------------"
        print "Loading JSON data from %s." % p

    try:
        data = json.load(open(p))

        if verbose is True:
            print "Data loaded successully. %s entities in dataset:" % (len(data))

        return(data)

    except Exception as e:
        print "Could not load %s file." % (p)
        return(None)

    if verbose is True:
        print "--------------------------------------------------"


# Function to delete resources. It helps "clean-up"
# datasets before adding resources to them.
def deleteResources(gallery_dict, apikey, verbose=verbose):

  print "--------------------------------------------------"
  print "//////////////////////////////////////////////////"
  print "--------------------------------------------------"
  print "/////////// DELETING GALLERY ITEMS ///////////////"
  print "--------------------------------------------------"
  print "//////////////////////////////////////////////////"
  print "--------------------------------------------------"

  # Checking for input.
  if (gallery_dict is None):
    print "No data provided. Provide a JSON package."
    print "--------------------------------------------------"
    return

  # Base config.
  related_delete_url = 'https://data.hdx.rwlabs.org/api/action/related_delete?id='
  headers = { 'X-CKAN-API-Key': apikey, 'content-type': 'application/json' }

  for item in gallery_dict:
    # Deleting previous resources to make sure
    # the new batch is the most up-to-date.

    # Action
    u = { 'id': item["id"] }
    re = requests.post(related_delete_url, data=json.dumps(u), headers=headers)

    if verbose is True:
      print "Status code: ", re.status_code
      print re.json()

    if re.status_code != 200:
      message = color("FAIL", "red", attrs=['bold'])
      print "%s : %s" % (item["url"], message)

    else:
      message = color("SUCCESS", "green", attrs=['bold'])
      print "%s : %s" % (item["url"], message)

  print "--------------------------------------------------"


try:
  # Loading dictionaries.
  gallery_dict = loadData(gallery_path)

  # Delete resources:
  deleteResources(gallery_dict=gallery_dict, apikey=apikey)

except Exception as e:
  print e