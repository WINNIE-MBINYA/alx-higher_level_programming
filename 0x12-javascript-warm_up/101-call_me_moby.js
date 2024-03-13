#!/usr/bin/node
function callXTimes (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}

module.exports = callXTimes;
