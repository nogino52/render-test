import requests

# base_url = "https://render-test-0e41.onrender.com/";
base_url = "http://localhost:1000/";

root_result = requests.get(base_url);
print(root_result.text);

omikuji_result = requests.get(base_url + "omikuji");
print(omikuji_result.text);