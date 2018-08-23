#!/bin/bash
# A script for generating a Vault token to use in Jenkins

if [ -z $VAULT_TOKEN ]
then
    echo "Main token not set! (\$VAULT_TOKEN empty)"
    exit 1
fi

if [ $# -ne 2 ]
then
    echo "Usage: $0 <role-name> <role-id>"
    exit 1
fi

ROLE_NAME=$1
ROLE_ID=$2

VAULT=$(which vault)
SECRET_ID=$($VAULT write -f -field=secret_id auth/approle/role/${ROLE_NAME}/secret-id)
# Get user token
$VAULT write -field=token auth/approle/login role_id=${ROLE_ID} secret_id=${SECRET_ID} > ./vault_token
