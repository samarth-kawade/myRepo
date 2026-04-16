# TaskHub - Task Management Application

A complete task management application with both web and Python interfaces that share the same data file.

## Project Structure

```
myRepo/
├── index.html      # Web application interface
├── style.css       # Web application styling
├── script.js       # Web application functionality
├── app.py          # Python command-line interface
├── tasks.json      # Shared task data file (auto-created)
└── README.md       # This file
```

## Features

### Web Application (TaskHub Web)
- ✅ Add, complete, and delete tasks
- ✅ Filter tasks (All, Active, Completed)
- ✅ Task statistics (total and completed count)
- ✅ **Export tasks** as JSON file
- ✅ **Import tasks** from JSON file
- ✅ **Clear all tasks** at once
- ✅ Persistent storage (browser localStorage)
- ✅ Beautiful UI with animations
- ✅ Fully responsive design

### Python Application (Task Manager CLI)
- ✅ Add, complete, and delete tasks from command line
- ✅ List tasks with visual indicators
- ✅ View task statistics
- ✅ **Synced with web app** via shared JSON file
- ✅ Simple menu-driven interface

## Usage

### Web Application

1. Open `index.html` in your web browser
2. Add tasks using the input field
3. Check off completed tasks
4. Use filters to view specific task categories
5. **Export** tasks to share or backup
6. **Import** tasks from a previously exported file

### Python Application

```bash
python app.py
```

Then select from the menu:
1. Add task
2. List tasks
3. Complete task
4. Delete task
5. View statistics
6. Exit

## Data Synchronization

Both applications use the same JSON file format (`tasks.json`):

```json
[
  {
    "id": 1713275641000,
    "text": "Sample task",
    "completed": false
  }
]
```

### How to Sync Data

1. **Web → Python:** Export tasks from the web app, then import the JSON file with Python app
2. **Python → Web:** Both apps write to `tasks.json` automatically
3. **Backup:** Use the Export feature to create regular backups
4. **Share:** Export from one device and import on another

## Workflow Example

### Scenario: Working across devices

1. **On Desktop (Web App):**
   - Add tasks using the web interface
   - Click "Export" to save `tasks-2026-04-16.json`

2. **On Laptop (Python App):**
   - Run `python app.py`
   - Manage tasks from command line
   - Changes are saved to `tasks.json`

3. **Back to Desktop (Web App):**
   - Click "Import" and select the file from laptop
   - Web app now shows all tasks from both devices

## Browser Compatibility

- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- All modern browsers with ES6 support

## System Requirements

- Python 3.6+ (for app.py)
- Any modern web browser (for web app)

## File Details

### index.html
- Semantic HTML5 structure
- Navigation bar with branding
- Task input and action buttons
- Task list with interactive elements
- Statistics display
- Hidden file input for imports

### style.css
- Modern gradient background
- Flexbox-based responsive layout
- Smooth animations and transitions
- Color scheme: Purple gradient (#667eea to #764ba2)
- Mobile-friendly design

### script.js
- Task CRUD operations
- Filter functionality
- LocalStorage persistence
- Export/Import functionality
- Data validation and XSS protection

### app.py
- Object-oriented design with TaskManager class
- JSON file synchronization
- Compatible task ID format with web app
- Command-line menu interface
- Error handling

## Tips & Tricks

1. **Backup automatically:** Export tasks weekly to a backup folder
2. **Share tasks:** Export and email the JSON file to collaborators
3. **Batch operations:** Export, edit JSON manually, and import back
4. **Mobile access:** The web app works perfectly on mobile browsers
5. **CLI power users:** Use app.py for keyboard-driven task management

## Keyboard Shortcuts (Web)

- **Enter** in task input field = Add task
- **Tab** to navigate buttons
- **Space** to toggle task completion

## Troubleshooting

### Tasks not saving?
- Check browser's localStorage is enabled
- Try exporting to backup your data
- Clear browser cache and try again

### Import not working?
- Ensure JSON file is valid (use Export to create valid files)
- Check file is not corrupted
- Try a different exported file

### Python app not finding tasks.json?
- Run Python app from the same directory as the JSON file
- Or modify the filename parameter in `TaskManager('path/to/tasks.json')`

## License

Free to use and modify for personal and educational purposes.

## Future Enhancements

- Cloud synchronization
- Task categories/tags
- Due dates and reminders
- Web API for mobile apps
- Dark theme toggle
- Recurring tasks
- Task notes/descriptions

---

**Created:** April 2026  
**Version:** 1.0
