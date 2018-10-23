## Greet
* greet
    - utter_greet

## bye
* bye
    - utter_bye

## thank
* thank
    - utter_thank

##affirm
* affirm
    - utter_happy

##deny
* deny
    -utter_bye

## consultar evento ambiguo
* query_event{"event": "prematricula"}
    - slot{"event": "prematricula"}
    - action_look_event
    - slot{"matching_events": ["Inicio de prematricula", "Per\u00edodo de modificaci\u00f3n de prematr\u00edcula (presencial).", "Per\u00edodo de modificaci\u00f3n de prematr\u00edcula (presencial).", "Retirar prematr\u00edcula el 3-2017-2018.", "Per\u00edodo de prematr\u00edcula para el 3-2017-2018.", "b) Retirar prematr\u00edcula del 1-2018-2019.", "Per\u00edodo de Prematr\u00edcula Estudiantes Ciclo Estudios Generales."]}
    - action_suggest

## consultar evento
* query_event{"event": "Inicio de prematricula"}
    - slot{"event": "Inicio de prematricula"}
    - action_look_event
    - action_ack_eventdate


## consultar evento sin nombre
* query_event
    - utter_event_not_found


## preguntar por dias importantes
* query_importantes
    - action_look_important
    - utter_another_question

## preguntar por cantidad de dias importantes
* count_importante
    - action_count_important
    - utter_ack_number_importantes

## preguntar por dias asuetos
* query_asueto
    - action_look_asuetos
    - utter_did_that_help
    - utter_another_question

## preguntar cantidad dia asueto
* count_asueto
    - action_count_asuetos
    - utter_another_question

## Generated Story 2421517452637475804
* query_indice
    - action_login_form

## default
* None
    - utter_default

## Generated Story 3741297509561492559
* query_indice
    - utter_ask_matricula
    - slot{"requested_slot": "matricula"}
* informar{"matricula": "20121917"}
    - slot{"matricula": "20121917"}
    - slot{"requested_slot": "password"}
    - utter_ask_password
* informar{"password": "123456"}
    - slot{"password": "123456"}
    - utter_indice

## Generated Story 6319266707024298916
* descripcion_proceso{"proceso": "bajas por prerrequisitos"}
    - slot{"proceso": "bajas por prerrequisitos"}
    - action_process_descripcion

## Generated Story -5112669426839210494
* what_should_i_ask
    - utter_you_should_ask

## Generated Story 7184186336441010786
* procedimiento_proceso{"proceso": "graduacion"}
    - slot{"proceso": "graduacion"}
    - action_process_procedimiento

## Generated Story -5821021971457789825
* query_asueto
    - action_look_asuetos
    - slot{"asueto_count": 1}

## Generated Story 9192142771012463284
* query_importantes
    - action_look_important
    - slot{"importantes_count": 11}

## Generated Story -189469721235285774
* nonsense
    - action_default_fallback
