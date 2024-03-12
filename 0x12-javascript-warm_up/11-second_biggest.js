#!usr/bin/node
function secondLargest (args) {
  const sortedArgs = args.sort((a, b) => b - a);
  return sortedArgs[1] || 0;
}

const args = process.argv.slice(2).map(arg => parseInt(arg, 10));

if (args.length <= 1) {
  console.log(0);
} else {
  console.log(secondLargest(args));
}
