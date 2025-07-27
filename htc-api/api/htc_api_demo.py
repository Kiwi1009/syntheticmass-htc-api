#!/usr/bin/env python3
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_caching import Cache

import logging
import sys

app = Flask(__name__)

# define the cache config, register the cache instance, and bind it to the app 
cache = Cache(app,config={'CACHE_TYPE': 'simple'})

CORS(app)

#
#API calls
#

#Documentation Index
@app.route('/htc/api/v1')
@cache.cached(timeout=300)
def documentation():
    return jsonify({
        "title": "MA High Tech Counsel API Documentation",
        "version": "1.0",
        "endpoints": [
            "/htc/api/v1/test - Test endpoint",
            "/htc/api/v1/counties/list - Get counties list",
            "/htc/api/v1/counties/stats - Get counties statistics"
        ]
    })

#Test endpoint
@app.route('/htc/api/v1/test', methods=['GET'])
@cache.cached(timeout=300)
def test_endpoint():
    """Test endpoint to verify API is working"""
    return jsonify({
        "status": "success",
        "message": "HTC API is running successfully",
        "version": "1.0",
        "python_version": sys.version,
        "endpoint": "/htc/api/v1/test"
    })

#Mock counties endpoint
@app.route('/htc/api/v1/counties/list', methods=['GET'])
@cache.cached(timeout=300)
def get_counties():
    """Counties list in JSON (mock data)"""
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
@cache.cached(timeout=300)
def get_counties_stats():
    """Counties statistics in JSON (mock data)"""
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
        },
        {
            "ct_fips": "027",
            "ct_name": "Worcester",
            "sq_mi": 1510.3,
            "pop": 862113,
            "pct_male": 0.49,
            "pct_female": 0.51,
            "pop_sm": 862113
        }
    ]
    return jsonify(mock_stats)

#Mock county by name endpoint
@app.route('/htc/api/v1/counties/name/<string:ct_name>', methods=['GET'])
@cache.cached(timeout=300)
def get_county_by_name(ct_name):
    """Get county data by name (mock data)"""
    county_data = {
        "Worcester": {
            "ct_fips": "027",
            "ct_name": "Worcester",
            "sq_mi": 1510.3,
            "pop": 862113,
            "pct_male": 0.49,
            "pct_female": 0.51,
            "pop_sm": 862113
        },
        "Suffolk": {
            "ct_fips": "025",
            "ct_name": "Suffolk",
            "sq_mi": 58.47,
            "pop": 770816,
            "pct_male": 0.48,
            "pct_female": 0.52,
            "pop_sm": 770816
        }
    }
    
    if ct_name in county_data:
        return jsonify(county_data[ct_name])
    else:
        return jsonify({"error": "County not found"}), 404

if __name__ == '__main__':
    print("Starting HTC API server...")
    print("API will be available at: http://localhost:8080/htc/api/v1")
    print("Test endpoint: http://localhost:8080/htc/api/v1/test")
    print("Press Ctrl+C to stop the server")
    app.run(debug=True, host="0.0.0.0", port=8080, threaded=True) 