// Determine what section to show
let url = window.location.search;

if (localStorage.length == 0) {
    document.getElementById('game').style.display = 'none';
    document.getElementById('final').style.display = 'none';
} else {
    document.getElementById('landing').style.display = 'none';
    document.getElementById('final').style.display = 'none';
    loadSituation();
}

async function loadSituation() {
  // Update index.html
  document.getElementById('name').innerHTML = localStorage.getItem('name');
  document.getElementById('turn').innerHTML = localStorage.getItem('t');
  document.getElementById('description').innerHTML = localStorage.getItem('desc');

  // Iterate through all bookings and create cards for each
  let cards = "";
  let options = localStorage.getItem('options');
  // Split string into array by commas
  options = options.split(',');
  // console.log('h',options,'h');
  // Remove all empty strings
  options = options.filter((option) => option != '');
  options.forEach((option) => {
      cards += `
      <div class="form-control">
        <label class="label cursor-pointer">
          <span class="label-text">${option}</span> 
          <input type="radio" name="radio-10" class="radio" required />
        </label>
      </div>
      `;
  });

  document.getElementById("options").innerHTML = cards;

  if (options.length == 0) {
    // document.getElementById('game').style.display = 'none';
    // Add restartGame as action for form
    document.getElementById('gameForm').addEventListener('submit', restartGame); 
    document.getElementById('submitDecision').value = 'Restart Game';
  }
}

async function getNextSituation() {
  let t = localStorage.getItem('t');
  let max_t = localStorage.getItem('max_t');
  let situation = localStorage.getItem('situation');
  let decision = localStorage.getItem('decision');

  // Send request to server api/run
  let r = await fetch('/api/run', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({t, max_t, situation, decision}),
  });
  let resp = await r.json();
  console.log(resp);

  // Update local storage
  localStorage.setItem('t', resp.t);
  localStorage.setItem('decision', null);
  if (resp.situation !== null) {
    localStorage.setItem('situation', resp.situation.name);
    localStorage.setItem('name', resp.situation.name);
    localStorage.setItem('desc', resp.desc + ' ' + resp.situation.description);
    localStorage.setItem('options', resp.situation.options);
  } else {
    localStorage.setItem('name', 'Survived WWII');
    localStorage.setItem('desc', resp.desc);
    localStorage.setItem('options', '');
  }

  loadSituation();
}

async function startGame(event) {
  event.preventDefault();

  document.getElementById('landing').style.display = 'none';
  document.getElementById('final').style.display = 'none';
  document.getElementById('game').style.display = 'block';


  let t=0;
  let max_t = 7;
  let situation = null;
  let decision = null;

  // Add to local storage
  localStorage.setItem('t', t);
  localStorage.setItem('max_t', max_t);
  localStorage.setItem('situation', situation);
  localStorage.setItem('decision', decision);
  localStorage.setItem('desc', '');
  localStorage.setItem('options', '');

  getNextSituation();
}

// Add startGame as action for form
document.getElementById('startForm').addEventListener('submit', startGame);

async function submitAnswer(event) {
  event.preventDefault();

  // Get which option was selected
  let i = 0;
  document.querySelectorAll('.radio').forEach((radio) => {
    if (radio.checked) {
      localStorage.setItem('decision', i);
    } 
    i++;
  });
  getNextSituation();
}

// Add submitAnswer as action for form
document.getElementById('gameForm').addEventListener('submit', submitAnswer);

async function restartGame() {
  localStorage.clear();
  window.location.href = '/';
}