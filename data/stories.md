
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
    - slot{"asueto_count": 1}
    - utter_ack_asuetos
    - utter_another_question
* deny
    - utter_bye

