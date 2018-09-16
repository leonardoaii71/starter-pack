-m rasa_nlu.train -c nlu_config.yml --data data/nlu_data.md -o models --fixed_model_name nlu --project current --verbose

-m rasa_core.train -d domain.yml -s data/stories.md -o models/current/dialogue --epochs 200

-m rasa_core.run -d models/current/dialogue -u models/current/nlu

interactive learning:

python -m rasa_core_sdk.endpoint --actions actions

python -m rasa_core.run  --interactive -d models/dialogue --stories-out stories_interactive.md -u models/default/nlu

run
python -m rasa_core.run -d models/current/dialogue  -u models/default/nlu --endpoints endpoints.yml