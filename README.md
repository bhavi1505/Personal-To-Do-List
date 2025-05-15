Personal To-Do List Application
📌 Project Overview
This Personal To-Do List Application helps users manage daily tasks efficiently with the ability to add, view, categorize, mark as complete, and delete tasks. Tasks are saved persistently using a JSON file and displayed in a simple, user-friendly Tkinter GUI.

💡 Features
✅ Add Tasks with Title, Description, and Category

✅ Categorization (e.g., Work, Personal, Urgent)

✅ Mark Tasks as Completed

✅ Delete Tasks

✅ Filter Tasks by Category

✅ Visual Color Cues:

Green: Completed Tasks

Red: Pending Tasks

💾 Data Persistence via tasks.json

🖼️ GUI Preview

Green = Completed, Red = Pending, Category-wise Filter at Top

🛠️ How to Run
Ensure Python 3.6+ is installed.

Clone or download the project folder.

Run the app with:

bash
Copy
Edit
python todo_gui.py
Interact with the interface to manage your tasks.

📁 Project Structure
bash
Copy
Edit
/to_do_list
├── todo_gui.py        # Main GUI Application
├── tasks.json         # Task Storage File
├── README.md          # Project Documentation
├── presentation.pptx  # Project Flow and Design
└── screenshots/       # GUI Screenshots
🧪 Sample Tasks.json
json
Copy
Edit
[
  {
    "title": "Complete Python Project",
    "description": "Finish the GUI and JSON handling",
    "category": "Work",
    "completed": true
  },
  {
    "title": "Buy groceries",
    "description": "Milk, bread, eggs",
    "category": "Personal",
    "completed": false
  }
]
🔮 Future Enhancements
⏰ Add due dates and reminders

🔍 Add search functionality

☁️ Cloud sync for backup across devices

📊 Task statistics (Completed vs. Pending count)

🙏 Acknowledgment
Thanks for using the Personal To-Do List App!
Crafted with 💚 using Python and Tkinter.

