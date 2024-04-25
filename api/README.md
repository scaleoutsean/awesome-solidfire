# SolidFire (ElementOS) API Collections

- SolidFire_Element_12.7_Bruno.json (source: Postman-to-[Bruno](https://www.usebruno.com/downloads) conversion by scaleoutSean)
- SolidFire_Element_12.7_Postman_v2.1.json ([source](https://github.com/solidfire/postman/))

### OpenAPI

There's no OpenAPI interface for SolidFire. Some method were exposed through HCI Management Node (find that Swagger file in the folder hcc), but very few.

SolidFire OpenAPI definition cannot be created by free Postman-to-OpenAPI tools because those don't work with JSON-RPC collections. 

Someone would have to use a commercial tool or craft a Swagger JSON for SolidFire. Consider this basic example for CreateVolume:

```json
{
  "id": 1,
  "method": "CreateVolume",
  "params": {
    "name": "test",
    "accountID": 1,
    "totalSize": 2000000000
  }
}
```

I've played with this a bit and created `solidfire_openapi_3.0.3_draft.yaml` (find it in this directory) which has some very basic elements in place. What it can do is this:


```sh
curl -X 'POST' \
  'https://192.168.1.30/json-rpc/12.7' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "method": "CreateVolume",
  "id": 1,
  "params": {
    "accountID": 1,
    "totalSize": 99999999999,
    "name": "vol55",
    "enable512e": false
  }
}'
```
 
I had to use `-k` to allow self-signed TLS certificate, and change RPC to 12.5 (as NetApp never released SolidFire Demo VM 12.5, we may as well change this to 12.5), but it works.

There's a lot of work to be done if it's done manually. Unfortunately - as far as I know - NetApp hasn't released this document, so I don't know of a better way than manually completing this when/if I want to use it one day. 

## License

SolidFire Postman collections are released under the Apache 2.0 License. The converted Bruno collection retains the same license.
