// =====================
// Display today values
// =====================
function showToday() {
    const todayEl = document.getElementById('today');
    const now = new Date();
    const options = { weekday: 'short', year: 'numeric', month: 'short', day: 'numeric' };
    todayEl.textContent = "Today: " + now.toLocaleDateString('en-US', options);
}

showToday();

// =====================
// TODO List logic
// =====================
const input = document.getElementById('taskInput');
const addBtn = document.getElementById('addBtn');
const taskList = document.getElementById('taskList');

function addTask() {
    const task = input.value.trim();
    if (task === '') return;

    const li = document.createElement('li');

    // Left side: checkbox + task text
    const leftDiv = document.createElement('div');
    leftDiv.className = 'task-left';

    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox';

    const span = document.createElement('span');
    span.className = 'task-text';
    span.textContent = task;

    leftDiv.appendChild(checkbox);
    leftDiv.appendChild(span);
    li.appendChild(leftDiv);

    // Event: tick checkbox → mark done
    checkbox.addEventListener('change', function() {
        if (checkbox.checked) li.classList.add('done');
        else li.classList.remove('done');
    });

    // Delete button
    const delBtn = document.createElement('button');
    delBtn.textContent = 'Delete';
    delBtn.className = 'delete-btn';
    delBtn.addEventListener('click', function() {
        taskList.removeChild(li);
    });

    li.appendChild(delBtn);
    taskList.appendChild(li);

    input.value = '';
}

// Add task on button click
addBtn.addEventListener('click', addTask);

// Add task on Enter key
input.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') addTask();
});