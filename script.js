// Task management application
let tasks = JSON.parse(localStorage.getItem('tasks')) || [];
let currentFilter = 'all';

const taskInput = document.getElementById('taskInput');
const addBtn = document.getElementById('addBtn');
const taskList = document.getElementById('taskList');
const filterBtns = document.querySelectorAll('.filter-btn');
const totalCount = document.getElementById('totalCount');
const completedCount = document.getElementById('completedCount');

// Event listeners
addBtn.addEventListener('click', addTask);
taskInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') addTask();
});

filterBtns.forEach((btn) => {
    btn.addEventListener('click', (e) => {
        filterBtns.forEach((b) => b.classList.remove('active'));
        e.target.classList.add('active');
        currentFilter = e.target.dataset.filter;
        renderTasks();
    });
});

// Add new task
function addTask() {
    const text = taskInput.value.trim();

    if (text === '') {
        alert('Please enter a task');
        return;
    }

    const task = {
        id: Date.now(),
        text,
        completed: false,
        createdAt: new Date().toLocaleString(),
    };

    tasks.push(task);
    saveTasks();
    taskInput.value = '';
    renderTasks();
}

// Delete task
function deleteTask(id) {
    tasks = tasks.filter((task) => task.id !== id);
    saveTasks();
    renderTasks();
}

// Toggle task completion
function toggleTask(id) {
    const task = tasks.find((t) => t.id === id);
    if (task) {
        task.completed = !task.completed;
        saveTasks();
        renderTasks();
    }
}

// Render tasks based on filter
function renderTasks() {
    taskList.innerHTML = '';

    let filteredTasks = tasks;

    if (currentFilter === 'active') {
        filteredTasks = tasks.filter((t) => !t.completed);
    } else if (currentFilter === 'completed') {
        filteredTasks = tasks.filter((t) => t.completed);
    }

    if (filteredTasks.length === 0) {
        taskList.innerHTML = '<div class="empty-state"><p>No tasks yet. Add one to get started!</p></div>';
    } else {
        filteredTasks.forEach((task) => {
            const li = document.createElement('li');
            li.className = `task-item ${task.completed ? 'completed' : ''}`;
            li.innerHTML = `
                <input 
                    type="checkbox" 
                    ${task.completed ? 'checked' : ''} 
                    onchange="toggleTask(${task.id})"
                />
                <span class="task-text">${escapeHtml(task.text)}</span>
                <button class="btn btn-delete" onclick="deleteTask(${task.id})">Delete</button>
            `;
            taskList.appendChild(li);
        });
    }

    updateStats();
}

// Update statistics
function updateStats() {
    totalCount.textContent = tasks.length;
    completedCount.textContent = tasks.filter((t) => t.completed).length;
}

// Save tasks to localStorage
function saveTasks() {
    localStorage.setItem('tasks', JSON.stringify(tasks));
}

// Escape HTML to prevent XSS
function escapeHtml(text) {
    const map = {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#039;',
    };
    return text.replace(/[&<>"']/g, (m) => map[m]);
}

// Initial render
renderTasks();
