const { hex_md5 } = require('./md5');

const input = 'dmypynyp';
const queue = [];
queue.push({path_so_far: '', coords: [0, 0]});

while( queue.length > 0) {
  // pop current loc
  let curr_state =  queue.shift();

  if (curr_state.coords[0] === 3 && curr_state.coords[1] === -3) {
    console.log('I win');
    console.log(curr_state.path_so_far);
    break;
  }
  // get children nodes
  let children = getPossibleMoves(curr_state.coords, curr_state.path_so_far);
  children.forEach((child) => {
    console.log(child);
    queue.push({path_so_far: curr_state.path_so_far + child.dir, coords: child.coords});
  })
}

function isLetterOpen(letter) {
  return ['b', 'c', 'd', 'e', 'f'].includes(letter);
}

function isInBounds(coords) {
  return coords[0] >= 0 && coords[1] <= 0 && coords[0] < 4 && coords[1] > -4;
}

// UP, DOWN, LEFT, RIGHT
function getPossibleMoves(coords, path_so_far) {
  // find the hash of the current state, then get which moves are possible
  const hash = hex_md5(input + path_so_far);
  const moves = [];
  if (isInBounds([coords[0], coords[1] + 1]) && isLetterOpen(hash[0])) {
    moves.push({dir: 'U', coords: [coords[0], coords[1] + 1]});
  }
  if (isInBounds([coords[0], coords[1] - 1]) && isLetterOpen(hash[1])) {
    moves.push({dir: 'D', coords: [coords[0], coords[1] - 1]});
  }
  if (isInBounds([coords[0] - 1, coords[1]]) && isLetterOpen(hash[2])) {
    moves.push({dir: 'L', coords: [coords[0] - 1, coords[1]]});
  }
  if (isInBounds([coords[0] + 1, coords[1]]) && isLetterOpen(hash[3])) {
    moves.push({dir: 'R', coords: [coords[0] + 1, coords[1]]});
  }
  return moves;
}
