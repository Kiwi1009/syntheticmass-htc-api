#!/usr/bin/env python3
from flask import Flask, jsonify, request, abort, g
from flask_cors import CORS
from flask_autodoc import Autodoc
from flask_caching import Cache

import logging
import re
import simplejson as json
import sys
import time

app = Flask(__name__)

# define the cache config, register the cache instance, and bind it to the app 
cache = Cache(app,config={'CACHE_TYPE': 'simple'})

CORS(app)
auto = Autodoc(app)

global log

#removes CR LF characters from string, for safer logging
def sanitize(s):
    return re.sub("[\r\n]+", " ", s)

#Get IP of client making the call, TO BE USED FOR DEBUGGING PURPOSES ONLY!
def get_ip():
    if not request.headers.getlist("X-Forwarded-For"):
        ip = request.remote_addr
    else:
        ip = request.headers.getlist("X-Forwarded-For")[0]
    return sanitize(ip)

#
#API calls
#

#Documentation Index
@app.route('/htc/api/v1')
@cache.cached(timeout=300) # cache this view for 5 minutes
def documentation():
    return auto.html(title='MA High Tech Counsel API Documentation')

#Test endpoint
@app.route('/htc/api/v1/test', methods=['GET'])
@auto.doc()
@cache.cached(timeout=300)
def test_endpoint():
    """Test endpoint to verify API is working"""
    log.debug("entering test_endpoint() IP=%s" % get_ip())
    return jsonify({
        "status": "success",
        "message": "HTC API is running successfully",
        "version": "1.0",
        "python_version": sys.version
    })

#Mock counties endpoint
@app.route('/htc/api/v1/counties/list', methods=['GET'])
@auto.doc()
@cache.cached(timeout=300)
def get_counties():
    """Counties list in JSON (mock data)"""
    log.debug("entering get_counties() IP=%s" % get_ip())
    mock_counties = [
        {"ct_name": "Barnstable", "ct_fips": "001"},
        {"ct_name": "Berkshire", "ct_fips": "003"},
        {"ct_name": "Bristol", "ct_fips": "005"},
        {"ct_name": "Dukes", "ct_fips": "007"},
        {"ct_name": "Essex", "ct_fips": "009"},
        {"ct_name": "Franklin", "ct_fips": "011"},
        {"ct_name": "Hampden", "ct_fips": "013"},
        {"ct_name": "Hampshire", "ct_fips": "015"},
        {"ct_name": "Middlesex", "ct_fips": "017"},
        {"ct_name": "Nantucket", "ct_fips": "019"},
        {"ct_name": "Norfolk", "ct_fips": "021"},
        {"ct_name": "Plymouth", "ct_fips": "023"},
        {"ct_name": "Suffolk", "ct_fips": "025"},
        {"ct_name": "Worcester", "ct_fips": "027"}
    ]
    return jsonify(mock_counties)

#Mock counties stats endpoint
@app.route('/htc/api/v1/counties/stats', methods=['GET'])
@auto.doc()
@cache.cached(timeout=300)
def get_counties_stats():
    """Counties statistics in JSON (mock data)"""
    log.debug("entering get_counties_stats() IP=%s" % get_ip())
    mock_stats = [
        {
            "ct_fips": "025",
            "ct_name": "Suffolk",
            "sq_mi": 58.47,
            "pop": 770816,
            "pct_male": 0.48,
            "pct_female": 0.52,
            "pop_sm": 770816
        },
        {
            "ct_fips": "017",
            "ct_name": "Middlesex",
            "sq_mi": 823.76,
            "pop": 1611699,
            "pct_male": 0.49,
            "pct_female": 0.51,
            "pop_sm": 1611699
        }
    ]
    return jsonify(mock_stats)

if __name__ == '__main__':
    log = app.logger
    #Logging levels: CRITICAL: 50, ERROR: 40, WARNING: 30, INFO: 20, DEBUG: 10, NOTSET: 0
    log.setLevel(10)
    logging.basicConfig(format="%(asctime)-15s %(threadName)s  %(message)s")
    log.debug("starting server")
    app.run(debug=True, host="0.0.0.0", port=8080, threaded=True) 