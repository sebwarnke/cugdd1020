FROM camunda/camunda-bpm-platform:run-7.14.0

COPY ./cugdd-config.yml /camunda/configuration/default.yml

COPY ./cugdd-tweet-approval.bpmn /camunda/configuration/resources/cugdd-tweet-approval.bpmn
COPY ./cugdd-tweet-check.dmn /camunda/configuration/resources/cugdd-tweet-check.dmn
COPY ./cugdd-start-form.html /camunda/configuration/resources/cugdd-start-form.html
