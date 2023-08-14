## Running Locally

Build the docker image and start the lambda handler on a port
```
./build-and-run.sh
```

Send a request to the lambda endpoint
```
curl "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'
```

