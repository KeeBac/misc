#!/usr/bin/env bash

#run decision tree - check records in mlflow
#python /test_url/decision_tree.py

#run fluentd - check records in kibana (test*)
#python /test_url/test_fluentd1.py

#print env vars
echo "printing env var..."
echo "$MLFLOW_TRACKING_URL"

