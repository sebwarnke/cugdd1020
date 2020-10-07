# Open API - Camunda REST API

- Check https://docs.camunda.org/manual/latest/reference/rest/openapi/

- Download Open API Spec here: https://app.camunda.com/nexus/service/rest/repository/browse/camunda-bpm/org/camunda/bpm/camunda-engine-rest-openapi/

- Unzip `openapi.json`: 

  - ```bash
    unzip camunda-engine-rest-openapi-7.14.0.jar openapi.json
    ```

- Download OpenAPITools Api Generator CLI here: https://mvnrepository.com/artifact/org.openapitools/openapi-generator-cli/4.3.1

- Generate Python API

  - ```bash
    java -jar openapi-generator-cli-4.3.1.jar generate -i ./openapi.json -g python -o ./cugdd-client
    ```

  

