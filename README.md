# esp32-grafana
esp32 client + grafana example


# Fastapi doc
https://fastapi.tiangolo.com/tutorial/first-steps/
https://fastapi.tiangolo.com/deployment/manually/


# esp32 http client example
https://www.techcoil.com/blog/how-to-post-json-data-to-a-http-server-endpoint-from-your-esp32-development-board-with-arduinojson/


## clone repo and run server
git clone https://github.com/524c/esp32-grafana

```
# setup and test
cd esp32-grafana

# after setup a python (version =>  3.8)
pip install -r requirements.txt

# run backend server
python server.py


# test
curl -X 'POST' \
  'http://localhost:8000/api/v1/sensor' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "string",
  "value": 0,
  "value2": 0,
  "description": "string"
}'

```
