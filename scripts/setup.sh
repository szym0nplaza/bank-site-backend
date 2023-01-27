#!/bin/bash

echo "Running setup script..."

pp="./src";
export PYTHONPATH=$pp;
echo "PYTHONPATH set to $pp";

alembic upgrade head;
echo "Loaded alembic migrations"

python src/fixtures/user_fixture.py;
echo "Applied fixtures"