#!/usr/bin/env bash

mongo "localhost:27017/ocl" ./export_user.js
mongoexport --db ocl --collection export.users -o exported_users.json