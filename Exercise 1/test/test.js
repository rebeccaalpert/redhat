let remoteMathService = require('../exercise1.js')
let assert = require('assert');

it('Returns 3', function() {
  remoteMathService(function(err, result) {
    expect(result).equals(3);
  });
});