"""File downloading utility used for getting demo datasets. 
Function is OS environment agnostic, i.e. doesn't rely on wget or similar."""

import os
import requests

def download_from_url(url, directory='', fname=None, overwrite=False):
    """Downloads a file from a specified url."""

    # Default behavior: Set fname by splitting url on last '/' character
    if not fname:
        fname = url.rsplit('/', 1)[1]
    
    fpath = os.path.join(directory, fname)

    if os.path.exists(fpath):
        if not overwrite:
            print(f'Not Downloaded: {fpath} already exists.')
            return 
        
    # Fetch response from HTTP request
    response = requests.get(url)
    
    # Save content to file if request is successful
    if response.status_code == 200:
        if not os.path.exists(directory):
            os.mkdir(directory)
            
        fpath = os.path.join(directory, fname)
        with open(fpath, 'wb') as f:
            f.write(response.content)
            
    print(f'Saved {fpath} from {url}')
    
    return     

def get_CalIt2_data(directory=''):
	
	base_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/event-detection/'
	filenames = [
	    'CalIt2.data',
	    'CalIt2.events',
	    'CalIt2.names',
	    'Dodgers.data',
	    'Dodgers.events',
	    'Dodgers.names'
	]

	for filename in filenames:
	    download_from_url(base_url+filename, directory='data')