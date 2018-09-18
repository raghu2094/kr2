import pytest
import server
import os
import json


def test_initial():
    test_app = server.app
    test_client = test_app.test_client()
    test_app.testing = True
    init = test_client.get('/jobs/testing')
    print(init)
    assert b"US Naukri" in init.data


def test_job():

    # Test if we are able to get jobs
    test_app = server.app
    test_client = test_app.test_client()
    test_app.testing = True
    headers_content_form_data = {'Content-Type': 'multipart/form-data'}
    jobs = test_client.post('/jobs/total',headers=headers_content_form_data,
        data={'desc': 'node','jobType':'true'})
    data = json.loads(jobs.get_data(as_text=True))
    #assert data["success"] == 1
    assert jobs.status_code == 200
'''    	
    # Test if we are able to get error when token is wrong
    test_app = app.flask_news("wrong_token")
    test_client = test_app.test_client()
    test_app.testing = True
    news = test_client.get('/top_headlines')
    data = json.loads(news.get_data(as_text=True))
    assert data["success"] == 0
'''
