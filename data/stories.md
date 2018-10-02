
## Generated Story -4488314089759311551
* greet
    - utter_greet
* query_event{"event": "prematricula"}
    - slot{"event": "prematricula"}
    - action_look_event
    - slot{"matching_events": ["Inicio de prematricula", "Per\u00edodo de modificaci\u00f3n de prematr\u00edcula (presencial).", "Per\u00edodo de modificaci\u00f3n de prematr\u00edcula (presencial).", "Retirar prematr\u00edcula el 3-2017-2018.", "Per\u00edodo de prematr\u00edcula para el 3-2017-2018.", "b) Retirar prematr\u00edcula del 1-2018-2019.", "Per\u00edodo de Prematr\u00edcula Estudiantes Ciclo Estudios Generales."]}
    - action_suggest
    - utter_another_question
* deny
    - utter_bye

## Generated Story 5197315882586877915
* greet
    - utter_greet
* query_event
    - utter_event_not_found
* query_event{"event": "Inicio del per?odo"}
    - slot{"event": "Inicio del per?odo"}
    - action_look_event
    - action_ack_eventdate
    - utter_another_question
* deny
    - utter_bye

 ## Generated Story 118097638415333074
* greet
    - utter_greet
* query_importantes
    - action_look_important
* query_asueto
    - action_look_asuetos
* query_event{"event": "Inicio de prematricula"}
    - slot{"event": "Inicio de prematricula"}
    - action_look_event
    - action_ack_eventdate
    - utter_another_question
* deny

## Generated Story 5794520989269452863
* greet
    - utter_greet
* query_importantes
    - action_look_important
* query_importantes
    - utter_ack_number_importantes
    - utter_another_question
* deny
    - utter_bye

## Generated Story 1777451537465237704
* greet
    - utter_greet
* query_event{"event": "Retiro de prematricula"}
    - slot{"event": "Retiro de prematricula"}
    - action_look_event
    - action_ack_eventdate
* query_event{"event": "Inicio de prematricula"}
    - slot{"event": "Inicio de prematricula"}
    - action_look_event
    - action_ack_eventdate
* query_importantes
    - action_look_important
* count_importante
    - utter_ack_number_importantes
* query_asueto
    - action_look_asuetos
    - utter_did_that_help
    - utter_another_question
* deny
    - utter_bye

## Generated Story 556867726090332950
* greet
    - utter_greet
* query_asueto
    - action_look_asuetos
* query_importantes
    - action_look_important
* count_importante
    - utter_ack_number_importantes
* query_event{"event": "Ultimo dia de docenciaa"}
    - slot{"event": "Ultimo dia de docencia"}
    - action_look_event
    - action_ack_eventdate
* bye
    - utter_bye

##eventos
## Generated Story -7869471021863825539
* greet
    - utter_greet
* query_event{"event": "retiro"}
    - slot{"event": "retiro"}
    - action_look_event
    - slot{"matching_events": ["Retiro de prematricula", "Fecha limite para retiro parcial", "Fecha limite para retiro total"]}
    - action_suggest
* query_event{"event": "Fecha limite para retiro parcial"}
     slot{"event": "Fecha limite para retiro parcial"}
    - action_look_event
    - action_ack_eventdate
    - utter_another_question
* deny
    - utter_bye


## Generated Story 4204010466835567889
* greet
    - utter_greet
* query_event{"event": "Ceremonia de la sexag?sima quinta graduaci?n ? Campus Santo Tom?s de Aquino"}
    - slot{"event": "Ceremonia de la sexag?sima quinta graduaci?n ? Campus Santo Tom?s de Aquino"}
    - action_look_event
    - slot{"matching_events": ["Solicitud de cambio de campus", "Solicitud de graduacion Campus de Santiago"]}
    - action_suggest
    - utter_another_question
* query_event{"event": "Fecha l?mite para solicitar cambio de campus para el per?odo 2-2018-2019"}
    - slot{"event": "Fecha l?mite para solicitar cambio de campus para el per?odo 2-2018-2019"}
    - action_look_event
    - slot{"date": "Tue, 06 Nov 2018 04:40:00 GMT"}
    - action_ack_eventdate
* query_asueto
    - action_look_asuetos
    - utter_another_question
* deny
    - utter_bye

## Generated Story -5686472202456436433
* greet
    - utter_greet
* query_asueto
    - action_look_asuetos
* count_asueto
    - action_count_asuetos
    - utter_ack_number_asuetos
* bye
    - utter_bye

## Generated Story 6920952130253025474
* greet
    - utter_greet
* procedimiento_proceso{"proceso": "graduacion"}
    - slot{"proceso": "graduacion"}
    - action_process_procedimiento
* descripcion_proceso{"proceso": "lista de espera"}
    - slot{"proceso": "lista de espera"}
    - action_process_descripcion
* advertencia_proceso{"proceso": "ausencia a clases"}
    - slot{"proceso": "ausencia a clases"}
    - action_process_advertencia
* penalidad_proceso{"proceso": "graduacion"}
    - slot{"proceso": "graduacion"}
    - action_process_penalidad
* importancia_proceso{"proceso": "fn"}
    - slot{"proceso": "fn"}
    - action_process_importancia
    - utter_another_question
* deny
    - utter_bye

## Generated Story -2207994436118184688
* greet
    - utter_greet
* what_should_i_ask
    - utter_you_should_ask
* descripcion_proceso{"proceso": "lista de espera"}
    - slot{"proceso": "lista de espera"}
    - action_process_descripcion
* procedimiento_proceso{"proceso": "graduacion"}
    - slot{"proceso": "graduacion"}
    - action_process_procedimiento
* penalidad_proceso{"proceso": "ausencia a clases"}
    - slot{"proceso": "ausencia a clases"}
    - action_process_penalidad
    - utter_another_question
* deny
    - utter_bye

## Generated Story -8702000158847953821
* what_should_i_ask
    - utter_you_should_ask
* nonsense
    - utter_default

## Generated Story 5625027582201784311
* greet
    - utter_greet
* procedimiento_proceso{"proceso": "graduacion"}
    - slot{"proceso": "graduacion"}
    - action_process_procedimiento
* penalidad_proceso{"event": "prematricula"}
    - slot{"event": "prematricula"}
    - action_process_penalidad
* what_should_i_ask
    - utter_you_should_ask
* advertencia_proceso{"proceso": "lista de clases"}
    - slot{"proceso": "lista de clases"}
    - action_process_advertencia
* importancia_proceso{"proceso": "correo estudiantil"}
    - slot{"proceso": "correo estudiantil"}
    - action_process_importancia
* bye
    - utter_bye
