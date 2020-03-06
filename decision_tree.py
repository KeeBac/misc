from enum import Enum
import json
import tracking

class Model(Enum):
    DECISION_TREE = 0
    RANDOM_FOREST = 1
    ADABOOST = 2
    GRADIENT_BOOST = 3

def main(model=Model.DECISION_TREE, seed=None):
    #original_train, original_validate = load_data()
    #train, validate = encode(original_train, original_validate)
    with tracking.track() as track:
        print('track is',track)
        track.set_model(model)
        #model, params = train_model(train, model, seed)
        #track.log_params(params)
        track.log_params({'a':10, 'b':20})
        #validation_predictions = make_predictions(model, validate)

        print("Calculating metrics")
        evaluation_metrics = {
            'nwrmsle': 10, #evaluation.nwrmsle(validation_predictions, validate['unit_sales'].values, validate['perishable'].values),
            'r2_score': 10 #metrics.r2_score(y_true=validate['unit_sales'].values, y_pred=validation_predictions)
        }
        track.log_metrics(evaluation_metrics)

        #write_predictions_and_score(evaluation_metrics, model, original_train.columns)

        print("Evaluation done with metrics {}.".format(json.dumps(evaluation_metrics)))


if __name__ == "__main__":
    main(model=Model.RANDOM_FOREST, seed=8675309)
