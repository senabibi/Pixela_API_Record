import requests
from datetime import datetime
USERNAME="nursena"
TOKEN="efvvbrgnthjmyjmfg"
pixela_end_point="https://pixe.la/v1/users"
GRAPH="bitirgensena"
user_params={
    "token":"efvvbrgnthjmyjmfg",
    "username":"nursena",
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

graph_end_point=f"{pixela_end_point}/{USERNAME}/graphs"
#response=requests.post(url=pixela_end_point,json=user_params)
#print(response.text)

graph_config={
    "id":"bitirgensena",
    "name":"Self-Development",
    "unit":"s/60",
    "type":"float",
    "color":"ajisai"
}
headers={
    "X-USER-TOKEN":TOKEN
}

#response=requests.post(url=graph_end_point,json=graph_config,headers=headers)
#print(response.text)

pixel_creation_end_point=f"{pixela_end_point}/{USERNAME}/graphs/{GRAPH}"

today=(datetime.now()).strftime("%Y%m%d")



pixel_data={
    "date":today,
    "quantity":"48.80",
}

response=requests.post(url=pixel_creation_end_point,json=pixel_data,headers=headers)
print(response.text)

update_endpoint=f"{pixela_end_point}/{USERNAME}/graphs/{GRAPH}/<{today}>"

new_pixel_data={
    "quantity":"4.5"
}
requests.put(url=update_endpoint,json=new_pixel_data,headers=headers)

print(response.text)

delete_endpoint=f"{pixela_end_point}/{USERNAME}/graphs/{GRAPH}/<{today}>"
response=requests.delete(url=delete_endpoint,headers=headers)

print(response)
