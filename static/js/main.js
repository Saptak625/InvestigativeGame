// Determine what section to show
let url = window.location.search;

if (localStorage.length > 0) {
    document.getElementById('landing').style.display = 'none';
    document.getElementById('final').style.display = 'none';
    const params = new Proxy(new URLSearchParams(url), {
        get: (searchParams, prop) => searchParams.get(prop),
    });
    // Get the value of "some_key" in eg "https://example.com/?some_key=some_value"
    let gridSize = params.grid;
    let diff = params.diff;
    let diff_scale = params.diff_scale;
    let diff_factor = params.diff_factor;
    let t = params.t;

    startGame(gridSize, diff, diff_scale, diff_factor, t);
} else {
    document.getElementById('game').style.display = 'none';
    document.getElementById('game_grid').style.display = 'none';
    document.getElementById('final').style.display = 'none';
}

async function getNextSituation() {
  let t = localStorage.getItem('t');
  let situation = localStorage.getItem('situation');

  // Send request to server api/run
  let r = await fetch('/api/run', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({t, situation}),
  });
  let resp = await r.json();
  console.log(resp);

  // Update index.html
  document.getElementById('name').innerHTML = resp['situation']['name'];
  document.getElementById('turn').innerHTML = resp['t'];
  document.getElementById('description').innerHTML = resp['situation']['description'];

  // Update local storage
  localStorage.setItem('t', resp.t);
  localStorage.setItem('situation', resp.situation);
}

async function startGame() {
  let t=1;
  let situation = null;

  // Add to local storage
  localStorage.setItem('t', 1);
  localStorage.setItem('situation', situation);

  getNextSituation();
}

// Add startGame as action for form
document.getElementById('startForm').addEventListener('submit', startGame);

async function submitAnswer() {
}

// Add submitAnswer as action for form
document.getElementById('gameForm').addEventListener('submit', submitAnswer);