 -m rasa_nlu.train -c nlu_config.yml --data data/nlu_data.md -o models
--fixed_model_name nlu --project current --verbose

-m rasa_core.train -d domain.yml -s data/stories.md -o models/current/dialogue --epochs 200

 -m rasa_core.run -d models/current/dialogue -u models/current/nlu
