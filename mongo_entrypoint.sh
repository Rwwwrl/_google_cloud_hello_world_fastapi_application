#!/bin/bash

echo "Starting replica set initialize"
until mongosh --host mongodb:27017 --eval "print(\"waited for connection\")"
do
    sleep 2
done
echo "Connection finished"

echo "Creating replica set"
mongosh --host mongodb:27017 <<EOF
try {
  // Attempt to initiate the replica set
  rs.initiate({
    _id: "rs0",
    members: [
      { _id: 0, host: "localhost:27017" }
    ]
  });
  print("Replica set initiated");
} catch (e) {
  print("Replica set initiation skipped: " + e);
}

EOF
echo "Replica set created"
