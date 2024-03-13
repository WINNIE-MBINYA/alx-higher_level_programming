#!/usr/bin/node
function callMeMoby (times, fn) {
  for (let i = 0; i < times; i++) {
    fn();
  }
}

module.exports = { callMeMoby };
