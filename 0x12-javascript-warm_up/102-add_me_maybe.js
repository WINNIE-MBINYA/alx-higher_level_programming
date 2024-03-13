#!/usr/bin/node
function addMeMaybe (number, callback) {
  const incrementedNumber = number + 1;
  callback(incrementedNumber);
}

module.exports = { addMeMaybe };
