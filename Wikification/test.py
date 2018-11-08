import sys, http.client, urllib.request, urllib.parse, urllib.error, json

from pprint import pprint

def wikilookup (lookUP):
    query = lookUP
    query = urllib.parse.quote_plus( query )

    # Call our function.
    url_data = get_url( 'en.wikipedia.org', '/w/api.php?format=json&action=query&prop=extracts&exlimit=max&explaintext&exintro&titles=' + query )
    # We know how our function fails - graceful exit if we have failed.
    if url_data is None :
        print( "Failed to get data ... Can not proceed." )
        return "not found"

    # http.client socket returns bytes - we convert this to utf-8
    url_data = url_data.decode( "utf-8" ) 

    # Convert the structured json string into a python variable 
    url_data = json.loads( url_data )

    # Pretty print
    pprint( url_data )


    return "found"

def get_url( domain, url ) :

    # Headers are used if you need authentication
    headers = {}
    
    # If you know something might fail - ALWAYS place it in a try ... except
    try:
        conn = http.client.HTTPSConnection( domain )
        conn.request("GET", url, "", headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
        return data 
    except Exception as e:
        # These are standard elements in every error.
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

    # Failed to get data!
    return None

print(wikilookup("HCI"))
